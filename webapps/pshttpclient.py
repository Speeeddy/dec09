import requests


def add_user():
    payload = dict(name='steve', gender='male', age=2)
    response = requests.post('http://127.0.0.1:7878/users', json=payload)
    print(response.text)

def delete_user():
    response = requests.delete('http://127.0.0.1:7878/users/22222')
    print(response.text, response.status_code)



if __name__ == '__main__':
    delete_user()
