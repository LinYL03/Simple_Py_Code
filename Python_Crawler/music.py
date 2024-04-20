# 发送请求的库
import requests
import json

# 音乐列表
list_url = 'https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1713617376825&mid=a5afaab1d4f0c44e88a94b52be2ef494&uuid=a5afaab1d4f0c44e88a94b52be2ef494&dfid=2UHwLc0RXaIU1bZMCV3rWVIv&keyword=%E6%9B%B8%E5%BA%97%E3%82%AC%E3%83%BC%E3%83%AB%C2%A0(Positive%C2%A0ver.)&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=05a09119fe3399a96c497b1a16c14c56'

# 音乐信息的url地址 (无法像视频中一样做删减，此url删除一部分会提取不到数据)
info_url = 'https://wwwapi.kugou.com/play/songinfo?srcappid=2919&clientver=20000&clienttime=1713616904614&mid=a5afaab1d4f0c44e88a94b52be2ef494&uuid=a5afaab1d4f0c44e88a94b52be2ef494&dfid=2UHwLc0RXaIU1bZMCV3rWVIv&appid=1014&platid=4&encode_album_audio_id=jewyy89&token=&userid=0&signature=41414122f9d8deae27a149c0ec7543a7'

# 目标URL
url = 'https://webfs.tx.kugou.com/202404191124/4c6b335e08b26592800c500e9fe8882c/v2/a7e525877d99f0397f4ac377c704aac0/G170/M0A/1D/01/6g0DAF12tEOAKZdDAC_pa13F6oo767.mp3'
# 网易云 https://m701.music.126.net/20240419120811/cc3e61933a10f9ba5826df426daef7a3/jdyyaac/015c/035a/0409/66fca6935140ee9455f13c45945784aa.m4a

# 防止被ban
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
}

# 获取资源
# m_resp = requests.get(url=url, headers=headers)
list_resp = requests.get(url=list_url, headers=headers)

# 测试，查看信息
# print(m_resp)
# print(m_resp.text)

print(f"访问结果为：{list_resp}")
print()
# text中有干扰信息，具体为开始的前8个字符，和最后一个字符，可以使用切片的方法[12:-2]，这样text就是一个json文件了，仅限酷狗音乐 使用json.loads()方法转成字典形式
# print(list_resp.text)
song_list = json.loads(list_resp.text[12:-2])['data']['lists']
# print(song_list)
# print()
"""
for i, song in enumerate(song_list):
这是一个循环语句，使用 enumerate 函数遍历 song_list 列表中的元素。enumerate 函数返回一个包含索引和值的迭代器，i 是索引，song 是值，代表列表中的每一首歌曲。
print(f"{i+1} --- {song.get('SongName')} --- {song.get('FileHash')}")
这是打印语句，使用了 f-string 格式化输出。具体含义如下：
{i+1}：打印歌曲的序号，因为索引从0开始，所以需要加1。
---：打印分隔符，用来分隔序号、歌曲名称和文件哈希。
{song.get('SongName')}：打印歌曲名称，使用 song.get('SongName') 来获取歌曲名称，如果该键不存在，则返回 None。
{song.get('FileHash')}：打印文件哈希，使用 song.get('FileHash') 来获取歌曲文件哈希，如果该键不存在，则返回 None。
.get()是python的字典中的方法
"""
for i, song in enumerate(song_list):
    print(f"{i+1} --- 歌曲名称：{song.get('SongName')} --- 哈希值：{song.get('FileHash')}")

"""
服务器相应的数据
文本使用.text
多媒体文件使用.content
.json()方法访问的文字是json类型
"""