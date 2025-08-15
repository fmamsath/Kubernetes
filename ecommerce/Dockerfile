FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py migrate
CMD ["gunicorn", "ecommerce.wsgi:application", "--bind", "0.0.0.0:8000"]