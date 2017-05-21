#!/bin/bash

docker build -t flask_web_server .
docker rm -f flask_web_server
docker run --name flask_web_server -t -p 127.0.0.1:5000:5000
