# 页面方法封装
import os, sys, yaml


class read_write_data:

    def __init__(self, file_name):
        self.file_path = os.getcwd() + os.sep + 'Data' + os.sep + file_name

    def read_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return yaml.load(f)

    def write_file(self, data):
        with open(self.file_path, 'w') as f:
            return yaml.dump(data, f, encoding='utf-8', allow_unicode=True)
