FROM python:3.10-slim

Expose 8082

WORKDIR /app

COPY ./app.py /app/app.py
COPY ./bestmodel.pkl /app/bestmodel.pkl
COPY ./features.yaml /app/features.yaml
COPY ./loc_kmeans.pkl /app/loc_kmeans.pkl
COPY ./build_features.py /app/build_features.py
COPY ./logger.py /app/logger.py
COPY ./predictor.py /app/predictor.py
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
