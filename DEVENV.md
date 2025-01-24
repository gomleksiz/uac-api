# Development environment

## Introduction

This project comes with a fully set up development environment. Included are
all the tools that developers need to start working on this project. Among other things it includes:

+ `pyenv`

    [pyenv](https://github.com/pyenv/pyenv) is a Python version manager which
    makes installing and working with multiple Python versions convenient.
    By default the following version of Python are installed:
    - _Python 3.7_
    - _Python 3.11_

    More versions can be installed as needed with `pyenv` by doing `pyenv install <version>`.
    For example to install the (currently) newest version of Python which is 3.12 simply run:
    ```bash
    $ pyenv install 3.12
    ```

+ `trivy`

    [trivy](dev) an open source vulnerability scanner. It can be used to scan
    your project for known vulnerabilities and misconfigurations.

+ `docker`

## Setup

### Requirements

In order to properly setup to development environment the following
dependencies are needed:

+ internet connection
+ at least **20Gb** of free disk space
+ `vagrant` - version _2.4.1_
+ `VirtualBox` - version _7.0.20_


### Initialization

To initialize the virtual machine navigate to the directory where this file is
located and run:
```bash
$ vagrant up
```
This will start the installation process. It can take several minutes to fully
complete.

## Environment

### Connecting

Once the installation process has completed the VM is ready to use. To access
it simply ssh into it by running:
```bash
$ vagrant ssh
```
Or for an advanced but more flexible setup run:
```bash
$ vagrant ssh-config
```
This will output a configuration section for `OpenSSH` which can be placed
inside `~/.ssh/config` and further customized.

### Configuration

Once connected this project can be found under `/vagrant`. For convenience it
may be symlinked to the user's home directory by running:
```bash
$ ln -s /vagrant ~/uac-api
```

### Environment variables

To build the project developers need access to our instance of
[Gitlab](https://gitlab.stonebranch.com/). This is where the project upstream
is located alongside any dependencies required.
For the build process to correctly fetch and install the needed dependencies
two environment variables need to be set, `REQUIREMENTS_GITLAB_USER` and
`REQUIREMENTS_GITLAB_PASS` which container your username and password
respectively. The easiest way to do this is to export them from your
`~/.bashrc` by appending the following lines:

```bash
    export REQUIREMENTS_GITLAB_USER='user.name'
    export REQUIREMENTS_GITLAB_PASS='password'
```

### Git hooks

This project comes with some useful Git hooks to perform various checks like
code formatting and checking if the commit message adheres to a specific
format. To install them simply:

```bash
    pip install -r requirements_dev.txt
    pre-commit install -t pre-commit -t commit-msg
```

Some hooks can be bypassed if needed by passing the `-n`, `--no-verify` flag
to `git commit`
