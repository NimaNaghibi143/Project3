from os import name
import string

class Media:
    def __init__(self,name):
        self._name=name

    @property  #getter
    def Name_(self):
        return self._name
     
#------------------------------------------- 

class Twitter_(Media):

    def __init__(self, name,t_list,type):
        super().__init__(name)
        self.t_list=[] 
        self._type=type
    def New_tweet(self):
        tweet_post=input("enter tweet  ")
        print("tweet is", tweet_post)
        if len(tweet_post) < 280:
            self.t_list.append(tweet_post)

        else:
            print("Error")
            
    def tweetfun(self):
        return self.t_list                  


 
class Instagram(Media):

    def __init__(self, User_name, p_list, Type):
        super().__init__(User_name)
        self.post_list=[] 
        self._Type=Type
    def New_post(self):
        post=input("enter post  ")
        print("post is",post)
        if len(post) < 2200:
            self.p_list.append(post)
        else:
            print("Error")
                 
    def New_post_(self):
        return self.p_list

 

T=Twitter_("t1", [], "persiantweeter")
T.New_tweet()
print(T.tweetfun())

