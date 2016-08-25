
# coding: utf-8

# In[10]:

import urllib.request as ur
def readtext():
    file = open("gre",encoding='utf-8')
    content = file.read()
    print(content)
    checkprofanity(content)
    file.close()
def checkprofanity(texttocheck):
    connection= ur.urlopen("http://www.wdylike.appspot.com/?q="+texttocheck)
    output=connection.read()
    print(output)
    connection.close()   
readtext()


# In[ ]:




# In[4]:


def readtext():
    file = open("gre",encoding='utf-8')
    content = file.read()
    print(content)
    checkprofanity(content)
    file.close()
def checkprofanity(texttocheck):
    import urllib.parse
    import urllib.request
    url = 'http://www.someserver.com/cgi-bin/register.cgi'
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8') # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
    the_page = response.read()


# In[18]:

import urllib.request as urllib

# file reader functions
def read_file():
    doc= open('gre')
    contents = doc.read()
    print (contents)
    doc.close()
    return contents

# function with google api to check profanity in contents
def check_contenct_profanity(contents):
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q='+contents)
    output = connection.read()
    print (output)
    connection.close()
    if 'true' in output :
        print (" Profanity Alert !! ")
    elif 'false' in output :
        print (" This document has not curse words :-)")
    else :
        print ("sorry could not scan the doc ")

# read the file and grab contents
contents = read_file()

# check for profanity
check_contenct_profanity(contents)


# In[ ]:



