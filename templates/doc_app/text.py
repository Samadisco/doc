# import requests
# resp = requests.post('https://textbelt.com/text', {
#   'phone': '+233559801548',
#   'message': 'Hello Samuel, you are the best programmer in the world.',
#   'key': 'textbelt',
# })
# print(resp.json())



import requests

url = "https://d7sms.p.rapidapi.com/messages/v1/balance"

headers = {
	"Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdXRoLWJhY2tlbmQ6YXBwIiwic3ViIjoiYjg1MGQ4ZTQtYTFlNi00NzJhLTg2MDUtNTcwMDM5ODUyNjFlIn0.sOzXXSh4uUQQWeIkKi2X6sabJKzfj2aVyRdnzJYXdes",
	"X-RapidAPI-Key": "68b7f209d7mshd7db1c286f0e999p1dc0e8jsndfacd3140731",
	"X-RapidAPI-Host": "d7sms.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)