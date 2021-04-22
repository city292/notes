Docker 配置
```bash
sudo apt-get install -y nvidia-docker2  nvidia-container-runtime
sudo nvidia-docker2 run --rm -it nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04 nvidia-smi
sudo nvidia-docker ps -a


apt-get update
apt-get upgrade
apt-get install vim
apt-get install openssh-server  openssh-clients
apt-get install libeigen3-dev gdb
vi /etc/ssh/sshd_config

RSAAuthentication yes #启用 RSA 认证
PubkeyAuthentication yes #启用公钥私钥配对认证方式
AuthorizedKeysFile .ssh/authorized_keys #公钥文件路径（和上面生成的文件同）
PermitRootLogin yes #root能使用ssh登录

service sshd restart

sudo docker rm  container_name/ID
sudo docker  ps  -a
docker images
docker rmi   image_name/ID

sudo nvidia-docker run -v /media/l/e6aa5997-4a1e-42e4-8782-83e2693751bd/city:/root/city -dit -p23456:22 --name=city_cuda10.0 -h=LAB_city city_cuda_100
sudo docker exec -it city_cuda10.0 /bin/bash
sudo docker stop



sudo docker run -v /media/l/e6aa5997-4a1e-42e4-8782-83e2693751bd/city:/root/city -it -dit -p23456:22 --name=city_pcl  youyue/pcl-docker
sudo docker exec -it city_pcl /bin/bash
sudo docker run -v  /media/l/e6aa5997-4a1e-42e4-8782-83e2693751bd/city:/root/city  -e DISPLAY=:0 -it -dit -p23456:22   --name=city_pcl  youyue/pcl-docker
# 启动Docker时，的参数
-e DISPLAY=:10.0
-v /media/l/e6aa5997-4a1e-42e4-8782-83e2693751bd/city:/root/city
sudo docker start 9d5c8e832d69


IP4.DNS[1]:                             192.168.32.82
IP4.DNS[2]:                             192.168.0.150
IP4.DNS[3]:                             192.168.0.151


```