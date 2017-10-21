import time
from slackNoti import notification
from naverCrawler import crawler
from slack import sc


def is_user(keys):
    return 'type' in keys and 'text' in keys


def is_data(data):
    return data != '[]'


if sc.rtm_connect():
    while True:
        receive_data = sc.rtm_read()

        if len(receive_data):
            keys = list(receive_data[0].keys())

            if is_user(keys):
                data = crawler(receive_data[0].get('text'))
                if is_data(data):
                    notification(data)

        time.sleep(1)
else:
    print("Connection Failed")
