FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt

ENTRYPOINT ["uvicorn", "dotalytics_api.main:main", "--host", "0.0.0.0", "--port", "8888"]
