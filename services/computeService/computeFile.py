from flask import jsonify
from services.readerService.FileReaderFactory import FileReaderFactory
from models.request import Request
from datetime import datetime
from models.db import SessionLocal
import os
import csv
from celeryApp.celery_worker import perform_computation

file_directory = 'docs'

async def storeAndComputeFile(file):
    data = FileReaderFactory().getReader(file)
    storeFile(data, file.filename)
    newRequest = Request(
        username='shubhammandlas',
        fileName=file.filename,
        createdAt=datetime.now()
    )
    with SessionLocal() as db:
        db.add(newRequest)
        db.commit()
        print('newRequestnewRequest', newRequest.id)
        task = perform_computation.delay(data,newRequest.id)
    return jsonify({"message": "Files are saved"}) 


def storeFile(data, filename):
    path = os.path.join('docs', filename)
    with open(path, 'w') as new_file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)
        


