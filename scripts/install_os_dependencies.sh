#!/bin/sh
set -e
apt-get update
apt-get install -y --no-install-recommends \
	build-essential \
	libpq-dev \
	nginx \
	python3-dev \
	python3-venv
systemctl stop nginx
