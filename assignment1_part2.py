#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Book:
    
    author = ""
    title = ""
    def __init__(self,Author, Title):
        self.author = Author
        self.title = Title
        
    def display(self):
        print("\""+self.title+", Written by "+self.author+"\"")

object1= Book("John Steinbeck", "Of Mice and Men")

object1.display()

object2= Book("Harper Lee","To kill a Mockingbird")

object2.display()
        


# In[ ]:




