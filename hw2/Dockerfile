FROM python:3.5-alpine
WORKDIR /work
ADD . /work
RUN pip install -r /work/requirements.txt
VOLUME /work
EXPOSE 8080
CMD ["/bin/sh", "/work/run.sh"]
