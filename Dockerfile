# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements file and install any needed packages
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Set the default command to run Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
