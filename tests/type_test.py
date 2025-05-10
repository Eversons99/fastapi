from datetime import date
from pydantic import BaseModel

def mains(user_id: str):
    return user_id

class User(BaseModel):
    id: int
    name: str
    joined: date


my_second_user = {
    "id": 4,
    "name": "Everson",
    "joined": "2018-11-30"
}

my_user: User = User(id=3, name="John Doe", joined="2018-07-19")
my_second_user: User(**my_second_user)





# FastAPi is all based on Pydantinc and use it to validate data types and data
# def process_item(item: int | str): the value can be int or (|) str
# # def process_item(item: int | None): the value can be int or (|) None
# Types in square brackets are callef Generic Types