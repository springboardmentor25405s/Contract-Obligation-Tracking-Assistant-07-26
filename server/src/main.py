from fastapi import FastAPI


app = FastAPI(title="Todo API")


@app.get("/health")
def health_check():
	return {"status": "ok"}
