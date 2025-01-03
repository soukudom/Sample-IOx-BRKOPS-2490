# Use quemu to emulate arm architecture on x86_64 based architecture
#FROM multiarch/qemu-user-static:x86_64-aarch64 as qemu
FROM arm64v8/alpine:latest

# Copy QEMU binary into the ARM64 image
#COPY --from=qemu /usr/bin/qemu-aarch64-static /usr/bin

RUN apk --no-cache add python3 py3-pip py3-bottle

EXPOSE 8000 
COPY main.py /main.py 
CMD ["python3", "/main.py"]

