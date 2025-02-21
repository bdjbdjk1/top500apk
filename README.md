# 应用宝APK批量下载与分析工具


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">应用宝APK批量下载与分析工具</h3>
  <p align="center">
    一个用于批量抓取和下载应用宝前500个热门应用的Python工具集
  </p>
</p>

## 目录

- [功能特点](#功能特点)
- [安装步骤](#安装步骤)
- [文件目录说明](#文件目录说明)
- [开发的架构](#开发的架构)
- [如何贡献](#如何贡献)
- [鸣谢](#鸣谢)

## 功能特点

- 自动抓取应用宝热门应用列表
- 获取应用详细信息(名称、包名、评分等)
- 批量下载APK文件
- MD5校验确保下载完整性
- 断点续传支持
- 详细的下载进度显示


## 安装步骤

1. 克隆项目
```bash
git clone https://github.com/[username]/top500apk.git
cd top500apk
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行脚本
```bash
python Geturl.py      # 获取应用URL
python Getdetail.py   # 获取应用详情
python Download.py    # 下载APK文件
python Md5.py        # MD5校验
```

## 文件目录说明

```
top500apk/
├── 源代码/
│   ├── Geturl.py      # 抓取应用详情页URL
│   ├── Getdetail.py   # 获取应用详细信息
│   ├── Download.py    # 下载APK文件
│   ├── Md5.py        # MD5校验工具
│   ├── app_urls.txt   # 存储应用URL列表
│   └── download_history.json # 下载历史记录
├── app_details.csv    # 应用详细信息数据
├── requirements.txt   # 依赖包
└── README.md
```

## 开发的架构

### 1. 获取应用URL (Geturl.py)
- 使用Selenium自动化访问应用宝首页
- 通过滚动加载获取前500个应用的详情页URL
- 使用BeautifulSoup解析页面内容

### 2. 获取应用详情 (Getdetail.py)
- 读取URL并访问详情页
- 解析提取应用信息
- 保存到CSV文件

### 3. 下载APK文件 (Download.py)
- 批量下载APK
- 支持断点续传
- 进度显示

### 4. MD5校验 (Md5.py)
- 文件完整性验证



## 如何贡献

1. Fork 本项目
2. 创建新特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request


## 鸣谢

- 感谢应用宝提供的开放平台
- 感谢所有贡献者的参与
