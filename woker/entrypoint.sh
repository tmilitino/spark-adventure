#!/usr/bin/env bash

spark-class org.apache.spark.deploy.worker.Worker -c 1 -m 512M spark://${MASTER_HOST}:7077

