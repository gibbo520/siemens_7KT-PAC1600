# siemens_7KT-PAC1600
Interfacing modbus RTU with siemens 7KT PAC1600

you need minimalmodbus ad serial
sudo apt install -y python3-pip python3
pip3 install minimalmodbus

/dev/ttyUSB0 is the port name of your rs485 to usb converter 

usage :

python3 7kt.py 1      to got all values 

python3 7kt.py 1 power.l1 to got instant power of L1
