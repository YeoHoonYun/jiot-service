FROM python:3

COPY ha_service_v3.py /usr/src/
COPY ha_service /usr/src/
WORKDIR /usr/src

RUN apt install tzdata
RUN TZ='Asia/Seoul'; export TZ
#RUN apt-get install -y git

# update pip
RUN python3 -m pip install pip --upgrade
RUN python3 -m pip install wheel
RUN python3 -m pip install paho-mqtt
RUN python3 -m pip install sseclient

CMD ["python3", "ha_service_v3.py"]
