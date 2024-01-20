import os
import shutil
import argparse

def rename_images(folder_path):
    # 获取文件夹下所有文件
    files = os.listdir(folder_path)


    # 逐个处理图片文件
    for old_name in files:
        # 获取文件扩展名
        _, extension = os.path.splitext(old_name)

        # 构建新的文件名
        new_name = f'{old_name}(1){extension}'

        # 构建完整的文件路径
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)

        # 重命名文件
        shutil.move(old_path, new_path)
        #print(f'Renamed: {old_name} -> {new_name}')

def main():
    # 设置命令行参数
    parser = argparse.ArgumentParser(description='Rename images in a folder.')
    parser.add_argument('folder_path', help='Path to the folder containing images.')


    # 解析命令行参数
    args = parser.parse_args()

    # 调用函数，传入文件夹路径和新的文件名前缀
    rename_images(args.folder_path)

if __name__ == "__main__":
    main()
