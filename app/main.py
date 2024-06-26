
from fastapi import FastAPI
from app.database import Base, engine
from app.routers import user, post

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(user.router)
app.include_router(post.router)
