#! /bin/bash

gunicorn main:app --bind 0.0.0.0:8000 -w 4 -k uvicorn.workers.UvicornWorker