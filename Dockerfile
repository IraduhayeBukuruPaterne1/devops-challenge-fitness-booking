FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the application code
COPY fitness_booking /app

# Set the entry point to the WSGI server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "fitness_booking.wsgi:application"]

