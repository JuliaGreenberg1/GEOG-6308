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


# SELECT:

# In[5]:


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


# CLIP:

# In[6]:


def state_districts_116(state):
    arcpy.Clip_analysis(
        "./Congressional districts/tl_2018_us_cd116.shp",
        "./output/select_%s.shp" % state,
        "./output/cong_%s.shp" % state
    )


# In[7]:


states = ['Hawaii','Georgia','Colorado','Idaho']


# In[8]:


for state in states:
    state_select(state)
    state_districts_116(state)

