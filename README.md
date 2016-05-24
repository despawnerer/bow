Bow
===

Bow is a CLI utility to manage isolated environments for your projects using Docker to avoid conflicts between dependencies, different versions of interpreters etc. It's like `virtualenv` + `virtualenvwrapper` or `pew`, but language-agnostic and even more isolated.


Requirements
============

- python 3
- docker


Setup
=====

1. Install.
2. Set `PROJECT_HOME` environment variable to the folder where your projects reside.


Usage
=====

- `bow create <-i IMAGE | -b> <name>`
- `bow rm <name>`
- `bow enter <name>`
- `bow cd <name>`
- `bow stop <name>`


Caveats
=======

- Docker containers created by `bow` for your projects need to be manually stopped when you stop using them. Otherwise, they will be kept running forever.
- There is no easy way to use e.g. `python` interpreter that is installed within the container from the host system (for code completion, for example), unless you're using something like PyCharm which has that feature out of the box.
- This is pre-release software, so use at your own risk.
