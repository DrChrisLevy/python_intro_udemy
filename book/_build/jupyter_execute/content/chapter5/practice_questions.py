#!/usr/bin/env python
# coding: utf-8

# # Practice Questions
# 
# In this chapter we learned how to install external libraries 
# and import them into our code. We also learned how to create virtual environments and set up those virtual environments within the Pycharm IDE. The purpose of the these questions is to practice some of these skills and tools.
# 
# In these practice questions we will be installing a library called [pandas](https://pandas.pydata.org/) and library called [seaborn](https://seaborn.pydata.org/). These questions are not supposed to teach you how to use these libraries. Instead, the objective is to get the code to run within Pycharm and Jupyter through the use of the virtual environment.
# You may encounter some issues. It is common to run into issues when dealing with packages and their dependencies. If you do so, Google the problems and read and try and find solutions.
# 
# If you get stuck at any point, go back and read this chapter over again. You can also checkout the videos for Chapter 5 in the [Udemy course videos](https://www.udemy.com/course/learn-to-code-with-an-introduction-to-python-3/?referralCode=42FB26846F76E2E41EF8) which go into lots of detail on setting up the virtual environment in Pycharm.

# In[1]:


# This cell is just to get the pandas_demo module from our notebooks section to work.
import sys
sys.path.append('../../../notebooks/')


# ## 1.
# Use the terminal/command prompt to create a virtual environment called `pandas_demo` in your `.venv` folder using the [venv](https://docs.python.org/3/library/venv.html) tool. Then activate it and install pandas into the virtual environment with the command `pip install pandas`. Also install Jupyter Notebook into this virtual environment with the command `pip install notebook`. Finally install seaborn with `pip install seaborn`.

# ## 2. 
# 
# In your `my_notebooks` folder create a folder called `pandas_demo`. Open a new project in Pycharm from the `pandas_demo` folder so that it is the main/root folder in your Pycharm project. Within the `pandas_demo` folder create a file called `python_demo.py`. Your setup should look something like the below screenshot.
# 
# ![pandas_demo](pycharm_screenshot.png)
# 

# ## 3.
# 
# Set up the Python interpreter within Pycharm to use the `pandas_demo` virtual environment you created above. If you forget how to do this go back and watch the videos from Chapter 5 [Udemy course videos](https://www.udemy.com/course/learn-to-code-with-an-introduction-to-python-3/?referralCode=42FB26846F76E2E41EF8) relative to this question.

# ## 4.
# 
# To check that the environment is working within Pycharm execute the following code within the Pycharm Python console.

# In[2]:


import pandas as pd
import seaborn as sns

df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['col1', 'col2', 'col3'])
print(df.head())

print('\n\n')

iris = sns.load_dataset('iris')
print(iris.head())


# ## 5.
# Within Pycharm, use the editor to add the following code to the file `pandas_demo.py`

# ```
# import seaborn as sns
# 
# 
# def load_data():
#     return sns.load_dataset("penguins")
# 
# 
# def pairs_plot(df):
#     return sns.pairplot(df, hue="species")
# 
# 
# def group_count(df, col_name):
#     return df.groupby(col_name).count()
# ```

# ## 6.
# 
# Create a Jupyter Notebook within your `my_notebooks` folder. In that notebook import the functions from the `pandas_demo.py`
# module and run the following code in Jupyter notebook. If you see the generated output then you completed these questions successfully.
# 
# Note that the functions we created in `pandas_demo.py` are a little silly. You would just call those libraries directly in practice. However, the point here is to understand how to import functions that you write within Python modules.

# In[3]:


from pandas_demo.pandas_demo import load_data, pairs_plot, group_count


# In[4]:


df = load_data()
df.head(10)


# In[5]:


pairs_plot(df)


# In[6]:


group_count(df, 'sex')

