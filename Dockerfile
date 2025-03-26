# Base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the application files
COPY . .

# Create static files directory
RUN mkdir -p /app/staticfiles

# Collect static files and apply migrations
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start the Django server with Gunicorn
CMD ["gunicorn", "fitness_booking.wsgi:application", "--bind", "0.0.0.0:8000"]
