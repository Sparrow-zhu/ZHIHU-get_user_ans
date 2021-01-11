import zhihu

if __name__ == '__main__':

    user_name = 'quan-wai-tong-xue'
    user_name_ch = "圈外同学"

    link = 'https://www.zhihu.com/api/v3/feed/members/' + user_name + \
           '/activities?limit=7&session_id=1258885770606923776&desktop=true'

    zhihu.get_user_ans(user_name_ch, link)