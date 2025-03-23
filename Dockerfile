# Use Python 3.11 as the base image
FROM python:3.11-slim

# Install system dependencies (bash, curl, etc.)
RUN apt-get update && apt-get install -y bash curl \
    && curl -sSLo /usr/local/bin/wait-for-it https://github.com/vishnubob/wait-for-it/releases/download/v2.3.0/wait-for-it.sh \
    && chmod +x /usr/local/bin/wait-for-it

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install the dependencies from the requirements file
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the application code into the container
COPY fitness_booking /app/fitness_booking

# Expose port 8000 for the web service
EXPOSE 8000

# Command to start the application with wait-for-it
CMD ["bash", "-c", "wait-for-it db:5432 -- python manage.py migrate && gunicorn fitness_booking.wsgi:application --bind 0.0.0.0:8000"]

