from requests import get
import requests
from bs4 import BeautifulSoup as soup
from time import sleep
import os.path
import re
import csv

'''
    Obtains usernames from url, save them into csv file corresponding to Club ID.
    
    Args:
        CID                     : club id corresponding to url
        output_folder           : optional argument. path to output
        ignore_present          : does not scrape if there's already a file present
        
'''
def get_users_from_club(CID , output_folder = "../data/club_usernames/", ignore_present = True):

    #Optional : do not grab anything if file already present
    if ignore_present:
        if os.path.isfile(output_folder + str(CID) + ".csv"):
            print("Club {} : File already present".format(CID))
            return
    
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
            sleep(3)
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
        TID                     : forum thread id corresponding to url
        output_folder           : optional argument. path to output
        ignore_present          : does not scrape if there's already a file present
        
'''
def get_users_from_forum_thread(TID , output_folder = "../data/forum_usernames/", ignore_present = True):
    
    #Optional : do not grab anything if file already present
    if ignore_present:
        if os.path.isfile(output_folder + str(TID) + ".csv"):
            print("Forum Topic {} : File already present".format(TID))
            return

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
            sleep(3)
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


"""
Function takes in username, returns list of all reviews

Args:
    username           : MyAnimeList username
    output_folder      : Output folder containing users anime list
    ignore_present     : Set True to skip users that have already been scraped. False to update.
    

Example of json:
{
    u'anime_airing_status': 2,
    u'anime_end_date_string': u'04-11-15',
    u'anime_id': 23587,
    u'anime_image_path': u'https://myanimelist.cdn-dena.com/r/96x136/images/anime/10/70733.jpg?s=efee95cdbf92ebacd1ae00e9be000dc9',
    u'anime_licensors': None,
    u'anime_media_type_string': u'TV',
    u'anime_mpaa_rating_string': u'PG-13',
    u'anime_num_episodes': 13,
    u'anime_season': None,
    u'anime_start_date_string': u'01-10-15',
    u'anime_studios': None,
    u'anime_title': u'The iDOLM@STER Cinderella Girls',
    u'anime_url': u'/anime/23587/The_iDOLMSTER_Cinderella_Girls',
    u'days_string': None,
    u'finish_date_string': None,
    u'has_episode_video': True,
    u'has_promotion_video': True,
    u'has_video': True,
    u'is_added_to_list': False,
    u'is_rewatching': 0,
    u'num_watched_episodes': 0,
    u'priority_string': u'Low',
    u'score': 0,
    u'start_date_string': None,
    u'status': 1,
    u'storage_string': u'',
    u'tags': u'',
    u'video_url': u'/anime/23587/The_iDOLMSTER_Cinderella_Girls/video'
 }
"""
def get_anime_list_from_user(username, output_folder="../data/user_anime_list/", ignore_present=True):
    
    # If we don't want to update existing users
    if ignore_present:
        if os.path.isfile(output_folder + username + ".csv"):
            print("User {} : File already present".format(username))
            return False
    
    URL = "https://myanimelist.net/animelist/{}/load.json?offset={}&status=7".format(username,"{}")
    OFFSET = 0
    
    anime_reviews = []
#    # Our header
#     anime_reviews = [
#         [   
#             "username",
#             "anime_id",
#             "anime_title",
#             "score",
#             "num_watched_episodes",
#             "status",
#             "priority_string"
#         ]
#     ]
    
    while(True):
        response = requests.get(URL.format(OFFSET))
        
        # Check for request refusal
        # Sleep for 0.5s before trying again
        while response.status_code == requests.codes.too_many_requests:
            print ("{} : ERROR {}".format(response.url, response.status_code))
            sleep(0.5)
            response = requests.get(URL.format(OFFSET))
        
        # test for 404 NOT FOUNDS
        if response.status_code != requests.codes.ok:
            print ("{} : ERROR {}".format(response.url, response.status_code))
            return False

        # Connection established successfully
        anime_list_json = response.json()

        # Check for empty json. Empty json indicates current user is finished.
        if not anime_list_json:            
            # Save review list to csv
            output_file_path = output_folder + username + ".csv"
            with open(output_file_path, "w") as f:
                writer = csv.writer(f , delimiter='|')
                writer.writerows(anime_reviews)
    
            print ("{} : Finished. {} Reviews --> {}".format(
                    username, 
                    len(anime_reviews),
                    output_file_path
                    ))
            return True

        # Loop through json file and create entries
        for anime_review in anime_list_json:
            anime_reviews.append([
                str(username),
                str(anime_review["anime_id"]),
                str(anime_review["anime_title"]),
                str(anime_review["score"]),
                str(anime_review["num_watched_episodes"]),
                str(anime_review["status"]),
                str(anime_review["priority_string"])
            ])
        OFFSET += 300    # update offset
    return False
            

