FROM python:3-alpine
RUN adduser -D -u 1000 pyuser
WORKDIR /opt
COPY --chown=1000:1000 . /opt 
USER pyuser
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "server.py"]
