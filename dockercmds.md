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




