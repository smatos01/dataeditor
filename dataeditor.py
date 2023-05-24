import pandas as pd
import streamlit as st
from datetime import date

st.set_page_config(layout="centered", page_title="Data Editor", page_icon="🧮")

st.title("✍️ Employee Resourcing Tool")
st.caption("This is a demo of the `st.experimental_data_editor`.")

st.write("")

# ---- READ DATA ----
df = pd.read_csv('employeesdummy.csv')
#st.dataframe(df)

df.Employee_Gender = df.Employee_Gender.astype("category")
df.Employee_Gender = df.Employee_Gender.cat.add_categories(("Male", "Female", "Other"))
                                                            
df.Comment = df.Comment.astype("string")

df_edited = st.experimental_data_editor(df,num_rows="dynamic",use_container_width=True)

st.download_button(
    "⬇️ Download edited file as .csv", df_edited.to_csv(index=False), date.today().strftime('%m%d%Y')+"employees.csv", use_container_width=True
)

save_changes = st.button("Save your changes to the data!",use_container_width=True)

if save_changes:
    df_edited.to_csv("employeesdummy.csv",index=False)
    st.markdown("The data has been updated.")
