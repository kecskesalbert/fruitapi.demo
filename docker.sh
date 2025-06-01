#!/bin/sh

NAME="kecskesalbert/fruitapi.demo"
VERSION="v1"
PORT=8001
REGISTRY="ghcr.io"
USERNAME=kecskesalbert
# CR_PAT must contain the GitHub access token

cmd=$1
shift

case "$cmd" in
  clean)
	set -x
    docker container prune --force --filter "label=$REGISTRY/$NAME:$VERSION"
    docker image rm $REGISTRY/$NAME:$VERSION "$@"
    docker image rm $REGISTRY/$NAME:latest "$@"
    ;;

  build)
    docker build . --tag $REGISTRY/$NAME:$VERSION --tag $REGISTRY/$NAME:latest "$@"
	docker images --filter "reference=$REGISTRY/$NAME:$VERSION"
    ;;

  run)
    docker run -it \
        -p $PORT:8000 \
        -e CONTAINER_NAME=$NAME \
        -e CONTAINER_VERSION=$VERSION \
        $REGISTRY/$NAME:$VERSION \
        fastapi run /app/main.py "$@" && \
    docker container rm $(docker ps -q --all --filter "ancestor=$REGISTRY/$NAME:$VERSION")
    ;;

  shell)
    docker exec -it $(docker ps -q --filter "ancestor=$REGISTRY/$NAME:$VERSION") /bin/bash
    ;;

  logs)
    docker container logs $(docker ps -q --all --filter "ancestor=$REGISTRY/$NAME:$VERSION")
    ;;

  push)
	set -e
	set -x
	docker login ghcr.io -u USERNAME --password $CR_PAT
    docker push $REGISTRY/$NAME:$VERSION
    ;;

  *)
    echo "Correct usage is:"
    echo "    docker.sh build [<docker build arguments, e.g. --no-cache>]"
    echo "              clean [--force]"
    echo "              run [<app run arguments>]"
    echo "              shell"
    echo "              logs"
    echo "              push"
  ;;

esac
