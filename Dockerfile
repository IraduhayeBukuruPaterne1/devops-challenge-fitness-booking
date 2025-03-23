# Use a Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the app into the container
COPY fitness_booking /app

# Expose the port and define the entry point
EXPOSE 8000
CMD ["python", "fitness_booking/app.py"]

