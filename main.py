from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
import requests
from bs4 import BeautifulSoup

app = FastAPI()

class ScrapeRequest(BaseModel):
    url: HttpUrl

@app.post("/scrape")
def scrape(req: ScrapeRequest):
    # 1) Fetch the page
    resp = requests.get(req.url)
    resp.raise_for_status()
    html = resp.text

    # 2) Parse the HTML
    soup = BeautifulSoup(html, "html.parser")

    # 3) Extract title, headings, body
    title = soup.title.string if soup.title else ""
    headings = [h.get_text(strip=True) for h in soup.find_all("h1")]
    body = " ".join(p.get_text(strip=True) for p in soup.find_all("p"))

    # 4) Return a JSON response
    return {"url": req.url, "title": title, "headings": headings, "body": body}
