import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px


def show_dashboard():
    st.title("📊 SAP KPI Dashboard")
    conn = sqlite3.connect("data/sap_transactions.db")

    df = pd.read_sql("SELECT * FROM purchase_orders", conn)
    st.subheader("Purchase Orders")
    st.dataframe(df)

    fig = px.bar(
        df, x="vendor_id", y="amount",
        color="status",
        title="Vendor-wise PO Amount")
    st.plotly_chart(fig)
