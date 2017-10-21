# 슬랙 - 연관 검색어

슬랙을 이용하여 연관 검색어 검색 결과 가져오기.


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

## 실행

```bash
 $ python app.py
```

## 결과

![]('./images/slack_result.png')