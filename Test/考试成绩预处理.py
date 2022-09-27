import os
import pandas as pd

path = '../Data/inputData/考试成绩数据/'
files = os.listdir(path)
result_df = pd.DataFrame()

# cj = pd.read_excel(path + '北京市昌平职业学校2021-2022春学期_信息技术系_大数据201-202班_互联网数据采集_期末考试成绩.xlsx')
# cj.index = cj['姓名']
# fx = pd.read_excel(path + '北京市昌平职业学校2021-2022春学期_信息技术系_大数据201-202班_大数据分析与实现_期末考试成绩.xlsx')
# fx.index = fx['姓名']
# sh = pd.read_excel(path + '北京市昌平职业学校2021-2022春学期_信息技术系_大数据201-202班_数据可视化设计与实现_期末考试成绩.xlsx')
# sh.index = sh['姓名']
# sy = pd.read_excel(path + '北京市昌平职业学校2021-2022春学期_信息技术系_大数据201-202班_职业素养_期末考试成绩_唐大成.xlsx')
# sy.index = fx['姓名']

# result_df['互联网数据采集'] = cj['总成绩']
# result_df['大数据分析与实现'] = fx['总成绩']
# result_df['数据可视化设计与实现'] = sh['总成绩']
# result_df['职业素养'] = sy['总成绩']
# result_df.to_csv('inputData/考试成绩数据/考勤成绩数据.csv', encoding='utf_8', index=True)

# 将 cj fx sh sy 转换为动态变量
loc = locals()
for file in files:
    if file.endswith('xlsx'):
