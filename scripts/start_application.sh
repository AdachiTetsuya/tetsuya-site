#!/bin/sh
set -e
systemctl restart gunicorn.service nginx.service
