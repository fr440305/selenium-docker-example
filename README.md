# `selenium-docker-example`

## Quick Start

First make sure that `docker`, `python` (3.8+), and `poetry` are available:

```
docker --version
python3 --version
python3 -m pip --version
poetry --version  # Make sure that poetry is installed correctly and can be directly invoked from command line.
```

Then setup dependencies:

```
poetry install
sudo docker run -p 4444:4444 -p 5900:5900 --shm-size=2g selenium/standalone-chrome-debug

# On a new terminal session:
poetry run python -m seleniumdockerexample
```
