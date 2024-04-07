import streamlit as st
from home import app as home_app
from contact_us import app as contact_us_app
# from Study import app as study_app
from streamlit_option_menu import option_menu
from signin import app as signin_app
# from website import app as website_app
def main():
    st.set_page_config("realcollege.ai")
    

    page=option_menu(
            menu_title=None,
            options=["Home" , "Explore" , "Contact"] ,
            icons=["house","book","envelope"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={
                 "container":{"margin":"0"},
                 "nav-link": {"font-size": "20px", "text-align": "center", "margin":"0px"},
                "nav-link-selected": {"background-color": "green"}, 
            }
        )
    if page == "Home":
        home_app()
    elif page == "Explore":
        signin_app()   
    elif page == "Contact":
        contact_us_app()

if __name__ == "__main__":
    main()
