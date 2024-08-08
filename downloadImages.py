import os
import re
import requests
from markdown import Markdown
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def sanitize_filename(filename):
    # Replace invalid characters with an underscore or any other valid character
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def download_image(url, save_path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {url} to {save_path}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def extract_image_links(md_content, base_url):
    md = Markdown(extensions=['markdown.extensions.fenced_code'])
    html_content = md.convert(md_content)
    soup = BeautifulSoup(html_content, 'html.parser')
    image_urls = []

    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            img_url = urljoin(base_url, src)
            image_urls.append(img_url)
    
    return image_urls

def process_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        md_content = file.read()
    
    base_url = 'file://' + os.path.dirname(file_path) + '/'
    image_urls = extract_image_links(md_content, base_url)
    
    for img_url in image_urls:
        img_name = sanitize_filename(os.path.basename(img_url))
        save_path = os.path.join('images', img_name)
        download_image(img_url, save_path)

def process_directory(directory):
    if not os.path.exists('images'):
        os.makedirs('images')
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_markdown_file(file_path)

if __name__ == "__main__":
    directory = 'blogs'  # Change this to your directory
    process_directory(directory)
