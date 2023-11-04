import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff

# df = pd.read_excel("Billet Macro report sms3 september.xlsx")
# print(df)
# sns.distplot(df["Diagonal Difference ( mm)"] )
# plt.xticks(rotation=90)
# plt.show()
figure= plt.figure()
import streamlit as st
#function

def main():
    #st.set_page_config(page_title="Data Visualization App",layout="centered",initial_sidebar_state="expanded")
        st.title("Data Visualization App")
    # menu =['Home','Dataset','Document Files','About']
    # choice = st.sidebar.selectbox("Menu",menu)
    # # HOME PAGE CONTENT
    # if choice =="Home":
        files =st.file_uploader("upload Multiple File",type=["xlsx"],accept_multiple_files=True)
        files_name =[]
        if files:
            for file in files:
                files_name.append(file.name)
        selected_files = st.multiselect("You can select multiple files",options=files_name)
        if selected_files:
            for file in files_name:
                if file in selected_files:
                    df = pd.read_excel(file)
                    st.write(df)
                    parameter1=st.selectbox("chose your parameter to plot", options = list(df.columns),key=5)
                    parameter2=st.selectbox("chose your parameter to plot", options = list(df.columns),key=6)
                    st.write(parameter1)
                    selected_graph=st.selectbox("Select the type of plot you want to plot",options=["Scatter","Bar Plot","BoxPlot","Pie Chart","Histogram"],key=1)
                    #for column in df.columns:
                         
                        
                    if selected_graph=="Scatter":
                            
                        fig1 = px.scatter(df,y=df[parameter1],x=df[parameter2])
                        st.write(fig1)
                    elif selected_graph == "BoxPlot" :
                             fig = px.box(df,df[parameter1])
                             st.write(fig)
                            #  fig_2 = px.box(df,df[parameter2])
                            #  st.write(fig_2)
                    elif selected_graph == "Bar Plot" :
                             fig2 = px.bar(df,x=df[parameter1])
                             st.write(fig2)
                    elif selected_graph == "Pie Chart" :        
                        fig = px.pie(df, values=df[parameter1],names=df[parameter2])
                        st.write(fig)         
                    elif selected_graph == "Histogram": 
                         fig = px.histogram(df, x=df[parameter1])  
                         st.write(fig)   
                    #elif selected_graph == "Combined Histogram" :
                        #fig = px.histogram(df, x=df[parameter1], y=df[parameter2], marginal="box") #rughover_data=df.columns)  
                       # st.write(fig) 
                    # elif selected_graph == "Distplot":
                    #      data = [df[parameter1]]
                    #      fig = ff.create_distplot(data, ['Data'], show_hist=False)
                    #      st.write(fig)
                            
                          
                            
                            

# # Define a dictionary to store user credentials (user_id: password)
# user_credentials = {
#     "Prashant": "9216",
#     "user2": "password2",
#     "user3": "password3",
# }

# # Create a Streamlit app
# st.title("User Authentication")

# # Create input fields for user ID and password
# user_id = st.text_input("User ID")
# password = st.text_input("Password", type="password")

# # Check if the user has submitted the login form
# if st.button("Login"):
#     if user_id in user_credentials and user_credentials[user_id] == password:
#         st.success("Authentication successful! Welcome, " + user_id)
        
#         # Add your application logic here
#     else:
#         st.error("Authentication failed. Please check your credentials.")




                            
                           

                    
        
                   

                    
                    
                 
                 



               

main()            # entity = ["Grade","Name of Internal Crack","crack length ","No.of crack","Diameter of piping in MM","Diagonal Difference ( mm)"]
            # parameter = st.radio("Select the parameters you want to plot",options=entity)
            
           
                    
                
            
                        
                   




                
    
