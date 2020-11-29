# raspi-fan-control
small script and service file to turn on fan if cpu is to hot

# INSTALL instructions
copy service file to /etc/systemd/system
```bash
sudo cp fan-control.service /etc/systemd/system/fan-control.service
sudo systemctl start fan-control.service
sudo systemctl enable fan-control.service
```