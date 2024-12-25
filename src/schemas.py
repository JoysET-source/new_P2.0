"""
qui usiamo la libreria pydantic per verificare e validare gli input nella nostra tabella di user
prima class , se email non e string(EmailStr) non possiamo creare(usercreate) user etc....
Usercreate lo usiamo nelle applicazioni POST e PUT
post lo usiamo per creare
put lo usiamo per modificare
"""


from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int



