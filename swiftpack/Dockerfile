FROM python:3.12.4-alpine3.20

WORKDIR /usr/src/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install poetry
RUN apk update && apk add pipx

# Copy the project directory into the container
COPY . .

# Install the project's dependencies
RUN pip install -r requirements.txt

# final base image
# FROM python:3.11.9-alpine3.20

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Expose port 8000
EXPOSE 8000

# Start the poetry development server
ENTRYPOINT ["uvicorn"]
CMD ["--port", "8000", "app.main:app", "--reload", "--workers", "1", "--host", "0.0.0.0"]
