import requests

API_URL = "http://127.0.0.1:8000/api/"

def get_posts():
    response = requests.get(API_URL + "get-posts")

    if response.status_code != 200:
        raise Exception(response.status_code)

    return response.json()

def get_all_posts():
    response = requests.get(API_URL + "get-all-posts")

    if response.status_code != 200:
        raise Exception(response.status_code)

    return response.json()

def get_post(id):
    response = requests.get(API_URL + "get-post/" + str(id))

    if response.status_code != 200:
        raise Exception(response.status_code)

    return response.json()

def create_post(title, description, content, author, thumbnail):

    data = {
        "title": title,
        "description":description,
        "content": content,
        "author": author,
        "thumbnail": thumbnail,
    }

    response = requests.post(API_URL + "create-post", data=data)

    if response.status_code != 200:
        raise Exception(response.status_code)

    return response.json()

def update_post(id, title, description, content, author, thumbnail):

    data = {
        "id": id,
        "title": title,
        "description": description,
        "content": content,
        "author": author,
        "thumbnail": thumbnail,
    }

    response = requests.post(API_URL + "update-post", data=data)

    if response.status_code != 200:
        raise Exception(response.status_code)

    return response.json()

def delete_post(post_id):

    response = requests.delete(API_URL + "delete-post/" + str(post_id))

    if response.status_code != 200:
        raise Exception(response.status_code)

    return response.json()