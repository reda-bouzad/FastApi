from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {
        "data" : {
            "name": "Reda"
        }
    }

@app.get("/about")
def about():
    return {
        "data":"about page"
    }

@app.get("/blog/unpublished")
def unpublished():
    return {
        "data": "all unpublished blogs"
    }


@app.get("/blog/{id}")
def show(id: int):
    return {
        "data": id
    }