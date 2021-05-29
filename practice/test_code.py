<<<<<<< HEAD
import requests
import json

data = {'key': 'value'}

r = requests.post('https://httpbin.org/post', json=json.dumps(
    data))  # отправляем пост-запрос, но только в этот раз тип передаваемых данных будет JSON
print(r.content)
=======
>>>>>>> f3b19fdf2b6459d6ea6e4d489f5e22e34c984bcb
