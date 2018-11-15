from requests import get
from bs4 import BeautifulSoup as soup
from time import sleep
import re

'''
    Obtains usernames from url, save them into csv file corresponding to Club ID.
    
    Args:
        CID : club id corresponding to url
        output_folder : optional argument. path to output
        
'''
def get_users_from_club(CID , output_folder = "../data/"):
    
    #Url which accesses users of a club
    URL = "https://myanimelist.net/clubs.php?action=view&t=members&id={}&show={}".format(CID,{})
    #Offset at which users are displayed
    OFFSET = 0
    
    while(True):

        print (URL.format(OFFSET))
        response = get(URL.format(OFFSET))
        html_soup = soup(response.text, 'html.parser')
        response.close()
        
        #Termination condition when no table is found
        if html_soup.table == None:
            print ("Club {} : No more users to grab".format(CID))
            return
        else:

            #Get html table containing users
            user_table = html_soup.table.find_all('a')

            #loop through each entry
            users = []
            for entry in user_table:
                username = entry.text.strip()

                #Some names are just images
                if username:
                    users.append(username)

            # write to file
            f = open(output_folder + '{}.csv'.format(CID),'a')
            f.write("\n".join(users))
            f.write("\n")
            f.close()
            
            OFFSET += 36
            sleep(3)

            
'''
    Obtains usernames from url, save them into csv file corresponding to forum thread ID.
    
    Args:
        TID : forum thread id corresponding to url
        output_folder : optional argument. path to output
        
'''
def get_users_from_forum_thread(TID , output_folder = "../data/forum_usernames/"):
    
    #Url which accesses users of a club
    URL = 'https://myanimelist.net/forum/?topicid={}&show={}'.format(TID,{})
    #Offset at which users are displayed
    OFFSET = 0
    
    while(True):

        print (URL.format(OFFSET))
        response = get(URL.format(OFFSET))
        html_soup = soup(response.text, 'html.parser')
        response.close()
        
        #Termination condition when no table is found
        if html_soup.table == None:
            print ("Forum Topic {} : No more users to grab".format(TID))
            return
        else:

            #Get html table containing users
            containers = html_soup.find_all('a', href=re.compile("/profile/"))

            #loop through each entry
            users = []
            for entry in containers:
                try:
                    users.append(entry.strong.text)
                except:
                    pass

            # write to file
            f = open(output_folder + '{}.csv'.format(TID),'a')
            f.write("\n".join(users))
            f.write("\n")
            f.close()
            
            OFFSET += 50
            sleep(3)
            

