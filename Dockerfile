# Use the official Python image
FROM python:3.8.3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /code

# Copy project files into the container
COPY . /code/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the port that the Django app will run on
EXPOSE 8000

# Run migrations and start the server
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput && python manage.py test && python manage.py runserver 0.0.0.0:8000"]
