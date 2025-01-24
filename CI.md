# Continuous Integration

<!--toc:start-->
- [Continuous Integration](#continuous-integration)
  - [Introduction](#introduction)
  - [CI Design](#ci-design)
  - [CI Environment](#ci-environment)
    - [Available Python versions](#available-python-versions)
    - [Storing artifacts](#storing-artifacts)
    - [Jenkinsfile options](#jenkinsfile-options)
  - [CI Stages](#ci-stages)
    - [Linting stage](#linting-stage)
    - [Testing stage](#testing-stage)
    - [Build stage](#build-stage)
    - [Vulnerability scan](#vulnerability-scan)
    - [SonarQube scan](#sonarqube-scan)
  - [Common `tox.ini` options](#common-toxini-options)
<!--toc:end-->

Before continuing readers are encouraged to familiarize themselves with
[tox](https://tox.wiki/en/stable/index.html).

## Introduction

This project uses [tox](https://tox.wiki/en/stable/index.html) as a Continuous
Integration (CI) frontend, allowing developers to easily modify and extend the
functionality of the pipeline. In addition to this, pretty much everything that
runs on the pipeline can be ran locally by invoking the same `tox` command that
is invoked by the pipeline.

For example, to run the linting stage to make sure the code is formatted
accordingly before committing:
```bash
$ tox run -m linting
```

A new pipeline run will be automatically started when doing a `push`, `merge`
or creating a new merge request.

## CI Design

The pipeline was designed to be as flexible as possible. It relies heavily on
the `tox.ini` file. This is where the logic for building, testing and linting
your project is placed. Specifically each action you want to perform is placed
inside a `tox` test environment. A minimal `tox.ini` file with one test
environment that just runs `pylint` on your project looks like the following:
```ini
[testenv:lint]
deps = pylint
commands =
    pylint {tox_root}/uac_api
```

Test environments can be logically grouped by adding labels to them. A label is
like a group that a test environment is part of. You can have as many labels as
you want. Take for example the following `tox.ini` file:

```ini
[testenv:check_formatting]
labels =
    linting
    formatting
description = check code formatting
skip_install = true
deps =
    black==22.3.0
    isort==5.11.5
commands =
    isort --profile black --check --diff {tox_root}/uac_api
    black -l 88 --check --diff --quiet {tox_root}/uac_api

[testenv:lint]
labels = linting
description = run pylint
skip_install = true
deps = pylint
commands =
    pylint {tox_root}/uac_api
```

In the example above there are two test environments, `check_formatting` and
`lint`. The first runs formatting checks on the code using `black` and `isort`
and the second one runs `pylint`. Both have the `linting` label to indicate
that these test environments are logically related to linting the source code.
These can both be executed one after the other by running the following
command:
```shell
$ tox run -m linting
```

Labels are a key part of the pipeline design. To keep code quality high
developers must implement tree labels with at least on test environment each
inside of the `tox.ini` file.

These labels are:
+ **linting** - everything related to linting and stylistic checks
+ **unit_tests** - everything related to testing, ex. running `pytest`
+ **build** - everything related to building and packaging your project
  (creating wheel files, building binaries, etc)

As mentioned above, at least one test environment must be implemented for each
label. Additional test environments may be implemented for these labels and
they will be ran as well when running the pipeline.

## CI Environment

### Available Python versions

During pipeline runs, `tox` test environments will have access to the following Python versions:
- *Python 3.7*
- *Python 3.8*
- *Python 3.9*
- *Python 3.10*
- *Python 3.11*
- *Python 3.12*

### Storing artifacts

Developers are provided the functionality to store artifacts (test/coverage
reports, project builds, etc) from the pipeline run. All `tox` test
environments will have access to an `artifacts/` directory at the top of the
project, where files can be placed which later will be stored as artifacts on
the pipeline. A directory with the same name **should not** be included in this
repository with `git` as it will conflict with the one that is available during
pipeline runs.

### Jenkinsfile options

The following options can be placed inside the function call inside of the
`Jenkinsfile` and can influence the pipeline behavior.

- `strict`
When a pipeline is executed from a branch that is not either `main` or
`develop` the error checking is more lenient. If for example the `linting`
stage fails it will be marked as _UNSTABLE_ and execution will carry on instead
of the pipeline failing and stopping at the stage that fails. By setting the
`strict: true` flag it the pipeline will stop and fail at any error it
encounters.

- `build_run_windows`
By default all stages run on a Linux environment. By setting
`build_run_windows: true` it will make the pipeline execute test environments
marked with the `build` label on a Windows machine as well. This is useful for
creating binaries or Windows specific wheel files.

## CI Stages

### Linting stage

This is where test environments with the `linting` label will be executed

### Testing stage

This is where test environments with the `unit_tests` label will be executed

### Build stage

This is where test environments with the `build` label will be executed

### Vulnerability scan

In this stage the requirements of the project are scanned for vulnerabilities.
The scan is performed using [trivy](https://trivy.dev/). The scanner expects a
`requirements.txt` file at the root of your project structure (where the
`tox.ini` file is) which lists all the top level depenendencies of your project.
If any of the depenendencies or sub-depenendencies have a CVE with a severity
greater than _MEDIUM_ this stage will fail.

### SonarQube scan

This stage performs a more detailed scan and analysis of the source code using `SonarQube`.
Scan results can be viewed on the `SonarQube` dashboard. If any critical issues are found
it will cause the pipeline to fail.

## Common `tox.ini` options
- `skip_install`

    When executing test environments `tox` will be default
    install your package as well alongside any depenendencies specified, if this
    option is set to `true` it will skip installing your package. This is useful
    if the test environment doesn't need your package to be installed.

- `skip_missing_interpreters`

    Test environments can be specified in a way as to run multiple times for each Python version given.
    Take for example the following test environment definition
    ```ini
    [testenv:py{37,311}-tests]
    ```

    The above definition will be expanded into `[testenv:py37-tests]` and
    `[testenv:py311-tests]`. Each will run with the specified Python version
    (in this case 3.7 and 3.11). If the version of Python isn't found on your
    system the test environment will fail. Setting `skip_missing_interpreters`
    to `true` will make `tox` skip test environment instead of failing it.

- `passenv`

    By default `tox` won't pass along any environment variables to test environment. These must be manually specified, like so:
    ```ini
    passenv =
        REQUIREMENTS_GITLAB_USER
        REQUIREMENTS_GITLAB_PASS
    ```

A full list of all available configuration options can be found in the tox
[configuration](https://tox.wiki/en/stable/config.html#) section.
