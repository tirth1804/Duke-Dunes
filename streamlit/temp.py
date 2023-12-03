import os
folder = "streamlit\pages"
topics= []
for i in os.listdir(folder):
    temp = i[:-3]
    topics.append(temp)
print(topics)