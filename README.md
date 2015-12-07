# wakeonpi
Use your Raspberry Pi as a wake-on-lan controller.  Steps are tailored to Raspbian.

## Twitter Preparation

Create an application for your twitter account at https://apps.twitter.com
* Give the application read, write and direct message access
* Create an application access token

## Installation

There are a few gyrations needed to make the older python 2.7.3 version that comes with Raspbian secure.

Make sure you have pip installed:
`sudo apt-get install python-setuptools python-dev build-essential`
`sudo easy_install pip`

Add required libraries:
```
sudo pip install requests[security]
sudo pip install tweepy pyyaml
```

Edit your wakeonpi.conf file:
* Provide your twitter OAUTH token information
* Provide a list of friendly computer names and their MAC addresses
