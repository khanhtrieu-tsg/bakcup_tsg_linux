#!/bin/bash
app="docker.license"
docker build -t ${app} .
docker run -d -p 88:80 \
  --name=${app} \
  -v $PWD:/app ${app}
