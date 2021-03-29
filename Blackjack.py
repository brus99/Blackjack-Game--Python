import numpy as np
f =np.array(["As","Ah","Ad","Ac","2s","2h","2c","2d","3s","3h","3d","3c","4s","4d","4c","4h","5h","5d","5s","5c","6h","6d","6c","6s","7s","7d","7c","7h","8h","8d","8c","8s","9s","9d","9c","9h","Th","Td","Tc","Ts","Js","Jd","Jh","Jc","Qs","Qd","Qh","Qc","Ks","Kc","Kd","Kh"])
scores = {"As":11,"Ah":11,"Ad":11,"Ac":11,"2s":2,"2h":2,"2c":2,"2d":2,"3s":3,"3h":3,"3d":3,"3c":3,"4s":4,"4d":4,"4c":4,"4h":4,"5h":5,"5d":5,"5s":5,"5c":5,"6h":6,"6d":6,"6c":6,"6s":6,"7s":7,"7d":7,"7c":7,"7h":7,"8h":8,"8d":8,"8c":8,"8s":8,"9s":9,"9d":9,"9c":9,"9h":9,"Th":10,"Td":10,"Tc":10,"Ts":10,"Js":10,"Jd":10,"Jh":10,"Jc":10,"Qs":10,"Qd":10,"Qh":10,"Qc":10,"Ks":10,"Kc":10,"Kd":10,"Kh":10}
def hit():
    global f
    MyHand2 = np.random.choice(f,1,replace=False)
    f = np.delete(f,np.where(f==MyHand2[0]))
    return MyHand2
def newscore(hand):
    count = 0
    for card in hand:
        count+= scores[card]
    return count
def didyouwin(hand):
    global y
    total = 0
    for card in hand:
        total+= scores[card]
    if total>21:
        print("You bust")
    elif total<=21:
        y= input("again or stand?")    
def dealerhits():
    global dealer
    for i in range(5):
        dealer = np.append(dealer,hit())
        dealertotal = newscore(dealer)
        print("dealer has",dealertotal)
        if dealertotal>21:
            print("dealer busts, you win")
            break
        elif dealertotal>total:
            print("the dealer has,",dealertotal,",you have,",total,"you lose")
            break
        elif dealertotal<total and dealertotal>=17:
            print("the dealer has",dealertotal,"you have",total,"you win")
            break
        elif dealertotal==total and dealertotal>=17:
            print("push")
            break  
dealer = np.random.choice(f,1,replace=False)
f = np.delete(f,np.where(f==dealer[0]))
print("the dealer has",dealer)
MyHand = np.random.choice(f,1,replace=False)
f = np.delete(f,np.where(f==MyHand[0]))
print("You have",MyHand)
x = input("Do you hit or double?")
if x == ("hit"):
    MyHand = np.append(MyHand,hit())
    print(MyHand)
    total = newscore(MyHand)
    print(total)
    didyouwin(MyHand)
    if y == ("again"):
        for i in range(3):
            MyHand= np.append(MyHand,hit())
            total = newscore(MyHand)
            print("You have",total)
            didyouwin(MyHand)
            if total>21 or y ==("stand"):
                break
    if y ==("stand"):
        dealerhits()
if x == ("double"):
    MyHand = np.append(MyHand,hit())
    print(MyHand)
    total = newscore(MyHand)
    print("you have",total)
    dealerhits()




    


    
