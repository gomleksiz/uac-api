#!/bin/bash

export DEBIAN_FRONTEND=noninteractive

wget https://github.com/aquasecurity/trivy/releases/download/v0.51.1/trivy_0.51.1_Linux-64bit.deb
sudo dpkg -i trivy_0.51.1_Linux-64bit.deb
sudo rm -vf trivy_0.51.1_Linux-64bit.deb

trivy --version
