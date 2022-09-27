FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "app:app"]