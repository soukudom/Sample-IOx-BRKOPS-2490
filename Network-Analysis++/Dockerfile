FROM rockylinux:9

RUN dnf install -y dnf-plugins-core && \
    dnf copr -y enable @CESNET/NEMEA && \
    dnf copr -y enable @CESNET/ipfixprobe && \
    dnf install -y epel-release && \
    dnf install -y ipfixprobe-nemea ipfixprobe-input-pcap ipfixprobe-nemea-process-experimental && \
    dnf install -y ipfixprobe-nemea-output-unirec nemea && \
    dnf clean all

RUN dnf install -y tcpdump
RUN dnf install -y dhclient
RUN dnf install -y net-tools

CMD ["tail", "-f", "/dev/null"]
