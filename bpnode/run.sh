#!/bin/bash

DATA_DIR=/data/eos/nodeos-data-volume/nodeos-data-bostest
mkdir -p $DATA_DIR/data
cp -r config $DATA_DIR

docker-compose -f docker-compose-bostest-init.yaml up -d