from sqlalchemy.orm import Session
import random
import string
from . import models, schemas

def get_lectures(db: Session):
    return db.query(models.Lectures).all()

def clear_lectures(db: Session):
    db.query(models.Lectures).delete()
    db.commit()

def create_lecture(db: Session):
    idx = 0
    for _ in range(1000):

        idx += 1
        random_three_digit_number = random.randint(100, 999)
        random_three_letter = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
        title = random_three_letter + " " +  str(random_three_digit_number)
    
        db_lecture = models.Lectures(id=idx, title=title)
        db.add(db_lecture)
        db.commit()
    


    