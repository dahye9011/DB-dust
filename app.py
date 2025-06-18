import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Seoul Dust Dashboard", layout="wide")
st.title("🚧 Seoul Re-suspended Dust Analysis Dashboard")
st.markdown("---")

# Pattern 1: Hourly Traffic
st.subheader("📈 Pattern 1: Average Traffic by Hour")
pattern1 = pd.read_csv("streamlit_data/pattern1_avg_traffic_by_hour.csv")
pattern1["hour_num"] = pattern1["hour"].str.extract(r'(\d+)').astype(int)
pattern1 = pattern1.sort_values("hour_num")

fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.barplot(data=pattern1, x="hour_num", y="avg_traffic", ax=ax1)
ax1.set_title("Average Traffic by Hour")
ax1.set_xlabel("Hour")
ax1.set_ylabel("Average Traffic")
ax1.tick_params(axis='x', rotation=0)

st.dataframe(pattern1[["hour", "avg_traffic"]])
st.pyplot(fig1)

# Pattern 2: Traffic vs Dust
st.subheader("🚛 Pattern 2: Heavy Traffic vs Dust Concentration")
pattern2 = pd.read_csv("streamlit_data/pattern2_traffic_vs_dust.csv")
st.dataframe(pattern2)

fig2, ax2 = plt.subplots(figsize=(6, 5))
sns.scatterplot(data=pattern2, x="avg_heavy_traffic", y="avg_dust", hue="district_name", s=100, ax=ax2)
ax2.set_title("Heavy Traffic vs Dust")
st.pyplot(fig2)

# Pattern 3: Traffic, Dust, and Policy Types
st.subheader("🚦 Pattern 3: Traffic, Dust, and Policy Types")
pattern3 = pd.read_csv("streamlit_data/pattern3_dust_traffic_policy.csv")
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
ax3.set_title("Traffic vs Dust by Policy Type")
ax3.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig3)

# Pattern 5: Policy Status and Land Use
st.subheader("🏗️ Pattern 5: Policy Status, Dust, and Land Use")
pattern5 = pd.read_csv("streamlit_data/pattern5_policy_vs_dust.csv")
st.dataframe(pattern5)

col1, col2 = st.columns(2)

with col1:
    fig4, ax4 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=pattern5, x="district_name", y="avg_dust", hue="policy_status", ax=ax4)
    ax4.set_title("Dust by Policy Status")
    st.pyplot(fig4)

with col2:
    fig5, ax5 = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=pattern5, x="road_area", y="avg_dust", hue="district_name", ax=ax5)
    ax5.set_title("Road Area vs Dust")
    st.pyplot(fig5)

fig6, ax6 = plt.subplots(figsize=(8, 4))
sns.scatterplot(data=pattern5, x="garage_area", y="avg_dust", hue="district_name", ax=ax6)
ax6.set_title("Garage Area vs Dust")
st.pyplot(fig6)

# Pattern 6: Population vs Dust
st.subheader("👥 Pattern 6: Population vs Dust")
pattern6 = pd.read_csv("streamlit_data/pattern6_population_vs_dust.csv")
st.dataframe(pattern6)

fig7, ax7 = plt.subplots(figsize=(6, 5))
sns.scatterplot(data=pattern6, x="population", y="avg_dust", hue="district_name", s=100, ax=ax7)
ax7.set_title("Population vs Dust")
st.pyplot(fig7)

st.markdown("---")
st.info("This analysis is based on public data from the Seoul Metropolitan Government (2024).")
