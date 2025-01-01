"""
qui usiamo la libreria pydantic per verificare e validare gli input nella nostra tabella di user
prima class , se email non e string(EmailStr) non possiamo creare(usercreate) user etc....
Usercreate lo usiamo nelle applicazioni POST e PUT
post lo usiamo per creare
put lo usiamo per modificare

qui definiamo il formato che devono avere gli input ricevuti per creare uno users e pydantic li verifica
perche questa libreria gia contiene le funzioni con regex etc...
"""


from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int



