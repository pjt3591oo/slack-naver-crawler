from slack import sc, channel


def notification(message):

    sc.api_call(
        "chat.postMessage",
         channel=channel,  # {#채널 }의 형태로 채널 지정
         text=message
    )

if __name__ == '__main__':
    notification('test')