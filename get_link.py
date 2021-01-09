import os
import json

url_list = []#空列表，用来存储每个视频链接
json_list = os.listdir(r'C:\Users\MSYU\Desktop\Dump-0107-14-06-54\aweme.snssdk.com\aweme\v1\aweme\post')#获取路径下面的文件名单
count = 0#计数，用来计算一共有多少个视频链接
for json_every in json_list:#循环名单下的每个json文件
    json_open = open(r'C:\Users\MSYU\Desktop\Dump-0107-14-06-54\aweme.snssdk.com\aweme\v1\aweme\post\{}'.format(json_every),encoding='utf-8')#打开json文件
    json_py = json.load(json_open)#将json对象转换为python对象

    for id in json_py['aweme_list']:
        aweme_id = id['aweme_id']#获取到字典中aweme_id对应的ID字符串数字
        share_url = 'https://www.iesdouyin.com/share/video/{}'.format(aweme_id)#拼接成抖音视频分享链接
        url_list.append(share_url)#将每个链接添加到列表中
        count += 1

with open(r'C:\Users\MSYU\Desktop\douyin.txt', 'w') as f:#新建一个douyin.txt文本
    for url_every in url_list:
        f.writelines(url_every + '\n')#将列表中的单个元素，写入到文本中，注意每行后面加个换行符
    print('视频{}下载完成'.format(count))
