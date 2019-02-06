# -*- mode: ruby -*-
# vi: set ft=ruby :

# handle getting and creating a local .env file
en = Hash.new
if not (File.file?(".env"))
  File.open(".env", 'w') { |file| 
    file.write("domain=#{`hostname`[0..-2]}\nTZ=America/Toronto\nloglevel=INFO\ndatafile=example_import.json") 
  }
end
File.open(".env").each do |line|
  spl = line.split('=')
  en[spl[0].strip] = spl[1].strip
end

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/bionic64"
  
  config.vm.host_name = en['domain']

  config.vm.box_check_update = true
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.network "forwarded_port", guest: 8081, host: 8081
  config.vm.network "forwarded_port", guest: 8082, host: 8082

  config.vm.synced_folder ".", "/obp"
  
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "8192"
  end

  config.vm.provision "shell", privileged: true, inline: <<-SHELL
    apt update
    apt install apt-transport-https ca-certificates curl software-properties-common apache2-utils inotify-tools python3-pip -y
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
  
  config.vm.provision "shell", privileged: true, run: 'always', env: en, inline: <<-SHELL
    cd /obp
    docker-compose down
    docker-compose --log-level ${loglevel} up -d

    pip3 install -r requirements.txt
    sleep 60
    python3 import-data.py
  SHELL

end