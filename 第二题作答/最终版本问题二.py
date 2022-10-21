# _*_coding : uft-8 _*_
# @Time : 2022-10-19 14:50
# @Author : 崔奕斐
# @File : 最终版本问题二
# @Project : Python基础
def getFollowingList(uid):
    url = f'https://api.bilibili.com/x/relation/followings?vmid={uid}&pn=1&ps=20&order=desc&order_type=attention&jsonp=jsonp&callback=__jp5'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'}
    infos = []

    subscribe = []


    for i in range(1, 6):
        html = requests.get(url = url,headers = headers)
        if html.status_code != 200:
            print("Error")

        html_data = html.text
        json_dict = json.loads(text)


        lists = json_dict['data']['list']

        for list in lists:
            info = {}
            info['uid'] = list['mid']
            info['name'] = list['name']
            info['fan'] = list['fans']
            info['level'] = list['level']

            subscribe.append((usr['mid'], list['mtime']))
            infos.append(info)

    newuid = insertUser(infos)
    insertFollowing(uid, subscribe)

    return newuid

#连接数据库源码
def createdb():
    link = sqlite3.connect('BiliFollowDB.db')

    print("database open success")

    User1TableDDL =
                create table (
                UID int PRIMARY KEY     NOT NULL,
                NAME varchar            NOT NULL,
                level int               NOT NULL,
                fans int                NOT NULL,)
    User2TableDDL =
                create table(
                UID int primary KEY NOT NULL,
                NAME varcha         NOT NULL,
                level int           NOT NULL,
                fans int            NOT NULL,
    )
     # 创建第一个用户
    link.execute(User1TableDDL)

    # 创建第二个用户
    link.execute(User1TableDDL)

    print("database create success")
    sql = f'select* from User1TableDDL natural join User1TableDDL'
    link.execute(sql)
    link.commit()
    link.close()

## 获取交集中得每个账号，给出UID、用户昵称、等级 粉丝数
def getRelations(userId):
    relation_text=requests.get(f'https://api.bilibili.com/x/relation/followings?vmid={uid}&pn=1&ps=20&order=desc&order_type=attention&jsonp=jsonp&callback=__jp5'.format(userId),headers=header).text
    relation_json=json.loads(relation_text)
    uids = relation_json['data']['mid']
    names = relation_json['data']['name']
    levels = relation_json['data']['level']
    fans = relation_json['data']['follower']
    return uids, names, levels, fans






