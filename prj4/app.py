import streamlit as st
import pandas as pd
import numpy as np

st.title("My first app")
# st.write("hello world")
# st.image("cat.jpg")

st.sidebar.title("My first app")
# st.sidebar.write("hello world")

# with st.sidebar:
#     st.write("hello world")
#     rt = st.radio("radio", ["apple", "banana", "berry"])
#     st.write(rt)
#     st.image("cat.jpg")

# col1, col2, col3 = st.columns(3)
# col1.image("cat.jpg")
# col2.image("dog.jpg")
# col3.image("owl.jpg")

col1, col2 = st.columns([2,1])
# col1.subheader("A cat")
# col2.subheader("A dog")

# col1.image("cat.jpg")
# col2.image("dog.jpg")

# with col1:
#     st.subheader("A cat")
#     st.image("cat.jpg")

# with col2:
#     st.subheader("A dog")
#     st.image("dog.jpg")


