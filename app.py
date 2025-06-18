import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

# ✅ NanumGothic 폰트 설치 후 적용
import os
import urllib.request

FONT_PATH = "/tmp/NanumGothic.ttf"
FONT_URL = "https://github.com/naver/nanumfont/blob/master/TTF/NanumGothic.ttf?raw=true"

if not os.path.exists(FONT_PATH):
    urllib.request.urlretrieve(FONT_URL, FONT_PATH)

plt.rcParams['font.family'] = fm.FontProperties(fname=FONT_PATH).get_name()
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

st.set_page_config(page_title="서울시 재비산먼지 분석", layout="wide")
st.title("🚧 서울시 재비산먼지 분석 대시보드")
st.markdown("---")

# 📈 패턴 1: 시간대별 평균 교통량
st.subheader("📈 패턴 1: 시간대별 평균 교통량")
pattern1 = pd.read_csv("streamlit_data/pattern1_avg_traffic_by_hour.csv", encoding="utf-8-sig")

# ✅ 숫자만 추출해서 새로운 column 추가
pattern1["hour_num"] = pattern1["hour"].str.extract(r'(\d+)').astype(int)

# ✅ hour 순서대로 정렬 (숫자 기준)
pattern1 = pattern1.sort_values("hour_num")

# ✅ x축 라벨을 숫자로만 표시
fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.barplot(data=pattern1, x="hour_num", y="avg_traffic", ax=ax1)

ax1.set_title("시간대별 평균 교통량")
ax1.set_xlabel("시간대 (시)")
ax1.set_ylabel("평균 교통량")
ax1.tick_params(axis='x', rotation=0)

st.dataframe(pattern1[["hour", "avg_traffic"]])
st.pyplot(fig1)


# 🚛 패턴 2: 교통량 vs 재비산먼지
st.subheader("🚛 패턴 2: 중차량 교통량과 재비산먼지 관계")
pattern2 = pd.read_csv("streamlit_data/pattern2_traffic_vs_dust.csv", encoding="utf-8-sig")
st.dataframe(pattern2)

fig2, ax2 = plt.subplots(figsize=(6, 5))
sns.scatterplot(data=pattern2, x="avg_heavy_traffic", y="avg_dust", hue="district_name", s=100, ax=ax2)
ax2.set_title("교통량 vs 재비산먼지")
st.pyplot(fig2)

# 🚦 패턴 3: 교통량, 미세먼지, 정책유형 종합 분석
st.subheader("🚦 패턴 3: 교통량 · 미세먼지 · 정책유형 종합 분석")
pattern3 = pd.read_csv("streamlit_data/pattern3_dust_traffic_policy.csv", encoding="utf-8-sig")
st.dataframe(pattern3)

fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.scatterplot(
    data=pattern3,
    x="avg_heavy_traffic",
    y="avg_dust",
    hue="policy_types",           # 정책유형별 색상
    style="district_name",        # 자치구별 마커 모양
    s=100,
    ax=ax3
)
ax3.set_title("교통량 vs 재비산먼지 (정책유형별)")
ax3.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # 범례 오른쪽으로 이동
st.pyplot(fig3)

# 🏗️ 패턴 5: 정책 시행 여부 및 도로/주차장 면적
st.subheader("🏗️ 패턴 5: 정책 시행 여부와 재비산먼지 농도 및 토지 이용 특성")
pattern5 = pd.read_csv("streamlit_data/pattern5_policy_vs_dust.csv", encoding="utf-8-sig")
st.dataframe(pattern5)

col1, col2 = st.columns(2)

with col1:
    fig4, ax4 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=pattern5, x="district_name", y="avg_dust", hue="policy_status", ax=ax4)
    ax4.set_title("정책 시행 여부에 따른 재비산먼지 농도")
    st.pyplot(fig4)

with col2:
    fig5, ax5 = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=pattern5, x="road_area", y="avg_dust", hue="district_name", ax=ax5)
    ax5.set_title("도로 면적 vs 재비산먼지 농도")
    st.pyplot(fig5)

fig6, ax6 = plt.subplots(figsize=(8, 4))
sns.scatterplot(data=pattern5, x="garage_area", y="avg_dust", hue="district_name", ax=ax6)
ax6.set_title("주차장 면적 vs 재비산먼지 농도")
st.pyplot(fig6)

# 👥 패턴 6: 인구수 vs 재비산먼지
st.subheader("👥 패턴 6: 인구수와 재비산먼지 관계")
pattern6 = pd.read_csv("streamlit_data/pattern6_population_vs_dust.csv", encoding="utf-8-sig")
st.dataframe(pattern6)

fig7, ax7 = plt.subplots(figsize=(6, 5))
sns.scatterplot(data=pattern6, x="population", y="avg_dust", hue="district_name", s=100, ax=ax7)
ax7.set_title("인구수 vs 재비산먼지")
st.pyplot(fig7)

# 하단 정보
st.markdown("---")
st.info("해당 분석은 서울시 공개 데이터를 바탕으로 2024년 기준 분석되었습니다.")