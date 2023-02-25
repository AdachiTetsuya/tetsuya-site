#!/bin/sh
set -e
SCRIPT_DIR=$(
	cd "$(dirname "$0")"
	echo "$PWD"
)
BASE_DIR=${SCRIPT_DIR%/*}
sudo cp -f "$BASE_DIR/data/gunicorn.service" /etc/systemd/system/
rm /etc/nginx/sites-enabled/*
cp "$BASE_DIR/data/nginx.conf" /etc/nginx/sites-enabled/tetsuya-site
