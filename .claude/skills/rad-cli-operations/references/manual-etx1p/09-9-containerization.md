# 9 Containerization

*Manual `ETX-1p_6.4_Mn_05-26_GA.pdf`, pages 629–635.*


## 9.1 Applicability and Scaling  *(p.629)*


## 9.2 Functional Description  *(p.629)*

ETX-1p features deployment of docker containers. The docker management is performed via the Docker 
native CLI, accessed via a ‘linux-tech’ user. 
A container is a standard unit of software that packages up code and all its dependencies, so that the 
application runs quickly and reliably from one computing environment to another. Everything within a 
container is preserved on something called an image – a code-based file that includes all libraries and 
dependencies. 
A Docker container image is a lightweight, standalone, executable package of software that includes 
everything needed to run an application: code, runtime, system tools, system libraries and settings. 
9.1 Applicability and Scaling 
In the current version, the docker management is performed via the Docker native CLI only.  
9.2 Functional Description 
Architecture and Components 
The docker architecture is shown in the figure below. 
9. Containerization 
 
Docker uses a client-server architecture. The Docker client talks to the Docker Daemon, which creates 
and maintains the docker containers. Docker Daemon listens for Docker API requests and manages 
Docker objects such as images, containers, networks, and volumes. 
The Docker client is the primary way that many Docker users interact with Docker (when you use 
commands such as docker run, the client sends these commands to dockerd (docker Daemon), which 
carries them out. The docker command uses the Docker API. The Docker client can communicate with 
more than one daemon. 
A Docker registry stores Docker images. Docker Hub is a public registry that anyone can use, and Docker 
is configured to look for images on Docker Hub by default. You can even run your own private registry. 
Docker Container Main Components 
The main docker container components are as follows: 
• 
Image. The image is pulled from the registry and is build of layers (marked as tags) – each layer 
is a version (tag) containing only the updates – hence the upgrade has small size. 
• 
Network. Connects the container to device host, physical ports, other containers. The available 
network types are host, bridge, and macvlan. 

## 9.3 Configuring the Docker  *(p.631)*

9. Containerization 
• 
Volume – the container disk, mapped to device disk. 
Life Cycle 
The docker container life cycle is supported as follows: 
• 
Deployment: 
 
Pull container image from registry (public or private) 
 
Create container (by CLI, compose file) 
 
Configure device related configuration 
 
Import container license, activate 
 
Configure container 
• 
Maintenance: 
 
Performance monitoring: CPU and memory utilization 
 
Fault management (liveness) 
 
Edit container deployment (by CLI, compose) 
 
Upgrade: device SW, device patch, container image 
• 
Backup & restore container: 
 
Restore container as is by import/export commands 
 
Restore container volume 
 
Restore container license, certificates 
9.3 Configuring the Docker 
 To access the Docker management: 
1. Navigate to config>mngmnt>login-user<user-name>#. 
2. Define the login user with ‘linux-tech’ level. 
config>mngmnt# login-user <user-name> 
config>mngmnt>login-user(<user-name>)$ level linux-tech 
config>mngmnt>login-user(<user-name>)$ 

## 9.4 Use Cases and Examples  *(p.632)*

9. Containerization 
3. Login to the device with ‘linux-tech’ user to get the Linux prompt. 
The Docker CLI is fully exposed to the user.  
4. Use the native Docker CLI according to the following reference: 
https://docs.docker.com/engine/reference/builder/ 
9.4 Use Cases and Examples 
This section illustrates the following selected Docker container use cases: 
• 
Host container 
• 
Host container with port forwarding 
• 
Host container with LAN port 
• 
Host container with serial port 
• 
Host container configured by docker compose 
Host Container  
In this case the traffic from the container host can reach LAN/WAN sites. 
 
Configuration example: 
docker run -dit --name alpine-host alpine ash 
9. Containerization 
Host Container with Port Forwarding  
In this case the traffic from outside with TCP port 8081 is reaching the container host with TCP port 
8080. 
 
 
Configuration example: 
docker run -dit -p 8081:8080 --name alpine-port alpine ash 
Host Container with LAN Port  
In this case: 
• 
Traffic from LAN3 is received directly by the container 
• 
Traffic is processed and sent via the router to the external device 
 
9. Containerization 
Configuration example: 
• 
Creating the network  
 
docker network create -d macvlan \ 
 
  --subnet=35.35.35.2/24 \ 
 
  --gateway=35.35.35.1 \ 
 
  -o parent=lan3 \ 
 
  my-macvlan-net 
• 
Creating the container  
 
docker run -dit --name my-macvlan-alpine alpine ash 
• 
Attaching the network to the container 
 
docker network connect my-macvlan-net my-macvlan-alpine 
 
Host Container Configured by Docker Compose 
CLI configuration example: 
docker run -dit --name alpine-host1 alpine ash 
Compose file example: 
version: “3.9” 
services: 
  alpine-host1: 
    tty: true 
    image: alpine 
    command: ash 
Docker compose configuration process:  
1. Prepare the docker compose yaml file. 
2. Place this yaml file onto your FTP server.  
3. Copy the compose file to the user file directory (located on the ETX-1p device), using the copy 
command 
copy <ftp_server_address>/alpine-host.yml user/alpine-host.yml 
For example:  
copy ftp://rad:rad123@172.17.160.127/alpine-host.yml user/alpine-host.yml) 
4. Create the linux-tech user and perform login. 
5. Create the container using the docker-compose command: 
9. Containerization 
 
Create the container: 
docker-compose -f /opt/rados_user_files/alpine-host.yml up -d 
optional: add -p flag to define project name 
docker-compose -p project1 -f /opt/rados_user_files/alpine-host.yml up -d 
 
 
Verify the container creation: 
[root@localhost ah1]# docker ps 
CONTAINER ID   IMAGE   COMMAND CREATED    STATUS   PORTS   NAMES 
207b27152fbf   alpine   "ash"  47 min ago Up 47 min        rados_user_files-alpine-
host1-1 
 
Note 
The container name consists of <directory/project name>-<file name>-
<number>. 
 
 
 
 