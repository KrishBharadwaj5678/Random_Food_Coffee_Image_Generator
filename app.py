import streamlit as st
import requests 
import time

# Defining Page Title,Icon
st.set_page_config(
    page_title="Random Food | Coffee Image Generator",
    page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSI46Lf5WnsInIevmoAxkiKucq4lgTHVHKk7A&s",
    menu_items={
        "About":"From spicy curries to decadent desserts, every picture is a culinary adventure. From beans to brews, our random coffee image generator serves up a fresh cup of visual delight with every click."
    }
)

t1,t2=st.tabs(["Random Food Image","Random Coffee Image"])

with t1:
    st.write("<h4>Explore new flavors, discover exotic ingredients, and indulge in the visual delight of food from every corner of the world.</h4>",unsafe_allow_html=True)
    generate=st.button(":green[Generate Food Image]")
    if generate:
        try:
            data=requests.get("https://foodish-api.com/api/")
            image=data.json()["image"]
            list=image.split("/")
            st.image(image,use_column_width=None)
            time.sleep(1)
            st.toast(f"{list[4].upper()} 😋")
        except:
            st.toast("Network Error",icon="🔌")

with t2:
    st.write("<h4>Indulge in the rich flavors and aromas of the world's best coffee, one image at a time.</h4>",unsafe_allow_html=True)
    generate2=st.button(":orange[Generate Coffee Image]")
    if generate2:
        try:
            data2=requests.get("https://coffee.alexflipnote.dev/random")
            bin_data=data2.content
            with open("coffee.jpg","wb") as coffee:
                coffee.write(bin_data)
                st.image("coffee.jpg",use_column_width=None)
        except:
            st.toast("Network Error",icon="🔌")
