#!/bin/sh
set -e
cd /home/ubuntu/tetsuya-site
sudo chown -R ubuntu:ubuntu /home/ubuntu/tetsuya-site
python3 -m venv .venv
. .venv/bin/activate
pip install -U pip setuptools wheel --no-cache
pip install -U -r requirements.txt --no-cache
pip install -U gunicorn --no-cache
./manage.py migrate
