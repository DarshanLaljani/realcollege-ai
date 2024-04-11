import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

def get_pdf_text(pdf_docs):
    text = ""
    try:
        for pdf in pdf_docs:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text()
    except Exception as e:
        st.error(f"Error occurred while extracting text from PDF: {e}")
    return text

def get_text_chunks(text):
    try:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
        chunks = text_splitter.split_text(text)
    except Exception as e:
        st.error(f"Error occurred while splitting text into chunks: {e}")
        chunks = []
    return chunks

def get_vector_store(text_chunks):
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
        vector_store.save_local("faiss_index")
    except Exception as e:
        st.error(f"You Haven't Uploaded file")

def get_conversational_chain():
    try:
        prompt_template = """
        Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
        provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
        Context:\n {context}?\n
        Question: \n{question}\n

        Answer:
        """

        model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

        prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
        chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    except Exception as e:
        st.error(f"Error occurred while loading conversational chain: {e}")
        chain = None
    return chain

def user_input(user_question):
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        
        new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
        docs = new_db.similarity_search(user_question)

        chain = get_conversational_chain()

        response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)

        
        # Appending the question and answer to a file
        # with open("qa_history.txt", "a") as f:
        #     f.write(f"Question: {user_question}\n")
        #     f.write(f"Answer: {response['output_text']}\n\n")
            

        st.write("Reply: ", response["output_text"])
        secret1 = st.popover("Secret 1")
        secret1.success("This website was created in Just 3 Days! ")
    except Exception as e:
        st.error(f"Click On Submit and Process to Chat")


def app():
    
    try:
        pdf_docs = st.sidebar.file_uploader("Upload File", accept_multiple_files=True)
        if pdf_docs: 
            user_question = st.text_input("Ask a Question from the PDF Files")

            if user_question:
                user_input(user_question)
            
            if st.sidebar.button("Submit & Process"):
                with st.spinner("Processing..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    get_vector_store(text_chunks)
                    st.success("Done")
            st.sidebar.markdown("---")
            st.sidebar.title("Additional Options:")
            st.sidebar.write("")
        else:
            st.warning("Upload PDF at Sidebar")
        if st.sidebar.button("YouTube"):
            st.write("This feature is underdevelopment!")

        if st.sidebar.button("Flash Cards"):
            st.write("This feature is underdevelopment!")

    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    app()
