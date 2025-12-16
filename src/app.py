from fastapi import Depends, FastAPI
import book_resource as br
import  dependencies as deps
#app = FastAPI(dependencies=[Depends(deps.get_query_token)])
app = FastAPI()


app.include_router(br.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

if __name__ == "__main__":
    # Run the application in debug mode
    app.run(debug=True)