import requests

var = 'http://httpbin.org/#/HTTP_Methods/post_post'
var1 = 'http://www.picshare.ru/upload/'

# print(
#     requests.request('options', var1).headers
# )

p = requests.get('http://www.picshare.ru/view/9603620/')
out = open("...\img.jpg", "wb")
out.write(p.content)
out.close()
