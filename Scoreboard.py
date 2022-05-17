import random as r

team1=input("Enter the name of Team 1: ")
team2=input("Enter the name of Team 2: ")
team_list=[team1,team2]
random_team=r.choice(team_list)
team_list.remove(random_team)
print("The winner of the toss is: ", random_team)

over=int(input("Enter the number of overs to be played: "))
over_count=0
dict_team1={}
dict_team2={}

wickets=0
totalruns=0
print('-'*20,random_team,'-'*20)
striker=input("Enter the name of Striker: ")
non_striker=input("Enter the name of Non-Striker: ")
batsman=[striker,non_striker]
reun=0
for i in range(over):
    j=0
    run=0
    extra=0
    totala=int(run)+int(extra)
    b=input("Enter the name of Bowler: ")
    while j<6:
        ballrun=input("Enter the runs scored on ball "+str(j+1)+" : ")
        if str(ballrun)=='0':
            run+=0
            j+=1
            totala+=int(ballrun)
        elif str(ballrun)=='1':
            run+=1
            j+=1
            totala+=int(ballrun)
        elif str(ballrun)=='2':
            run+=2
            j+=1
            totala+=int(ballrun)
        elif str(ballrun)=='3':
            run+=3
            j+=1
            totala+=int(ballrun)
        elif str(ballrun)=='4':
            run+=4
            j+=1
            totala+=int(ballrun)
        elif str(ballrun)=='5':
            run+=5
            j+=1
            totala+=int(ballrun)
        elif str(ballrun)=='6':
            run+=6
            j+=1
            totala+=int(ballrun)
        elif str(ballrun)=='wide':
            extra+=1
            j+=0
        elif str(ballrun)=='no ball':
            reun=int(input("Enter runs scored in free hit: "))
            extra+=1
            tt=int(reun)+int(extra)
            totala+=tt
            j+=1
        elif str(ballrun)=='out':
            random_bat=r.choice(batsman)
            wickets+=1
            j+=1
            dict_team1[random_bat]=int(run)+int(extra)
            new_bat=input("Enter the name of new batsman: ")
            batindex=batsman.index(random_bat)
            batsman[batindex]=new_bat
        elif int(ballrun)>6:
            print("Not in range")
            j+=0

    over_count+=1
    totala=int(run)+int(extra)
    totalruns+=totala
    print('-'*60)
    print("\t\t",team1,"VS",team2)
    print("\t\t\t",random_team)
    print("Runs scored:\t",run+reun,"\t\tExtras:\t",extra)
    print("Over Number: ",over_count)
    print("Total Runs Scored:\t",totalruns,"\t\tWickets Lost:\t",wickets)
    if wickets>0:
        print("Players : Total Runs at which wicket lost")
    for name in dict_team1:
        print(name, ":",dict_team1[name])
    print("-"*60)
first="FIRST INNING ENDS"
nfirst=first.center(24,'*')
print(first)
print("Target: ",totalruns)


batsman=[striker,non_striker]
print('-'*20,team_list[0],'-'*20)
striker=input("Enter the name of Striker: ")
non_striker=input("Enter the name of Non-Striker: ")
wickets=0
totalruns1=0
riun=0
over_count=0
for i in range(over):
    j=0
    run=0
    extra=0
    totalb=int(run)+int(extra)
    b=input("Enter the name of Bowler: ")
    while j<6:
        ballrun=input("Enter the runs scored on ball "+str(j+1)+" : ")
        if int(totalruns1)+int(totalb)+int(ballrun)>int(totalruns):
            break
        else:
            if str(ballrun)=='1':
                run+=1
                j+=1
                totalb+=int(ballrun)
            elif str(ballrun)=='2':
                run+=2
                j+=1
                totalb+=int(ballrun)
            elif str(ballrun)=='3':
                run+=3
                j+=1
                totalb+=int(ballrun)
            elif str(ballrun)=='4':
                run+=4
                j+=1
                totalb+=int(ballrun)
            elif str(ballrun)=='5':
                run+=5
                j+=1
                totalb+=int(ballrun)
            elif str(ballrun)=='6':
                run+=6
                j+=1
                totalb+=int(ballrun)
            elif str(ballrun)=='wide':
                extra+=1
                j+=0
            elif str(ballrun)=='no ball':
                extra+=1
                riun=int(input("Enter runs scored in free hit: "))
                tae=int(riun)+int(extra)
                totalb+=tae
                j+=1
            elif str(ballrun)=='out':
                random_bat=r.choice(batsman)
                wickets+=1
                j+=1
                dict_team1[random_bat]=int(run)+int(extra)
                new_bat=input("Enter the name of new batsman: ")
                batindex=batsman.index(random_bat)
                batsman[batindex]=new_bat
            elif int(ballrun)>6:
                print("Not in range")
                j+=0
            
    over_count+=1
    totalb=int(run)+int(extra)
    totalruns1+=totalb
    print('-'*60)
    print("\t\t",random_team,"VS",team_list[0])
    print("\t\t\t",team_list[0])
    print("Runs scored:\t",run,"\t\tExtras:\t",extra)
    print("Over Number: ",over_count)
    print("Total Runs Scored:\t",totalruns1,"\t\tWickets Lost:\t",wickets)
    if wickets>0:
        print("Players : Total Runs at which wicket lost")
    for name in dict_team2:
        print(name, ":",dict_team2[name])
    print("-"*60)
    
if int(totalruns)>int(totalruns1):
    print(team_list[0],"won by",int(totalruns)-int(totalruns1),"runs.")
elif int(totalruns)==int(totalruns1):
    print("DRAW. WORK UNDER PROGRESS IN SUPER OVER")
else:
    print(random_team,"won by",10-wickets,"wickets.")
