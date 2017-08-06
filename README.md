# echo-linebot
heroku echo linebot app for python

## Installation
```
pip install django-toolbelt
```
download echo-linebot from github. It is premised that Heroku is installed. If Heroku is not installed, please install and login.

## Features / How to use
### Heroku Deploy
```
cd echo-linebot-master
heroku login
...
git init
git add .
git commit -m "first commit."

heroku create
heroku config:set DISABLE_COLLECTSTATIC=1

pip freeze > requirements.txt
```
In the `line/setting.py`, add the application name of heroku which created earlier to the "Invalid HTTP_HOST header" countermeasure ALLOWED_HOSTS when accessing after deployment.
```python:setting.py
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'xxxxx.herokuapp.com']
```
Please get the long-term token that is displayed permanently from LINE developers. To acquire, you need to create a LINEBOT account. If you have not created an account, please select `Start using Developer Trial` from [Line Developers](https://business.line.me/en/services/bot), create an account, and create LINEBOT from `Start using Messaging API`. Set the token to Heroku's environment variable.
```
heroku config:set ACCESS_TOKEN="{your line bot channel access token}"
```
When you are done, re-commit and deploy to heroku.
```
git add .
git commit -m "first commit"
git push heroku master
```
If deployment is successful, BOT should be running. Please send a message to BOT at LINE. A Json format reply should be returned.

### LINE BOT Settings

Added the address of bot/webhook of heroku to "Webhook URL" of LINE Developers.
