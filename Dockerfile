#Set the base image to Python (lastest version)
FROM python:latest

#Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

#Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Copy the entire project directory into the container
COPY . .

#Set the command to run when the container starts
CMD ["python", "watch_next.py"]

