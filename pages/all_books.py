import streamlit as st
import requests
import pandas as pd
st.write("all books")

def fetch_all_books():
    response=requests.get("https://library-manager.azurewebsites.net/api/books")
    data=response.json()
    books=data.get('books')
    df=pd.DataFrame(books,columns=["bookID","title","authors","isbn13","language_code","num_pages","publication_date","publisher"])
    st.dataframe(df,width=1000,height=1000)

if __name__=="__main__":
    fetch_all_books()