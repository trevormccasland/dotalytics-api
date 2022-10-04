FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "dotalytics_api.main:app", "--host", "0.0.0.0", "--port", "8888"]
