import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 기본 설정
st.set_page_config(page_title="Seoul Re-suspended Dust Dashboard", layout="wide")
st.title("🚧 Seoul Re-suspended Dust Analysis Dashboard")
st.markdown("---")

# ✅ 매핑 딕셔너리 정의
district_map = {
    '영등포구': 'Yeongdeungpo',
    '강남구': 'Gangnam',
    '강서구': 'Gangseo',
    '동작구': 'Dongjak',
    '마포구': 'Mapo',
    '송파구': 'Songpa'
}

policy_status_map = {
    '친환경보일러 교체 시행': 'Implemented',
    '미시행': 'Not Implemented'
}

policy_type_map = {
    '벽면녹화, 친환경보일러 교체(일부–선정결과없음)': 'Green Wall & Boiler',
    '미세먼지 차단 방진시설법, 벽녹화 경고표지': 'Dust Barrier & Warning',
    '기타, 녹지 확보, 벽면녹화, 친환경보일러, 클링포그': 'Mixed Policies',
    '차량진입제한기, 분사형 경고표지, 나대지 녹화, 미세먼지 저감숲, 미세먼지 차단 숲형커튼, 미세먼지 차단 필터기스톤, 벽면녹화':
        'Advanced Multiple'
}

# 📈 Pattern 1: Hourly average traffic
st.subheader("📈 Pattern 1: Hourly Average Traffic Volume")
pattern1 = pd.read_csv("streamlit_data/pattern1_avg_traffic_by_hour.csv", encoding="utf-8-sig")
pattern1["hour_num"] = pattern1["hour"].str.extract(r'(\d+)').astype(int)
pattern1 = pattern1.sort_values("hour_num")

fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.barplot(data=pattern1, x="hour_num", y="avg_traffic", ax=ax1)
ax1.set_title("Average Traffic Volume by Hour")
ax1.set_xlabel("Hour")
ax1.set_ylabel("Average Traffic")
st.dataframe(pattern1[["hour", "avg_traffic"]])
st.pyplot(fig1)

# 🚛 Pattern 2: Heavy traffic vs dust
st.subheader("🚛 Pattern 2: Heavy Traffic vs Dust")
pattern2 = pd.read_csv("streamlit_data/pattern2_traffic_vs_dust.csv", encoding="utf-8-sig")
pattern2['district_name'] = pattern2['district_name'].map(district_map)
st.dataframe(pattern2)

fig2, ax2 = plt.subplots(figsize=(6, 5))
sns.scatterplot(data=pattern2, x="avg_heavy_traffic", y="avg_dust", hue="district_name", s=100, ax=ax2)
ax2.set_title("Heavy Traffic vs Dust")
ax2.set_xlabel("Average Heavy Traffic")
ax2.set_ylabel("Average Dust")
st.pyplot(fig2)

# 🚦 Pattern 3: Traffic, dust, and policy types
st.subheader("🚦 Pattern 3: Traffic, Dust & Policy Type Analysis")
pattern3 = pd.read_csv("streamlit_data/pattern3_dust_traffic_policy.csv", encoding="utf-8-sig")
pattern3['district_name'] = pattern3['district_name'].map(district_map)
pattern3['policy_types'] = pattern3['policy_types'].map(policy_type_map)
st.dataframe(pattern3)

fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.scatterplot(
    data=pattern3,
    x="avg_heavy_traffic",
    y="avg_dust",
    hue="policy_types",
    style="district_name",
    s=100,
    ax=ax3
)
ax3.set_title("Heavy Traffic vs Dust (by Policy Type)")
ax3.set_xlabel("Average Heavy Traffic")
ax3.set_ylabel("Average Dust")
ax3.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig3)

# 🏗️ Pattern 5: Policy status vs dust
st.subheader("🏗️ Pattern 5: Policy Implementation vs Dust & Land Use")
pattern5 = pd.read_csv("streamlit_data/pattern5_policy_vs_dust.csv", encoding="utf-8-sig")
pattern5['district_name'] = pattern5['district_name'].map(district_map)
pattern5['policy_status'] = pattern5['policy_status'].map(policy_status_map)
st.dataframe(pattern5)

col1, col2 = st.columns(2)

with col1:
    fig4, ax4 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=pattern5, x="district_name", y="avg_dust", hue="policy_status", ax=ax4)
    ax4.set_title("Dust by Policy Status")
    ax4.set_xlabel("District")
    ax4.set_ylabel("Average Dust")
    st.pyplot(fig4)

with col2:
    fig5, ax5 = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=pattern5, x="road_area", y="avg_dust", hue="district_name", ax=ax5)
    ax5.set_title("Road Area vs Dust")
    ax5.set_xlabel("Road Area")
    ax5.set_ylabel("Average Dust")
    st.pyplot(fig5)

fig6, ax6 = plt.subplots(figsize=(8, 4))
sns.scatterplot(data=pattern5, x="garage_area", y="avg_dust", hue="district_name", ax=ax6)
ax6.set_title("Garage Area vs Dust")
ax6.set_xlabel("Garage Area")
ax6.set_ylabel("Average Dust")
st.pyplot(fig6)

# 👥 Pattern 6: Population vs dust
st.subheader("👥 Pattern 6: Population vs Dust")
pattern6 = pd.read_csv("streamlit_data/pattern6_population_vs_dust.csv", encoding="utf-8-sig")
pattern6['district_name'] = pattern6['district_name'].map(district_map)
st.dataframe(pattern6)

fig7, ax7 = plt.subplots(figsize=(6, 5))
sns.scatterplot(data=pattern6, x="population", y="avg_dust", hue="district_name", s=100, ax=ax7)
ax7.set_title("Population vs Dust")
ax7.set_xlabel("Population")
ax7.set_ylabel("Average Dust")
st.pyplot(fig7)

# Footer
st.markdown("---")
st.info("This dashboard is based on Seoul Open Data and reflects analysis as of 2024.")
