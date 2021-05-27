import requests


def testing_create_with_list():
    """
    Тестирование POST-запроса №1
    """

    response = requests.post('https://petstore.swagger.io/v2/user/createWithList', json=[{
        "id": 0,
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
        }])
    assert response.status_code == 200, 'That is not correct test!'


def testing_get_1():
    """
    Тестирование GET-запроса №1
    """

    response = requests.get('https://petstore.swagger.io/v2/user/string')
    data = dict(response.json())
    assert response.status_code == 200, 'Status code is not 200!'
    assert data['username'] == 'string', 'Username is incorrect'


def testing_put_1():
    """
    Тестирование PUT-запроса №1
    """

    response = requests.put('https://petstore.swagger.io/v2/user/{username}', json={"username": "string"})
    assert response.status_code == 200, 'Status code is not 200!'


def testing_delete_1():
    """
    Тестирование DELETE-запроса №1
    """

    response = requests.delete('https://petstore.swagger.io/v2/user/string')
    assert response.status_code == 200, 'Status code is not 200!'


def testing_get_2():
    """
    Тестирование GET-запроса №2
    """

    response = requests.get('https://petstore.swagger.io/v2/user/login?username=Pavel&password=12345')
    assert response.status_code == 200, 'Status code is not 200!'


def testing_get_3():
    """
    Тестирование GET-запроса №3
    """

    response = requests.get('https://petstore.swagger.io/v2/user/logout')
    assert response.status_code == 200, 'Status code is not 200!'


def testing_create_with_array():
    """
    Тестирование POST-запроса №2
    """

    response = requests.post('https://petstore.swagger.io/v2/user/createWithArray', json=[{
        "id": 0,
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
        }])
    assert response.status_code == 200, 'Status code is not 200!'


def testing_create_user():
    """
    Тестирование POST-запроса №2
    """

    response = requests.post('https://petstore.swagger.io/v2/user', json={
        "id": 0,
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
        })
    assert response.status_code == 200, 'Status code is not 200!'
