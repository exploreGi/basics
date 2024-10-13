## Jenkins Installation
### Install Java
sudo apt install fontconfig openjdk-17-jre
java --version

### Install jenkins
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins

http://<public-ip>:8080/
cat /var/lib/jenkins/secrets/initialAdminPassword

## Install Docker Pipeline Plugin
- Log in to Jenkins.
- Go to Manage Jenkins > Manage Plugins.
- In the Available tab, search for "Docker Pipeline".
- Select the plugin and click the Install button.
- Restart Jenkins after the plugin is installed.

## Docker Slave Configuration
`sudo apt-update`
`sudo apt install docker.io`

## Grant Jenkins user and Ubuntu user permission to docker deamon.
`usermod -aG docker jenkins`
`usermod -aG docker ubuntu`
`systemctl restart docker`

## Retart Jenkins
http://<ec2-instance-public-ip>:8080/restart


## Jenkins MAster Slave
### Step1
Create a master Ec2 .Install java,jenkins.Configure edit inbound rules and add 8080,9007 in security groups.
Manage Jenkins->Security
- Agents
- TCP port for inbound agents -> Fixed 9007
- Git Hooks -> check Allow on Controller and Allow on Agents
Manage Jenkins -> Nodes -> New Node
- specify the name, node and check Permananent agent
- Remote Root Directory -> /home/ubuntu
- Labels -> node
### Step2

Create a slave EC2 , node.Install java
Run the two commands in slave EC2 specified in the node screen on Jenkins web.
- curl -sO http://54.161.86.164:8080/jnlpJars/agent.jar
- java -jar agent.jar -jnlpUrl http://54.161.86.164:8080/computer/node/jenkins-agent.jnlp -secret ac2eaddecee092174ea0a5499e4689f3cab3462fa361727965ca42309d929519 -workDir "/home/ubuntu"
Keep the terminal connected.
Open a new EC2 terminal.

### Step3
Create a new job ,freestyle jon in master.
IN Configure, select
Restrict where this project can be run and specify the label expression as node.

### Step4 
Verify the workspace created in /h0me/ubuntu in slave EC2 machine.




