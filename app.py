import streamlit as st
from bonefate import BoneFates
from bonefate.utils import DIZHI, get_24_hour_time

def main():
    st.markdown("# 称骨算命 - 袁天罡八字称骨算命")
    st.markdown("是一个称骨算命的工具, 通过输入阳历或农历信息, 可以得到称骨命书。")
    st.markdown("参考: 袁天罡八字称骨算命")
    st.markdown("## 请输入阳历或农历信息")
    year = st.number_input("年份", min_value=1900, max_value=2100, value=2021)
    month = st.number_input("月份", min_value=1, max_value=12, value=1)
    day = st.number_input("日期", min_value=1, max_value=31, value=1)
    hour = st.selectbox("时辰", list(DIZHI.values()), format_func=lambda x: f"{x}时————({'时-'.join(map(str, get_24_hour_time(x)))}点)")
    lunar = st.checkbox("输入日期为农历")
    
    bonefate = BoneFates(year, month, day, hour, lunar)
    
    st.markdown(f"阳历: {bonefate.solar.toString()}")
    st.markdown(f"农历: {bonefate.lunar.toFullString()}")
    st.markdown(f"称骨: {bonefate.bone_weight}")
    st.markdown(f"称骨命书: {bonefate.poem}")

if __name__ == "__main__":
    main()