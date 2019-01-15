''' 
   Simulation: On average, how many emails get sent RCDS news per day?
        Assume there are 10 active clubs that send emails 1 out of 3 days per cycle (days 2, 4, and 6 do not have any clubs).
        Assume that there are 5 major sports teams that send emails for their home games about once every week.
        Assume there's 1 email about serving detentions once a week.
        Assume there's Daily Announcements every day.
        
'''
from pythonds.basic.stack import Stack
import random

class NewsQueue:
    # generate a random cycle and week day to simulate, use a Stack to keep emails in last in first out order
    def __init__(self):
        self.cycleday = random.randrange(1, 7)
        self.weekday = random.randrange(0, 5)
        self.items = Stack()
        
    # generate the emails for the day and add them to the items Stack    
    def getMail(self):
        
        # 1: daily announcement emails -- every day
        weekdaynames = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.items.push("\tDaily Announcements: " + weekdaynames[self.weekday] +", Day " + str(self.cycleday))
        
        # 2: detention emails -- 1/5 days a week
        if self.weekday == 4:
            self.items.push("\tServe your detentions, folks")
            
        # 3: home game emails -- on any given day, 5 sports teams each have a 1/5 chance of having a home game
        for i in range(5):
            t = Team()
            
            if t.gameday == self.weekday:
                self.items.push("\t"+t.getMessage())   
                
        # 4: club emails -- on cycle days 1, 3, and 5, 10 clubs have a 1/3 chance of meeting   
        for i in range(10):
            c = Club()
            
            if c.meetday == self.cycleday:
                self.items.push("\t"+c.getMessage())
                
    def size(self):
        return self.items.size()
    
    # pop all items to show inbox in order   
    def dumpItems(self):
        s = "RCDS News: " + str(self.items.size()) + " unread\n"
        for i in range(self.items.size()):
            s += self.items.pop() +"\n"
        return s
        
class Club:
    # randomize a cycle day when this Club meets from 1, 3, and 5 (club days) and email message
    def __init__(self):
        clubdays = [1, 3, 5]
        self.meetday = clubdays[random.randrange(0, 3)]
    
    def getMessage(self):
        messages = ["COME TO CLUB", "Come to room " + str(random.randrange(100, 311)) + " during break!", "club meeting, WILL HAVE FOOD", 
            "club meeting, WILL HAVE FOOD (for real this time)", "club!!!!!! :)", "Do you like things? Come to thing club during break", "CLUB PIZZA SALE",
            "CLUB DRESS DOWN DAY", "club.", "Club meeting in " + str(random.randrange(100, 311)), "pls come to club", "CLUUUUUUBBBB", "literally just come to my club"]
        return messages[random.randrange(len(messages))]

class Team:
    # randomize a week day 1-5 when this Team plays and email message
    def __init__(self):
        self.gameday = random.randrange(0, 5)
    
    def getMessage(self):
        teams = ["Girls", "Boys", "JV", "Varsity", "soccer", "hockey", "basketball", "lacrosse", "fencing", "squash", "golf", "tennis"]
        return teams[random.randrange(0, 2)] + " " + teams[random.randrange(2, 4)] + " " +teams[random.randrange(4, len(teams))] + " game today"
        
def simulation(n):
    avg = 0
    for i in range(n): # initialize/print n NewsQueues, add sizes to avg, divide after the loop
        nq = NewsQueue()
        nq.getMail()
        avg += nq.size()
        print(nq.dumpItems())
    avg /= n
    print("Average RCDS News emails per day: " + str(avg))
    

simulation(15)
    
        
        
     
    
    
    
    