## Resources

- this repository: ```https://github.com/hlussi/cat-repellent-water-gun.git```
- pan/tilt tracking: https://www.pyimagesearch.com/2019/04/01/pan-tilt-face-tracking-with-a-raspberry-pi-and-opencv/
- opencv: https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/
- 


# Setup & Configuration 

## Raspberry Pi Baseline

- enable I2C
```
sudo apt-get install -y python-smbus
sudo apt-get install -y i2c-tools
# enable configuration in "Interfacing Options" -> "I2C" & "SPI"
sudo raspi-config
```

- reboot,loging and check
```
sudo i2cdetect -y 1
```

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

- enable camera module

- reboot and check /var/log/boot.log

## Project

- create venv
```
cd $PROJECT/pi
make install
. ./venv/bin/activate
```

## Tensor Flow

see https://towardsdatascience.com/real-time-object-tracking-with-tensorflow-raspberry-pi-and-pan-tilt-hat-2aeaef47e134

- install dependencies
```
sudo apt-get update && sudo apt-get install -y python3-dev libjpeg-dev libatlas-base-dev raspi-gpio libhdf5-dev python3-smbus
```

- install venv
```
mkdir rpi-deep-pantilt && cd rpi-deep-pantilt
python3 -m venv venv
source venv/bin/activate && python3 -m pip install --upgrade pip
```

- install TensorFlow
```
# pip install https://github.com/leigh-johnson/Tensorflow-bin/blob/master/tensorflow-2.0.0-cp37-cp37m-linux_armv7l.whl?raw=true
pip install https://github.com/leigh-johnson/Tensorflow-bin/blob/master/tensorflow-1.15.0-cp35-cp35m-linux_armv7l.whl?raw=true
```

- install rpi-deep-pantilt Python package
```
python3 -m pip install rpi-deep-pantilt```
