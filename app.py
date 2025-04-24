import uvicorn



if __name__ == "__main__":
    uvicorn.run("api:app", host="192.168.1.11", port=8001, reload=True)
