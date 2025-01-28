# Use the official Python image from the Docker Hub
FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /biteboard
# Set work directory
WORKDIR /biteboard

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

# # Install Python dependencies
# COPY requirements.txt /biteboard/
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# Copy project
COPY . /biteboard/
RUN pip install -r requirements.txt

# # Collect static files
# RUN python manage.py collectstatic --noinput

# # Run migrations
# RUN python manage.py migrate

# # Expose port 8000
# EXPOSE 8000

# # Start the application using Gunicorn
# CMD ["gunicorn", "biteboard.wsgi:application", "--bind", "0.0.0.0:8000"]
