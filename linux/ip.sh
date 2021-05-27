#!/bin/bash

function change_ip(){  # 设置IP为静态IP
	ip_addr=$(ip addr |grep 'ens'|grep 'inet'|awk '{print $2}'|awk -F '/' '{print $1}')  # 主机当前ip地址
	file_name=$(ls /etc/sysconfig/network-scripts/|grep 'ifcfg-ens')  # 网卡名
	sed -i s#BOOTPROTO=dhcp#BOOTPROTO=static#g /etc/sysconfig/network-scripts/$file_name
	sed -i s#ONBOOT=no#ONBOOT=yes#g /etc/sysconfig/network-scripts/$file_name
	sed -i '$a IPADDR='$ip_addr'' /etc/sysconfig/network-scripts/$file_name
	sed -i '$a NETMASK=255.255.255.0' /etc/sysconfig/network-scripts/$file_name
	sed -i '$a GATEWAY=192.168.1.1' /etc/sysconfig/network-scripts/$file_name
	sed -i '$a DNS1=114.114.114.114' /etc/sysconfig/network-scripts/$file_name
	sed -i '$a DNS2=202.98.192.167' /etc/sysconfig/network-scripts/$file_name
	systemctl restart network

}

change_ip
