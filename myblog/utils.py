import requests

API_URL = "http://127.0.0.1:8000/api/"

def getPosts():
    response = requests.get(API_URL + "getPosts")

    if response.status_code != 200:
        raise Exception(response.status_code)

    return response.json()

def getAllPosts():
    response = requests.get(API_URL + "getAllPosts")

    if response.status_code != 200:
        raise Exception(response.status_code)

    return response.json()

def getPost(id):
    response = requests.get(API_URL + "getPost/" + str(id))

    if response.status_code != 200:
        raise Exception(response.status_code)

    return response.json()

def createPost(title, description, content, author, thumbnail):

    data = {
        "title": title,
        "description":description,
        "content": content,
        "author": author,
        "thumbnail": thumbnail,
    }

    response = requests.post(API_URL + "createPost", data=data)

    if response.status_code != 200:
        raise Exception(response.status_code)

    return response.json()

def updatePost(id, title, description, content, author, thumbnail):

    data = {
        "id": id,
        "title": title,
        "description": description,
        "content": content,
        "author": author,
        "thumbnail": thumbnail,
    }

    response = requests.post(API_URL + "updatePost", data=data)

    if response.status_code != 200:
        raise Exception(response.status_code)

    return response.json()

def deletePost(id):

    response = requests.delete(API_URL + "deletePost/" + str(id))
    if response.status_code != 200:
        raise Exception(response.status_code)

    return response.json()