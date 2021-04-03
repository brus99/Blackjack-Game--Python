import numpy as np
f =np.array(["As","Ah","Ad","Ac","2s","2h","2c","2d","3s","3h","3d","3c","4s","4d","4c","4h","5h","5d","5s","5c","6h","6d","6c","6s","7s","7d","7c","7h","8h","8d","8c","8s","9s","9d","9c","9h","Th","Td","Tc","Ts","Js","Jd","Jh","Jc","Qs","Qd","Qh","Qc","Ks","Kc","Kd","Kh"])
scores = {"As":1,"Ah":1,"Ad":1,"Ac":1,"2s":2,"2h":2,"2c":2,"2d":2,"3s":3,"3h":3,"3d":3,"3c":3,"4s":4,"4d":4,"4c":4,"4h":4,"5h":5,"5d":5,"5s":5,"5c":5,"6h":6,"6d":6,"6c":6,"6s":6,"7s":7,"7d":7,"7c":7,"7h":7,"8h":8,"8d":8,"8c":8,"8s":8,"9s":9,"9d":9,"9c":9,"9h":9,"Th":10,"Td":10,"Tc":10,"Ts":10,"Js":10,"Jd":10,"Jh":10,"Jc":10,"Qs":10,"Qd":10,"Qh":10,"Qc":10,"Ks":10,"Kc":10,"Kd":10,"Kh":10}
Aces = (["Ah","Ad","Ac","As"])
dealertotal=0
def hit():                                                  
    global f                                                 
    MyHand2 = np.random.choice(f,1,replace=False)              #randomly chooses a card without replacement
    f = np.delete(f,np.where(f==MyHand2[0]))                   #deletes chosen card from deck f
    return MyHand2                                                
def newscore(hand):                                              
    count = 0
    for card in hand:
        count+= scores[card]                                   #count score from map
    return count
def didyouwin(total,hand):                                          #determines if the player may continue playing
    global y
    if total>21:
        print("you bust")
    elif total==21 and len(hand)==21:
        print("BLACKJACK!!! Player wins!")
    elif total<=21:
        y= input("again or stand?:  ")
def HasAnAce(hand,points):
    for i in range(len(Aces)):
        if Aces[i] in hand and points<=11:
            points+=10                                         #if an Ace causes a bust (>21), Ace = 1, else Ace = 11    
    return points 
def dealerhits(dealer,dealertotal):
    for i in range(7):                                         #runs a loop until the dealer busts, beats the player, or a push is present
            dealer = np.append(dealer,hit())
            dealertotal = newscore(dealer)                     
            dealertotal = HasAnAce(dealer,dealertotal)
            print(dealer)
            print("The dealer has",dealertotal)
            if dealertotal>21:
                print("dealer busts, you win")
                break
            elif dealertotal>total1:
                print("the dealer has,",dealertotal,",you have,",total1,",you lose")
                break
            elif dealertotal<total1 and dealertotal>=17:
                print("the dealer has,",dealertotal,",you have,",total1,",you win")
                break
            elif dealertotal==total1 and dealertotal>=17:
                print("push")
                break
def Blackjack(total):
    if total1 ==21:
        print("BLACKJACK!!! Player wins!")
dealer = np.random.choice(f,1,replace=False)                                #first dealer card 
f = np.delete(f,np.where(f==dealer[0]))
print("the dealer has",dealer)                                                          
MyHand = np.random.choice(f,1,replace=False)                                #players first card
f = np.delete(f,np.where(f==MyHand[0]))
print("You have",MyHand)
x = input("Do you hit or double?:   ")
if x == ("hit"):                                                            #initial input that runs hit,scoring, and conditional ace functions
    MyHand = np.append(MyHand,hit())
    print(MyHand)
    total1 = newscore(MyHand)
    total1 = HasAnAce(MyHand,total1)
    print(total1)
    didyouwin(total1,MyHand)
    if y == ("again"):                                                     #allows the user to hit as much as they like, given they dont bust
        for i in range(6):
            MyHand= np.append(MyHand,hit())
            total1 = newscore(MyHand)
            total1 = HasAnAce(MyHand,total1)
            print(MyHand)
            print("You have",total1)
            didyouwin(total1,MyHand)
            if total1>21 or y ==("stand"):
                break
    if y ==("stand"):                                                      #once the user is done hitting, the dealer will run its course until a win/bust/push occurs
        dealerhits(dealer,dealertotal)
if x == ("double"):                                                        #allows for a double where the player gets one card.... 
    MyHand = np.append(MyHand,hit())                                       #and then the dealer begins drawing
    print(MyHand)
    total1 = newscore(MyHand)
    total1 = HasAnAce(MyHand,total1)
    Blackjack(total1)
    print("you have",total1)
    dealerhits(dealer,dealertotal)
    




    


    
