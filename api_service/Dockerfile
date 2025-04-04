FROM openjdk:21-jdk-slim

ARG STAGE=${STAGE}
WORKDIR /app

RUN apt-get update && apt-get install -y maven

COPY config/${STAGE}/pom.xml .
RUN mvn dependency:resolve

COPY config/${STAGE}/.env .
ENTRYPOINT export $(xargs < .env) && mvn spring-boot:run