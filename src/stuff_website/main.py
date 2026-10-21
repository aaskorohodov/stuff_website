from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from stuff_website.logic.curses import get_random_curse
from stuff_website.logic.chuck_norris import get_random_chuck
from stuff_website.logic.your_mama import get_random_mama


app = FastAPI()

# Mount static files (CSS, JS)
app.mount("/static", StaticFiles(directory="src/stuff_website/static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="src/stuff_website/templates")


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
  return templates.TemplateResponse(request, "index.html", {"title": "Home"})

# ----------------


@app.get("/curses", response_class=HTMLResponse)
async def curses(request: Request):
  return templates.TemplateResponse(
      request, "curses.html", {"title": "Curses"}
  )


@app.get("/api/random-curse")
async def fetch_random_curse():
  return {"text": get_random_curse()}


# ----------------

@app.get("/your_mama", response_class=HTMLResponse)
async def your_mama(request: Request):
  return templates.TemplateResponse(
      request, "your_mama.html", {"title": "Your Mama..."}
  )


@app.get("/api/random-your-mama")
async def fetch_random_mama():
  return {"text": get_random_mama()}


# ----------------

@app.get("/chuck_norris", response_class=HTMLResponse)
async def your_mama(request: Request):
  return templates.TemplateResponse(
      request, "chuck.html", {"title": "Chick Norris"}
  )


@app.get("/api/random-chuck-norris")
async def fetch_random_mama():
  return {"text": get_random_chuck()}
