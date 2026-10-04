from fastapi import FastAPI, HTTPException
from finops.costs import InputError, summarize

app = FastAPI()


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.post("/costs")
def post_costs(body: dict):
    try:
        return summarize(body.get("lines"), body.get("budget"))
    except InputError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
