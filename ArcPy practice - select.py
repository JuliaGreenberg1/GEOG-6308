#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import arcpy


# In[2]:


os.getcwd()


# In[3]:


arcpy.env.workspace = os.getcwd()


# In[4]:


arcpy.env.overwriteOutput = True


# In[5]:


# make new folder
os.mkdir("output")


# In[ ]:


arcpy.Select_analysis(
    # Input features
    "States/tl_2018_us_state.shp",
    # Output shapefile
    "./output/select_Arkansas.shp",
    # Expression
    '"NAME" = \'Arkansas\''
)


# In[6]:


def state_select(state):
    input = "States/tl_2018_us_state.shp"
    output = "./output/select_%s.shp" % state
    select = ' "NAME" = \'%s\'' % state
    arcpy.Select_analysis(
        input,
        output,
        select
    )
    print output


# In[8]:


state_select('Kansas')

