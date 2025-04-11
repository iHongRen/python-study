# 批量给代码文件加上头注释

# 之前的代码忘记加头注释，现在需要批量给代码文件加上头注释

import os
import time

# 定义头注释
header = """/**
 * @filename : {filename}
 * @author : {author}
 * @date : {date}
 * @description : 文件描述
 */
 
"""


def add_header_to_file(dir_path, file_exts=[".ets"], author="@cxy", header=header):
    # 遍历目录下的所有文件
    for root, dirs, files in os.walk(dir_path):
        # 遍历所有文件
        for file in files:
            # 判断文件是否为指定类型的文件
            if file.endswith(tuple(file_exts)):
                filePath = os.path.join(root, file)
                # 读取文件内容
                with open(filePath, "r", encoding="utf-8") as f:
                    content = f.read()

                # 获取文件创建时间
                date = time.strftime(
                    "%Y/%m/%d", time.localtime(os.path.getctime(filePath))
                )

                # 获取原文件的创建时间和修改时间
                ctime, mtime = os.path.getctime(filePath), os.path.getmtime(filePath)

                # 替换头注释中的占位符
                new_content = (
                    header.format(filename=file, author=author, date=date) + content
                )

                # 将新内容写入文件
                with open(filePath, "w", encoding="utf-8") as f:
                    f.write(new_content)

                os.utime(filePath, (ctime, mtime))  # 还原文件时间

                print(f"已为文件 {filePath} 添加头注释")


if __name__ == "__main__":
    dir_path = "/Users/cxy/Desktop/xxx"
    add_header_to_file(dir_path, file_exts=[".ets", ".ts"], author="@cxy")
