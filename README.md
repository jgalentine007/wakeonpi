# wakeonpi
Use your Raspberry Pi as a wake-on-lan controller

## Twitter Preparation

Create an application for your twitter account at https://apps.twitter.com
* Give the application read, write and direct message access
* Create an application access token

## Installation

Make sure you have pip installed:
  sudo apt-get install python-setuptools
  sudo easy_install pip

Add required libraries:
`sudo pip install tweepy pyyaml`

Edit your wakeonpi.conf file:
* Provide your twitter OAUTH token information
* Provide a list of friendly computer names and their MAC addresses
