import numpy as np

# 使用 input() 函数获取用户输入，并用 float() 转换成数字
user_input = input("请输入您的初始本金金额: ")
principal = float(user_input)

print(f"--- 财富模型环境已就绪 ---")
print(f"您输入的本金为: {principal:,.2f} 元") 

# 模拟一个简单的年化 5% 收益计算
wealth_next_year = principal * 1.05
print(f"按 5% 年化计算，一年后预计为: {wealth_next_year:,.2f} 元")