#!/usr/bin/env python
# coding: utf-8

# # Intro to Virtual Environments
# 
# In the previous section we learned how to import modules or libraries
# from the Python Standard Library. In this section you will learn how to
# install external packages for use within Python. This is a very common task
# and is essential to do when your working on specific projects.
# For example, when you first started this course/book you needed to install 
# Jupyter Notebook. You typed `pip install notebook` to install Jupyter Notebook.
# 
# **PIP** is a package manager for Python packages and modules.
# You use the `pip` command in the terminal shell to install
# packages from the [The Python Package Index (PyPI)](https://pypi.org/).
# 
# For example, if you were working on a data science or machine learning project you may need packages such as:
# 
# - [numpy](https://pypi.org/project/numpy/), [official docs](https://numpy.org/)
# - [pandas](https://pypi.org/project/pandas/), [official docs](https://pandas.pydata.org/docs/index.html)
# - [scikit-learn](https://pypi.org/project/scikit-learn/), [official docs](https://scikit-learn.org/stable/index.html)
# 
# 
# Or for example, if you were working on a backend web application you may need the package:
# - [flask](https://pypi.org/project/Flask/), [official docs](https://flask.palletsprojects.com/en/1.1.x/)
# 
# Do not attempt to install these packages yet because we need to learn about virtual environments first. The main point here is that Python has a super rich ecosystem of
# external libraries you can install and use. It is perfectly normal and safe to do so.
# It is completely expected to have such requirements for different projects.
# 
# But different projects have different requirements. Depending on what you are working on,
# you will only need specific packages for specific projects. You won't need to install all the libraries and packages for every project. Also, you do not want to install hundreds of packages into your base system Python. It can get messy real quick, and even worse, it can break stuff.
# 
# When you first installed Python, that is known as your base system Python. It's good to keep it clean and tidy. It is bad practice to install all sorts of libraries and modules into
# your base system Python installation. Rather, you should create **virtual environments**. For each project, you have a different virtual environment and in within those environments you will install the required libraries or packages that you need (and only the ones you need).
# 
# There are so many different ways to work with virtual environments and packages in Python.
# It is actually a little annoying that there is not a a single universal tool. However, if you are interested I highly recommend the following to at least know and learn about. It is not required for the moment or in this course right now to know or even look into these. But I want to just plant these names in the back of your mind because you will most certainly run into them if you stick with coding and Python.
# 
# - [poetry](https://python-poetry.org/)
#     - Relatively new as of writing this and well maintained. A good alternative to pipenv (see below). Makes it really easy to publish your own packages to PiPy.
# - [annaconda](https://www.anaconda.com/)
#     - Great for data science and many people use it. Although personally, I stick with docker and poetry for my projects at work. A lot of windows user especially like this option because it usually just works and makes Python and Windows play nice together. I would highly recommend using [miniconda](https://docs.conda.io/en/latest/miniconda.html) if you go this route.
# - [pipenv](https://pipenv.pypa.io/en/latest/)
#     - Although very popular, it appears dead in terms of no future development. I would
#     personally recommend [poetry](https://python-poetry.org/) over pipenv.
# - [docker](https://www.docker.com/)
#     - Probably overkill if you are just starting and docker is so much more than Python virtual environments. It's amazing though for setting up all sorts of isolated environments. Look into this in the future. 
#     
# Again, at this moment in time, I don't suggest you go out and try to learn all the above and use it. Just focus on learning Python and getting good at it. It's just good to know about the above in the back of your mind and you can look into it down the road. Besides, for the time being we are going to use a simple tool for managing virtual environments that comes with Python 3.3 and above. No need to install anything extra. This way you can learn the basics and how to install packages into virtual environments. Once you know the basics and work on a few different projects, then you can do your own research on the above tools and make your own decision on whether they will be useful.
# 

# ## `venv`
# 
# We will be using a tool called [venv](https://docs.python.org/3/tutorial/venv.html)
# for creating virtual environments, at least initially. It comes with Python 3 
# and is easy to use. You can read about it and how to use it [here](https://docs.python.org/3/tutorial/venv.html). Because of the nature
# of this topic I will not be giving tons of detail here in this book.
# However, I will go into lots of detail in the Udemy [course videos](https://www.udemy.com/course/learn-to-code-with-an-introduction-to-python-3/?referralCode=42FB26846F76E2E41EF8) on how to use it
# so checkout the videos and the section that corresponds to this section
# of the book.
# 
# ### Basic Usage
# You can checkout the [venv documentation](https://docs.python.org/3/tutorial/venv.html)
# for complete details as well the Udemy [course videos](https://www.udemy.com/course/learn-to-code-with-an-introduction-to-python-3/?referralCode=42FB26846F76E2E41EF8). This is just
# a quick look up reference guide.
# 
# First open the terminal (mac) or command-prompt (windows) and navigate 
# to the directory where you want to create the virtual environment.
# These commands are written with `python3` but you may have to use
# `python`. Use whichever results in Python 3.6 or higher. You can always
# check with `python --version` or `python3 --version`.
# 
# **Create the virtual environment** and replace `my-env` with whatever name you want to use 
# for the environment. Type this in the terminal shell or command prompt. Type it from the directory where your project is located. 
# 
# `python3 -m venv my-env`
# 
# **To activate the virtual environment on a mac:**
# 
# `source my-env/bin/activate`
# 
# **To activate the virtual environment on windows:**
# 
# `my-env\Scripts\activate.bat`
# 
# **Once the environment is activated you can install packages inside the virtual environment.**
# 
# Here we will install the requests, numpy, and Jupyter Notebook packages as an example.
# 
# `pip install requests`
# 
# `pip install numpy`
# 
# `pip install notebook`
# 
# **To list the installed packages in the virtual environment:**
# 
# `pip freeze` or `pip list`
# 
# To put the packages in a requirements.txt file you can type
# `pip freeze > requirements.txt`
# 
# **Remove a package from the virtual environment:**
# 
# While in the activate environment, type
# `pip uninstall requests` to remove the `requests` package for example.
# 
# **To exit the virtual environment**
# 
# `deactivate`
# 
# As I said, checkout the Udemy [course videos](https://www.udemy.com/course/learn-to-code-with-an-introduction-to-python-3/?referralCode=42FB26846F76E2E41EF8) for more details.

# In[ ]:




