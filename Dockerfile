# Use a Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install dependencies and the wait-for-it script
RUN apt-get update && apt-get install -y bash curl && \
    curl -sSLo /usr/local/bin/wait-for-it https://github.com/vishnubob/wait-for-it/releases/download/v2.3.0/wait-for-it.sh && \
    chmod +x /usr/local/bin/wait-for-it

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the application code into the container
COPY fitness_booking /app

# Expose port 8000 for the web service
EXPOSE 8000

# Command to start the application with wait-for-it
CMD ["bash", "-c", "wait-for-it db:5432 -- python manage.py migrate && gunicorn fitness_booking.wsgi:application --bind 0.0.0.0:8000"]

