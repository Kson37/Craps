from dice import Die
die = Die(6)
rolls = die.roll(2)

bet = 0
roundcont = 0
temp = 0
Totalgold = 100
print("Welcome to Craps you start with 100$.")
while True:
  choice = int(input("Would you like to bet on 1-Pass or 2-Don't Pass 3-Quit?\n"))
  if(choice == 1):
    bet = int(input("How much would you like to bet on pass?\n"))
    if(bet):
      total = sum(rolls)
      Totalgold = Totalgold - bet
      print("Money left",Totalgold,"\nYour roll",total)
      if(total == 7 or total == 11):
        print("Shooter has won")
        Totalgold += bet*2
        print(Totalgold)
      else:
        Point = total
        print(Point,"is your Point.")
        fourbet = int(input("What would you like to bet on 4?\n"))
      if(fourbet):
        Totalgold = Totalgold - fourbet
        print("Money left", Totalgold)
      fivebet = int(input("What would you like to bet on 5?\n"))
      if(fivebet):
        Totalgold = Totalgold - fivebet
        print("Money left", Totalgold)
      sixbet = int(input("What would you like to bet on 6?\n"))
      if(sixbet):
        Totalgold = Totalgold - sixbet
        print("Money left", Totalgold)
      eightbet = int(input("What would you like to bet on 8?\n"))
      if(eightbet):
        Totalgold = Totalgold - eightbet
        print("Money left", Totalgold)
      ninebet = int(input("What would you like to bet on 9?\n"))
      if(ninebet):
        Totalgold - Totalgold - ninebet
        print("Money left", Totalgold)
      tenbet = int(input("What would you like to bet on 10?\n"))
      if(tenbet>=0):
        Totalgold = Totalgold - tenbet
        print("Money left", Totalgold)
         #end of getting bets
        while True:
          total = sum(die.roll(2))
          if(total == Point):
            Totalgold += bet*2
          elif(total == 7):
            print("Hey you rolled a seven",total)
            break
          else:
            print("Your Roll",total)
            if(total == 4):
              Totalgold = Totalgold + fourbet
              print(Totalgold)
            elif(total == 5):
              Totalgold = Totalgold + fivebet
              print(Totalgold)
            elif(total == 6):
              Totalgold = Totalgold + sixbet
              print(Totalgold)
            elif(total == 8):
              Totalgold = Totalgold + eightbet
              print(Totalgold)
            elif(total == 9):
              Totalgold = Totalgold + ninebet
              print(Totalgold)
            elif(total == 10):
              Totalgold = Totalgold + tenbet
              print(Totalgold)
            else:
              print(Totalgold)
          roundcont = int(input("Roll Again? 1-yes 2-no\n"))
          if(roundcont ==2):
            print("\nYour total amount is",Totalgold)
            
        #end of pass
  elif(choice == 2):
    bet = int(input("How much would you like to bet on don't pass?"))
    if(bet):
      Totalgold = Totalgold - bet
      print(Totalgold)
      if(int(total == 2))or(int(total == 3)):
        print("Shooter has won",Totalgold)
        Totalgold += bet*2
        print(Totalgold)
      elif(int(total == 12)):
        Totalgold += bet
        print("Tie game", Totalgold)
      else:
        Point = total
        print(Point,"is your Point.")
        fourbet = int(input("What would you like to bet on 4?\n"))
      if(fourbet):
        Totalgold = Totalgold - fourbet
        print("Money left", Totalgold)
      fivebet = int(input("What would you like to bet on 5?\n"))
      if(fivebet):
        Totalgold = Totalgold - fivebet
        print("Money left", Totalgold)
      sixbet = int(input("What would you like to bet on 6?\n"))
      if(sixbet):
        Totalgold = Totalgold - sixbet
        print("Money left", Totalgold)
      eightbet = int(input("What would you like to bet on 8?\n"))
      if(eightbet):
        Totalgold = Totalgold - eightbet
        print("Money left", Totalgold)
      ninebet = int(input("What would you like to bet on 9?\n"))
      if(ninebet):
        Totalgold - Totalgold - ninebet
        print("Money left", Totalgold)
      tenbet = int(input("What would you like to bet on 10?\n"))
      if(tenbet>=0):
        Totalgold = Totalgold - tenbet
        print("Money left", Totalgold)
        
         #end of getting bets
        while True:
          total = sum(die.roll(2))
          if(total == Point):
            print("You rolled your point you lose")
            break
          elif(total == 7):
            print("Hey you rolled a seven you win",total)
            break
          else:
            print("Your Roll",total)
            if(total == 4):
              Totalgold = Totalgold + fourbet
              print(Totalgold)
            elif(total == 5):
              Totalgold = Totalgold + fivebet
              print(Totalgold)
            elif(total == 6):
              Totalgold = Totalgold + sixbet
              print(Totalgold)
            elif(total == 8):
              Totalgold = Totalgold + eightbet
              print(Totalgold)
            elif(total == 9):
              Totalgold = Totalgold + ninebet
              print(Totalgold)
            elif(total == 10):
              Totalgold = Totalgold + tenbet
              print(Totalgold)
            else:
              print(Totalgold)
          roundcont = int(input("Roll Again? 1-yes 2-no\n"))
          if(roundcont ==2):
            print("Your total amount is",Totalgold)
            
    #end of dont pass
    
  
  elif(choice == 3):
    print("Thanks for playing! Here are your winnings.\n",Totalgold)
    exit(0)
    #quit