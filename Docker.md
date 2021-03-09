Docker 配置
```bash
sudo apt-get install -y nvidia-docker2  nvidia-container-runtime
sudo nvidia-docker2 run --rm -it nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04 nvidia-smi
sudo nvidia-docker ps -a


apt-get update
apt-get upgrade
apt-get install vim
apt-get install openssh-server

sudo docker rm  container_name/ID
sudo docker  ps  -a
docker images
docker rmi   image_name/ID

sudo nvidia-docker run -v /media/l/e6aa5997-4a1e-42e4-8782-83e2693751bd/city:/root/city -dit -p23456:22 --name=city_cuda10.0 -h=LAB_city city_cuda_100
sudo docker exec -it city_cuda10.0 /bin/bash
sudo docker stop
```