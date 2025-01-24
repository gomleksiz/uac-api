# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|
  config.vm.box = 'ubuntu/jammy64'
  config.vm.box_check_update = false
  config.ssh.insert_key = false

  # VM options
  # Here you can increase/decrease VM resources if needed
  config.vm.provider 'virtualbox' do |vb|
    vb.memory = 2048
    vb.cpus = 4
  end

  # Network Settings
  # Here you can setup more port forwarding rules if needed
  config.vm.network :forwarded_port, guest: 22, host: 3200, id: 'ssh'
  config.vm.network :forwarded_port, guest: 8080, host: 3201, id: 'misc'

  # Here you can setup shared directories across the host and VM if needed
  # config.vm.synced_folder "../", "/shared"

  require 'time'
  offset = ((Time.zone_offset(Time.now.zone) / 60) / 60)
  timezone_suffix = offset >= 0 ? "-#{offset}" : "+#{offset}"
  timezone = "Etc/GMT#{timezone_suffix}"

  if ARGV[0] == 'up'
    # Link correct timezone
    config.vm.provision :shell, :inline => "sudo rm /etc/localtime && sudo ln -s /usr/share/zoneinfo/#{timezone} /etc/localtime", run: 'always'

    provision_dir_name = 'provisioning'
    provision_dir = File.join(File.dirname(__FILE__), provision_dir_name)

    # Run provisioning scripts
    config.vm.provision 'shell', path: File.join(provision_dir, 'setup_deps.sh')
    config.vm.provision 'shell', path: File.join(provision_dir, 'setup_docker.sh')
    config.vm.provision 'shell', path: File.join(provision_dir, 'setup_trivy.sh')
    config.vm.provision 'shell', privileged: false, path: File.join(provision_dir, 'setup_python.sh')
    config.vm.provision 'shell', privileged: false, inline: 'python3.11 -m pip install -U pip tox'
  end
end
