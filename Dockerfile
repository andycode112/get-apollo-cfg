# Use an official Python runtime as a parent image
FROM python:3.7-slim-stretch
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.163.com/pypi/simple/
# Make port 80 available to the world outside this container
EXPOSE 5000
# Define environment variable
ENV apolloip 10.7.7.22
ENV apolloport 8001
# Run app.py when the container launches
CMD ["python", "main.py"]