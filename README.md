Development Setup
=================

Configuration
-------------
A steam api key is required to run this app. You can obtain one by going
to this address: https://steamcommunity.com/dev/apikey

Then create a config.ini file with the following content:
```commandline
[DEFAULT]
dotaAPIKey=<your key goes here>
```

For a first time setup you will have to install the requirements:
```bash
python setup.py develop
```
Then you can run the app like so:
```bash
dotalytics-api
```

Dockerfile
----------

If you have docker installed, you can use the container to run the app:
```bash
docker build -t dotalytics-api .
docker run -p 8888:8888 dotalytics-api
```
