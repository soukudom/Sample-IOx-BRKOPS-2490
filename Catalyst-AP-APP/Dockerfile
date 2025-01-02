#FROM multiarch/qemu-user-static:x86_64-aarch64 as qemu
FROM arm64v8/alpine:latest
#COPY --from=qemu /usr/bin/qemu-aarch64-static /usr/bin

RUN apk --no-cache add python3 py3-pip dhclient py3-bottle

EXPOSE 8000 
COPY main.py /main.py 
COPY init.sh /init.sh 
CMD ["/bin/sh", "/init.sh"]

