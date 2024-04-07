import streamlit as st

# from login import app as login_app

def app():
    # Center align the main text
    st.markdown("<h1 style='text-align: center; font-size: 7vw'>Welcome to RealCollege.ai</h1>", unsafe_allow_html=True)
    
    # Tagline
    st.markdown("<h3 style='text-align: center; font-style: italic;'>RealCollege.ai is your gateway to a smarter, more efficient way of learning. We're here to empower your educational journey with innovative tools and resources tailored to your needs.</h3>", unsafe_allow_html=True)

    # First section
    st.write("")
    st.write("")
    
    st.markdown("<h2 style='text-align: center;'>Chat with PDFs</h2>", unsafe_allow_html=True)
    st.image("photo-1.jpeg" , use_column_width=True )
    st.markdown("<h3 style='text-align: center;'>Easily interact with PDF documents like never before. Highlight important sections, add notes, and collaborate with others seamlessly.</h3>", unsafe_allow_html=True)

    # Second section
    st.write("")
    st.write("")
    st.markdown("<h2 style='text-align: center;'>Chat with Blogs and Websites </h2>", unsafe_allow_html=True)
    st.image("photo-4.jpeg", use_column_width=True)
    st.markdown("<h3 style='text-align: center;'>Explore a world of knowledge through interactive conversations with blogs and websites. Engage with diverse content effortlessly.</h3>", unsafe_allow_html=True)

    # Third section
    st.write("")
    st.write("")
    st.markdown("<h2 style='text-align: center;'>Flashcards for Better Retention</h2>", unsafe_allow_html=True)
    st.image("photo-3.jpeg", use_column_width=True)
    st.markdown("<h3 style='text-align: center;'>Enhance your learning with digital flashcards. Create, study, and revise key concepts with ease.</h3>", unsafe_allow_html=True)

    # Fourth section
    st.write("")
    st.write("")
    st.markdown("<h2 style='text-align: center;'>Personalized Recommendations</h2>", unsafe_allow_html=True)
    st.image("photo-2.jpeg", use_column_width=True)
    st.markdown("<h3 style='text-align: center;'>Get personalized video recommendations based on your learning preferences. Discover new content that matches your interests and goals.</h3>", unsafe_allow_html=True)
    secret2 = st.popover("Secret 2")
    secret2.success("Gangadhar hi Shaktimaan He! ")
if __name__ == "__main__":
    app()
