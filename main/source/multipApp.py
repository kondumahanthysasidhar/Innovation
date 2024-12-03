import streamlit as st

from pdfextraction import readfile


def main():
    st.set_page_config(page_title="Extraction App", layout="wide")

    # Home Page
    if "page" not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        st.title("Welcome to the Extraction App")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("URL Extraction"):
                st.session_state.page = "url_extraction"

        with col2:
            if st.button("Document Extraction"):
                st.session_state.page = "document_extraction"

    elif st.session_state.page == "url_extraction":
        url_extraction_page()
    elif st.session_state.page == "document_extraction":
        document_extraction_page()


# URL Extraction Page
def url_extraction_page():
    st.title("URL Extraction")

    tab1, tab2, tab3 = st.tabs(["Extract Links", "Process Metadata", "Analyze Content"])

    with tab1:

        st.header("Extract Links")
        # url = st.text_input("Enter the URL")
        file = st.file_uploader("Upload a file", type="pdf")
        if st.button("Extract"):
            st.write(f"Links extracted from {file} (example result)")

    with tab2:
        st.header("Process Metadata")
        st.write("Feature coming soon!")

    with tab3:
        st.header("Analyze Content")
        st.write("Feature coming soon!")

    if st.button("Back to Home"):
        st.session_state.page = "home"


# Document Extraction Page
def document_extraction_page():
    st.title("Document Extraction")

    tab1, tab2, tab3 = st.tabs(["Upload Document", "Extract Text", "Analyze Data"])

    with tab1:
        st.header("Upload Document")
        uploaded_file = st.file_uploader("Choose a document", type=["pdf", "docx", "txt"])
        if uploaded_file is not None:
            st.success(f"Uploaded {uploaded_file.name}")
            readfile(uploaded_file)

    with tab2:
        st.header("Extract Text")
        if st.button("Extract from Document"):
            s = uploaded_file
            readfile(s)
            st.write("Text extraction feature coming soon!")

    with tab3:
        st.header("Analyze Data")
        st.write("Analysis feature coming soon!")

    if st.button("Back to Home"):
        st.session_state.page = "home"

#
if __name__ == "__main__":
    main()
