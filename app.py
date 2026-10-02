import streamlit as st
import plotly.express as px
import time
from mock_data import get_supply_chain_data

st.set_page_config(page_title="EcoBiz Scope 3", layout="wide")

st.title("🌱 EcoBiz Scope 3 AI Intelligence")
st.caption("Automated Scope 3 Emissions & GNN Supply-Chain Risk Profiler")

nodes, edges = get_supply_chain_data()

# Metric cards
c1, c2, c3 = st.columns(3)
c1.metric("Total Tracked Emissions", f"{nodes['emissions'].sum():,} tCO2e", delta="-4.2%")
c2.metric("Tier-1 Suppliers", len(nodes[nodes['tier'] == 1]))
c3.metric("High-Risk Hotspots", "2 Entities", delta="Critical", delta_color="inverse")

st.divider()

# Interactive File Upload Demo
st.subheader("1. Ingest Invoices & Certifications")
uploaded_file = st.file_uploader("Upload Supplier Audit Document (PDF/CSV)", type=["pdf", "csv", "xlsx"])

if uploaded_file is not None:
    with st.spinner("AI parsing document & recalculating supply-chain graph..."):
        time.sleep(2)
    st.success(f"Successfully processed `{uploaded_file.name}`. Scope 3 values updated!")

# Visualization
st.subheader("2. Emissions by Supplier & Tier")
fig = px.bar(
    nodes,
    x="label",
    y="emissions",
    color="tier",
    labels={"label": "Supplier / Facility", "emissions": "Emissions (tCO2e)", "tier": "Supply Tier"},
    title="Supply Chain Carbon Footprint",
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("3. Raw Supplier Intelligence")
st.dataframe(nodes[["label", "tier", "country", "emissions"]], use_container_width=True)
