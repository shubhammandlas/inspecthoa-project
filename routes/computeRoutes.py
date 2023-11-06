from flask import Blueprint, jsonify, request, send_file
from flask_restful import Api, Resource, reqparse, inputs
from models.db import get_db
from models.user import User
from models.request import Request
from models.db import SessionLocal
import asyncio
import aiohttp
from celeryApp.celery_worker import perform_computation
import csv
import openpyxl
from datetime import datetime
import os
from services.computeService.computeFile import storeAndComputeFile

api_routes = Blueprint('api_data', __name__)
file_directory = 'docs'

@api_routes.route('/compute', methods=['POST'])
async def compute_route():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"error": "Authorization header is missing"}), 401
    token = auth_header.split("Bearer ")[-1]
    if (os.environ['AUTH_TOKEN'] != token):
        return jsonify({"error": "Authorization header is invalid"}), 401
    uploaded_file = request.files.get('file')
    await storeAndComputeFile(uploaded_file)
    return jsonify({"message": "Files are saved"})


@api_routes.route('/files', methods=['GET'])
def get_files():
    response = []
    with SessionLocal() as db:
        requests = db.query(Request).all()
        
    for filename in os.listdir(file_directory):
        file_path = os.path.join(file_directory, filename)
        response.append({'filename': filename, 'path': file_path})
    return jsonify(response)


@api_routes.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    file_path = os.path.join(file_directory, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return 'File not found', 404
