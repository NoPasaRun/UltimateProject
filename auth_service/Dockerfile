FROM python:3.11

ARG STAGE=${STAGE}

COPY requirements/${STAGE}/requirements.txt ./
COPY config/${STAGE}/.env ./

RUN pip3 install -r requirements.txt

ENTRYPOINT export $(xargs < .env) && python app/manage.py makemigrations && \
           python app/manage.py migrate && python app/manage.py runserver 0.0.0.0:2288
