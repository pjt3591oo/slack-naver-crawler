# 슬랙 - 연관 검색어

슬랙을 이용한 네이버 연관 검색어 가져오기.


## 의존성 모듈 설치

```bash
 $ pip install requirements.txt
```

## 설정파일

*`SLACK_CONFIG.py`*

```python

token = '발급받은 토큰'

channel = '#general'
```

[토큰 확인]('https://api.slack.com/custom-integrations/legacy-tokens')

token은 해당 슬렉에 맞는 토큰으로 바꾸어 준다. 

## 실행

```bash
 $ python app.py
```

## 결과

![결과 이미지](https://github.com/pjt3591oo/slack-naver-crawler/blob/master/images/slack_result.png)

[결과 보러가기!]('https://api.slack.com/custom-integrations/legacy-tokens')