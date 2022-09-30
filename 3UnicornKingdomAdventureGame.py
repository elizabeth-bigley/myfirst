# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:54:39 2022

@author: eliza
"""

print('''
 *
  *
   *     **
    *   ******
     ************                                        ****
      *** **********                                   ********
     ****************                                 *****  ****
    ********************                             ****    ****
    *******  ******************             ******   ***     ***
     *****    ****************************************        *
               *****************************************
                ***************************************
                **************************************
                 ********************     ***********
             ***********                  *********
         *******                          ********
        ***                                ******
       **                                     ****
      **                                       ***
     ***                                     ****
''')
print("Welcome to the Unicorn Kingdom!")
print("Your mission is to save the unicorns.") 


#Write your code below this line 👇
print("The unicorn queen has sent out a desperate plea. The unicorns are losing their magic! \nA new evil force has entered the kingdom, and it seeks to destroy everything good. It hates the beauty and goodness of the unicorns.")
willhelp = str(input("Will you answer the call of the unicorn queen? Will you come help the unicorns? \nPlease type Y or N: "))
willhelp.lower()
if willhelp == 'y':
  print("\nYou have chosen to help the unicorns. The queen will be forever grateful! You must leave immediately. The queen is sending you with her most trusted companion and guard, Lofting. He will help you along the way.")
  destination = str(input("Where will you go to seek the evil? Will you go to Pegasus Forest, or to the Plains of Magic? \nPlease type 'forest' or 'plains'. "))
  destination.lower()
  if destination == 'plains':
    print("\nYou and Lofting gallop quickly away towards the Plains of Magic, wasting little time.")
    investigate = str(input("Before long, you find a fresh campsite. Do you choose to look around, or move along? \nPlease type 'look' or 'move'. "))
    investigate.lower()
    if investigate == 'look':
      print("While looking around the campsite, you find an evil witch, desperate to destroy the beautiful race of unicorns. \nYou and Lofting caught her by surprise, and captured her without incident. You take the prisoner back to the unicorn queen. \nYou have saved the unicorn kingdom! \n\nCongratulations!")
    else:
      print("\nYou passed by an evil witch, intent on the destruction of the unicorns, giving her enough time to destroy you. You have failed. \nYou and your quest have met an untimely end.\nGame over.")
  else:
    print("\nYou would have found the great evil on the Plains of Magic! \nGame over.")
else:
  print("\nThe unicorns will certainly perish! \nGame over. ")
input("Press <enter> to exit.")