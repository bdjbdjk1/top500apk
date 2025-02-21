import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import json
import time

# 定义函数，抓取应用详情
def scrape_app_details(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()  
    soup = BeautifulSoup(response.text, 'html.parser')

    # 应用名称
    app_name = soup.find('h1', class_='GameCard_name__Tqfsj').text
    print(app_name)
    
    # 应用包名
    app_package = url.split('/')[-1] 
    print(app_package)

    # 标签
    tags = soup.find('a', class_='TagList_tagName__rrPrj TagList_tagName-0__1lsEk Link_link__2eb5_').text
    print(tags)

    # 评分
    score = soup.find('p', class_='GameCard_starNumber__3yRPf').text
    print(score)

    # 开发者信息
    dev_info = soup.find('div', class_='AppInfo_info__p5Jlf')
    dev_p_tags = dev_info.find_all('p')
    for i in range(len(dev_p_tags)-1):
        if dev_p_tags[i].text.strip() == "开发者：":
            developer = dev_p_tags[i+1].text.strip()
            break
    else:
        developer = "未知开发者"
    print(developer)

    try:
        json_data = soup.find('script', id='__NEXT_DATA__').string
        data = json.loads(json_data)
        
        # 从dynamicCardResponse中获取应用信息
        app_info = data['props']['pageProps']['dynamicCardResponse']['data']['components'][1]['data']['itemData'][0]
        
        # 获取版本号和MD5
        version = app_info['version_name']
        md5 = app_info['md_5']
        print(f"版本号: {version}")
        print(f"MD5: {md5}")
        
        # 构建下载链接
        download_url = f"https://imtt2.dd.qq.com/sjy.00009/sjy.00004/16891/apk/{md5}.apk?fsname={app_package}_{version}.apk"
        print(f"下载链接: {download_url}")
        
    except Exception as e:
        version = ""
        md5 = ""
        download_url = ""
        print(f"提取信息失败: {e}")
    
    return {
        "Name": app_name,
        "Package": app_package,
        "Tags": tags,
        "Score": score,
        "Developers": developer,
        "Version": version,
        "MD5": md5,
        "Download_URL": download_url
    }

# 定义CSV表头
COLUMNS = ["Name","Package","Tags","Score","Developers","Version","MD5","Download_URL"]

# 读取txt文件中的URL
with open('app_urls.txt', 'r', encoding='utf-8') as file:
    urls = [line.strip() for line in file]

output_file = 'app_details.csv'
# 检查文件是否存在
file_exists = os.path.isfile(output_file)

# 遍历每个链接并抓取数据
print("开始抓取数据...")
for index, url in enumerate(urls):
    print(f"正在抓取第 {index + 1} 个链接: {url}")
    try:
        app_details = scrape_app_details(url)
        # 转换为DataFrame
        df_new = pd.DataFrame([app_details], columns=COLUMNS)  # 使用定义的列顺序
        
        # 如果文件不存在，创建新文件并写入表头
        # 如果文件存在，追加数据不写入表头
        df_new.to_csv(output_file, 
                     mode='a',
                     header=not file_exists,
                     index=False, 
                     encoding='utf-8-sig')
        
        # 第一次写入后，文件就存在了
        file_exists = True
        
        print(f"抓取到的数据: {app_details}")
    except Exception as e:
        print(f"抓取失败: {e}")

print(f"抓取完成，结果已保存至 {output_file}")
print(f"总共处理URL数量: {len(urls)}")