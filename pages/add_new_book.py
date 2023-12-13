
import streamlit as st
import requests
import json
st.write("Add a new book")
# ["bookID","title","authors","isbn13","language_code","num_pages","publication_date","publisher"]
title=st.text_input(label="Title *")
authors=st.text_input(label="Authors *")
isbn13=st.number_input(label="isbn13 *",format="%d",step=1,min_value=0)
language_code=st.text_input(label="Language Code *")
num_pages=st.number_input(label="Number of Pages *",format="%d",step=1)
publication_date=st.text_input(label="Publication Date")
publisher=st.text_input("Publisher *")

def add_new_book(title,authors,isbn13,language_code,num_pages,publication_date,publisher):
    if title and authors and isbn13 and language_code and num_pages and publication_date and publisher:
        data={"title":title, "authors":authors,"isbn13":isbn13,"language_code":language_code,"num_pages":num_pages,"publication_date":publication_date,"publisher":publisher}
        st.write(data)
        headers = {"Content-Type": "application/json"}
        response=requests.post("https://library-manager.azurewebsites.net/api/books",json=data,headers=headers)
        st.write(response.json())
    else:
        st.warning(body="All Fields are required")

if st.button("Add Book"):
    add_new_book(title, authors, isbn13, language_code, num_pages, publication_date, publisher)
    # add_new_book(title,authors,isbn13,language_code,num_pages,publication_date,publisher)

