
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import random


# In[2]:


def cleanphoneno (ph):
    """
    cleanphonenumber to change the phone number from integer/float to text form.
    """
    if len(str(ph)) <11:
        return '0'+str(ph)
    return ph


# In[ ]:


def back_to_num(x):
    """
     back_to_num to change the phone number from integer/float to text form.
     use with apply fxn
    """
    x = '0'+str(int(x))
    return x


# In[1]:


def nameclean (x):
    """
    to do basic the name cleaning such as 
    shorten longname etc
    adding dots to abbreviated name
    """
    for i in range(len(x.split() )):
        if len(x.split()[i]) ==1 :
            x.split()[i] = x.split()[i].upper()+'.'
    x = ' '.join(u)
    return x
            
    if len(str(x).strip()) >20:
        u = x.strip().split()
        u[1] = str(u[1][0]).upper()+'.'
        x = ' '.join(u)
        return x
    return x


# In[2]:


def candc (str1,str2):
    """
    to check for similar names  
    
    """
    str1 = str1.upper()
    str2 = str2.upper()
    set1 = set(str1.split(' '))
    set2 = set(str2.split(' '))
    if len(set1&set2)>=2:
        if len((set1.union(set2)) - (set1&set2)) >=2:
            return False
        return True
    return False
               


# In[3]:


def cross_checker(dframe,col,col2 = 'PHONE NO.'):
    """
    to check and return similar names  and their phone numbers.
    """
    place_keeper = []
    post_keeper = {}
    ndframe = dframe[col]
    for i in range (len(ndframe)):
        #print(i)
        if i in place_keeper:
            continue
        for k in range (i+1,len(ndframe)):
            #print(ndframe[i],ndframe[k])
            if candc(ndframe[i].strip() , ndframe[k].strip()):
                
                if ndframe[i] in post_keeper:
                    post_keeper[ndframe[i]].append((k,ndframe[k],dframe[col2][k]))
                else:
                    post_keeper[ndframe[i]] = []
                    post_keeper[ndframe[i]].append((i,ndframe[i],dframe[col2][i]))
                    
                    post_keeper[ndframe[i]].append((k,ndframe[k],dframe[col2][k]))
                place_keeper.append((i,k))
                #post_keeper.append((dframe[:][i],dframe[:][k]))
           
                
   # print (post_keeper)
   # print( place_keeper)
    return post_keeper
                
                


# In[6]:


#are = pd.DataFrame.from_dict(re)
def listthem(ans):
    """
    takes in a dictionary(one returned by cross_checker) and returns a panda data frame
    """
    final_list = []
    for k in ans:
        for i in ans[k] :
            final_list.append(i)
            
    final_list = pd.DataFrame(final_list, columns = ('s/no','Names','Phone No'))        
    return final_list

            
        


# In[7]:



def cleansing(data,dirt,inplace = False):
    """
    dirt represent the column you want to clean.  basically this is done for the phone number
    
    """
    dd = map(back_to_num,data[dirt])
    dd = pd.Series(dd)
    dd.name = 'Phone'
    data['New ' + dirt] = dd
    dd = data.drop(columns = [dirt],axis = 1, inplace = inplace)
    return dd

