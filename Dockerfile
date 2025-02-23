FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /code/requirements.txts

RUN pip install -r /code/requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]