import os,json,requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
#伪装头
videos_list = os.listdir(r'C:\Users\MSYU\Desktop\Dump-0107-14-06-54\aweme.snssdk.com\aweme\v1\aweme\post')
                         # r'获取文件夹内所有json包名

count = 1  #计数，用来作为视频名字

for videos in videos_list:  #循环json列表，对每个json包进行操作
    a = open(r'C:\Users\MSYU\Desktop\Dump-0107-14-06-54\aweme.snssdk.com\aweme\v1\aweme\post\{}'.format(videos),encoding='utf-8')  #打开json包
    content = json.load(a)['aweme_list'] #取出json包中所有视频
    try:
        for video in content:  #循环视频列表，选取每个视频
            video_url = video['video']['play_addr_265']['url_list'][3] #获取视频url，每个视频有多个url，我选的第3个
            # 注意这里视频的链接可能在['url_list'][3]也可能在其他['url_list'][4]，需要具体操作
            print(video_url)
            videoMp4 = requests.request('get',video_url,headers=headers,verify=False).content #获取视频二进制代码
            with open(r'C:\Users\MSYU\Desktop\video\{}.mp4'.format(count),'wb') as f: #以二进制方式写入路径，记住要先创建路径
                f.write(videoMp4)  #写入
                print('视频{}下载完成'.format(count)) #下载提示
            count += 1 #计数+1
    except Exception as e:
        for video in content:  # 循环视频列表，选取每个视频
            video_url = video['video']['play_addr_265']['url_list'][2]  # 获取视频url，当没有第3个链接时，换回获取第2个链接
            print(video_url)
            videoMp4 = requests.request('get', video_url, headers=headers, verify=False).content  # 获取视频二进制代码
            with open(r'C:\Users\MSYU\Desktop\video\{}.mp4'.format(count), 'wb') as f:  # 以二进制方式写入路径，记住要先创建路径
                f.write(videoMp4)  # 写入
                print('视频{}下载完成'.format(count))  # 下载提示
            count += 1  # 计数+1
