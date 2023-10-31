# Use the official Python image as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install PostgreSQL development files (required for psycopg2)
# RUN apt-get update && apt-get install -y libpq-dev

# Copy the contents of your project directory to the container
COPY . /app

# Install required dependencies
RUN pip install -r requirements.txt

# Expose the port on which your Flask app will run (change as needed)
EXPOSE 5000

# Specify the command to run your Flask app
CMD ["python3", "app.py"]
