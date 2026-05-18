import requests

headers = {
 "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZXhwIjoxNzc5NjcxNjk2fQ.hQC6Tl7n3WgFCgyOgvlCVVCzuOrH226vHZRvvS270kk"
}

requisicao = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)

print(requisicao)
print(requisicao.json())