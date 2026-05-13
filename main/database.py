# 2. 2. Non-functional Requirements
'''2.1 Database Integration
Use any SQL-based database of choice(PSQL)'''

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()
app = FastAPI()

engine = create_engine("postgresql://username:password@localhost/database_name")
Session = sessionmaker(bind=engine)
session = Session()


'''2.2 Authentication (Optional)
-Implement a basic authentication mechanism using OAuth
-Secure the `POST /expenses/` and `GET /expenses/` endpoints with authentication.'''

async def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "username")
    correct_password = secrets.compare_digest(credentials.password, "password")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username