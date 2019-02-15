FROM ubuntu:16.04

COPY geckodriver-v0.24.0-linux64.tar.gz /

RUN apt-get update \
		&& apt-get -y upgrade \
		&& apt-get -y install software-properties-common \
		&& apt-add-repository ppa:mozillateam/firefox-next \
		&& apt-get install -y firefox xvfb python3 python3-pip \
		&& tar -xvzf geckodriver-v0.24.0-linux64.tar.gz \
		&& chmod +x geckodriver \
		&& cp geckodriver /usr/local/bin/ \
		&& mkdir CCMA

RUN Xvfb :10 -ac &
ENV DISPLAY=:10

COPY requirements.txt consultas_salud.csv eleconomista.py /CCMA/

RUN pip3 install -r /CCMA/requirements.txt

VOLUME /Users/jorgequintana/Desktop/CCMA /CCMA

WORKDIR /CCMA

CMD python3 eleconomista.py
