import pandas as pd
import random

stu = [
    '崔昊元',
    '贾靖程',
    '吴俊岳',
    '王浩羽',
    '吕梦丽',
    '李博远',
    '牛皓冬',
    '张阔',
    '孙佳奇',
    '郑佳睦',
    '王孝天',
    '付一鸣',
    '李蓉轩',
    '陈观绅',
    '赵鑫博',
    '张子豪',
    '叶平'
]


# 欢迎来到随机点名小程序。请按任意键开始！输入T测试概率，输入Y开始点名

def main():
    print('欢迎来到随机点名小程序。请按任意键开始！')
    print('输入T测试概率，输入Y开始点名')
    while True:
        a = input('请输入：')
        if a == 'T' or 't':
            df = pd.DataFrame(stu)
            df['count'] = 0

            print('测试概率')
            print('输入数字N，测试N次随机点名的概率')
            while True:
                num = input('请输入：')
                if num.isdigit():
                    num = int(num)
                    break
                else:
                    print('输入错误，请重新输入！')
            for i in range(num):
                name = random.choice(stu)
                df.loc[df[0] == name, 'count'] += 1
            df['probability'] = df['count'] / num
            print(df)
            print('测试完毕！')
        elif a == 'Y' or 'y':
            while True:
                print(random.choice(stu))
                if input("q结束，其他键回车继续") == "q":
                    break


if __name__ == '__main__':
    main()
