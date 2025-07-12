# scraping/fetcher.py
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import os

def fetch_chapter(url: str, output_dir: str = "data") -> str:
    os.makedirs(output_dir, exist_ok=True)
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path=f"{output_dir}/screenshot.png", full_page=True)
        
        content = page.content()
        soup = BeautifulSoup(content, "html.parser")
        browser.close()

        # Find main content block (Wikisource structure)
        main_content = soup.find("div", class_="mw-parser-output")
        if not main_content:
            print("[Warning] Could not find main content div.")
            return "No main content found."

        # Extract clean text from <p> tags
        paragraphs = main_content.find_all("p")
        cleaned_paragraphs = [
            p.get_text(strip=True) 
            for p in paragraphs 
            if p.get_text(strip=True) and len(p.get_text(strip=True)) > 50
        ]

        chapter_text = "\n\n".join(cleaned_paragraphs)

        # Save raw cleaned chapter text
        with open(f"{output_dir}/chapter_raw.txt", "w", encoding="utf-8") as f:
            f.write(chapter_text)

        return chapter_text
