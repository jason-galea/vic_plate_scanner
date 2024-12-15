#!/usr/bin/bash


echo "==> Build latest docker image"
docker build . --tag vic_plate_scanner


if [ $(docker images | grep '<none>' | wc -l) -ne 0 ]; then
    echo "==> Remove previous docker images"
    docker images | grep '<none>' | awk '{print $3}' | xargs docker image rm
fi


echo "==> Scan!"
docker run --rm -v ./src:/src/ vic_plate_scanner python3 /src/vic_plate_scanner.py
