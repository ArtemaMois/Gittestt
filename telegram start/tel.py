import requests


query = {
    'posts' : requests.get("https://jsonplaceholder.typicode.com/posts").json(),
    'comments' : requests.get("https://jsonplaceholder.typicode.com/comments").json()
}


def Answer(b):
    comment = []
    post = []
    for i in range(len(query['posts'])):
        if query['posts'][i]['userId'] == b:
                post.extend(query['posts'][i].items())
        for j in range(len(query['comments'])):
            if query['comments'][j]['postId'] == query['posts'][b]['id']:
                    comment.extend(query['comments'][j].items())

    answer = {'comment' : comment,
            'post' : post}

    return answer

def User(a):
     user = {'userId' : Answer(a)}
     return user

  
a = User(2)
print(a)

