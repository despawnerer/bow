Bow
===

[![PyPI version](https://badge.fury.io/py/bow.svg)](https://badge.fury.io/py/bow)

Bow is an experimental CLI utility to manage isolated environments for your projects using Docker to avoid conflicts between dependencies, different versions of interpreters etc. It's like `virtualenv` + `virtualenvwrapper` or `pew`, but language-agnostic and even more isolated.


Requirements
------------

- python 3
- docker


Setup
-----

1. `pip3 install bow`
2. Set `PROJECT_HOME` environment variable to the folder where your projects reside.


Usage
-----

### Create a project

    bow create -i IMAGE PROJECT_NAME
    
### Enter project's container

    bow enter PROJECT

### Switch to the project's directory on the host

    bow cd PROJECT
    
### Remove project

    bow rm PROJECT
    
### Stop project's container

    bow stop PROJECT


Caveats
-------

- Docker containers created by `bow` for your projects need to be manually stopped when you stop using them. Otherwise, they will be kept running forever.
- There is no easy way to use e.g. `python` interpreter that is installed within the container from the host system (for code completion, for example), unless you're using something like PyCharm which has that feature out of the box.
- It always runs `bash` inside the container.
- This is experimental software, so use at your own risk.
