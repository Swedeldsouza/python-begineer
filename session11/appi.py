import requests
import json
url='https://reqres.in/api/users'
data=requests.get(url)


plain_text=data.text               #plain text convert to text to be read bt python
print(plain_text)

res=json.loads(plain_text)
print(res)


print(res['data'][0]['id'])

for i in res['data']:
    print(i['email'])
