import streamlit as st

# Dummy user database (replace this with a real database in a production app)
users = []

def signup():
    st.subheader("Sign Up")
    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password")
    
    if st.button("Sign Up"):
        users.append({"username": new_username, "password": new_password})
        st.success("You have successfully signed up!")

def login():
    st.subheader("Log In")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Log In"):
        user = next((u for u in users if u["username"] == username and u["password"] == password), None)
        if user:
            st.success("Logged in as: " + user["username"])
        else:
            st.error("Invalid username or password")

def main():
    st.title("Login and Signup Example")
    
    option = st.selectbox("Choose an action", ["Login", "Sign Up"])
    
    if option == "Login":
        login()
    elif option == "Sign Up":
        signup()

if __name__ == '__main__':
    main()
