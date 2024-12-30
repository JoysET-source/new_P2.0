"""
questo lo usiamo per creare n users in automatico usando libreria requests
"""

import requests
import random
import string

def generate_random_string(lenght):
    return "".join(random.choices(string.ascii_letters, k=lenght))

def create_new_users(n):
    url = "http://127.0.0.1:8000/users/"
    for i in range(n):
        user = {
            "email": f"user{i}@example.com",
            "username": f"string{i}",
            "password": generate_random_string(8)
            }
        response = requests.post(url, json=user)
        print(f"Created users {i}: {response.status_code}")

create_new_users(10)