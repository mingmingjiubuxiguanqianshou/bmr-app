import streamlit as st

st.set_page_config(page_title="智能BMR与TDEE计算器", page_icon="🔥")

st.title("🔥 智能BMR与TDEE计算器") 

with st.sidebar:
    st.header("📝 填写你的数据") 
    gender = st.radio("请选择性别：", ["男", "女"]) 
    weight = st.number_input("体重：", min_value=0.0, value=70.0) 
    height = st.number_input("身高：", min_value=0.0, value=175.0) 
    age = st.number_input("年龄：", min_value=0.0, value=25.0) 
    activity_level = st.selectbox("运动量：", 
        [1, 2, 3, 4, 5], 
        format_func=lambda x: ["1=几乎不动", "2=轻度", "3=中度", "4=高强度", "5=专业"][x-1]) 

def calculate_bmr(gender, weight, height, age): 
    if gender == "男": 
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5 
    else: 
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161 
    return bmr 

def calculate_tdee(bmr, level): 
    multipliers = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9} 
    return bmr * multipliers[level] 

bmr_result = calculate_bmr(gender, weight, height, age) 
tdee_result = calculate_tdee(bmr_result, activity_level) 

st.subheader("📊 你的身体数据报告：") 
col1, col2 = st.columns(2) 
col1.metric("基础代谢 (BMR)", f"{bmr_result:.0f} 千卡/天") 
col2.metric("每日总耗 (TDEE)", f"{tdee_result:.0f} 千卡/天") 

st.divider() 
st.subheader("🎯 饮食行动指南：") 
st.success(f"🏃‍♂️ 想要减脂：每天摄入约 **{tdee_result - 500:.0f}** 千卡") 
st.info(f"⚖️ 想要维持：每天摄入约 **{tdee_result:.0f}** 千卡") 
st.warning(f"💪 想要增肌：每天摄入约 **{tdee_result + 300:.0f}** 千卡") 

# ==========================================
# 👇 下面是新加的签名代码 👇
# ==========================================
st.divider() # 加一条分割线，和上面的计算结果隔开

# 使用 markdown 的 HTML 语法来调整颜色，让签名看起来低调不喧宾夺主
# 你可以把“你的名字/昵称”改成你想要的任何字！
st.markdown(
    '<p style="text-align: center; color: #9e9e9e; font-size: 14px;">'
    '✨ Made with ❤️ by <b>铭铭就</b> ✨</p>', 
    unsafe_allow_html=True
)
