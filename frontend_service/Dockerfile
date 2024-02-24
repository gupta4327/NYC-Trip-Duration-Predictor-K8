from python:3.10-slim

Expose 8080

WORKDIR /app

COPY ./static /app/static
COPY  ./templates /app/templates
COPY ./app.py /app/app.py
COPY ./logger.py /app/logger.py
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "app.py"]