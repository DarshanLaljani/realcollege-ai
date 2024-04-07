import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate

def app():
        
    # Sidebar input for website URL
    web_url = st.sidebar.text_input("Website URL")
    if web_url == "":
        st.warning("Add URL in Sidebar.")
        return
    
    # Instantiate ChatGoogleGenerativeAI
    llm = ChatGoogleGenerativeAI(model="gemini-pro")

    # Instantiate WebBaseLoader and load article
    loader = WebBaseLoader(web_url)
    docs = loader.load()

    # Define the summarization template
    template = """
        You are a helpful assistant. Please ask your question and wait for the answer.
        context:{context}
        input:{input}
        answer:
        """
    prompt = PromptTemplate.from_template(template)

    # Instantiate LLMChain
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    # Instantiate StuffDocumentsChain
    stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="context")

    # Ask for questions
    user_query = st.text_input("Ask Your Question...")
    is_process=st.button("Process")
    if is_process:
        
        # Invoke the chain only if a question is asked
        if user_query.strip() != "":
            # Invoke the chain
            response = stuff_chain.invoke({"input_documents": docs, "input": user_query})

            # Display the output text
            if "output_text" in response:
                st.write(response["output_text"])
                secret3 = st.popover("Secret 3")
                secret3.success("You are Amazing! ")
            else:
                st.write("No answer found in the response.")
    else:
        st.warning("Click Process to get Answers")
if __name__ == "__main__":
    app()
