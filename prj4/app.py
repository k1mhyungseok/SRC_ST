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

#col1, col2 = st.columns([2,1])
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

######## tab #########
# t1, t2, t3 = st.tabs(["cat","dog","owl"])

# with t1 :
#     st.header("A cat")
#     st.image("cat.jpg", width = 400)

# with t2 :
#     st.header("A dog")
#     st.image("dog.jpg", width = 400)

# with t3 :
#     st.header("A owl")
#     st.image("owl.jpg", width = 400)


########### container ###########
# ct1 = st.container()
# ct2 = st.container()

# ct1.title("cat!!!")
# ct2.title("dog!!!")

# ct1.image("cat.jpg", width = 400)
# ct2.image("dog.jpg", width = 400)

cn = st.container()
cn.text("hello world1")
cn.text("hello world2")
cn.text("hello world3")
cn.text("hello world4")


import time
emp = st.empty()
emp.text("hello world1")
time.sleep(2)
emp.text("hello world2")
time.sleep(2)
emp.text("hello world3")
time.sleep(2)
emp.text("hello world4")
