# A Raspberry Pi Radio

This is a simple webapp written in Python 3 to control a RasperryPi, which is used as a radio. :)

## Setup
1. Clone this repository
```bash
git clone https://github.com/JoramM/radio.py.git
```
Or download and extract the zip file.

2. Install the [VLC Player](https://www.videolan.org/vlc/#download). For Ubuntu use:
```bash
sudo apt-get insrall vlc
```
The LibVLC API is used to play music with the VLC Player (see "Useful Links").

3. Navigate to project directory and install the Python requirements:
```bash
pip install -r requirements.txt
```
If you have Python 2.7 **and** Python 3 installed, use this command instead:
```bash
pip3 install -r requirements.txt
```

## Start
```bash
python main.py
```
If you have Python 2.7 **and** Python 3 installed, use this command instead:
```bash
python3 main.py
```

This will start the Flask webserver which is accessible over http://localhost:8080

## Useful Links
* [Jinja2 Documentation](http://jinja.pocoo.org/docs/)
* [Flask Documentation](flask.pocoo.org/docs/)
* [Bindings for the LibVLC public API](https://www.olivieraubert.net/vlc/python-ctypes/doc/)
