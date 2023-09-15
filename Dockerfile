# Use an official Python 3.11 runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
RUN mkdir /pp
WORKDIR /pp

# Copy the current directory contents into the container at /src
COPY src/ .

# Install any needed packages specified in requirements.txt
RUN apt-get update -y
RUN apt-get install libpq-dev -y
RUN pip install --upgrade wheel
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000
EXPOSE 5432
RUN pwd

# Define the command to start the Flask API using main.py
CMD ["python", "/pp/main.py"]
