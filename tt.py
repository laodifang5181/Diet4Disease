import os

def rename_json_files(folder_path):
    # 获取文件夹中所有的 JSON 文件
    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    
    # 按文件名排序（可选）
    json_files.sort()
    
    # 遍历并重命名文件
    for index, old_name in enumerate(json_files, start=1):
        # 构造新的文件名
        new_name = f"{index}.json"
        
        # 获取完整的文件路径
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        
        # 重命名文件
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")

# 示例用法
folder_path = R"C:\Users\29920\Desktop\github\t\knowledge_base"  # 替换为你的文件夹路径
rename_json_files(folder_path)