# import streamlit as st
# from PIL import Image
# from bs4 import BeautifulSoup as soup
# from urllib.request import urlopen
# from newspaper import Article
# import io
# import nltk
# import pyperclip
# nltk.download('punkt')
# from google.oauth2 import id_token
# from google.auth.transport import requests

# # st.title("Sign Up")
# # name = st.text_input("Name")

# # username = st.text_input("Username")
# # password = st.text_input("Password", type="password")
# # if st.button("Sign Up"):
# #     # Implement your login logic here
# #     st.success(f"Logged in as {username}")



# # Define a function for Google OAuth2 authentication
# # def authenticate_with_google():
#     # Implement your Google OAuth2 authentication logic here
#     # You can use third-party libraries or services like OAuth2
#     # to handle the authentication process.

# st.title("Sign Up")
# name = st.text_input("Name")
# username = st.text_input("Username")
# password = st.text_input("Password", type="password")

# # Add a "Sign Up with Google" button
# # if st.button("Sign Up"):
#     # Implement your sign-up logic here
#     # st.success(f"Account created for {username}")

# # Add a "Sign Up with Google" button
# # if st.button("Sign Up with Google"):
# #     # Call the authentication function
# #     authenticate_with_google()

#     # st.title("Your Streamlit App")
    
#     # Google Authentication
# st.subheader("Google Authentication")
# client_id = "650627225-706vcvsv6ssp05kolbhj6cgvamkg868n.apps.googleusercontent.com"  # Replace with your OAuth client ID
# token = st.text_input("Enter your Google ID token", type="password")
# if st.button("Authenticate"):
#     try:
#         idinfo = id_token.verify_oauth2_token(token, requests.Request(), client_id)
#         if idinfo['aud'] != client_id:
#             raise ValueError("Invalid client ID")
#         st.success(f"Authentication successful: {idinfo['name']}")
#         # Continue with the rest of your app logic here
#     except ValueError as e:
#         st.error("Authentication failed")
#         st.error(e)

import streamlit as st
from PIL import Image
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
# from newspaper import Article
import io
import nltk
import pyperclip
nltk.download('punkt')
import streamlit as st
import firebase_admin
from firebase_admin import credentials, db




# cred = credentials.Certificate("E:\7sem\CP3\InNews-master\credentials.json")
# firebase_admin.initialize_app(cred, {"databaseURL" : "https://newscp-default-rtdb.firebaseio.com/"})

# auth = firebase_admin.auth()
# ref = db.reference("/")

# # Create the Streamlit app
# st.title("User Signup")

# # Define form fields
# email = st.text_input("Email")
# password = st.text_input("Password", type="password")
# confirm_password = st.text_input("Confirm Password", type="password")

# if st.button("Sign Up"):
#     if password == confirm_password:
#         try:
#             # Create a new user with email and password
#             auth.create_user_with_email_and_password(email, password)
#             st.success("Account created successfully. You can now login.")
#         except Exception as e:
#             st.error(f"Error: {e}")
#     else:
#         st.error("Passwords do not match.")

# # Add a link to the login page (assuming you have a separate login page)
# st.markdown("[Go to Login](/login)")


import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
import json

# Firebase configuration data
firebase_config = {
    "apiKey": "AIzaSyDMoLbiBNz6fdNAuTGeTQBxSGeyhzIQNEg",
    "authDomain": "newscp.firebaseapp.com",
    "databaseURL": "https://newscp-default-rtdb.firebaseio.com",
    "projectId": "newscp",
    "storageBucket": "newscp.appspot.com",
    "messagingSenderId": "650627225",
    "appId": "1:650627225:web:117e1179be3f2df30d5008",
    "measurementId": "G-1P443YCSWY"
}

# Initialize Firebase
cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred, {"databaseURL" : "https://newscp-default-rtdb.firebaseio.com/"})

auth = firebase_admin.auth()
ref = db.reference("/users")

# Create the Streamlit app
st.title("User Management")

# Define form fields
email = st.text_input("Email")
password = st.text_input("Password", type="password")
user_id = st.text_input("User ID")

# Function to create a new user
def create_user():
    user_data = {
        'email': email,
        # Add other user information here
    }
    new_user_ref = ref.push(user_data)
    return new_user_ref.key

# Function to update user information
def update_user():
    user_data = {
        'email': email,
        # Add other user information here
    }
    ref.child(user_id).update(user_data)

# Function to delete a user
def delete_user():
    ref.child(user_id).delete()

# Function to retrieve all users
def get_all_users():
    users = ref.get()
    return users

# Sign-up or CRUD operations
operation = st.radio("Select Operation", ["Sign Up", "Create", "Update", "Delete", "Get All Users"])

if operation == "Sign Up":
    if st.button("Sign Up"):
        try:
            # Create a new user with email and password
            auth.create_user_with_email_and_password(email, password)
            st.success("Account created successfully. You can now login.")
        except Exception as e:
            st.error(f"Error: {e}")

elif operation == "Create":
    if st.button("Create User"):
        new_user_id = create_user()
        st.success(f"User created with ID: {new_user_id}")

elif operation == "Update":
    if st.button("Update User"):
        update_user()
        st.success("User information updated.")

elif operation == "Delete":
    if st.button("Delete User"):
        delete_user()
        st.success("User deleted.")

elif operation == "Get All Users":
    if st.button("Fetch Users"):
        users = get_all_users()
        st.write("All Users:")
        st.write(users)

# Add a link to the login page (assuming you have a separate login page)
st.markdown("[Go to Login](/login)")
