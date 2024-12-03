`docker build -t jenkinsimage .`

`docker run -it -v /home/rajani:/docker_rajani ubuntu /bin/bash`

`docker run --name pear --rm ubuntu ls /`

`docker run --name apple --rm ubuntu ls pwd`

`docker run --name apple ubuntu pwd`

`docker exec 7c96286c0fbc ls /root`

`docker exec -it elastic_tharp sh`

ctrl p ctrl q to come out of the container without killing it

`docker run --rm -v /home/rajani/file2.txt:/data/file.txt pimage:nov8.2`

`docker run --rm -v /home/rajani/:/data/ pimage:nov8.2 python3.8 /mydir/printfile.py /data/docker-test/file1.txt`

`docker commit c3f279d17e0a  r1/testimage:version1`

`docker run --rm -p 9002:80 httpd`  # port mapping 9002 on host to 80 on container

`uname -a` # displays the name of the operating system

`docker build -t multiarchdemo:v1 .`

`docker tag multiarchdemo:v1 ranniuser/multiarchdemo:v1`

`docker builder ls` #to see builder instances available on your machine

`docker buildx create --name multiarchbuilder --platform linux/amd64,linux/arm64 --driver=docker-container --bootstrap --use`

`docker builder ls`

`docker buildx build --platform linux/amd64,linux/arm64 --push -t ranniuser/multiarchdemo:v1 .` # builds the image for two linux platforms and pushes to docker hub




