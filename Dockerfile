from python:3.7

WORKDIR /usr/src/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app app/

ENTRYPOINT [ "python"]