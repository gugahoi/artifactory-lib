#!/usr/bin/env bash

set -e

function cleanup {
    rm ~/.pypirc
}

trap cleanup EXIT

echo "[server-login]" > ~/.pypirc
echo "username:" ${PYPI_USER} >> ~/.pypirc
echo "password:" ${PYPI_PASSWORD} >> ~/.pypirc

docker run \
    -v $(pwd):/root/app \
    -v ~/.pypirc:/root/.pypirc \
    -w /root/app \
    python:2.7 \
    python setup.py sdist upload
