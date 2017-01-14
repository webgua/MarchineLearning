import urllib.request

url = 'http://www.qiushibaike.com/hot/'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
print(response.read())
# except urllib.error.URLError as e:
#     if hasattr(e,"code"):
#         print(e.code)
#     if hasattr(e,"reason"):
#         print(e.reason)
