# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy Django project files
COPY . .

# Expose port
EXPOSE 8000

# Use Gunicorn as the WSGI server
CMD ["gunicorn", "fitness_booking.wsgi:application", "--bind", "0.0.0.0:8000"]

