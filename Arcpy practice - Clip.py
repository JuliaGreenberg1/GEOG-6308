#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import arcpy


# In[2]:


os.getcwd()


# In[ ]:


arcpy.env.workspace = os.getcwd()


# In[ ]:


arcpy.env.overwriteOutput = True


# In[3]:


arcpy.Clip_analysis("Congressional districts/tl_2018_us_cd116.shp",
                    "output/select_Kansas.shp",
                    "output/cong_Kansas.shp"
                   )


# In[14]:


def state_districts_116(state):
    arcpy.Clip_analysis(
        "./Congressional districts/tl_2018_us_cd116.shp",
        "./output/select_%s.shp" % state,
        "./output/cong_%s.shp" % state
    )


# In[18]:


state_districts_116('Arkansas')

