import numpy as np

def check_safety_margin(intrinsic_value, current_price):
    """
    底层逻辑：只有当价格低于内在价值的 70% 时，才触发‘安全边际’警告
    """
    margin = (intrinsic_value - current_price) / intrinsic_value
    if margin >= 0.3:
        print(f"✅ 发现安全边际: {margin:.1%}. 这是一个格雷厄姆式的机会！")
    else:
        print(f"⚠️ 当前安全边际仅为 {margin:.1%}. 可能需要更深入的分析。")

def run_wealth_model():
    print("\n" + "="*40)
    print("      🚀 专业财富复利对比工具 (v2.0) ")
    print("="*40)

    try:
        # 1. 基础复利模拟
        principal = float(input("💰 请输入初始本金 (元): "))
        years = int(input("⏳ 请输入持有年限 (年): "))
        
        rates = np.array([0.03, 0.05, 0.10])
        labels = ["保守型 (3%)", "稳健型 (5%)", "进取型 (10%)"]

        print(f"\n📊 模拟 {years} 年后的财富图景：")
        print("-" * 40)

        final_amounts = principal * (1 + rates) ** years

        for label, total in zip(labels, final_amounts):
            profit = total - principal
            print(f"{label}: {total:,.2f} 元 | 净赚: {profit:,.2f}")

        # 2. 整合格雷厄姆底层逻辑 (新增调用)
        print("\n🛡️  格雷厄姆安全边际检测：")
        val = float(input("📉 请输入该资产的估算内在价值: "))
        price = float(input("🏷️  请输入当前市场价格: "))
        check_safety_margin(val, price) # 👈 确保调用

        print("-" * 40)
        print("💡 提示：哪怕只有 2% 的利率差，在时间作用下也会产生巨大鸿沟。")

    except ValueError:
        print("❌ 输入有误，请输入纯数字。")

if __name__ == "__main__":
    run_wealth_model()