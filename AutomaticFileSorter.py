#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os,shutil


# In[2]:


path = r"C:/Users/Marwan Mukhtar/Desktop/ay kalam/"


# In[3]:


file_name = os.listdir(path)


# In[4]:


folder_names = ['CSV Files', 'Image Files', 'Video Files', 'Text Files']
for loop in range(0,4):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs((path + folder_names[loop]))
        
        


# In[5]:


for file in file_name:
    if ".xlsx" in file and not os.path.exists(path + "CSV Files/" + file):
        shutil.move(path + file, path + "CSV Files/"+ file )
    elif ".jpg" in file and not os.path.exists(path + "Image Files/" + file):
        shutil.move(path + file, path + "Image Files/"+ file )
    elif ".mp4" in file and not os.path.exists(path + "Video Files/" + file):
        shutil.move(path + file, path + "Video Files/"+ file )
    elif ".txt" in file and not os.path.exists(path + "Text Files/" + file):
        shutil.move(path + file, path + "Text Files/" + file)
    else:
        print("There were files in this path that weren't moved!")


# In[ ]:




