FROM python:3.8.7-alpine

ENV PYTHONUNBUFFERED 1

ENV ENV /etc/profile

ADD profile.d/* /etc/profile.d/

ADD . /app

WORKDIR /app

RUN apk update \
    && apk add --virtual .build-deps gcc g++ python3-dev musl-dev make curl \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python \
    && source $HOME/.poetry/env \
    && poetry install --no-root --no-interaction --no-ansi --no-dev \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

COPY ./entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
