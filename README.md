# CrawlData Project
## Require: chrome version 97 to use chromedriver
### 1. wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
### 2. sudo dpkg -i google-chrome-stable_current_amd64.deb
## First choice:
### 1. sudo apt install pip -y
### 2. pip install -r /path/to/requirements.txt
## Second choice:
### 1. pip3 install selenium
### 2. pip install simplejson
### 3. pip3 install requests
## After install successfully necessary library:
### python3 main.py to run application
## Exception handle
### urllib3 ( ) or chardet ( ) doesn't match a supported
use sudo python3 -m pip install --upgrade requests to update requests lib
