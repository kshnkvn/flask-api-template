FROM python:3.8-alpine

WORKDIR /usr/app/

COPY ./requirements.txt /usr/app/requirements.txt

RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    python -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

EXPOSE 5000

COPY . /usr/app/

ENTRYPOINT ["python"]

CMD [ "wsgi.py" ]
