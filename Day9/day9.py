data_path = './day9_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

grid = file_content.split('\n')

# Plan
# 1 - 