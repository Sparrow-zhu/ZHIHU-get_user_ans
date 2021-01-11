import requests

def get_data(url):
    '''
    功能：访问 url 的网页，获取网页内容并返回
    参数：
        url ：目标网页的 url
    返回：目标网页的 html 内容
    '''

    # 用'cookie'模拟登录网页解决跳转登录的问题！
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'cookie': '''_zap=5af1d8c0-fbdc-4de4-9e41-190de568d21d; _xsrf=c5479e9c-866a-494e-8d8d-f0707d5043e4; d_c0="ANDRQfB1eBGPTqmQ4kihicWKnJywGW7C9XA=|1592921756"; _ga=GA1.2.504778147.1592921761; tst=h; tshl=; l_n_c=1; n_c=1; __utmc=51854390; __utmv=51854390.100-1|2=registration_date=20180309=1^3=entry_date=20180309=1; __utma=51854390.504778147.1592921761.1606446798.1607399670.2; __utmz=51854390.1607399670.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/349474297/answer/1423622054; anc_cap_id=28126de6df1d4667a253a29e30d522c9; q_c1=0618fdc555614340b32cc006ab8c0bd5|1609728874000|1594393532000; capsion_ticket="2|1:0|10:1609729982|14:capsion_ticket|44:YTAwN2ZmMTA2ZmZhNGEyYjljNDM1MTdmYWQ5NTA3YWU=|4e7868e02f87117b2e510b95dca47412c4763dccdd38f8395e332db6824d4274"; z_c0="2|1:0|10:1609730003|4:z_c0|92:Mi4xbU1JZENBQUFBQUFBME5GQjhIVjRFU2NBQUFDRUFsVk4weFFhWUFEMFZSa3IyeVZHQ2lXTFo4UXloNWJjSVVNSXdB|e2e1e401ce2552e885f976b561a82082b95f455ba823d0202f83d0b0cc8cd087"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1609296687,1609732902,1609732906,1609752018; SESSIONID=PKgDznPTECrdI6Q3xtFPYSafhBTIQOgRC2VrGPrlysi; JOID=VV8VB0utJ88NcP8gfq6g1Z6gXato_WusTQ2Rdy7vZLptPc5xSv8hPFF3-CN-YYJ1hfPChmscKEL_nbUrDFBp_ZI=; osd=UlwRCkiqJMsAc_gjeqOj0p2kUKhv_m-hTgqScyPsY7lpMM12SfssP1Z0_C59ZoFxiPDFhW8RK0X8mbgoC1Nt8JE=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1609813202; KLBRSID=d017ffedd50a8c265f0e648afe355952|1609813282|1609811687'''
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text

    except requests.HTTPError as e:
        print(e)
        print("HTTPError")
    except requests.RequestException as e:
        print(e)
    except:
        print("Unknown Error !")