import os

# 指定文件夹路径
folder_path = r"C:\Users\Winfred_Lu\Desktop\SF Symbols 5\Multicolour"

# 创建文件夹（如果不存在）
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 创建20个空的 .svg 文件
for i in range(1, 21):
    filename = f"file{i}.svg"
    file_path = os.path.join(folder_path, filename)
    with open(file_path, "w") as f:
        f.write("<svg></svg>")

print("成功创建20个空的 .svg 文件。")
