# Dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /api

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY ./api ./api
COPY .env .env

# Expose the port
EXPOSE 8000

# Command to run the FastAPI app using uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]