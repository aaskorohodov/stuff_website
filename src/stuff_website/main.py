from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from stuff_website.logic.curses import get_random_curse


app = FastAPI()

# Mount static files (CSS, JS)
app.mount("/static", StaticFiles(directory="src/stuff_website/static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="src/stuff_website/templates")


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
  return templates.TemplateResponse(request, "index.html", {"title": "Home"})


@app.get("/curses", response_class=HTMLResponse)
async def read_subpage1(request: Request):
  return templates.TemplateResponse(
      request, "curses.html", {"title": "Curses"}
  )


# API Endpoint returning JSON
@app.get("/api/random-curse")
async def fetch_random_text():
  return {"text": get_random_curse()}