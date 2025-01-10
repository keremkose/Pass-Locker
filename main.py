from fastapi import FastAPI

app=FastAPI(root_path="http://localhost:8000/")

app.include_router()
