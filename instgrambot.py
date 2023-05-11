from logging import exception

from Demos.win32cred_demo import username
from instabot import Bot
import  time
my_bot: Bot=Bot()

 #login
my_bot.login(username="",password="")

 #Folow a user
 # in this string you can type any frind user name and then you can run the program
 my_bot.follow("")

# if we want to follow multiple user you can just type or paste the usernames of the folowers
#my_bot.follow_users(["haroon21,mamaoon_323"]) ap to soo on

my_bot.follow_users([""])

# unfollow the non folower

my_bot.unfollow_non_followers()

# uplaod an image
# you can here upload the path name of photo in the strings and if you want to to set any captionn you can  i will show the demo in comment
#my_bot.upload_photo("python.jpg",caption="Hy its a python automation work ")

my_bot.upload_photo("",caption="Hy its a python automation work ")

# sending the message to any user to their username

#my_bot.send_message("Hey i m python coder and your friend","tyoe your friend username ")
try:
    my_bot.send_message("Hey i m python coder and your friend","")
except Exception :
    print(Exception)

time.sleep(60)

# like a post
#my_bot.like_user("type username",amount=2)
try:
    my_bot.like_user("",amount=2,filtration=False)
except Exception :
    print(Exception)
#comment
time.sleep(20)
#user_id=my_bot.get_user_id_from_username("tyoe username ")
try:
    user_id=my_bot.get_user_id_from_username("")
    media_id=my_bot.get_last_user_medias(user_id,1)
    my_bot.comment(media_id[0],"Picture looks soo beautiful")
except Exception :
    print(Exception)
# get list of all user folower of any usre
time.sleep(20)
#follower_list=my_bot.get_user_followers("type here username ")
#follower_list=my_bot.get_user_following("tyoe here usrename ")
try:
    follower_list=my_bot.get_user_followers("")
    followeing_list=my_bot.get_user_following("")
except Exception:
    print(Exception)
for count,each_follower in  enumerate(follower_list):
    if count>4:
        continue
    sleep(5)
    print(my_bot.get_username_from_user_id(each_follower))

for count,each_followe in enumerate( followeing_list):
    if count>4:
        continue
    sleep(5)

    print(my_bot.get_username_from_user_id(each_followe))

