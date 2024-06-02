import pandas as pd

# 读取Excel文件
df = pd.read_excel('example.xlsx')

# 指定要提取的行和列
selected_rows = list(range(0, 301, 10))  # 从第10行到第300行
selected_columns = [7]

# 使用iloc函数提取数据
selected_data = df.iloc[selected_rows, selected_columns]

# 打印提取的数据
print(selected_data)
