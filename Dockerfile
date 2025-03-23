# Use the Python slim image as base
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files and buffering stdout
ENV PYTHONUNBUFFERED=1

# Install required packages for wait-for-it
RUN apt-get update && apt-get install -y bash curl \
    && curl -sSLo /usr/local/bin/wait-for-it https://github.com/vishnubob/wait-for-it/releases/download/v2.3.0/wait-for-it.sh \
    && chmod +x /usr/local/bin/wait-for-it

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the application code into the container
COPY fitness_booking /app/fitness_booking

# Expose port 8000 for the web service
EXPOSE 8000

# Command to start the application with wait-for-it
CMD ["bash", "-c", "wait-for-it db:5432 -- python manage.py migrate && gunicorn fitness_booking.wsgi:application --bind 0.0.0.0:8000"]

# Install required packages for wait-for-it
RUN apt-get update && apt-get install -y bash curl \
    && curl -sSLo /usr/local/bin/wait-for-it https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x /usr/local/bin/wait-for-it \
    && ls -l /usr/local/bin/wait-for-it  # Debug step to check if the file exists and is executable
