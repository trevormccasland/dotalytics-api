FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "dotalytics_api.main:main", "--host", "0.0.0.0", "--port", "8888"]
