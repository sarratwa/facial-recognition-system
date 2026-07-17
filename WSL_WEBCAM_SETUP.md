---> for taking pics on wsl : 
Administrator PowerShell:
wsl --update
wsl --shutdown  
winget install --interactive --exact dorssel.usbipd-win
usbipd list
usbipd bind --busid 2-4
Normal powershell:
usbipd attach --wsl --busid 2-4 (2-4 with your actual webcam bus ID.)

check inside wsl:
sudo apt update
sudo apt install -y usbutils v4l-utils
lsusb
ls -l /dev/video*

v4l2-ctl --list-devices

/dev/video0