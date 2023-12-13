import streamlit as st
import requests
import pandas as pd
st.write("Update Book info")

data=dict()
index=None
id=st.number_input(label="Enter BookID",step=1)
if id:
    response=requests.get("https://library-manager.azurewebsites.net/api/books")
    data=response.json()
    books=data.get('books')
    df=pd.DataFrame(books,columns=["bookID","title","authors","isbn13","language_code","num_pages","publication_date","publisher"])
    data=df[df['bookID']==id]
    try:
        index=data.index.tolist()[0]
    except:
        pass
    data=data.to_dict()

title=st.text_input(label="Title ",value=(data.get("title")[index] if index!=None else None))
authors=st.text_input(label="Authors ",value=(data.get("authors")[index] if index!=None else None))
isbn13=st.number_input(label="isbn13 ",format="%d",step=1,min_value=0,value=(data.get("isbn13")[index] if index!=None else None))
language_code=st.text_input(label="Language Code ",value=(data.get("language_code")[index] if index!=None else None))
num_pages=st.number_input(label="Number of Pages ",format="%d",step=1 ,value=(data.get('num_pages')[index] if index!=None else None))
publication_date=st.text_input(label="Publication Date",value=(data.get("publication_date")[index] if index!=None else None))
publisher=st.text_input("Publisher ",value=(data.get("publisher")[index] if index!=None else None))

def update_book(id,title,authors,isbn13,language_code,num_pages,publication_date,publisher):
    data={"title":title, "authors":authors,"isbn13":isbn13,"language_code":language_code,"num_pages":num_pages,"publication_date":publication_date,"publisher":publisher}
    headers = {"Content-Type": "application/json"}
    response=requests.post(f"https://library-manager.azurewebsites.net/api/books/{id}/",json=data,headers=headers)
    st.write(response.json())

if st.button("Update Book"):
    update_book(id,title, authors, isbn13, language_code, num_pages, publication_date, publisher)
