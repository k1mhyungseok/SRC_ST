import streamlit as st
import numpy as np
import pandas as pd
import time

#st.title("My first app")

# ### progress bar
# mp = st.progress(0)
# for i in range(100):
#     time.sleep(0.1)
#     mp.progress(i+1)

# with st.spinner("wait for it.."):
#     time.sleep(5)
# st.success("Done")
# # st.balloons()
# # st.snow()

# st.error("This is an error")
# st.warning("This is a warning")
# st.success("This si a success message")
# e = RuntimeError("This is an exception of type RuntimeError")
# st.exception(e)

# form = st.form("my_form")
# sl = form.slider("inside the form")
# rd = form.radio("radio",("1","2","3"))
# cb = form.checkbox("checkbox")
# form.form_submit_button("Submit")

# st.write("slider", sl, "radio", rd, "checkbox", cb)

# with st.form("my_form2"):
#     sl = st.slider("inside the form")
#     rd = st.radio("radio",("1","2","3"))
# #     cb = st.checkbox("checkbox")
# #     ms = st.multiselect('Buy', ["milk", "apples", "potatoes"])
# #     st.form_submit_button("Submit")

# # st.write("slider", sl, "radio", rd, "multiselect", ms, "checkbox", cb)


# st.set_page_config(
#     page_title = "Cool App",
#     page_icon = "😶‍🌫️",
#     layout = "wide",
#     initial_sidebar_state = "collapsed",
#     menu_items = {
#         "Get Help" : "https://www.google.com",
#         "Report a bug" : "https://www.naver.com",
#         "About" : "데이터 분석 과정"
#     }
#     )

# st.title("My first app")
# st.sidebar.title("sidebar")
# st.sidebar.write("This is a sidebar")

# def getname():
#     return "John"

# gr = "안녕하세요"
# un = getname()

# st.write(gr, un, "님")

import graphviz

gp = graphviz.Digraph()
gp.edge("run", "intr")
gp.edge("intr", "runb1")
gp.edge("runb1", "run")
gp.edge("run", "kernel")
gp.edge("kernel", "zombie")
gp.edge("sleep", "swap")
gp.edge("swap", "runswap")

st.graphviz_chart(gp)