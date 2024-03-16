FROM python:3-alpine
COPY . /opt 
WORKDIR /opt
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "server.py"]
