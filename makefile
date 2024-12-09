IMAGE_NAME = ioet-houses-bot-listener
CONTAINER_NAME = ioet-houses-bot-listener-container
PORT = 8000

build:
    docker build -t $(IMAGE_NAME) .

run:
    docker run --env-file .env -p $(PORT):$(PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME)

stop:
    docker stop $(CONTAINER_NAME)

rm:
    docker rm $(CONTAINER_NAME)

rebuild: stop rm build run