#!/bin/bash

export DEBIAN_FRONTEND=noninteractive

apt install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /tmp/docker-archive-keyring

sudo gpg \
    --no-tty \
    --batch \
    --yes \
    --no-permission-warning \
    --dearmor \
    -o /usr/share/keyrings/docker-archive-keyring.gpg \
    /tmp/docker-archive-keyring

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

apt update -y

apt install -y \
    docker-ce \
    docker-ce-cli \
    containerd.io

usermod -aG docker vagrant

curl -fsSL \
    "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" \
    -o /usr/local/bin/docker-compose

chmod -v +x /usr/local/bin/docker-compose

systemctl enable --now docker
