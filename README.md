# wakeonpi
Use your Raspberry Pi as a wake-on-lan controller by sending yourself Tweets!  Steps are tailored to Raspbian.

## Twitter Preparation

Create an application for your twitter account at https://apps.twitter.com
* Give the application read, write and direct message access
* Create an application access token

## Installation

There are a few gyrations needed to make the older python 2.7.3 version that comes with Raspbian secure.

Make sure you have pip installed:
```
sudo apt-get install python-setuptools python-dev build-essential libffi-dev libssl-dev
sudo easy_install pip
```

Add required libraries (may take a few minutes):
```
sudo pip install requests[security]
sudo pip install tweepy pyyaml
```

Clone wakeonpi from Github into a directory of your choosing:
```
git clone https://github.com/jgalentine007/wakeonpi.git
chmod u+x wakeonpi.py
```
Edit your wakeonpi.conf file (an example file is provided):
* Provide your twitter OAUTH token information
* Provide a list of friendly computer names and their MAC addresses

Test the program interactively:
`./wakeonpi.py -c wakeonpi.conf`

Add the program to your rc.local file:
`python /home/pi/wakeonpi/pi/wakeonpi.py -c /home/pi/wakeonpi/pi/wakeonpi.conf &`

## Waking up a computer

To wake up a computer in your list, simply send yourself a *direct message* like so:
`@jgalentine007 wol pc1`

## To-do

~~Need to add persistent error handling to keep the stream running at all times.~~
