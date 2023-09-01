from fastapi import FastAPI,Depends,status,File, UploadFile
from typing import Optional
from pydantic import BaseModel
import models
import schema
from dataBase import engine,SessionLocal
from sqlalchemy.orm import Session
from faker import Faker
models.Base.metadata.create_all(engine)
app = FastAPI()

@app.get('/e')
def fast():
    return {'message': {"NAME":"gowtham"}}
@app.get('/aut/{ids}')
def an(ids:int):
    return {'message': {"NAME":ids}}

@app.get('/ac')
def index(limit,pulished=True):
    return {'message': {"NAME":{limit}}}


@app.get('/acd')
def index(limit=9,pulished: bool=True,sort: Optional[str]=None):
    return {'message': {"NAME":{limit}}}




def get_db():
    db = SessionLocal()
    try:
        yield db 

    finally:
        db.close()



@app.post("/users",status_code=status.HTTP_201_CREATED)
def posting(request:schema.user,db:Session=Depends(get_db)):
    new = models.user(name=request.name,lastname=request.lastname)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@app.get("/users",status_code=status.HTTP_200_OK)
def geting(db:Session=Depends(get_db)):
    users = db.query(models.user).all()
    return users

@app.get("/users/{id}",status_code=status.HTTP_200_OK)
def getting_id(id,db:Session=Depends(get_db)):
    users=db.query(models.user).filter(models.user.id==id).first()
    return users

@app.delete("/users/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
def deleting(id,db:Session=Depends(get_db)):
    users=db.query(models.user).filter(models.user.id==id).delete(synchronize_session=False)
    db.commit()
    return "deleted"




@app.get('/aut/{ids}')
def an(ids:int):
    return {'message': {"NAME":ids}}

@app.get("/{id}",status_code=status.HTTP_200_OK)
def fake(id:int):
    from faker import Faker

    fake = Faker()
    user_data = []

    for i in range(id):
        name = fake.name()
        address = fake.address()
        email = fake.email()
        profile_picture = fake.image_url()
        
        user_data.append({
            "Name": name,
            "Address": address,
            "Email": email,
            "Profile Picture": profile_picture
        })
    
    return user_data
   
       


