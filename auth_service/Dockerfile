FROM python:3.11

ARG STAGE=${STAGE}

COPY config/${STAGE}/.env ./
COPY requirements/${STAGE}/requirements.txt ./

RUN pip3 install -r requirements.txt
WORKDIR /app

ENTRYPOINT export $(xargs < .env) && python manage.py makemigrations && \
           python manage.py migrate && python manage.py runserver
