FROM ubuntu:18.04

RUN apt-get -yq update && apt-get -yq upgrade \
&& apt-get -y install python3 \
&& apt-get -y install python-pip \
&& apt-get -y install python-dev \
&& alias python=python3 \ 
&& apt-get -y install ipython3

ADD . /app/

WORKDIR /app/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD export FLASK_APP=hello.py \
&& flask run --host=0.0.0.0
