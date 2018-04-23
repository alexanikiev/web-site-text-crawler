FROM python:3.6

ADD requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

ADD src /app/src

WORKDIR /app/src

EXPOSE 8000
CMD python3 -m sanic server.app --host=0.0.0.0 --workers=2
