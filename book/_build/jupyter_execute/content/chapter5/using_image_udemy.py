#!/usr/bin/env python
# coding: utf-8

# # Using Our Image Module
# 
# In Pycharm IDE we had written some functions for
# downloading an image from the web and creating
# a [PIL](https://pillow.readthedocs.io/en/stable/reference/Image.html) image object.
# Here we import the function `pil_image_from_url` which is a function we wrote in our
# `image.py` module which is within the `image` folder.

# In[1]:


# This cell is just to get the image module from our notebooks section to work.
import sys
sys.path.append('../../../notebooks/')


# In[2]:


from image.image import pil_image_from_url


# In[3]:


# pick any image_url from the web you want to use
image_url = 'https://cdn.britannica.com/82/212182-050-50D9F3CE/basketball-LeBron-James-Cleveland-Cavaliers-2018.jpg'


# In[4]:


img = pil_image_from_url(image_url)


# In[5]:


type(img)


# In[6]:


img


# In[7]:


img.size


# In[8]:


img.rotate(45)


# In[9]:


img.rotate(90)


# In[10]:


(left, upper, right, lower) = (500, 400, 800, 600)
img_crop = img.crop((left, upper, right, lower))


# In[11]:


img_crop


# ## Downloading Images
# 
# We also wrote a simple function to download some images from the web.

# In[12]:


from image.image import download_images
image_urls = ['https://upload.wikimedia.org/wikipedia/commons/1/18/Dog_Breeds.jpg',
              'https://static.im-a-puzzle.com/gallery/Animals/Dogs/Dog_in_the_snow.jpg',
              'https://upload.wikimedia.org/wikipedia/commons/4/43/Cute_dog.jpg'
              ]
# change the folder_path on your machine
images = download_images(image_urls,
                         folder_path='/Users/guestadmin/junk/downloaded_images')
images

