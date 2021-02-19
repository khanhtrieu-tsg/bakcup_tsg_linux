#!/bin/bash
app="docker.test.tesst.license"
docker build -t ${app} .
docker run -d -p 56734 \
  --name=${app} \
  -v $PWD:/app ${app}
