# Dockerfile

# Pull base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code/

# Install dependencies
RUN apt-get update -qy
RUN pip install pipenv
COPY Pipfile* /code/
RUN pipenv install --system



