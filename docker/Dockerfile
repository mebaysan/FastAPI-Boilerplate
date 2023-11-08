FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ../src/ .

RUN pip install --upgrade pip  

RUN pip install -r requirements.txt

RUN mkdir -p /var/log/myapp/myapp.log

RUN chmod 777 /var/log/myapp/myapp.log

RUN touch /var/log/myapp/myapp.log

RUN chmod 777 /var/log/myapp/myapp.log

EXPOSE 8000  

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget -qO- http://localhost:8000/healthcheck/ || exit 1

ENTRYPOINT [ "bash", "entrypoint.sh" ]