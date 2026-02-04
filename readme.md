# Git bash version
## YouTube Link
For the full 1 hour course watch on youtube:
https://www.youtube.com/watch?v=6YZvp2GwT0A

# Installation
## Build the Jenkins BlueOcean Docker Image (or pull and use the one I built)
```bash
docker build -t myjenkins-blueocean:2.414.2 .

#IF you are having problems building the image yourself, you can pull from my registry (It is version 2.332.3-1 though, the original from the video)

docker pull devopsjourney1/jenkins-blueocean:2.332.3-1 && docker tag devopsjourney1/jenkins-blueocean:2.332.3-1 myjenkins-blueocean:2.332.3-1
```
các version ở trên không dùng được ở máy tui - cái này Docker in Docker

```bash
  docker run --name jenkins-blueocean --restart=on-failure --detach \
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  jenkins/jenkins:lts-jdk21
```

## Create the network 'jenkins'
```
docker network create jenkins
```

## Run the Container
### MacOS / Linux
```
docker run --name jenkins-blueocean --restart=on-failure --detach \
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins-blueocean:2.332.3-1
```

### Windows
```
docker run --name jenkins-blueocean --restart=on-failure --detach `
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 `
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 `
  --volume jenkins-data:/var/jenkins_home `
  --volume jenkins-docker-certs:/certs/client:ro `
  --publish 8080:8080 --publish 50000:50000 myjenkins-blueocean:2.414.2
```


## Get the Password (on gitbash)
``` bash
docker exec jenkins-blueocean cat //var/jenkins_home/secrets/initialAdminPassword
```
or using docker logs (faster)
```bash
docker logs jenkins-blueocean
```


## Connect to the Jenkins
```
https://localhost:8080/
```

## Installation Reference:
https://www.jenkins.io/doc/book/installing/docker/


## alpine/socat container to forward traffic from Jenkins to Docker Desktop on Host Machine

https://stackoverflow.com/questions/47709208/how-to-find-docker-host-uri-to-be-used-in-jenkins-docker-plugin
```
docker run -d --restart=always -p 127.0.0.1:2376:2375 --network jenkins -v /var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock
docker inspect <container_id> | grep IPAddress
```

## Using my Jenkins Python Agent
```
docker pull devopsjourney1/myjenkinsagents:python
```

## some more
- find a port with its PID
```bash
netstat -ano | findstr :8080  
```
- kill a task with its PID (Git Bash on administrator)
```bash
taskkill //F //PID 21100
```
- remove an docker container
```bash
docker rm jenkins-blueocean
```

- 431 Request Header Fields Too Large on Jenkins (because of cookies) => delete cookie or open an private tab

- to add another url in a previously committed repo
```bash
git remote set-url origin https://github.com/trandongtruclam/jenkins-101.git
```

- choosing POLL SCM: 2 phút sẽ kiểm tra github 1 lần, có code push lên sẽ tự chạy build
```bash
H/2 * * * *
```

## Docker
- image just an artifact that can not run the app itself

```bash 
docker build -t book-service:latest .

or

docker build -t book-service:v1.0 .

```


- detached mode (starting in the background instead of in the terminal )
``` bash
docker run -d -p 3000:3000 --name book-service-v.1.0 book-service 
```
``` bash
docker run -d -p 8080:3000 book-service book-service 
// expose 3000 express server to 8080 
logs:
$ docker run -d -p 8080:3000 --name book-service-v2.0 book-service
0c26317e7159d77f7b268032ea24bb8f1b23e319ae135a6231bdb1140cc18c41
docker: Error response from daemon: ports are not available: exposing port TCP 0.0.0.0:8080 -> 127.0.0.1:0: listen tcp 0.0.0.0:8080: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted.

docker run -d --name book-service-v1.0 book-service (name container - image)
// (named the container instead of the random string)
```

- execute the container in bash, it - interact with process inside the window

```bash
docker exec -it book-service-v2.0 bash
```

- connect mongodb 
```bash
mongodb://book-service-db:27017/books
```

- remove dangling images
```bash
docker image prune
```

- List all container in use
```bash
docker ps -a
```
