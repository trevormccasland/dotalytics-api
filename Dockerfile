FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt

COPY ./dotalytics_api /app/dotalytics_api

ENTRYPOINT ["uvicorn", "dotalytics_api.main:main", "--host", "0.0.0.0", "--port", "8888"]