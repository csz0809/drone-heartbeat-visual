import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("无人机通信心跳监测可视化")

# 读取数据（如果文件不存在，显示提示）
try:
    df = pd.read_csv("heartbeat_data.csv")
except FileNotFoundError:
    st.warning("请先运行 heartbeat.py 生成数据文件！")
    st.stop()

# 显示数据表格
st.subheader("心跳包数据")
st.dataframe(df)

# 绘制折线图
st.subheader("心跳包序号随时间变化")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["时间"], df["序号"], marker="o", color="#1f77b4", linewidth=2)
ax.set_xlabel("时间")
ax.set_ylabel("序号")
ax.set_title("无人机心跳包时序图")
plt.xticks(rotation=45)
st.pyplot(fig)
