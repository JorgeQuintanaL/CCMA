FROM python

RUN mkdir CCMA

COPY requirements.txt google.py /CCMA/

RUN pip install -r /CCMA/requirements.txt

WORKDIR /CCMA

CMD python google.py
