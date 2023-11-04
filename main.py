import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit_authenticator as stauth
figure = plt.figure()

#AUTHENTICATION
usernames=['CR','Atul']
names=['General','Admin']
passwords=['PDQC@2023','Atul@2023']
hashed_passwords = stauth.Hasher(passwords).generate()
credentials={"usernames":{}}

for uname,name,pwd in zip(usernames,names,hashed_passwords):
    user_dict = {"name": name,"password": pwd}
    credentials["usernames"].update({uname: user_dict})

#st.write(credentials)
authenticator=stauth.Authenticate(credentials,'qwedfgety','BFF385726FB6ABC1EACF669BAAEDF',cookie_expiry_days=30)
named,authentication_status, username=authenticator.login("Login","main")
#st.write(authentication_status)
if authentication_status:
    authenticator.logout("logout","sidebar")
    with st.sidebar:
        selected = option_menu("Home", ["CR"], 
        icons=['house','gear'], menu_icon="cast", default_index=0)
        selected
        

    st.header("CR Parameter")  
    conn = psycopg2.connect(host="10.10.45.173",database="atul", user="postgres", password="admin")

    # Query the database to get the unique values in the 'column' column
    with conn.cursor() as cur:
        cur.execute('SELECT DISTINCT "CR TDC" FROM "anjibd"''')
        unique_values = [row[0] for row in cur.fetchall()]

    # Close the connection
    conn.close()

st.title ("data analysis app")
#sl.markdown(f"<h1>Data Visualizer</h1>")
st.markdown("...",unsafe_allow_html = True)
files = st.file_uploader("upload multiple files",type=["xlsx"],accept_multiple_files=True)
files_name = list()
if files :
    for file in files:
        files_name.append(file.name)
    selected_files =st.multiselect("select files", options = files_name) 
    if selected_files:
        option =st.radio("select Entity",options =("none") )
        if option!= "none":
            for file in files_name:
                if file in selected_files:
                    df = pd.read_excel(file)
                    sns.distplot(df["Frequency"])
                    sns.scatterplot(x=df["Frequency"],y =df["Negative strip time"],hue =df["Grade"])
                st.write(figure)  
        
                
             
