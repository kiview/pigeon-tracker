#!/usr/bin/env bash

docker run -it \
    --rm \
    -p 8888:8888 \
    -v $(pwd):/pigeon-tracker \
    --workdir /pigeon-tracker \
    pigeon-tracker \
    jupyter lab --ip=0.0.0.0
