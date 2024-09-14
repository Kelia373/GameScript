import os
import shutil
import subprocess

# 找到体积最大的文件
def find_largest_file(directory):
    largest_file = None
    largest_size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size > largest_size:
                largest_size = file_size
                largest_file = file_path
    return largest_file

# 移动文件
def move_file(file_path, target_directory):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    shutil.move(file_path, target_directory)
    print(f"已将 '{file_path}' 移动到 '{target_directory}'")

# 使用 7-Zip 进行解压
def extract_7z(archive_paths, extract_to, passwords):
    seven_zip_path = r'D:\Star Rail\7z.exe'  # 指定 7z.exe 的完整路径
    for archive_path in archive_paths:
        for password in passwords:
            command = [seven_zip_path, 'x', archive_path, f'-o{extract_to}', f'-p{password}']
            try:
                result = subprocess.run(command, check=True, capture_output=True, text=True)
                print(result.stdout)
                if "Everything is Ok" in result.stdout:
                    print(f"Extraction completed successfully with password: {password}")
                    return  # 解压成功后，退出
            except subprocess.CalledProcessError as e:
                print(f"Failed with password: {password}")
        print(f"Failed to extract {archive_path} with provided passwords.")

