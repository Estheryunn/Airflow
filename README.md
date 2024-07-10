## Requirements

The minimum requirements:

Docker for Mac: Docker >= 20.10.2

Docker for Windows:

Installation: Docker

Manual installation steps for older WSL version: Docker WSL 2

## Instructions

Create a DockerFile which fetches a docker image to setup airflow on your local machine:

FROM puckel/docker-airflow

Information about the image we are using can be found here: https://github.com/puckel/docker-airflow

If you have already launched airflow webserver, you need to kill all containers to use port number 8080 to host airflow:

docker stop $(docker ps -a -q)

Build a docker image called local-airflow on your local machine:

docker image build -t local-airflow .

Run airflow on port number 8080: docker run -d -p 8080:8080 local-airflow webserver

Access airflow webserver at http://localhost:8080