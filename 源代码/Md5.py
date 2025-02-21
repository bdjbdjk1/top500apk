import hashlib
import os
import csv

# 文件夹路径
folder_path = r'E:\Python应用开发\应用宝\apk_list'

# 计算单个文件的 MD5
def calculate_md5(file_path):
    file_hash = hashlib.md5()
    with open(file_path, "rb") as file:
        while chunk := file.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()

# 批量计算文件夹下所有APK文件的MD5
def batch_calculate_md5(folder_path):

    # 遍历文件夹中的所有APK文件
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.apk'):
                file_path = os.path.join(root, file)
                md5_value = calculate_md5(file_path)
                print(f"MD5 of {file}: {md5_value}")

# 执行批量计算
if __name__ == '__main__':
    batch_calculate_md5(folder_path)