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

### 
