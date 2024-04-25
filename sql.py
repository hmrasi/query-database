from dotenv import load_dotenv
load_dotenv()

import os

import streamlit as st
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def generate_sql_response(userquestion, Input_Prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([Input_Prompt,userquestion])
    return response.text

def retrieve_data_from_db(db,sql):
    connection = sqlite3.connect(db) 
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    connection.close()
    for i in data:
        print(i)
    return data


Input_Prompt = """
You are an expert in converting English questions to SQL query!
The SQL database has the name student_info and has the following columns - student_name, CLASS,
SECTION \n\nFor example, \nExample 1 - How many entries of records are present?,
the SQL command will be something like this SELECT COUNT(*) FROM student_info ;
\nExample 2 Tell me all the students studying in Data Science class?,
the SQL command will be something like this SELECT * FROM student_info where CLASS="Data Science";
also the sql code should not have in beginning or end and sql word in output
"""


st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")
question=st.text_input("Input: ",key="input")
submit=st.button("Query")
# if submit is clicked
if submit:
    response=generate_sql_response(question, Input_Prompt)
    print(response)
    response=retrieve_data_from_db("database_example.db", response)
    st.subheader("The answer is")
    for row in response:
        print(row)
        st.header(row)