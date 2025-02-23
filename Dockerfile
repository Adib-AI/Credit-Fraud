FROM python:3.9

WORKDIR /app

# Menyalin requirements.txt ke dalam container dengan nama yang benar
COPY requirements.txt /requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /requirements.txt

# Menyalin semua file ke dalam container
COPY . .

# Menjalankan FastAPI dengan Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]