class Instagram:
    def __init__(self,title, description,Creator_name,Location):  
        self.title = title
        self.description = description
        self.Creator_name=Creator_name
        self.Location=Location
        self.Comments=[]
        self.likes = 0
    def display_title(self):
        print("The title of the reel is ",self.title)
    def display_description(self):
        print("The description of the reel is ",self.description)
    def display_likes(self):
        print("The likes of the reel is ",self.likes)
    def display_Creator_name(self):
        print("The Creator name of the reel is :",self.Creator_name)
    def display_Location(self):
        print("The Location of the reel is :",self.Location)
    def display_Comments(self):
        if(len(self.Comments)==0):
            print("No comments yet.")
        else:
            print("The comments on the reel are:")
            for comment in self.Comments:
              print(comment)
    def add_comments(self,comment):
        self.Comments.append(comment)
        
    def delete_last_comments(self):
        temp_comment=self.Comments.pop()
        print("The last comment is deleted ",temp_comment)
        #self.remove("comment1") only work with u know element

        
    def display_all_details(self):
        print("Title:",self.title)
        print("Description:",self.description)
        print("Creator Name:",self.Creator_name)
        print("Location:",self.Location)
        print("Likes:",self.likes)
        print("Comments:",self.Comments)
    
    
    
    def liked(self):
        self.likes += 1
    def disliked(self):
        if self.likes > 0:
            self.likes-=1
    


reel1=Instagram("dancing","dancing with friends","Rashmi","banglore")
# 0
reel1.disliked() #0
reel1.liked() #1





reel1.liked() #2
# 0

reel1.disliked() #1
reel1.display_likes()


print("before commenting:")
print(reel1.Comments)
print("after comments:")
reel1.add_comments("comment1")
reel1.add_comments("comment2")
reel1.display_Comments()
#print(reel1.display_Creator_name())
#print(reel1.display_Location())
reel1.delete_last_comments()
#print(reel1.display_Comments())
reel1.display_all_details()