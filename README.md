# rpi-band
A smart band prototype based on raspberry pi (model zero w).


# envrionment
- Hardware: Raspberry Pi model zero w, model 4b.
- OS: Buster
- Package dependencies: BlueZ(included in Buster)
- Python dependencies: bleson (optional: aioblescan)


# usage
- Make sure you are at the root of this repo.
- First install bleson with sudo: `sudo pip install bleson`
- Run `sudo python3 src/main.py`


# error check
- Make sure your system is up-to-date Buster.
- Check if you have the BlueZ installed. `bluetoothctl -v`


# Reference
- [aioblescan](https://github.com/frawau/aioblescan)
- [bleson](https://github.com/TheCellule/python-bleson)
