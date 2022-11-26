sudo apt-get update -y
sudo apt-get install -y apt-transport-https ca-certificates curl

sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg

echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list

sudo apt-get update -y
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl

sudo sed -i "/EnvironmentFile/a Environment=\"KUBELET_EXTRA_ARGS=--node-ip=$(hostname -I |  \
     awk '{print $2}')\"" /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
#sudo sed -i -e "s/=/=--node-ip=$(hostname -I | awk '{print $2}')/g" /etc/default/kubelet
sudo init 6

