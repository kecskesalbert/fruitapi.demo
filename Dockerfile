FROM debian:stable-slim
LABEL org.opencontainers.image.source=https://github.com/kecskealbert/fruitapi.demo
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt -y update
RUN apt -y install python3 python3-pip
RUN pip install --no-cache-dir --only-binary :all: --break-system-packages "fastapi[standard]"
COPY src /app
