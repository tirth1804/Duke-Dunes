import os
import io
import nltk
import pyperclip
import streamlit as st
from PIL import Image
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from newspaper import Article
# from streamlit_option_menu import option_menu

folder = "pages"
topics= ['--Select--']
for i in os.listdir(folder):
    temp = i[:-3]
    topics.append(temp)

nltk.download('punkt')

st.set_page_config(page_title='News Hub 📰 Portal', page_icon='./assets/DDlogo.webp')

def fetch_news_search_topic(topic):
    site = 'https://news.google.com/rss/search?q={}'.format(topic)
    op = urlopen(site)  # Open that site
    rd = op.read()  # read data from site
    op.close()  # close the object
    sp_page = soup(rd, 'xml')  # scrapping data from site
    news_list = sp_page.find_all('item')  # finding news
    return news_list


def fetch_top_news():
    site = 'https://news.google.com/news/rss'
    op = urlopen(site)  # Open that site
    rd = op.read()  # read data from site
    op.close()  # close the object
    sp_page = soup(rd, 'xml')  # scrapping data from site
    news_list = sp_page.find_all('item')  # finding news
    return news_list


def fetch_category_news(topic):
    site = 'https://news.google.com/news/rss/headlines/section/topic/{}'.format(topic)
    op = urlopen(site)  # Open that site
    rd = op.read()  # read data from site
    op.close()  # close the object
    sp_page = soup(rd, 'xml')  # scrapping data from site
    news_list = sp_page.find_all('item')  # finding news
    return news_list


def fetch_news_poster(poster_link):
    try:
        u = urlopen(poster_link)
        raw_data = u.read()
        image = Image.open(io.BytesIO(raw_data))
        st.image(image, use_column_width=True)
    except:
        image = Image.open('./assets/no_image.png')
        st.image(image, use_column_width=True)


def display_news(list_of_news, news_quantity):
    c = 0
    for news in list_of_news:
        c += 1
        # st.markdown(f"({c})[ {news.title.text}]({news.link.text})")
        st.write('**({}) {}**'.format(c, news.title.text))
        news_data = Article(news.link.text)
        try:
            news_data.download()
            news_data.parse()
            news_data.nlp()
        except Exception as e:
            st.error(e)
        fetch_news_poster(news_data.top_image)
        with st.expander(news.title.text):
            st.markdown(
                '''<h6 style='text-align: justify;'>{}"</h6>'''.format(news_data.summary),
                unsafe_allow_html=True)
            st.markdown("[Read more at {}...]({})".format(news.source.text, news.link.text))
        st.success("Published Date: " + news.pubDate.text)

        share_button = st.button("Share", key=f"share_{c}")
        if share_button:
            pyperclip.copy(news.link.text)

        if c >= news_quantity:
            break


def run():
    st.title("News Hub 📰")
    image = Image.open('./assets/whitelogo.png')
    

    col1, col2, col3 = st.columns([3, 5, 3])

    with col1:
        st.write("")

    with col2:
        st.image(image, use_column_width=False)

    with col3:
        st.write("")

    chosen_topic = "Trending News"
    user_topic = st.text_input("Enter your Topic")
    no_of_news = st.slider('Number of News:', min_value=5, max_value=25, step=1)
    if st.button("Search") and user_topic != '':
        user_topic_pr = user_topic.replace(' ', '')
        news_list = fetch_news_search_topic(topic=user_topic_pr)
        if news_list:
            st.subheader("✅ Here are the some {} News for you".format(user_topic.capitalize()))
            display_news(news_list, no_of_news)
        else:
            st.error("No News found for {}".format(user_topic))
    else:
        # st.warning("Please write Topic Name to Search")
        news_list = fetch_top_news()
        if news_list:
            st.subheader("✅ Here are the some {} News for you".format(chosen_topic))
            display_news(news_list, no_of_news)
        else:
            st.error("No News found for {}".format(chosen_topic))
        
    # cat_op = st.selectbox('Select your Category', topics)
    # if cat_op == topics[0]:
    #     st.warning('Please select Type!!')
    # news_list = fetch_top_news()
    # if news_list:
    #     st.subheader("✅ Here are the some {} News for you".format(chosen_topic))
    #     display_news(news_list, no_of_news)
    # else:
    #     st.error("No News found for {}".format(chosen_topic))
    
    
    
    # with st.sidebar:        
    #     app = option_menu(
    #         menu_title='News Hub',
    #         options=['Home','Account','Trending','Your Posts','about'],
    #         icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
    #         menu_icon='chat-text-fill',
    #         default_index=1,
    #         styles={"container": {"padding": "5!important","background-color":'black'},
    #                 "icon": {"color": "white", "font-size": "23px"}, 
    #                 "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
    #                 "nav-link-selected": {"background-color": "#02ab21"}
    #                 }
    #     )

    
    # if app == "Home":
    #     business.app()
    # if app == "Account":
    #     test.app()    
    # if app == "Trending":
    #     trending.app()        
    # if app == 'Your Posts':
    #     your.app()
    # if app == 'about':
    #     about.app()
             

run()
