import requests
import json
import base64
from getpass import getpass

url = 'https://cae-bootstore.herokuapp.com'

endpoint_login = "/login"
endpoint_user = "/user"
endpoint_book = "/book"

class ApiFuncs():
    def get_books():
        books = requests.get(url+endpoint_book)
        return books.json()['books']

    def get_single_book(book_id):
        single_book = requests.get(url+endpoint_book +'/'+str(book_id))
        return single_book.json()

    def register_user(payload):
        payload_json_string = json.dumps(payload)
        headers = {
            'Content-Type':'application/json'
        }
        response = requests.post(
            url + endpoint_user,
            data = payload_json_string,
            headers = headers
        )
        return response.text

    def login_user(user_name, password):
        auth_string = user_name + ":" + password
        
        headers={
            'Authorization' : "Basic "+base64.b64encode(auth_string.encode()).decode()
        }
        user_data = requests.get(
            url + endpoint_login,
            headers=headers
        )
        return user_data.json()

    def edit_user(token, payload):
        payload_json_string = json.dumps(payload)
        headers={
            'Content-Type':'application/json',
            'Authorization':'Bearer ' + token
        }
        response = requests.put(
            url + endpoint_user,
            data=payload_json_string,
            headers=headers
        )
        return response.text

    def delete_user(token):
        headers = {
            'Authorization':"Bearer " + token
        }
        response = requests.delete(
            url+endpoint_user,
            headers=headers
        )
        return response.text
