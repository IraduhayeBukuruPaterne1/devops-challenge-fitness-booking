# Base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies (including PostgreSQL client)
RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev musl-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the application files
COPY . .

# Collect static files and apply migrations
RUN mkdir -p /app/staticfiles
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start the Django server with Gunicorn
CMD ["gunicorn", "fitness_booking.wsgi:application", "--bind", "0.0.0.0:8000"]
