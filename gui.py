import streamlit as st
import requests
import json

# 1. Configuration
API_URL = "http://127.0.0.1:8000/generate-blueprint"
st.set_page_config(page_title="OutSystems Architect AI", layout="wide")

# 2. Header
st.title("🚀 OutSystems AI Architect")
st.markdown("Describe your app idea below, and I'll generate the Data Model Blueprint + SQL.")

# 3. Input Section
with st.form("blueprint_form"):
    description = st.text_area(
        "Application Description", 
        height=150, 
        placeholder="e.g. A library management system where Users can borrow Books. Books have Authors and Genres."
    )
    submitted = st.form_submit_button("Generate Blueprint")

# 4. Logic & Display
if submitted and description:
    with st.spinner("🤖 Consulting the AI Architect..."):
        try:
            # Call our own FastAPI Backend
            response = requests.post(API_URL, json={"description": description})
            
            if response.status_code == 200:
                data = response.json()
                
                # Extract the two parts
                blueprint = data.get("Blueprint", [])
                sql_script = data.get("SQL", "-- No SQL Generated")

                # Create Tabs for cleaner UI
                tab1, tab2, tab3 = st.tabs(["🏗️ Blueprint Visualizer", "💾 SQL Script", "📄 Raw JSON"])

                # TAB 1: Visual Entities
                with tab1:
                    if isinstance(blueprint, list):
                        col1, col2 = st.columns(2)
                        for i, entity in enumerate(blueprint):
                            # Alternating columns for masonry-like effect
                            target_col = col1 if i % 2 == 0 else col2
                            with target_col:
                                with st.expander(f"🔹 {entity.get('Name')}", expanded=True):
                                    st.caption(entity.get('Description'))
                                    st.dataframe(entity.get('Attributes'), hide_index=True)
                    else:
                        st.warning("Blueprint format unexpected.")

                # TAB 2: SQL Code
                with tab2:
                    st.markdown("### T-SQL Create Script")
                    st.code(sql_script, language="sql")

                # TAB 3: Raw JSON
                with tab3:
                    st.json(data)

            else:
                st.error(f"Error {response.status_code}: {response.text}")

        except Exception as e:
            st.error(f"Connection Failed. Is the backend running? \n\nError: {e}")