from slackclient import SlackClient
from SLACK_CONFIG import token, channel

slack_token = token
sc = SlackClient(slack_token)