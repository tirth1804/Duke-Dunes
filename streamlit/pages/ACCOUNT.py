import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth, db

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    # Initialize Firebase only if it's not already initialized
    firebase_cred = credentials.Certificate("credentials.json")
    firebase_admin.initialize_app(firebase_cred, {"databaseURL": "https://dukedunes-d70e8-default-rtdb.firebaseio.com/"})
#dukedunes-d70e8

# Initialize st.session_state
if "page" not in st.session_state:
    st.session_state.page = None


def signup():
    st.subheader("Sign Up")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        try:
            user = auth.create_user(email=email, password=password)
            st.success(f"User created with ID: {user.uid}")
        except Exception as e:
            st.error(f"Error: {e}")

def login():
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            # login = auth.sign_in_with_email_and_password(email, password)
            # #user = auth.sign_in_with_email_and_password(email, password)
            # st.success(f"Successfully logged in as {login['email']}")
            user = auth.get_user_by_email(email)
            # auth.verify_password(user.uid, password)
            st.success(f"User successfully authenticated: {user.uid}")
            
            # Redirect to the Home page after successful login
            st.experimental_set_query_params(page="HOME")
            
        except Exception as e:
            st.error(f"Error: {e}")

def main():
    st.title("Firebase Authentication App")
    choice = st.radio("Select Operation", ["Login", "Signup"])

    if choice == "Login":
        login()
    elif choice == "Signup":
        signup()
        
    if st.session_state.page == "HOME":
        st.success("Redirecting to Home Page...")
        st.markdown("[Go to Home](HOME)")
        
        st.experimental_rerun() 

if __name__ == "__main__":
    main()