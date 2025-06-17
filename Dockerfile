# Use the official Python image as the base image
FROM python:3.13.2

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port the bot will run on (optional, if applicable)
EXPOSE 8080

# Command to run the bot
CMD ["python", "bot.py"]
