#!/bin/bash

function setups() { # 常规设置
  yum install wget --quiet -y
  wget -O /etc/yum.repos.d/CentOS-Base.repo https://repo.huaweicloud.com/repository/conf/CentOS-7-reg.repo
  yum install epel-release --quiet -y
  yum clean all && yum makecache
  yum install --quiet -y vim bash-completion ntpdate net-tools lrzsz
  systemctl disable firewalld.service --now   # 停止并禁止防火墙开机启动
  ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime   # 修改时区
  sed -i 's#SELINUX=enforcing#SELINUX=disabled#g' /etc/selinux/config  
  setenforce 0
  ntpdate time.windows.com
  swapoff -a
  echo "swapoff -a" >> /etc/profile
}

function edit_hosts() {
  cat <<EOF | sudo tee /etc/hosts
192.168.1.224    master
192.168.1.225    node1
192.168.1.221    node2
EOF

}

function mod_config() {
    cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF
    sudo sysctl --system
}



function init() {
  if [ $role == "master" ]; then
    yum install --quiet -y kubeadm kubectl kubelet docker-ce-18.09.9-3.el7.x86_64
	mkdir -p /etc/docker/
	docker_config
    systemctl enable kubelet --now && systemctl enable docker --now
	echo 'source <(kubectl completion bash)' >>~/.bashrc
    kubeadm init --image-repository=registry.aliyuncs.com/google_containers --pod-network-cidr=10.244.0.0/16 |tee /root/k8s_init.log \
    && mkdir -p $HOME/.kube && sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config && \
    kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
  else
    yum install --quiet -y kubeadm kubelet docker-ce-18.09.9-3.el7.x86_64
	mkdir -p /etc/docker/
	docker_config
    systemctl enable kubelet --now && systemctl enable docker --now
  fi

}

function config_docker_yum() { # 配置docker华为源
  sudo yum remove docker docker-common docker-selinux docker-engine
  sudo yum install -y yum-utils device-mapper-persistent-data lvm2
  wget -O /etc/yum.repos.d/docker-ce.repo https://repo.huaweicloud.com/docker-ce/linux/centos/docker-ce.repo
  sudo sed -i 's+download.docker.com+repo.huaweicloud.com/docker-ce+' /etc/yum.repos.d/docker-ce.repo

}

function config_k8s_yum() { # 配置k8s华为源
  cat <<EOF >/etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://repo.huaweicloud.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=0
gpgkey=https://repo.huaweicloud.com/kubernetes/yum/doc/yum-key.gpg https://repo.huaweicloud.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF
}

function docker_config() {  # 配置docker
	cat <<EOF >/etc/docker/daemon.json
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "registry-mirrors": [
      "https://fz5yth0r.mirror.aliyuncs.com",
      "https://dockerhub.mirrors.nwafu.edu.cn/",
      "https://mirror.ccs.tencentyun.com",
      "https://docker.mirrors.ustc.edu.cn/",
      "https://reg-mirror.qiniu.com",
      "http://hub-mirror.c.163.com/",
      "https://registry.docker-cn.com"
  ],
  "storage-driver": "overlay2",
  "storage-opts": [
    "overlay2.override_kernel_check=true"
  ],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m",
    "max-file": "3"
  }
}
EOF
}

read -p "master or node?" role
setups
config_docker_yum
config_k8s_yum
mod_config
edit_hosts
init
