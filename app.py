import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit config
st.set_page_config(page_title="서울시 재비산먼지 대시보드", layout="wide")
st.title("🚧 서울시 재비산먼지 분석 대시보드")
st.markdown("---")

# 📈 패턴 1: 시간대별 평균 교통량
st.subheader("📈 패턴 1: 시간대별 평균 교통량")
pattern1 = pd.read_csv("streamlit_data/pattern1_avg_traffic_by_hour.csv", encoding="utf-8-sig")
pattern1["hour_num"] = pattern1["hour"].str.extract(r'(\d+)').astype(int)
pattern1 = pattern1.sort_values("hour_num")

fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.barplot(data=pattern1, x="hour_num", y="avg_traffic", ax=ax1)
ax1.set_title("시간대별 평균 교통량")
ax1.set_xlabel("시간")
ax1.set_ylabel("평균 교통량")
st.dataframe(pattern1[["hour", "avg_traffic"]])
st.pyplot(fig1)

# 🚛 패턴 2: 대형 교통량과 재비산먼지 관계
st.subheader("🚛 패턴 2: 대형 교통량과 재비산먼지 관계")
pattern2 = pd.read_csv("streamlit_data/pattern2_traffic_vs_dust.csv", encoding="utf-8-sig")

district_map = {
    "영등포구": "Yeongdeungpo", "강남구": "Gangnam", "강서구": "Gangseo",
    "동작구": "Dongjak", "마포구": "Mapo", "송파구": "Songpa"
}
pattern2["district_name"] = pattern2["district_name"].replace(district_map)

st.dataframe(pattern2)

fig2, ax2 = plt.subplots(figsize=(6, 5))
sns.scatterplot(data=pattern2, x="avg_heavy_traffic", y="avg_dust", hue="district_name", s=100, ax=ax2)
ax2.set_title("대형 교통량 대비 재비산먼지 농도")
ax2.set_xlabel("평균 대형 교통량")
ax2.set_ylabel("평균 재비산먼지")
st.pyplot(fig2)

# 🚦 패턴 3: 교통량, 재비산먼지, 정책 유형 분석
st.subheader("🚦 패턴 3: 교통량, 재비산먼지, 정책 유형 분석")
pattern3 = pd.read_csv("streamlit_data/pattern3_dust_traffic_policy.csv", encoding="utf-8-sig")
pattern3["district_name"] = pattern3["district_name"].replace(district_map)

def categorize_policy(text):
    if "벽면녹화" in text or "보일러" in text:
        return "Green Wall & Boiler"
    elif "방진시설" in text or "경고표지" in text:
        return "Dust Barrier & Sign"
    elif "쿨링포그" in text or "녹지" in text:
        return "Etc (CoolingFog, GreenSpace)"
    elif "차량진입" in text or "저감" in text or "필터" in text:
        return "Vehicle Limit & Sprayers"
    else:
        return "Other"

pattern3["policy_types"] = pattern3["policy_types"].apply(categorize_policy)
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
ax3.set_title("정책 유형별 대형 교통량 대비 재비산먼지")
ax3.set_xlabel("평균 대형 교통량")
ax3.set_ylabel("평균 재비산먼지")
ax3.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig3)

# 🏗️ 패턴 5: 정책 시행 여부에 따른 재비산먼지 및 토지 이용
st.subheader("🏗️ 패턴 5: 정책 시행 여부에 따른 재비산먼지 및 토지 이용")
pattern5 = pd.read_csv("streamlit_data/pattern5_policy_vs_dust.csv", encoding="utf-8-sig")
pattern5["district_name"] = pattern5["district_name"].replace(district_map)

pattern5["policy_status"] = pattern5["policy_status"].replace({
    "친환경보일러 교체 시행": "Implemented",
    "미시행": "Not Implemented"
})

st.dataframe(pattern5)

col1, col2 = st.columns(2)

with col1:
    fig4, ax4 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=pattern5, x="district_name", y="avg_dust", hue="policy_status", ax=ax4)
    ax4.set_title("정책 시행 여부에 따른 재비산먼지 농도")
    ax4.set_xlabel("자치구")
    ax4.set_ylabel("평균 재비산먼지")
    ax4.legend(title="정책 시행 여부", bbox_to_anchor=(1.05, 1), loc="upper left")
    st.pyplot(fig4)

with col2:
    fig5, ax5 = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=pattern5, x="road_area", y="avg_dust", hue="district_name", ax=ax5)
    ax5.set_title("도로 면적 대비 재비산먼지")
    ax5.set_xlabel("도로 면적")
    ax5.set_ylabel("평균 재비산먼지")
    st.pyplot(fig5)

fig6, ax6 = plt.subplots(figsize=(8, 4))
sns.scatterplot(data=pattern5, x="garage_area", y="avg_dust", hue="district_name", ax=ax6)
ax6.set_title("주차장 면적 대비 재비산먼지")
ax6.set_xlabel("주차장 면적")
ax6.set_ylabel("평균 재비산먼지")
st.pyplot(fig6)

# 👥 패턴 6: 인구수와 재비산먼지 관계
st.subheader("👥 패턴 6: 인구수와 재비산먼지 관계")
pattern6 = pd.read_csv("streamlit_data/pattern6_population_vs_dust.csv", encoding="utf-8-sig")
pattern6["district_name"] = pattern6["district_name"].replace(district_map)

st.dataframe(pattern6)

fig7, ax7 = plt.subplots(figsize=(6, 5))
sns.scatterplot(data=pattern6, x="population", y="avg_dust", hue="district_name", s=100, ax=ax7)
ax7.set_title("인구수 대비 재비산먼지")
ax7.set_xlabel("인구수")
ax7.set_ylabel("평균 재비산먼지")
st.pyplot(fig7)

# Footer
st.markdown("---")
st.info("본 대시보드는 서울 열린데이터를 기반으로 2024년 데이터를 분석한 결과입니다.")
