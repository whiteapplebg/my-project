import os
import platform
from datetime import datetime

def generate_report():
    # 1. 获取系统信息
    sys_info = f"操作系统: {platform.system()} | 运行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    # 2. 模拟之前的本金逻辑
    try:
        principal = float(input("请输入要存入报告的初始本金: "))
        content = f"{sys_info}\n初始本金记录: {principal:,.2f} 元\n状态: 已存档"
        
        # 3. 自动化文件操作：写出报告
        with open("wealth_report.txt", "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"✅ 报告已自动生成：{os.path.abspath('wealth_report.txt')}")
    except ValueError:
        print("❌ 输入错误，未生成报告。")

if __name__ == "__main__":
    generate_report()
