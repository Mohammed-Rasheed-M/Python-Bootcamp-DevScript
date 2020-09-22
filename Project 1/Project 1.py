print("\t\tWELCOME")
repeat ="y"
while repeat == "y":

  print("Choose your horoscope to know about your day\n")
  print('''
  \t 1. Aquarius
  \t 2. Pisces
  \t 3. Aries
  \t 4. Tauras
  \t 5. Gemini
  \t 6. Cancer
  \t 7. Leo
  \t 8. Virgo
  \t 9. Libra
  \t10. Scorpio
  \t11. Sagittarius
  \t12. Capricorn  
  ''')
  s = int(input("What is your horoscope?\n"))

  if s == 1:
    print("\nYet again money is the most important factor in your chart, and it will take little to make you explode with frustration, perhaps over others’ incompetence. However, the underlying question may be irritation at the way you personally have been undervalued.")
  elif s == 2:
    print("\nToday’s lunar alignments signify sharp changes in your mood. Early uncertainty may be replaced by burgeoning confidence, and that has to be good news. You’re on a slow fuse and it could be a question of lighting the blue touch paper and then retiring to a safe distance.")
  elif s == 3:
    print("\nWhy are you so secretive? Because you have good reason is the only realistic answer. It may be that other people are just not ready to hear what you have to say. Perhaps they haven’t enough sensitivity to give you a fair hearing. Leave it a couple of days if you wish.")
  elif s == 4:
    print("\nSocial pressures are powerful, and could prove distracting, but the underlying issue in your chart concerns your long-term hopes and wishes. It’s a useful moment for summoning up all your reserves of determination, and for setting out your stall for the future.")
  elif s == 5:
    print("\nThere is a time for everything, and now is the moment to compete. Professional types should spare no effort in aiming for the top, which means changing their attitude to a number of colleagues. All of you, whether you’re at work or not, should now make a bid for recognition and acclaim.")
  elif s == 6:
    print("\nThe areas of your life which stand to benefit most, at least in the long run, include higher education, legal questions, moral issues and overseas connections. It’s important to keep an eye on matters of principle, and always to hold the ethical high ground.")
  elif s == 7:
    print("\nYour own ideas are good, but perhaps not good enough. Do take great care with joint finances, especially if you’re spending other people’s money. Indeed, it may be sensible to follow the most cautious path possible and put everything on hold for a few days.")
  elif s == 8:
    print("\nLook, listen and learn is the best planetary advice. The Moon’s challenge to your sign is a powerful call for mature and considered responses, rather than hasty reactions based on past experience. Besides, if you do try to go it alone, a partner may stand in your way.")
  elif s == 9:
    print("\nTread carefully at work. This is an appropriate moment for beginning a new job, but, by the same token, you could also be giving up old responsibilities. It’s important to see that events work out in your favour. Also, bear in mind that what really interests you is helping others out of a tight spot.")
  elif s == 10:
    print("\nThe planets are urging you to give in to your desires. Whether you do or not depends on what they are and, of course, your circumstances. You should pay all necessary attention to children, listen carefully to younger relations and cultivate your creative powers.")  
  elif s == 11:
    print("\nThere seems to be an inexorable pressure for change at home. Whether this comes to fruition or not depends on you, for you will have to take current developments and carry them that extra mile. You might be owed an apology, by the way, but it may be slow in coming.")
  elif s == 12:
    print("\nYou are about to take a step backwards in at least one major ambition. The precise implications are unclear, but it could be that you are soon to rediscover the significance of something which you had previously given up, perhaps because you lost your confidence.")
  else:
    print("\nWrong horoscope. Try again.")

  repeat=input("\nDo you want to try again ? (y/n)\n")
  
print("\n\t\tTHANK YOU")
