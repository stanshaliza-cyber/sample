"""
E-commerce Analytics Dashboard
Main landing page for the Streamlit multi-page application.
"""

import streamlit as st
import sys
sys.path.append('src')

from data_loader import EcommerceDataLoader
from analytics import EcommerceAnalytics
from visualizations import EcommerceVisualizations

# Page config
st.set_page_config(
    page_title="E-commerce Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS (optimized for dark theme)
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #58a6ff;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        text-align: center;
        color: #c9d1d9;
        margin-bottom: 2rem;
    }
    .feature-box {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: rgba(110, 118, 129, 0.2);
        border: 1px solid rgba(110, 118, 129, 0.3);
        margin: 1rem 0;
    }
    .metric-card {
        background-color: rgba(110, 118, 129, 0.15);
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        border: 1px solid rgba(110, 118, 129, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for data loading
@st.cache_resource
def load_data():
    """Load and cache data."""
    loader = EcommerceDataLoader(data_dir="data")
    loader.load_all()
    analytics = EcommerceAnalytics(loader)
    viz = EcommerceVisualizations(analytics)
    return loader, analytics, viz

# Main content
def main():
    # Header
    st.markdown('<div class="main-header">📊 E-commerce Analytics Dashboard</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="sub-header">TechGadgets CZ - Data Analysis & Visualization Portfolio</div>',
                unsafe_allow_html=True)

    # Important notice about fictional data
    st.info("""
⚠️ **Portfolio Project Notice**: This dashboard uses **completely fictional data** from a
non-existent company "TechGadgets CZ". All customer names (Jan Novák, Marie Svobodová, etc.),
order transactions, product information, and business metrics are synthetically generated for
demonstration purposes only. This is a portfolio project showcasing data analysis and
visualization capabilities.
""")

    # Load data
    with st.spinner('Loading data...'):
        loader, analytics, viz = load_data()

    # Quick stats
    st.markdown("---")
    st.subheader("📈 Quick Overview")

    metrics = analytics.get_basic_metrics()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="💰 Total Revenue",
            value=f"{metrics['total_revenue']:,.0f} CZK",
            delta=f"{metrics['delivery_rate']:.1f}% delivered"
        )

    with col2:
        st.metric(
            label="📦 Total Orders",
            value=f"{metrics['total_orders']:,}",
            delta=f"Avg: {metrics['avg_order_value']:,.0f} CZK"
        )

    with col3:
        st.metric(
            label="👥 Customers",
            value=f"{metrics['total_customers']}",
            delta=f"{metrics['vip_customers']} VIP ({metrics['vip_rate']:.0f}%)"
        )

    with col4:
        st.metric(
            label="🛍️ Products",
            value=f"{metrics['total_products']}",
            delta=f"{metrics['total_categories']} categories"
        )

    # Features section
    st.markdown("---")
    st.subheader("🎯 Dashboard Features")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="feature-box">
        <h3>📊 Overview</h3>
        <ul>
            <li>Key performance indicators (KPIs)</li>
            <li>Revenue trends over time</li>
            <li>Category performance</li>
            <li>Seasonality analysis</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-box">
        <h3>📈 Products</h3>
        <ul>
            <li>Top selling products</li>
            <li>Product performance metrics</li>
            <li>Price vs rating analysis</li>
            <li>Category comparison</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-box">
        <h3>👥 Customers</h3>
        <ul>
            <li>Customer segmentation</li>
            <li>RFM analysis (Recency, Frequency, Monetary)</li>
            <li>Customer lifetime value</li>
            <li>Spending patterns</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-box">
        <h3>🔍 Analysis</h3>
        <ul>
            <li>Advanced RFM segmentation</li>
            <li>Basket analysis (products bought together)</li>
            <li>Correlation matrices</li>
            <li>Network visualizations</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    # Navigation guide
    st.markdown("---")
    st.subheader("🚀 Get Started")

    st.info("""
    **👈 Use the sidebar to navigate** between different sections of the dashboard.

    Each page offers unique insights and interactive visualizations:
    - **Overview**: Get a high-level view of your business metrics
    - **Products**: Dive deep into product performance
    - **Customers**: Understand your customer base
    - **Analysis**: Explore advanced analytics and insights
    """)

    # About section
    st.markdown("---")
    st.subheader("ℹ️ About This Dashboard")

    with st.expander("📖 Project Information"):
        st.markdown("""
        ### E-commerce Analytics Portfolio Project

        **Dataset**: TechGadgets CZ - Fictional e-commerce store
        - 📅 Period: 2023-2024 (2 years)
        - 📦 6,725 orders
        - 👥 100 customers
        - 🛍️ 25 products across 11 categories
        - 💰 527M CZK total revenue

        **Technologies**:
        - Python 3.12.3
        - Streamlit (Web Dashboard)
        - Plotly (Interactive Visualizations)
        - Pandas (Data Analysis)
        - NetworkX (Network Graphs)

        **Special Feature**:
        This dataset represents a Czech e-commerce company with global reach -
        customer names are Czech (Jan Novák, Marie Svobodová...) while the
        tech stack is English-first, demonstrating real-world localization capabilities.

        **Author**: Roman Novak
        **Ubuntu**: 24.04 | **Python**: 3.12.3
        **Purpose**: Portfolio project showcasing data analysis and visualization skills
        """)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p>📊 E-commerce Analytics Dashboard | Built with Streamlit & Plotly</p>
        <p>🇨🇿 Czech localization | 🌍 Global-ready tech stack</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
