#!/usr/bin/env python
# coding: utf-8

# # part 1
# ### Login to your Instagram Handle
# ### Submit with sample username and password

# In[8]:


from selenium import webdriver  # importing webdriver
import time                     # import time for further use
driver =  webdriver.Chrome(executable_path = 'C:/Users/umang/chromedriver.exe')   # path fro opening chromedriver


# In[9]:


driver.get('https://www.instagram.com')  #open instagram website


# In[10]:


time.sleep(3)  #wait for opeing complete site
username = driver.find_element_by_name('username')  # finding username element
username.send_keys('sa.mple7827')  # entering username


# In[11]:


time.sleep(3)  # wait for username success
password = driver.find_element_by_name('password')  # finding password element
password.send_keys('817827')   # enterning password 


# In[12]:


btn = driver.find_element_by_xpath('//button[contains(@class, "sqdOP  L3NKy   y3zKF     ")]')  # handling the notification for save password
btn.submit()


# In[13]:


time.sleep(3)
btn1 = driver.find_element_by_xpath('//div[contains(@class, "cmbtv")]')  # handling further popups
btn1.click()


# In[14]:


time.sleep(3)
notification = driver.find_element_by_xpath('//button[contains(@class, "_a9-- _a9_1")]') 
notification.click()


# # part 2
# ### Type for “food” in search bar and print all the names of the Instagram Handles that are displayed in list after typing “food”

# In[26]:


time.sleep(3)
search = driver.find_element_by_xpath('//input[contains(@class, "_aawh _aawj  _aauy")]')  # finding the search option
search.send_keys('food') # entering 'food' in search bar


# In[27]:


time.sleep(3)  # waiting for pages to show up
allpages = driver.find_elements_by_xpath('//div[contains(@role,"none")]') # selecting all pages 


# In[28]:


print(len(allpages)) # pring length of pages that shows up


# In[31]:


for i in allpages:   # for printing usernames of pages
    if i.text[0]!='#':
        print(i.text.split('\n')[0])


# In[32]:


search_dlt= driver.find_element_by_xpath('//div[contains(@class, "_aawn _9-lv")]')
search_dlt.click()  # clearinf=g the text from search bar


# # part 3
# ### Searching and Opening a profile using 
# ### Open profile of “So Delhi” 

# In[37]:


search_box= driver.find_element_by_xpath('//input[contains(@class, "_aawh _aawj _aauy")]')
search_box.send_keys('sodelhi')  # entering newtext'sodelhi' in search bar


# In[39]:


open_acc= driver.find_element_by_xpath('//div[contains(@class, "_abn_")]')
open_acc.click()  # selecting and opening so delhi account


# # part 4
# ### Follow/Unfollow given handle - 
# ## 1. Open the Instagram Handle of “So Delhi”
# ## 2.Start following it. Print a message if you are already following
# ## 3. After following, unfollow the instagram handle. Print a message if you have already unfollowed.

# In[63]:


# following the account
open_acc= driver.find_element_by_xpath('//div[contains(@class, "_aacl _aaco _aacw _aad6 _aade")]')
if open_acc.text == 'Follow':  # locating the follow button
    open_acc.click()
else:   # pring the message if already follwed
    print("you are already follwing it")


# In[64]:


# unfollwing the aacount
open_acc= driver.find_element_by_xpath('//div[contains(@class, "_aacl _aaco _aacw _aad6 _aade")]')
if open_acc.text == 'Follow':
    print("you have already unfollowed")
else:   # printing the meassage if already unfollwed
    open_acc.click()


# In[65]:


time.sleep(2)   
popup= driver.find_element_by_xpath('//button[contains(@class, "_a9-- _a9-_")]')
popup.click()  # confirming the unfollow request


# # part 5
# ### Like/Unlike posts
# ## 1. Liking the top 30 posts of the ‘dilsefoodie'. Print message if you have already liked it.
# ## 2. Unliking the top 30 posts of the ‘dilsefoodie’. Print message if you have already unliked it.

# In[15]:


home_page=driver.find_element_by_class_name('_aagx')
home_page.click() # going back to home page 


# In[16]:


search=driver.find_element_by_class_name('_aaw8')
search.click() # locating the search bar


# In[17]:


dlt_text=driver.find_element_by_xpath('//div[contains(@class, "_aawn _9-lv")]')
dlt_text.click() # deleting the previous text


# In[18]:


search_box=driver.find_element_by_xpath('//input[contains(@class, "_aawh _aawj _aauy")]')
search_box.send_keys('dilsefoodie') # entering dilsedelhi into the search bar


# In[20]:


open_acc= driver.find_element_by_xpath('//div[contains(@class, "_abn_")]')
open_acc.click() # selecting and opening the page


# In[27]:


posts = driver.find_elements_by_class_name('_aagw')
print(len(posts))  # counting the number of posts showwn in first scroll


# In[42]:


post = driver.find_element_by_class_name('_aagw') # locating the first post
post.click() # opening the first post
#start liking post from first post
count=1 # Initiating i=0 as we have to like the first 30 posts only
while True: # Running an infinite loop and breaking when the i beccomes 29
     # Checking if the post is already liked or not
    # If it is already liked then priting the required message
    if count==30:
        break
    like = driver.find_element_by_xpath('//span[contains(@class,"_aamw")]')
    if(like!='like'):
        like.click()
        count+=1
        time.sleep(2)
        nextb2 = driver.find_element_by_xpath('//div[contains(@class," _aaqg _aaqh")]')
        nextb2.click()
        time.sleep(5)
    # If it is already liked then priting the required message

    else:
        print('Already Liked')
        time.sleep(2)
        nextb2 = driver.find_element_by_xpath('//div[contains(@class," _aaqg _aaqh")]')
        nextb2.click()
        time.sleep(5)
    
close = driver.find_element_by_xpath('//div[contains(@class,"futnfnd5 li38xygf q0p5rdf8 mudwbb97")]')
close.click()


# In[43]:


## unlike 30 posts
post = driver.find_element_by_class_name('_aagw')
post.click() # opeing the first post
#start liking post from first post
count=1
while True: # Running an infinite loop and breaking when the i beccomes 29
     # Checking if the post is already unliked or not
        # If it is already unliked then priting the required message
    if count==30:
        break
    unlike = driver.find_element_by_xpath('//span[contains(@class,"_aamw")]')
    
    unlike.click()
    count+=1
    time.sleep(2)
    nextb2 = driver.find_element_by_xpath('//div[contains(@class," _aaqg _aaqh")]')
    nextb2.click()
    time.sleep(5)
# After breaking the loop closing the 30th post which is currently openend on the screen     
close = driver.find_element_by_xpath('//div[contains(@class,"futnfnd5 li38xygf q0p5rdf8 mudwbb97")]')
close.click()


# # part 6
# ### Extract list of followers
# ## 1.Extract the usernames of the first 500 followers of ‘foodtalkindia’ and ‘sodelhi’.
# 

# In[54]:


# After doing the required operations returning back to the home page
home_page=driver.find_element_by_class_name('_aagx')
home_page.click()
time.sleep(2)
search=driver.find_element_by_class_name('_aaw8')
search.click()
time.sleep(1)
dlt_text=driver.find_element_by_xpath('//div[contains(@class, "_aawn _9-lv")]')
dlt_text.click()
search_box=driver.find_element_by_xpath('//input[contains(@class, "_aawh _aawj _aauy")]')
search_box.send_keys('foodtalkindia') # Typing foodtalkindia into the search bar


# In[57]:


time.sleep(5)
open_acc= driver.find_element_by_xpath('//div[contains(@class, "_abn_")]')
open_acc.click()
# selecting and opening the account


# In[60]:


# importing the required library 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
followers =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href = "/foodtalkindia/followers/"]')))
followers.click()  #


# In[70]:


# Since the data is changing by scroing down the list of followers so we have to use the concept 
while True:
        # Using scrollIntoview funtion to scroll down by locating the xpath of the entire list of followers
        driver.execute_script('arguments[0].scrollIntoView(0, 100);', driver.find_element_by_xpath('//ul[contains(@class, "_aaey")]'))
        # Locating the followers and savig into the users list
        users=driver.find_elements_by_class_name('_aaei') 
        if len(users)>650:
            break
        time.sleep(2) # Waiting for 2 seconds between each scroll


# In[73]:


#After scrolling we have loaded all the followers , now we just have to take the valid  usernames
for i in range(0,500):
    print(users[i].text.split('\n')[0])


# In[84]:


close = driver.find_element_by_xpath('//div[contains(@class,"_ac7b _ac7d")]')
close.click() # # Closing the followers list and going back to the page of foodtalkindia


# In[145]:


## Similarly repeating the above process to calculate the first 500 followers of the 'so delhi'
search=driver.find_element_by_class_name('_aaw8')
search.click()
time.sleep(1)
dlt_text=driver.find_element_by_xpath('//div[contains(@class, "_aawn _9-lv")]')
dlt_text.click()
search_box=driver.find_element_by_xpath('//input[contains(@class, "_aawh _aawj _aauy")]')
search_box.send_keys('sodelhi')


# In[146]:


# selecting and opening the account
open_acc= driver.find_element_by_xpath('//div[contains(@class, "_abn_")]')
open_acc.click()
time.sleep(3)


# In[93]:



from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
followers =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href = "/sodelhi/followers/"]')))
followers.click()
time.sleep(3)


# In[94]:


while True:
        # Using scrollIntoview funtion to scroll down by locating the xpath of the entire list of followers
        driver.execute_script('arguments[0].scrollIntoView(0, 100);', driver.find_element_by_xpath('//ul[contains(@class, "_aaey")]'))
        # Locating the followers and savig into the users list
        users=driver.find_elements_by_class_name('_aaei') 
        if len(users)>650:
            break
        time.sleep(2) # Waiting for 2 seconds between each scroll


# In[95]:


for i in range(0,500):
    print(users[i].text.split('\n')[0])


# ## 2.Now print all the followers of “foodtalkindia” that you are following but those who don’t follow you.

# In[97]:


close = driver.find_element_by_xpath('//div[contains(@class,"_ac7b _ac7d")]')
close.click()


# In[120]:


home = driver.find_element_by_class_name('_aagx')
home.click()


# In[121]:


# Locating the my profile button on the home page and clicking on it 
my_profile = driver.find_element_by_class_name('_aaav')
my_profile.click()


# In[122]:


my_profile2 = driver.find_element_by_xpath('//div[contains(@class,"_ab8w  _ab94 _ab99 _ab9h _ab9m _ab9o")]')
my_profile2.click()


# In[123]:


# Opening my followers list 
followers = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href = "/sa.mple7827/followers/"]')))
followers.click()
time.sleep(3)


# In[125]:


# Calculating the number of followers i have so that i can have a terminating conditon for my loop
myfollowers = driver.find_element_by_class_name('_aae-')
followers = []
followers.append(myfollowers.text.split('\n')[0])


# In[126]:


close = driver.find_element_by_xpath('//div[contains(@class,"_ac7b _ac7d")]')
close.click()


# In[127]:


# Now opening the foodtalhindia page to store the usernames that i follow and that also follow foodtalkindia
search=driver.find_element_by_class_name('_aaw8')
search.click()
time.sleep(1)
dlt_text=driver.find_element_by_xpath('//div[contains(@class, "_aawn _9-lv")]')
dlt_text.click()
search_box=driver.find_element_by_xpath('//input[contains(@class, "_aawh _aawj _aauy")]')
search_box.send_keys('foodtalkindia')


# In[129]:


open_acc= driver.find_element_by_xpath('//div[contains(@class, "_abn_")]')
open_acc.click()
time.sleep(3)


# In[138]:


#search mutual followers & create set for it
m = driver.find_elements_by_xpath('//span[contains(@class,"_aaai")]')
mutualfollowers = []
for i in range(len(m)):
    mutualfollowers.append(m[i].text.split('\n')[0])
print(mutualfollowers)


# In[139]:


#find the difference between two sets so that we get followers of foodtalkindia who do not follow me
x = set(mutualfollowers) - set(followers)
print(x)


# # part 7
# ## Check the story of ‘coding.ninjas’. 
# 

# In[140]:


search=driver.find_element_by_class_name('_aaw8')
search.click()
time.sleep(1)
dlt_text=driver.find_element_by_xpath('//div[contains(@class, "_aawn _9-lv")]')
dlt_text.click()
search_box=driver.find_element_by_xpath('//input[contains(@class, "_aawh _aawj _aauy")]')
search_box.send_keys('coding.ninjas')  # search coding ninajs page


# In[141]:


open_acc= driver.find_element_by_xpath('//div[contains(@class, "_abn_")]')
open_acc.click()
time.sleep(3)


# In[143]:


# only viwing the story simply
story = driver.find_element_by_xpath('//div[contains(@class,"_aarf _aarg")]')
story.click()


# In[144]:



#check is story is present using aria-disabled attribute
story = driver.find_element_by_xpath('//div[contains(@class,"_aarf _aarg")]')
if story.get_attribute('outerHTML').split(' ')[3].split('=')[1].strip('"') == 'true':
    print('Coding Ninjas has no story')

#if story is present check if you have viewed the story by checking height attribute 
else:
    check = driver.find_element_by_xpath('//canvas[contains(@class,"_aarh")]')
    if check.get_attribute('outerHTML').split(' ')[2].split('=')[1].strip('"') == '208':
        print('I have already seen the story')

#if not viewed then view the story
    else:
        viewstory = driver.find_element_by_xpath('//span[contains(@class,"_aa8h")]')
        viewstory.click()
        time.sleep(3)
        while True:
            try:
                nextb = driver.find_element_by_xpath('//button[contains(@class,"_ac0d")]')
                nextb.click()
                time.sleep(3)
            except:
                break
                


# In[ ]:




