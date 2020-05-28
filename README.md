## Resources

this repository: ```https://github.com/hlussi/cat-repellent-water-gun.git```

## pyenv
```
brew install pyenv
brew install pyenv-virtualenv
pyenv virtualenv 3.6.7 wassermat
pyenv local wassermat
pip install --proxy http://proxy.adnovum.ch:3128 -r requirements.txt
```

## Raspberry Pi

- Configure wpa_supplicant

```
raspi-config
```

```
\# sudo vi  /etc/wpa_supplicant/wpa_supplicant-wlan0.conf
country=CH
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="xyz"
    psk="xxx"
    key_mgmt=WPA-PSK
    id_str="xyz"
}
```

```
sudo wpa_cli -i wlan0 reconfigure
sudo ip link set wlan0 down
sudo ip link set wlan0 up

```

- reboot and check /var/log/boot.log

