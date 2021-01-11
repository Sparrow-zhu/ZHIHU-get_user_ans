import requests
import get_data
import time
import datetime
import locale
import re
import json
import izhiqunDB

id = 0
date = ''
title = ''
ans_link = ''
looked = 0
followers = 0
totals = 1 # 获取当下话题的总回答数

final_data = [] # 最终数据
comment = [] # 用来存放数据

def parse_anslink(ans_link):

    global id
    global title
    global date
    global looked
    global followers
    global comment
    global final_data

    # 转化 str型且含有逗号 的数字为int型
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    ########### 请求过于频繁可能会遇到【('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))】这个问题，忽略掉 ###########
    try:
        comment = []
        id += 1

        # 获取话题的关注人数,浏览量和编辑日期
        html_ans_link = get_data.get_data(ans_link)

        title = re.findall('<h1 class="QuestionHeader-title">(.*?)</h1>', html_ans_link)[0]
        date = re.findall('<span data-tooltip="(.*?)</span>', html_ans_link)[0].replace('">', ' > ')
        followers = locale.atoi(re.findall('关注者</div><strong class="NumberBoard-itemValue" title="(.*?)"', html_ans_link)[0])
        looked = locale.atoi(re.findall('被浏览</div><strong class="NumberBoard-itemValue" title="(.*?)"', html_ans_link)[0])
        totals = locale.atoi(re.findall('<meta itemProp="answerCount" content="(.*?)"/>', html_ans_link)[0])

    except requests.exceptions.ConnectionResetError:
        print(ans_link)
        print('Handle Exception1')

    except requests.exceptions.ConnectionError:
        print(ans_link)
        print('Handle Exception2')

    comment.append(id)
    comment.append(date)
    comment.append(title)
    comment.append(ans_link)
    comment.append(looked)
    comment.append(followers)
    comment.append(totals)
    print(comment)

    final_data.append(comment)

    return

def get_user_ans(user_name_ch, link):
    global ans_link
    print("～～～～～～～～～～～～～～～～～feed～～～～～～～～～～～～～～～～～")

    html_data = get_data.get_data(link)  # 返回的就是response.text

    infor_list = re.findall('\{"target":(.*?)"feed", "id":(.*?)\}', html_data)

    for data in infor_list:

        # 此时data是元组，需要转换成str类型用来正则
        data = str(data)
        if_answer = re.findall('"verb": "(.*?)"',data)[0]

        # 只有'ANSWER_CREATE'的情况是回答问题，需要爬取
        if if_answer == 'ANSWER_CREATE':

            link_id1 = re.findall('"https://api.zhihu.com/questions/(.*?)"', data)[0]
            link_id2 = re.findall('"url": "https://api.zhihu.com/answers/(.*?)"', data)[0]

            # 获得探长的回答链接
            ans_link = 'https://www.zhihu.com/question/' + link_id1 + '/answer/' + link_id2

            # 分析探长的回答链接
            parse_anslink(ans_link)

    # 判断feed中还有没有下一页，返回的是bool值
    judge = json.loads(html_data)
    feed_is_end = judge['paging']['is_end']
    print(feed_is_end)

    if feed_is_end == False:

        # 进入下一个feed流信息
        next_link = re.findall('"next": "(.*?)"', html_data)[0]
        get_user_ans(user_name_ch, next_link)

        time.sleep(0.4)

    else:

        izhiqunDB.create_table(user_name_ch)
        for info in final_data:
            izhiqunDB.insert(user_name_ch, info)
        izhiqunDB.regulate(user_name_ch)
        print("所有数据爬取完毕！")

    return