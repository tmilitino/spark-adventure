FROM openjdk:11-jdk

RUN mkdir /woker
RUN mkdir /opt/spark

ENV SPARK_HOME /opt/spark

RUN apt update

RUN  apt install -y python3-pip

RUN apt install -y wget

RUN wget https://archive.apache.org/dist/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz

RUN tar zxvf spark-3.1.2-bin-hadoop3.2.tgz

RUN mv spark-3.1.2-bin-hadoop3.2/* /opt/spark/

ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

RUN export SPARK_HOME

RUN python3 -m pip install pyspark

COPY ./entrypoint.sh /woker/entrypoint.sh