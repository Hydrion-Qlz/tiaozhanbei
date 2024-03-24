# 处理行业新闻，将其从excel形式存储为json的格式

import pandas as pd
import json

# 指定 Excel 文件路径
excel_file = './info.xlsx'

# 读取 Excel 文件中的所有 sheet
data = pd.read_excel(excel_file, sheet_name=None)

# 构建最终的 JSON 数据结构
json_data = {}  # 最外层的 JSON 对象

# 遍历每个 sheet
for sheet_name, df in data.items():
    # 获取第一行第一列的值
    value = df.iloc[0, 0]
    
    # 将第一列的所有字段都更改为该值
    df.iloc[:, 0] = value
    
    # 将 DataFrame 转换为字典列表
    sheet_data = df.to_dict('records')

    # 将当前 sheet 的数据添加到最外层的 JSON 对象中
    json_data[sheet_name] = sheet_data

# 将 JSON 数据以漂亮的格式保存到文件中
output_file = './info.json'
with open(output_file, 'w') as f:
    s = json.dumps(json_data, indent=4).encode('utf-8').decode('unicode_escape')
    print(s)
    f.write(s)