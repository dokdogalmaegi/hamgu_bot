import discord
import urllib.request
import simplejson, requests
import json
import requests
from bs4 import BeautifulSoup


class DiscordChatBot:
    def __init__(self):
        print('ready')
    def naver_search(self, title):
        client_id = "client_id"  # 애플리케이션 등록시 발급 받은 값 입력
        client_secret = "client_secret"  # 애플리케이션 등록시 발급 받은 값 입력
        encText = urllib.parse.quote(title)
        url = "https://openapi.naver.com/v1/search/kin.json?query=" + encText + "&display=1&sort=sim"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            json_rt = response.read().decode('utf-8')
            py_rt = json.loads(json_rt)
            api_count = len(py_rt['items'])
            for i in range(api_count):
                res = py_rt['items'][i]['link']
                return res
        else:
            print('error')
    def namu_search(self, title):
        return 'https://namu.wiki/go/{}'.format(title)
    def youtube_search(self, title):
        return 'https://www.youtube.com/results?search_query={}'.format(title)
    def kakao_translate(self, lang, text):
        if (lang == '01'):
            lang = 'kr'
        if (lang == '02'):
            lang = 'en'
        if (lang == '03'):
            lang = 'jp'
        if (lang == '04'):
            lang = 'cn'
        if (lang == '05'):
            lang = 'vi'
        if (lang == '06'):
            lang = 'id'
        if (lang == '07'):
            lang = 'ar'
        if (lang == '08'):
            lang = 'bn'
        if (lang == '09'):
            lang = 'de'
        if (lang == '10'):
            lang = 'es'
        if (lang == '11'):
            lang = 'fr'
        if (lang == '12'):
            lang = 'hi'
        if (lang == '13'):
            lang = 'it'
        if (lang == '14'):
            lang = 'ms'
        if (lang == '15'):
            lang = 'nl'
        if (lang == '16'):
            lang = 'pt'
        if (lang == '17'):
            lang = 'ru'
        if (lang == '18'):
            lang = 'th'
        if (lang == '19'):
            lang = 'tr'
        url = "https://kapi.kakao.com/v1/translation/translate"
        kakao_key = "kakao_key"
        r = requests.get(url, params={'query' : text, 'src_lang' : 'kr', 'target_lang' : lang}, headers={'Authorization' : 'KakaoAK ' + kakao_key } )
        js = simplejson.JSONEncoder().encode(r.json())
        return "".join(r.json()['translated_text'][0])
    def Rsix(self, title):
        def get_html(url):
            _html = ""
            resp = requests.get(url)
            if resp.status_code == 200:
                _html = resp.text
                return resp.text
        id = title
        url = "https://r6.tracker.network/profile/pc/" + id
        html = get_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        # img_soup.findAll('img')[0]['src']
        img_soup = soup.findAll('div', 'trn-defstat__value')[4]

        level = soup.findAll('div', 'trn-defstat__value')[0].text.replace("\n","") # level
        kda = soup.findAll('div', 'trn-defstat__value')[45].text.replace("\n","") # KDA
        rating = soup.findAll('div', 'trn-text--dimmed')[1].text[:5] # rating
        rank = soup.findAll('div', 'trn-text--dimmed')[0].text # rank   
        img_url = img_soup.findAll('img')[0]['src'] # img_url
        return level, kda, rating, rank, img_url
