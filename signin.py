import streamlit as st
from firebase_admin import credentials, auth
from Study import app as study_app
from streamlit_option_menu import option_menu
from website import app as website_app
import firebase_admin
if not firebase_admin._apps:
    cred = credentials.Certificate('realcollege-ai-9ad92897d992.json') 
    default_app = firebase_admin.initialize_app(cred)

def app():
    
    st.session_state.setdefault('username', "")
    st.session_state.setdefault('useremail', "")
    # st.toast("Login/Sign-up from Sidebar")
    def login_user():
        try:
            
            user = auth.get_user_by_email(email)
            st.write("Login Success")
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            st.session_state.is_signed_in = True
        except:
            st.warning('Sign-up from Sidebar')
            

    def sign_out():
        st.session_state.is_signed_in = False
        st.session_state.username = ""

    st.session_state.setdefault('is_signed_in', False)

    if not st.session_state['is_signed_in']:
        choice = st.sidebar.select_slider('Login/Signup', ['Login', 'Sign Up'])
        if choice == 'Login':
            st.title("Login")
            email = st.text_input('Email ')
            password = st.text_input('Password ', type='password')
            st.button('Login', on_click=login_user)
        else:
            st.title("Sign-up")
            email = st.text_input("Email")
            password = st.text_input("Password", type='password')
            username = st.text_input("Username")
            if st.button('Create my account'):
                try: 
                    user = auth.create_user(email=email, password=password, uid=username)
                    st.success('Account created Successfully')
                    st.markdown('Please login to Continue')
                except Exception as e:
                    st.error(f"User Already Exist")

    else:
        
        st.sidebar.button('Sign out', on_click=sign_out)
        page=option_menu(
            menu_title=None,
            options=["Ask PDF" , "Ask Link"] ,
            icons=["book","link"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={
                 "container":{"margin-top":"5!important"},
                 "nav-link": {"font-size": "20px", "text-align": "center", "margin":"0px"},
                "nav-link-selected": {"background-color": "blue"},  
                 
            }
        )
        if page == "Ask PDF":
            study_app()
        elif page == "Ask Link":
            website_app()   

if __name__ == "__main__":
    app()
