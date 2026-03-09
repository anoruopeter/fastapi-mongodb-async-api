# official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# create logs directory
RUN mkdir -p logs

#Expose FastApi port
EXPOSE 8000

# Start the API
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]


