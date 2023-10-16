# FastAPI Base for Development

## Pipenv

* Use pipenv in the root to prepare the requirements.txt

### Create virtual environment
``$ pipenv shell``

### Install package(s)
``$ pipenv install {package-name}``

### Create requirements.txt
``$ pipenv requirements > requirements.txt``

## Docker Compose

### Start Docker Containers
``$ docker compose up -d [--build]``

Options:<br>
``-d``          for detached<br>
``--build``     to build the container

### Stop Docker Containers
``$ docker compose down``

### Enter Container
``$ docker exec -it {container-name} [sh|bash]``
