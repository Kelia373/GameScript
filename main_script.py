import os
from file_utils import find_largest_file, move_file, extract_7z

# 配置输入信息
source_directories = [
    r'G:\Game\Steam\steamapps\workshop\content\431960\3318024587'
]  # 替换为实际的源路径列表
target_directories = [r'F:\Game\Game_5']  # 替换为实际的目标路径列表
passwords = ['FS', 'W', 'YS', '33157']  # 替换为实际的密码列表
move_only = True # 设置为 True 以仅移动文件
extract_only = True  # 设置为 True 以仅解压文件

# 确保目录存在
def ensure_directories(directories):
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")

# 主逻辑
def main(source_directories, target_directories, passwords, move_only=False, extract_only=False):
    if move_only or (not extract_only and not move_only):
        ensure_directories(target_directories)  # 确保目标目录存在
        for source_directory in source_directories:
            largest_file = find_largest_file(source_directory)
            if largest_file:
                move_file(largest_file, target_directories[0])  # 假设只使用一个目标目录
            else:
                print(f"No files found in the directory: {source_directory}")

    if extract_only or (not move_only and not extract_only):
        ensure_directories(target_directories)  # 确保目标目录存在
        for target_directory in target_directories:
            for file in os.listdir(target_directory):
                if file.endswith('.7z') or file.endswith('.7z.001') or file.endswith('.rar'):
                    archive_path = os.path.join(target_directory, file)
                    extract_7z([archive_path], target_directory, passwords)
                    break
            else:
                print("No .7z or .rar files found in the target directories.")

if __name__ == "__main__":
    main(source_directories, target_directories, passwords, move_only, extract_only)
