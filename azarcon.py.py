import streamlit as st

st.set_page_config(page_title="Christian Era website",page_icon=":tada:", layout="wide")

with st.container():
    st.subheader("Programming Logic and Design  Project")
    st.title("Welcome to Christian Era website")
    st.write("Hi, I am Christian era A. Azarcon. 19 years old a 1st computer Engineering students at Surigao Del Norte State University")

with st.container():
    st.write("---")
    left_column, rigth_column = st.columns(2)
    with left_column:
        st.subheader("More information about Me:")
        st.write("##")
        st.write(
            """
            - live at  Barangay Capayahan Tubod Surigao Del Norte
            - Birth Date: April 23, 2004  
            - Fathers Name: Joel Azarcon 
            - Mothers Name: Annalee alaan
            - 3 siblings namely; Prince Era Azarcon, Princess Ira Alaan and Joel j.r Azarcon
            
            """
        )

    st.subheader("Hobbies:")
    st.write("##")
    st.write(
        """
        - love watching Kdrama and Anime
        - Cooking
        - Photography
        - Traveling
        - Dancing
        """
    )

with st.container():
    st.subheader("This is my social media account if you want to know more about me:")
    st.write("##")
    st.write(
        """
        - Facebook: https://www.facebook.com/christian.azarcon.313455666666
        - Instagram: https://instagram.com/azarconchristianera?igshid=OGQ5ZDc2ODk2ZA==
        """
    ) 
    
with st.container():
    st.write("---")
    st.header("Get In Touch With Me")
    st.write("##")

    contact_form = """
    <from action="https://formsubmit.co/azarconchristianera@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textrarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, rigth_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with rigth_column:
        st.empty()




    