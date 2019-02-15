FROM ubuntu:16.04

RUN apt-get update \
		&& apt-get install -y libasound2 libnspr4 libnss3 libxss1 xdg-utils unzip lsb-release \
		&& apt-get install -y libappindicator1 fonts-liberation wget python3 python3-pip \
		&& wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
		&& dpkg -i google-chrome*.deb \
		&& wget https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip \
		&& unzip chromedriver_linux64.zip \
		&& mv chromedriver /usr/bin/chromedriver \
		&& chown root:root /usr/bin/chromedriver \
		&& chmod +x /usr/bin/chromedriver \
		&& mkdir CCMA

COPY requirements.txt eleconomista.py /CCMA/

RUN pip3 install -r /CCMA/requirements.txt

VOLUME /Users/jorgequintana/Desktop/CCMA /CCMA

WORKDIR /CCMA

CMD python3 eleconomista.py
