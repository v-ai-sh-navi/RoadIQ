import streamlit as st
from queries import *
from gis import create_map
from streamlit_folium import st_folium
from analytics import (
    ward_complaint_chart,
    complaint_status_chart,
    monthly_trend_chart
)
from priority import generate_priority

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="RoadIQ",
    page_icon="🛣️",
    layout="wide"
)
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("RoadIQ")

city = st.sidebar.selectbox(
    "Select City",
    ["Bengaluru"]
)

st.sidebar.markdown("---")
st.sidebar.info("""
**Current Coverage**

- Bengaluru

**Planned Expansion**

- Mumbai
- Pune
- Hyderabad
- Chennai
""")

# -----------------------------
# Header
# -----------------------------
st.markdown(
    "<h1 style='text-align: center;'>RoadIQ</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: gray; font-size:18px;'>GIS-Based Road Maintenance Intelligence Platform</p>",
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# Load KPI Data
# -----------------------------
roads = int(get_total_roads()["Total_Roads"].iloc[0])
potholes = int(get_total_potholes()["Total_Potholes"].iloc[0])
repairs = int(get_total_repairs()["Total_Repairs"].iloc[0])
wards = int(get_total_wards()["Total_Wards"].iloc[0])

# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🛣️ Road Network", f"{roads:,}")

with col2:
    st.metric("🕳️ Pothole Complaints", f"{potholes:,}")

with col3:
    st.metric("🔧 Repair Records", f"{repairs:,}")

with col4:
    st.metric("🏙️ Wards Covered", f"{wards}")

st.divider()

# Placeholder for future modules
# ==========================================
# Dashboard Layout
# ==========================================

left, right = st.columns([2, 1])

# ---------------- LEFT ----------------


with left:
    # ==========================================
# GIS MAP
# ==========================================

    st.header("🗺 GIS Map")

m = create_map()

st_folium(
    m,
    height=600,
    width=None,
    returned_objects=[],
    key="road_map"
)

st.divider()

# ==========================================
# ANALYTICS
# ==========================================

st.header("Analytics")

col1, col2, col3 = st.columns([1.2, 1.6, 1.2])

# -------------------------
# Complaint Status
# -------------------------

with col1:

    status_df = get_complaint_status()

    fig = complaint_status_chart(status_df)

    st.plotly_chart(
        fig,
        width="stretch"
        #use_container_width=True
    )

# -------------------------
# Monthly Trend
# -------------------------

with col2:

    trend_df = get_monthly_complaints()

    fig = monthly_trend_chart(trend_df)

    st.plotly_chart(
        fig,
        width="stretch"
    )

# -------------------------
# Top 10 Wards
# -------------------------

with col3:

    ward_df = get_top_wards()

    fig = ward_complaint_chart(ward_df)

    st.plotly_chart(
        fig,
        width="stretch"
    )

st.divider()

# ==========================================
# PRIORITY TABLE
# ==========================================

st.header("Maintenance Priority Recommendations")

priority_df = get_priority_data()

priority_df = generate_priority(priority_df)

st.dataframe(
    priority_df,
    hide_index=True,
    width="stretch"
)

st.divider()

st.caption(
    "RoadIQ • GIS-based Road Infrastructure Intelligence Platform | "
    "Built using Python, Streamlit, GeoPandas, SQLite and Plotly"
)
    





