import uvicorn

if __name__ == "__main__":
    uvicorn.run("book_collector.app.main:app", host="localhost", port=8003, reload=True)
