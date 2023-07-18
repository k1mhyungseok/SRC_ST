import streamlit as st

## select box
sb = st.selectbox("Choose", ["image","music","video"])
if sb == "image":
    st.image("puppy.jpg")
elif sb == "music":
    st.audio("Lost_Stars.flac")
else:
    st.video("music.mp4")

## checkbox
cb = st.checkbox("Show/Hide")
if cb:
    st.image("puppy.jpg")


## button
def btn_click():
    st.write("button clicked")
    st.image("puppy.jpg")

# btn = st.button("click1")
# if btn:
#     st.write("you clicked me")

btn = st.button("click me", on_click = btn_click)


## multimedia
# st.image("puppy.jpg")
# st.audio("Lost_Stars.flac")
# st.video("music.mp4")

st.title("Hello World")
st.write("This is my first streamlit app!")
st.subheader("This is a subheader")
st.markdown("## This is a markheader")