FROM telegraf:latest

WORKDIR /root

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
 DEBIAN_FRONTEND=noninteractive apt-get install -y python3 && \
 DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y python3-pip && \
 python3 -m pip install line-protocol-parser --break-system-packages --no-cache-dir && \
 rm -rf /var/lib/apt/lists/*

EXPOSE 8125/udp 8092/udp 8094

ENTRYPOINT ["/entrypoint.sh"]
CMD ["telegraf"]

