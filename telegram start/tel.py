import requests
query = {
    'posts' : requests.get("https://jsonplaceholder.typicode.com/posts").json(),
    'comments' : requests.get("https://jsonplaceholder.typicode.com/comments").json()
}
print(query['posts'][0]['userId'])

