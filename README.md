# 应用宝APK批量下载与分析工具

这是一个用于批量抓取和下载应用宝(sj.qq.com)前500个热门应用的Python工具集。该项目可以自动获取应用详情、下载APK文件并进行MD5校验。

## 功能特点

- 自动抓取应用宝热门应用列表
- 获取应用详细信息(名称、包名、评分等)
- 批量下载APK文件
- MD5校验确保下载完整性
- 断点续传支持
- 详细的下载进度显示

## 项目结构

1. Geturl.py 获取应用包前500个软件详细页面链接
2. Getdetail.py 应用名称、应用包名、标签、评分、开发者、版本、md5、下载地址保存为csv文件
3. download.py 读取csv中的下载地址下载所有apk并计算md5码和抓取到的md5码对比，如果一致则表示下载成功


top500apk/
├── 源代码/
│ ├── Geturl.py # 抓取应用详情页URL
│ ├── Getdetail.py # 获取应用详细信息
│ ├── Download.py # 下载APK文件
│ ├── Md5.py # MD5校验工具
│ ├── app_urls.txt # 存储应用URL列表
│ └── download_history.json # 下载历史记录
├── app_details.csv # 应用详细信息数据
└── README.md



## 实现流程

### 1. 获取应用URL (Geturl.py)

- 使用Selenium自动化访问应用宝首页
- 通过滚动加载获取前500个应用的详情页URL
- 使用BeautifulSoup解析页面内容
- 将URL保存到app_urls.txt文件

### 2. 获取应用详细信息 (Getdetail.py)

- 读取app_urls.txt文件中的URL
- 使用Selenium自动化访问每个应用详情页
- 使用BeautifulSoup解析页面内容
- 提取应用名称、包名、评分、开发者、版本、MD5值、下载地址
- 将数据保存到app_details.csv文件


### 3. 下载APK文件 (Download.py)

- 读取app_details.csv中的下载地址
- 使用requests库下载APK文件
- 支持断点续传
- 显示下载进度条
- 记录下载历史到download_history.json



### 4. MD5校验 (Md5.py)

- 计算下载文件的MD5值
- 与应用商店提供的MD5进行对比验证
- 确保文件完整性

## 依赖库要求

- requests
- beautifulsoup4 
- selenium
- pandas
- tqdm

## 安装使用

1. 克隆项目:
```bash
git clone https://github.com/[username]/top500apk.git
cd top500apk
```

2. 安装依赖:
```bash
pip install -r requirements.txt
```

3. 运行脚本:
```bash
python Geturl.py      # 获取应用URL
python Getdetail.py   # 获取应用详情
python Download.py    # 下载APK文件
python Md5.py        # MD5校验
```

## 注意事项

1. 需要安装Chrome浏览器和ChromeDriver
2. 确保网络连接稳定
3. 下载大量APK需要足够的存储空间
4. 仅用于学习研究用途

## 数据文件说明

- `app_urls.txt`: 存储应用详情页URL列表
- `app_details.csv`: 包含应用的详细信息(名称、包名、标签、评分等)
- `download_history.json`: 记录下载成功和失败的应用

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request来帮助改进项目。


## 致谢

感谢应用宝提供的开放平台。