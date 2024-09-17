#!/bin/bash

###########
# Author :Rajani
# Date : Sep 17,2024
# This script outputs the node health
# # version v1
############

set -x  # debug mode
set -e  # exit when there is error
set -o pipefail # pipe will see only if last cmd is success or not
df -h
free -g
nproc
ps -ef | grep "init" | awk -F " " '{print $2}'
