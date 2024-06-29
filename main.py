import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app:app", host="deepak.prashne.com",port=80, log_level="info")
