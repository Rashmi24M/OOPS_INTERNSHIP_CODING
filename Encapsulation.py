#Instagram Account system using Encapsulation
class InstagramAccount:
    def __init__(self,account_name):
        self.account_name=account_name
        self.__private_reels=[]
        self.__archived_reels=[]
    def add_private_reel(self,reel_name):
        self.__private_reels.append(reel_name)
    def display_private_reels(self,is_follower):
        self.is_follower=is_follower
        if is_follower==is_follower:
            print("Private Reels of",self.account_name,":",self.__private_reels)
        else:
            print("Access Denied! Only folowers can view private reels.")
    def add_archived_reel(self,reel_name):
        self.__archived_reels.append(reel_name)
    def display_archived_reels(self):
        password="admin123"
        entered_password=input("Enter password to view reels:")
        if password==entered_password:
            print("Archived Reels are:",self.__archived_reels)
        else:
            print("Access Denied! Only account holder can view archived reels.")
acc=InstagramAccount("Rashmi")
acc.add_private_reel("dancing with friends")
acc.add_private_reel("cooking")
acc.add_archived_reel("vacation memories")      
acc.add_archived_reel("birthday celebration")
acc.display_private_reels("ramya") # Access granted
acc.display_private_reels("Rashmi") # Access granted
acc.display_archived_reels() # Access granted
