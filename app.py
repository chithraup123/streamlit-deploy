import streamlit as st
import pandas as pd

st.title("Crop Production Analysis")
file = st.file_uploader("Upload your dataset in csv")
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df)
    total_production = df['Production_Tonnes'].sum()
    #st.write(f"Total Crop Production: {total_production} Tonnes")
    st.metric(label="Total Production", value=f"{total_production} Tonnes")
    top_country = df.loc[df['Production_Tonnes'].idxmax()]['Country']
    st.bar_chart(df.set_index('Country')['Production_Tonnes'])
    st.write(f"Top Producing Country: {top_country}")
