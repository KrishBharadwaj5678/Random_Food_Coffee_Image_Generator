#  http://numbersapi.com/?ref=public_apis#28 

import streamlit as st
import requests 
import time

t1,t2=st.tabs(["Random Food Image","Random Coffee Image"])

with t1:
    data=requests.get("https://foodish-api.com/api/")
    image=data.json()["image"]
    list=image.split("/")
    st.markdown("# :orange[Random Food Image Generator]")
    generate=st.button(":green[Generate Food Image]")
    if generate:
        st.image(image,use_column_width=None)
        time.sleep(1)
        st.toast(f"{list[4].upper()} 😋")

with t2:
    st.markdown("# :blue[Random Coffee Image Generator]")
    generate2=st.button(":orange[Generate Coffee Image]")
    if generate2:
        data2=requests.get("https://coffee.alexflipnote.dev/random")
        bin_data=data2.content
        with open("coffee.jpg","wb") as coffee:
            coffee.write(bin_data)
            st.image("coffee.jpg",use_column_width=None)

 



        
