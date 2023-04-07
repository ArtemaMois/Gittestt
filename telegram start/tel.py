import requests
def Name(b):
    a = input()
    if a is not None:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        print("Post_Id: ",response.json()[b]["userId"])
        print("Post_title: ", response.json()[b]["title"])
        print("Post_body: ", response.json()[b]["body"])


def Comment(b):
    a = input()
    if a is not None:
        response = requests.get("https://jsonplaceholder.typicode.com/comments")
        print("Comments_id: ", response.json()[b]["id"])
        print("Comments_name", response.json()[b]["name"])
        print("Comments_email", response.json()[b]["email"])
        print("Comments_body", response.json()[b]["body"])


response = requests.get("https://jsonplaceholder.typicode.com/posts")
for i in range(len(response.json())):
    Name(i)
    print("\n", "Comments", "\n")
    Comment(i)



