FROM python

RUN mkdir CCMA

COPY requirements.txt twitter.py /CCMA/

RUN pip install -r /CCMA/requirements.txt

WORKDIR /CCMA

CMD python twitter.py
