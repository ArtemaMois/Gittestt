import requests
query = {
    'posts' : requests.get("https://jsonplaceholder.typicode.com/posts").json(),
    'comments' : requests.get("https://jsonplaceholder.typicode.com/comments").json()
}

comment = []
post = []
for i in range(len(query['posts'])):
    if query['posts'][i]['userId'] == 1:
            post.extend(query['posts'][i].items())
    for j in range(len(query['comments'])):
        if query['comments'][j]['postId'] == query['posts'][1]['id']:
                comment.extend(query['comments'][j].items())

answer = {'comment' : comment,
          'post' : post}

print(answer['post'])