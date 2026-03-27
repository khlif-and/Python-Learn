import requests
from rich import print

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data_list = response.json()

for post in data_list[:10]:
    print(f"ID: {post['id']} | Judul: {post['title']} | ISI: {post['body']}")
    print(f"-" * 50)