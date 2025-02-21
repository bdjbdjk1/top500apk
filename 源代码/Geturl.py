import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# 初始化浏览器
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

url = "https://sj.qq.com/app"
driver.get(url)
time.sleep(5)  # 初始加载时间

# 设置翻页次数
scroll_times = 20  # 需要翻页的次数
scroll_pause_time = 3  # 每次滚动后的等待时间
software_list = []  # 使用列表来保持顺序
seen_urls = set()  # 使用集合来检查重复

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
software_cards = soup.find_all('a', {'class': 'List_gameCard__n7zLP GameCard_gameCard__2kBjh GameCard_COMMON__jZRY5 Link_link__2eb5_'})

for card in software_cards:
    app_url = card.get('href')
    if app_url:
        full_url = f"https://sj.qq.com{app_url}"
        if full_url not in seen_urls:  # 检查是否已存在
            seen_urls.add(full_url)  # 添加到去重集合
            software_list.append(full_url)  # 保持顺序添加到列表


for i in range(scroll_times):
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    
    software_cards = soup.find_all('a', {'class': 'List_gameCard__n7zLP GameCard_gameCard__2kBjh GameCard_COMMON__jZRY5 Link_link__2eb5_'})
        
    for card in software_cards:
        app_url = card.get('href')
        if app_url:
            full_url = f"https://sj.qq.com{app_url}"
            if full_url not in seen_urls:  # 检查是否已存在
                seen_urls.add(full_url)  # 添加到去重集合
                software_list.append(full_url)  # 保持顺序添加到列表
driver.quit()

# 将所有链接写入文件
with open('appdetail_urls.txt', 'w', encoding='utf-8') as file:
    for url in software_list:
        file.write(url + '\n')

print(f"总共抓取到 {len(software_list)} 个不重复的URL")
print("所有URL已保存到 app_urls.txt 文件中")
