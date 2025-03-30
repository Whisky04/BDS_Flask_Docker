# Use the official Python 3.11.9 image from Docker Hub as the base image.
FROM python:3.11.9-slim

# Set a working directory inside the container.
WORKDIR /app

# Copy the requirements file and install Python dependencies.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code.
COPY . .

# Expose port 5000 to the host.
EXPOSE 5000

# Set the default command to run the Flask app.
CMD ["python", "app.py"]
