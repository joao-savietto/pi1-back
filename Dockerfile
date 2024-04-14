FROM python:3.11.9-bullseye

EXPOSE 8000
# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app
# Copy project
COPY . /app/

RUN chmod +x start_django.sh

# Install mysql driver
RUN apt update && apt install -y default-libmysqlclient-dev build-essential pkg-config default-mysql-client

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt


