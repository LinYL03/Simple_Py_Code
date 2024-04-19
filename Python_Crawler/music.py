# 发送请求的库
import requests

# 目标URL
url = 'https://webfs.tx.kugou.com/202404191124/4c6b335e08b26592800c500e9fe8882c/v2/a7e525877d99f0397f4ac377c704aac0/G170/M0A/1D/01/6g0DAF12tEOAKZdDAC_pa13F6oo767.mp3'
# 网易云 https://m701.music.126.net/20240419120811/cc3e61933a10f9ba5826df426daef7a3/jdyyaac/015c/035a/0409/66fca6935140ee9455f13c45945784aa.m4a

# 防止被ban
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
}

# 获取资源
resp = requests.get(url=url, headers=headers)

# 测试，查看信息
print(resp)
print(resp.content)