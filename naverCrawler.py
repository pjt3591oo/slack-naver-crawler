import requests as rq
from bs4 import BeautifulSoup


def crawler(keyword):
    url = '''http://search.naver.com/search.naver?
            sm=tab_hty.top
            &where=nexearch
            &query=%s
            &oquery=as
            &tqi=TPc6bdpySpZssceniZZssssssIR-049889'''%(keyword)
    res = rq.get(url)
    soup = BeautifulSoup(res.content,'lxml')

    a_tags = soup.select('#nx_related_keywords')

    result = []

    for a_tag in a_tags:
        result.append(a_tag.text.strip())
    return str(result)

if __name__ =='__main__':
    print(crawler('스타크래프트'))
