from instabot import Bot #pip install instabot

bot = Bot()

bot.login(username="________",password='**********')      #login to insta account

bot.follow('username to follow any account')       #follow any account on insta

bot.unfollow('username to unfollow any account')   #unfollow any account on insta

bot.upload_photo("file path",caption="Enter any caption") #use {/} instead of\     #Upload photo on insta

bot.send_message("Enter any message",["username1","username2"])      #send message

# See Followers...
followers = bot.get_user_followers("__________")
for follower in followers:
   print(bot.get_user_info(follower))

# See Followings...
followings=bot.get_user_following("My Username")
for following in followings:
   print(bot.get_user_info(following))