FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir  --upgrade -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0", "app:create_app()"]
