import re
import pandas as pd

name = '北京市昌平职业学校2021-2022春学期_信息技术系_大数据201-202班_互联网数据采集_期末考试成绩.xlsx'

# 使用正则表达式匹配'北京市昌平职业学校2021-2022春学期_信息技术系_大数据201-202班_互联网数据采集_期末考试成绩.xlsx'中的 '互联网数据采集_期末考试成绩'
# 用于后面的文件重命名
# re.findall(r'_(.*?)_', name)
# ['互联网数据采集', '期末考试成绩']
# re.findall(r'_(.*?)_', name)[0]
# '互联网数据采集'
# re.findall(r'_(.*?)_', name)[1]
# '期末考试成绩'
# re.findall(r'_(.*?)_', name)[0] + re.findall(r'_(.*?)_', name)[1]

# 创建dataframe并将索引修改成‘naem’
df = pd.read_excel(name)
df.index = df['name']


