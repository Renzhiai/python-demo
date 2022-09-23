# -*- coding:utf-8 -*-
import os


# 给文件名字最后加上new
def rename_files(dir_path):
    for file in os.listdir(dir_path):
        # 得到所有的文件名字
        files = os.path.splitext(file)
        # 修改所有名字
        new_filename = files[0] + '_new'
        new_file = new_filename + files[1]
        os.rename(
            # 连接dir和file
            os.path.join(dir_path, file),
            os.path.join(dir_path, new_file)
        )


if __name__ == "__main__":
    rename_files('C:\\test')
