# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the application port
EXPOSE 8000

# Use Gunicorn as the WSGI server
CMD ["gunicorn", "fitness_booking.wsgi:application", "--bind", "0.0.0.0:8000"]

