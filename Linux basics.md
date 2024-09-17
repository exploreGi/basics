`rpm -aq`

`rpm -aq openssh telnet ansible`

`sudo rpm -i /opt/ftp-0.17-67.el7.x86_64.rpm`

`rpm -aq | grep ftp`

`sudo rpm -e opt/ftp-0.17-67.el7.x86_64.rpm`

`sudo yum install -y ansible`

### Identify the package that provides ansible
`sudo yum list ansible`

`sudo yum remove -y ansible`

`yum repolist`

`ls /etc/yum.repos.d/`

`cat /etc/yum.repos.d/CentOS-Base.repo`

=================

`sudo systemctl start httpd`

===========================

### Run docker commands without giving sudo
you need to add your user (who has root privileges) to docker group. For this run following command:

`sudo usermod -aG docker $USER`
Now, have the user logout then login again

===========================================

### Assign ip address of system to interface eth0
 `ip addr add 192.168.10.1/24 dev etho0`

### Show the ip addresses assigned to the interface
`ip addr show`

### Display the kernel routing table
`route`

======================================================
### shell script in debug mode 
set -x

### shell script to show error
set -e

### shell script to show error even when there is a pipeline
set -o pipefail

### to see file system disk space usage
df -h

### print amount of freeand used memory in system
free -g

### print no.of processing units available (CPUs)
nproc

### print total no.of processess with all details,pid,memory usage, etc (this command helps to analyze the node status)
top

### info about processes, awk-> pattern scanning and processing language
ps -ef | grep amazon | awk -F" " '{print$2}'

### date
date | echo "today is"
the above command sends the output of the date(system defined command) to stdin and hence pipe output is null .
