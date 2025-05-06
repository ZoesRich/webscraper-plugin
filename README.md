# Web Scraper Plugin

A Dify.ai plugin that scrapes any website (via BeautifulSoup and optional pagination), returns structured JSON (title, headings, links, body), and respects robots.txt.

## Features

- HTTP error handling (4xx/5xx detection)  
- Optional Selenium fallback for dynamic content  
- Automatic pagination via “Next” links  
- Rate-limiting and User-Agent rotation  
- `robots.txt` compliance  

## Quickstart

### 1. Clone this repo  
```bash
git clone https://github.com/<your-username>/webscraper-plugin.git
cd webscraper-plugin
