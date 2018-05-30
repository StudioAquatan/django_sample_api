FROM alpine:3.7

ENV PROJECT_DIR /opt/sample_api

COPY ./ ${PROJECT_DIR}

WORKDIR ${PROJECT_DIR}

RUN apk update && \
    apk add --no-cache \
        python3 \
        zlib-dev \
        libjpeg-turbo-dev \
        musl-dev && \
    apk add --no-cache --virtual=build_dep \
        python3-dev \
        gcc \
        tzdata \
        linux-headers && \
    pip3 install --upgrade pip && \
    pip3 install pipenv && \
    pipenv install --three && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del --purge build_dep && \
    rm -rf /var/cache/apk/*

WORKDIR ${PROJECT_DIR}/src

CMD ["pipenv", "run", "uwsgi", "--ini", "uwsgi.ini"]