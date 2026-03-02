import numpy as np

def run_wealth_model():
    print("\n" + "="*40)
    print("      🚀 专业财富复利对比工具 (v2.0) ")
    print("="*40)

    try:
        # 获取输入
        principal = float(input("💰 请输入初始本金 (元): "))
        years = int(input("⏳ 请输入持有年限 (年): "))
        
        # 定义对比利率：3%(大额存单), 5%(稳健理财), 10%(进取指数)
        rates = np.array([0.03, 0.05, 0.10])
        labels = ["保守型 (3%)", "稳健型 (5%)", "进取型 (10%)"]

        print(f"\n📊 模拟 {years} 年后的财富图景：")
        print("-" * 40)

        # 核心逻辑：复利公式 A = P * (1 + r)^n
        final_amounts = principal * (1 + rates) ** years

        for label, total in zip(labels, final_amounts):
            profit = total - principal
            # :,.2f 让数字带上千分位逗号，更像银行账单
            print(f"{label}: {total:,.2f} 元 | 净赚: {profit:,.2f}")

        print("-" * 40)
        print("💡 提示：哪怕只有 2% 的利率差，在时间作用下也会产生巨大鸿沟。")

    except ValueError:
        print("❌ 输入有误，请输入纯数字。")

if __name__ == "__main__":
    run_wealth_model()