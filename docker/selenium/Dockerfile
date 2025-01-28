# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ../../ /app

# Install Selenium
RUN pip install selenium

# Run app.py when the container launches
CMD ["python", "app.py"]