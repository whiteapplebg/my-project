import numpy as np
import argparse
import csv
from datetime import datetime
import os  # 用于检查文件是否存在

# 1. 核心计算函数 (逻辑保持纯粹)
def calculate_compound_interest(principal, rate, years):
    return principal * (1 + rate) ** years

def check_safety_margin(intrinsic_value, current_price):
    """
    底层逻辑：只有当价格低于内在价值的 70% 时，才触发‘安全边际’警告
    """
    if intrinsic_value <= 0:
        print("❌ 错误：内在价值必须大于 0")
        return
    margin = (intrinsic_value - current_price) / intrinsic_value
    if margin >= 0.3:
        print(f"✅ 发现安全边际: {margin:.1%}. 这是一个格雷厄姆式的机会！")
    else:
        print(f"⚠️ 当前安全边际仅为 {margin:.1%}. 可能需要更深入的分析。")

def save_to_csv(data, filename="history.csv"):
    """
    将计算结果追加到 CSV 文件中
    data: 包含 [时间, 本金, 利率, 年限, 结果, 币种] 的列表
    """
    file_exists = os.path.isfile(filename)
    
    # 使用 'a' 模式（append）追加写入，newline='' 防止空行
    with open(filename, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # 1. 如果是第一次创建文件，写入表头
        if not file_exists:
            writer.writerow(["记录时间", "初始本金", "年化利率", "投资年限", "最终财富", "币种"])
        
        # 2. 写入本次计算的数据
        writer.writerow(data)

# 2. 核心 CLI 入口 (彻底移除 run_wealth_model 与所有 input 语句)
def main():
    parser = argparse.ArgumentParser(description="🚀 专业财富复利 CLI 工具")
    
    # 定义命令行参数
    parser.add_argument("--verbose", action="store_true", help="显示详细计算过程")
    parser.add_argument("--principal", type=float, required=True, help="初始本金 (元)")
    parser.add_argument("--rate", type=float, required=True, help="年化利率 (如 0.05)")
    parser.add_argument("--years", type=int, required=True, help="持有年限")
    parser.add_argument("--value", type=float, help="估算内在价值")
    parser.add_argument("--price", type=float, help="当前市场价格")
    parser.add_argument("--compare_rates", type=float, nargs="+", help="输入多个利率进行对比")
    parser.add_argument("--currency", choices=["CNY", "USD", "EUR"], default="CNY")
    
    args = parser.parse_args()
    
    # 3. 计算与输出 (直接读取 args 参数)
    final_amount = calculate_compound_interest(args.principal, args.rate, args.years)
    if args.verbose: print("正在逐年计算复利...")
    print("\n" + "="*40)
    print("      💰 财富复利计算结果 ")
    print("="*40)
    print(f"💵 初始投入: {args.principal:,.2f} 元")
    print(f"📈 预估利率: {args.rate:.1%}")
    print(f"⏳ 持有时间: {args.years} 年")
    print(f"💎 最终财富: \033[1;32m{final_amount:,.2f}\033[0m 元")

    # 4. 安全边际逻辑注入
    
    if args.value is not None and args.price is not None:
        print("-" * 40)
        print("🛡️  格雷厄姆安全边际检测：")
        check_safety_margin(args.value, args.price)
        print("="*40)
    # 在 print("="*40) 下方添加
    if args.compare_rates:
        print("\n📈 多利率对比分析：")
        for r in args.compare_rates:
            alt_amount = calculate_compound_interest(args.principal, r, args.years)
            print(f"利率 {r:.1%}: {alt_amount:,.2f} {args.currency}")
    # 准备要存入的数据包
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_data = [
        current_time, 
        args.principal, 
        f"{args.rate:.1%}", 
        args.years, 
        f"{final_amount:.2f}", 
        args.currency
    ]
    
    # 执行保存
    try:
        save_to_csv(log_data)
        print(f"✅ 计算结果已同步至 history.csv")
    except Exception as e:
        print(f"⚠️ 写入日志失败: {e}")


# 5. 唯一合法的程序入口 (必须缩进调用 main)
if __name__ == "__main__":
    main()