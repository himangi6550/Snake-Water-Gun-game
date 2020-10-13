print("WELCOME TO THE SNAKE WATER GUN GAME\n\n")

m=0
fc_pts=0
fu_pts=0
c_pts=0
u_pts=0
def play(j,m,fc_pts,fu_pts):
    global c_pts
    global u_pts
    c_pts=0
    u_pts=0
    print("Instruction: \nEnter s for snake, w for water, g for gun\n")
    import random
    lst=["s","w","g"]
    n=int(input("How many chances do you want to play: "))
    m=m+n
    i=1
    
    
    def c_points():
        global c_pts
        c_pts=c_pts+1
        
    def u_points():
        global u_pts
        u_pts=u_pts+1
        
    while i<=n:
        c=random.choice(lst)
        u=input("\nChoose between s, w, g: ")
        if c==u:
            print("Tie. Try again.\n")
        else:
            if c=="s" and u=="w":
                c_points()
                print("Computer wins this turn\n") 
            elif c=="s" and u=="g":
                u_points()
                print("You win this turn\n") 
            elif c=="w" and u=="s":
                u_points()
                print("You win this turn\n") 
            elif c=="w" and u=="g":
                c_points()
                print("Computer wins this turn\n") 
            elif c=="g" and u=="s":
                c_points()
                print("Computer wins this turn\n") 
            elif c=="g" and u=="w":
                u_points()
                print("You win this turn\n")
            else:
                print("You entered the wrong key. Try again\n")
                i=i-1
        i=i+1
    fc_pts=fc_pts+c_pts
    fu_pts=fu_pts+u_pts
    if c_pts>u_pts:
        print("Computer wins with",c_pts,"points\n")
    elif u_pts>c_pts:
        print("You won with",u_pts,"points\n")
    else:
        print("Tie.")
       
    print("Total score of both the teams: \nComputer: ",c_pts,"\nYour: ",u_pts,"\n")
    ag=input("Do you want to play again? [Y/N]: ")
    if ag=="Y" or ag=="y":
        j=j+1
        play(j,m,fc_pts,fu_pts)
    elif ag=="N" or ag=="n":
        f=input("Do you want to see the final score? [Y/N]: ")
        if f=="Y" or f=="y":
            print("You played",j,"times\nTotal chances:",m,"\nYour score:",fu_pts,"\nComputer's score:",fc_pts)
        print("Game ended")
       


def answer():
    global ans
    ans=input("Do you want to play the game? [(Y)/(N)]: ")
    if ans=="Y" or ans=="y":
        j=1
        m=0
        fc_pts=0
        fu_pts=0
        play(j,m,fc_pts,fu_pts)
    elif ans=="N" or ans=="n":
        print("Game ended")
    else:
        print("Wrong input. Try again.\n")
        answer()
answer() 


                
            
        
