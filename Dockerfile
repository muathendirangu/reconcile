# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app


# Run app.py when the container launches
CMD ["python", "reconciler.py", "-s", "source.csv", "-t", "target.csv", "-o", "reconciliation.csv"]
