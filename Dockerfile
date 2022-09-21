FROM python:3.7

RUN pip install pytest pytest-cases pytest-rerunfailures
RUN apt-get -y update
RUN apt install -y libsm6 \
                libxext6 \
                ffmpeg \
                libfontconfig1 \
                libxrender1 \
                libgl1-mesa-glx \
                libgeos-dev

WORKDIR /usr/src/labelbox
COPY requirements.txt /usr/src/labelbox
RUN pip install -r requirements.txt
COPY setup.py README.md  /usr/src/labelbox/
COPY labelbox/ /usr/src/labelbox/labelbox/
COPY tests/ /usr/src/labelbox/tests/

RUN python setup.py install
