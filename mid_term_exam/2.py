url = 'https://search.daum.net/search?w=tot&q=bigdata'
splitted_url = url.split('?')[1].split('&')
dic = {}
for i in splitted_url:
    key, value = i.split('=')
    dic[key] = value

print(dic)

dic['q'] = 'iot'

print(dic)