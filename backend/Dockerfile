# Get the base image
FROM python:3.10-slim
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire dir. 
COPY . /app/backend

# Set the environment variables
ENV FLASK_APP=backend/app.py 
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

# Run the application
CMD ["flask", "run"]
