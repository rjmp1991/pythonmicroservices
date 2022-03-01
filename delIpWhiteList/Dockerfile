FROM alpine
LABEL mainteiner="Rafael Jose Montoya <rjmp1991@gmail.com>"
LABEL Description="API TOR delip" Vendor="RafaelMontoya" Version="1"
ENV TZ=America/Bogota
USER root
RUN mkdir -p /home/appuser && HOME=/home/appuser && chmod -R 0755 /home/appuser && addgroup -S -g 10101 appuser && adduser -u 101010 -S -D -s /sbin/nologin -h /home/appuser -G appuser appuser
WORKDIR /home/appuser
COPY delip.py requirements.txt ./
RUN apk update --no-cache && apk add python3 && apk add py3-pip && pip install --no-cache-dir -r requirements.txt
USER appuser
EXPOSE 8084
CMD [ "python3", "delip.py"]