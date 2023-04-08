import requests
import json
def Name(a):
    print("Введите id: ")
    try:
        response= requests.get("https://jsonplaceholder.typicode.com/posts/"+a)
        response_2 = requests.get("https://jsonplaceholder.typicode.com/comments/"+a)
        print("Post_id: ", response_2.json()['postId'])
        print("Post_title: ", response.json()['title'])
        print("Post_body: ", response.json()['body'])
        print("Com_id: ", response_2.json()['id'])
        print("User_name: ", response_2.json()['name'])
        print("User_email: ", response_2.json()['email'])
        print("Com_body: ", response_2.json()['body'])
    except:
        return "Error 404"

while True:
    print("Введите id: ")
    a = input()
    Name(a)


