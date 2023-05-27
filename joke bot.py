import random
from colorama import Fore, Style


knock_jokes_dic={"joke1":"Knock, knock. \nWho’s there?\nBoo.\nBoo who?\nDon't cry, it's just a joke."
      , "joke2":"Knock, knock.\nWho’s there?\nLettuce.\nLettuce who?\nLettuce in, it's cold out here!" 
      , "joke3":"Knock, knock.\nWho’s there?\nOrange.\nOrange who?\nOrange you going to answer the door?" 
      ,"joke4":"Knock, knock.\nWho’s there?\nTank.\nTank who?\nYou're welcome!"}
knock_jokes_list=list(knock_jokes_dic.values())
#print (knock_jokes_dic["joke1"])
dad_jokes_dic={"joke1":"Did you hear about the restaurant on the moon? Great food, no atmosphere." 
      , "joke2":"I'm reading a book on anti-gravity. It's impossible to put down!" 
      , "joke3":"What do you call a fake noodle? An impasta."
      , "joke4":"Why don't skeletons fight each other? They don't have the guts."}
dad_jokes_list=list(dad_jokes_dic.values())
programming_jokes_dic={"joke1":"Why do programmers prefer dark mode? Because light attracts bugs."
           , "joke2":"Why did the programmer quit his job? He didn't get arrays."
           , "joke3":"There are 10 types of people in the world: those who understand binary, and those who don't."
           ,"joke4":"Why did the JavaScript developer wear glasses? Because he couldn't C#."}
programming_jokes_list=list(programming_jokes_dic.values())

name=input("Hello, Welcome to the joke bot! Please type in your name: " )

def joke_bot():
  category=input(f"""
                     Dear {name}, Please choose a joke category.
                     You can choose between three categories:
                     For knock-knock jokes, type 'knock knock' 
                     For dad jokes, type 'dad'
                     For programming jokes, type 'programming' """)
  if category=="knock knock":
    if len(knock_jokes_list)>0:
      a=random.choice(knock_jokes_list)
      knock_jokes_list.remove(a)
      print (Fore.GREEN + f"\n{a}\n" + Style.RESET_ALL)
    else:
      print ("\nSorry, we have no more knock knock jokes left ):\n")

  elif category=="dad":
    if len(dad_jokes_list)>0:
      b=random.choice(dad_jokes_list)
      dad_jokes_list.remove(b)
      print (Fore.BLUE + f"\n{b}\n" + Style.RESET_ALL)

    else:
      print ("\nSorry, we have no more dad jokes left ):\n")

  elif category=="programming":
    if len(programming_jokes_list)>0:
      c=random.choice(programming_jokes_list)
      programming_jokes_list.remove(c)
      print (Fore.RED + f"\n{c}\n" + Style.RESET_ALL)

    else:
      print ("\nSorry, we have no more programming jokes left ):\n")

  else:
    print ("\nPlease only choose between 'knock knock', 'dad' or 'programming', otherwise we can't move forward :)")
    joke_bot()

  again=input("""
              Would you like another joke? Then type 'yes'
              If you had enough laughs for today, type 'done'
              """)
  if again=='yes':
    return joke_bot()
  elif again=='done':
    print ("\nThank you for using the joke bot!")
  else:
    print ("\nPlease type either 'yes' or 'done'\n")
    return again()

joke_bot()
