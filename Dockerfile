# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Selenium
RUN pip install selenium
RUN pip install ollama

# Make port 80 available to the world outside this container
EXPOSE 80

RUN ls -la

# Run app.py when the container launches
CMD ["python", "app.py"]