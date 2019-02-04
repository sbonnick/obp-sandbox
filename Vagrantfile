# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/bionic64"

  config.vm.box_check_update = true
  config.vm.network "forwarded_port", guest: 80, host: 80
  config.vm.network "forwarded_port", guest: 443, host: 443

  config.vm.synced_folder ".", "/obp"
  
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "8192"
  end

  config.vm.provision "shell", privileged: true, inline: <<-SHELL
    apt update
    apt install apt-transport-https ca-certificates curl software-properties-common apache2-utils inotify-tools -y
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    apt update
    apt-cache policy docker-ce
    apt install docker-ce -y
    curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
    sudo usermod -aG docker vagrant
    docker -v
  SHELL
  
  config.vm.provision "shell", privileged: true, run: 'always', inline: <<-SHELL
    cd /obp
    docker-compose up -d
  SHELL
end


## ensure docker-compose files exists
## for any envars, put them in .env
## services default to *.obp.localhost