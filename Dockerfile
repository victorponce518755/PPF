FROM python:3


ENV PYTHONBUFFERED TRUE

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./


RUN pip install -r requeries.txt
RUN pip install Flask gunicorn


CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 PPF.app:app

