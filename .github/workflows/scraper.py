import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Điều chỉnh selector này để phù hợp với trang web bạn muốn scrape
    article = soup.find('article')
    
    if article:
        return article.get_text()
    else:
        return "Không tìm thấy nội dung bài viết."

def save_content(content):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"scraped_content_{today}.txt"
    
    # Tạo thư mục scraped_content nếu nó chưa tồn tại
    os.makedirs("scraped_content", exist_ok=True)
    
    # Lưu file vào thư mục scraped_content
    filepath = os.path.join("scraped_content", filename)
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

if __name__ == "__main__":
    # Thay đổi URL này thành trang web bạn muốn scrape
    url = "https://example.com/article"
    
    content = scrape_website(url)
    save_content(content)
