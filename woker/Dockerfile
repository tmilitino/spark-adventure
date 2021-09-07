FROM openjdk:8-jdk-alpine

RUN apk --update add wget tar bash coreutils procps openssl

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

RUN wget https://archive.apache.org/dist/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz

RUN tar zxvf spark-3.1.2-bin-hadoop3.2.tgz
RUN ls
RUN mv spark-3.1.2-bin-hadoop3.2/ /opt/spark

RUN python3 -m pip install pyspark

RUN mkdir /woker

COPY ./entrypoint.sh /woker/entrypoint.sh