import pandas as pd
import requests
import os
from tqdm import tqdm
import json

def load_download_history():
    """加载下载历史记录"""
    history_file = 'download_history.json'
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            return json.load(f)
    return {'completed': [], 'failed': []}

def save_download_history(completed, failed):
    """保存下载历史记录"""
    history_file = 'download_history.json'
    with open(history_file, 'w') as f:
        json.dump({'completed': completed, 'failed': failed}, f)

def download_apk(url, package_name):
    """
    下载APK文件
    
    Args:
        url: APK下载链接
        package_name: 应用包名，用于命名文件
    """
    try:
        if not os.path.exists('apk_list'):
            os.makedirs('apk_list')
            
        file_path = os.path.join('apk_list', f'{package_name}.apk')
        
        # 检查文件是否已存在
        if os.path.exists(file_path):
            print(f"\n文件已存在，跳过: {package_name}")
            return True, package_name
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
        
        response = requests.get(url, stream=True, headers=headers)
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        
        print(f"\n开始下载: {package_name}")
        
        with open(file_path, 'wb') as f, tqdm(
            desc=package_name,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for data in response.iter_content(chunk_size=1024*1024):
                size = f.write(data)
                pbar.update(size)
        
        print(f"下载完成: {file_path}")
        return True, package_name
        
    except Exception as e:
        print(f"下载失败 {package_name}: {str(e)}")
        return False, package_name

def main():
    try:
        # 加载历史记录
        history = load_download_history()
        completed = history['completed']
        failed = history['failed']
        
        # 检查并清理已完成列表中的无效条目
        completed = [pkg for pkg in completed if os.path.exists(os.path.join('apk_list', f'{pkg}.apk'))]
        
        df = pd.read_csv('app_details.csv')
        total = len(df)
        success = len(completed)  # 初始成功数从历史记录中获取
        
        print(f"已完成下载: {len(completed)}")
        print(f"之前失败: {len(failed)}")
        
        for index, row in df.iterrows():
            package_name = row['Package']
            
            # 跳过已完成的下载
            if package_name in completed:
                continue
                
            if pd.notna(row['Download_URL']) and row['Download_URL'].strip() != '':
                success_flag, pkg = download_apk(row['Download_URL'], package_name)
                if success_flag:
                    success += 1
                    completed.append(package_name)
                else:
                    if package_name not in failed:
                        failed.append(package_name)
                
                # 每完成一个下载就保存一次进度
                save_download_history(completed, failed)
        
        print(f"\n下载完成!")
        print(f"成功: {success}/{total}")
        if failed:
            print("下载失败的应用:")
            for pkg in failed:
                print(f"- {pkg}")
        
    except Exception as e:
        print(f"处理CSV文件时出错: {str(e)}")
        # 发生错误时也保存进度
        save_download_history(completed, failed)

if __name__ == "__main__":
    main()