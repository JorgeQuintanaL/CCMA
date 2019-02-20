FROM python

RUN mkdir CCMA

COPY requirements.txt gogle.py /CCMA/

RUN pip install -r /CCMA/requirements.txt

WORKDIR /CCMA

CMD python eleconomista.py
