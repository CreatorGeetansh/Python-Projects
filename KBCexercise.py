print('''                                                                 KBC game me aapka swagat hai..
                                                                    taliyan bajti rehni chahiye

                                                                    CHALIYE GAME SHURU KRTE HAI.''')

print('''              RULES ---                            This game contains three questions 1st question contains 10000 points
                                                       2nd questions contains 20000 points and 3rd ques contains 70000 points..
                                                       If you wish to quit this game type quit in enter answer section and you will
                                                       loose no money..YOU WILL LOOSE 10000 POINTS ON EVERY WRONG ANSWER this is a 
                                                       fun game and fast forward game it will show you next question after every  
                                                       correct answer.. All right guys s lest get started with our game''')

import time as ti

import win32com.client as wc
speak = wc.Dispatch("SAPI.SPVoice")

print("type 1 to start this wonderfull game")
b = int(input("Enter: "))

a = ["What is the full form of ISRO?","what is full form of AI?","what is this language called..?"]

x =["International space research organisation","International spray ratio organisation","Indian space research organisation","Indian sprite reverse osmosis"]

y = ["Artificial Insaan", "Artificial Intelligence", "Aalsi Insaan", "Aalsi Intelligence"]

z = ["C++", "Jawa script", "HTML", "Python"]

win_price = 0
match b:
    case 1:
        print("Yeh raha question aapki computer screen per..")
        speak.Speak("Yeh raha question aapki computer screen per..")
        print("\n")
        print("\n")
        speak.Speak("pehla question 10,000 points ke liy ae")
        print("pehla question 10,000 points ke liye")
        print("\n")
        print("\n")
        ti.sleep(2)
        print((a[0]).center(450))
        speak.Speak(a[0])
        print("\n")
        print("\n")
        print("ab bari hai options ki... to yeh rahe options aapke computer screen per:")
        speak.Speak("ab bari hai options ki... to yeh rahe options aapke computer screen per:")
        print("\n")
        print("\n")
        ti.sleep(2)
        print(''' A)International space research organisation                              B) International spray ratio organisation
        C)Indian space research organisation                                       D)Indian sprite reverse osmosis''')
        speak.Speak(f"option A.. {x[0]}..   option b..  {x[1]}.. option .. c  {x[2]} and option d is....  {x[3]}")
        h = input("Enter answer: ")
        if(h == "c" or h == "C"):
            print("\n")
            print("\n")
            print('''                                                            Sahi Jawab!... bht aache bhaishab..taliyan''')
            speak.speak("Sahi Jawab!... nice job!")
            win_price = win_price + 10000
            print('''                                                                                                                        winning amount:''',win_price)

        elif(h == "quit"):
            print('''                         WIN amount is 0''')
            exit
            

        else:
            print('''                                                            Ye galat jawab hai.... dhumtana dhumtana''')
            speak.speakt("Yeh galat jawab hai.... dhumtana dhumtana")
            print("\n")
            print('''                                                                          you lost!''')
            speak.speak("you lost!")
            print("\n")
            print('''                                                         aaj aap yaha se dhanrashi lekr ja rhe h!''',win_price-10000)
            exit
        
        if (win_price == 10000):
          ti.sleep(2)
          print('''                                  NEXT QUESTION IS RIGHT BELOW''')
          speak.speak('''                                  NEXT QUESTION IS RIGHT BELOW''')
          print("Yeh raha question aapki computer screen per..")
          speak.speak("Yeh raha question aapki computer screen per..")
          print("\n")
          print("\n")
          print("dusra question 20,000 points ke liye")
          speak.speak("dusra question 20,000 points ke liye")
          print("\n")
          print("\n")
          ti.sleep(2)
          print((a[1]).center(450))
          speak.speak((a[1]))
          print("\n")
          print("\n")
          print("ab bari hai options ki... to yeh rahe options aapke computer screen per:")
          speak.speak("ab bari hai options ki... to yeh rahe options aapke computer screen per:")
          print("\n")
          print("\n")
          ti.sleep(2)
          print(''' A)Artificial Insaan                              B)Artificial Intelligence
        C)Aalsi Insaan                                      D)Aalsi Intelligence''')
          speak.Speak(f"option A.. {y[0]}..   option b..  {y[1]}.. option .. c  {y[2]} and option d is....  {y[3]}")
          h = input("Enter answer: ")
          if(h == "b" or h == "B"):
            print("\n")
            print("\n")
            print('''                                                            Sahi Jawab!... bht aache bhaishab..taliyan''')
            speak.speak("Sahi Jawab!...Nice job!")
            win_price = win_price + 20000
            print('''                                                                                                                        winning amount:''',win_price)

          elif(h == "quit"):
            print('''                         WIN amount is:''',win_price)
            exit

          else:
            print('''                                                            Ye galat jawab hai.... dhumtana dhumtana''')
            speak.speak("Yeh galat jawab hai.... dhumtana dhumtana")
            print("\n")
            speak.speak("you lost!")
            print("\n")
            print('''                                                         aaj aap yaha se dhanrashi lekr ja rhe h:''',win_price-10000)
            exit
    
        if (win_price == 30000):
          ti.sleep(2)
          print("Yeh raha question aapki computer screen per..")
          speak.speak("Yeh raha question aapki computer screen per..")
          print("\n")
          print("\n")
          print("third question 70,000 points ke liye")
          speak.speak("third question 70,000 points ke liy ae")
          print("\n")
          print("\n")
          ti.sleep(2)
          print((a[2]).center(450))
          speak.speak((a[2]))
          print("\n")
          print("\n")
          print("ab bari hai options ki... to yeh rahe options aapke computer screen per:")
          speak.speak("ab bari hai options ki... to yeh rahe options aapke computer screen per:")
          print("\n")
          print("\n")
          ti.sleep(2)
          print(''' A)C++                              B)Jawa script
        C)HTML                                      D)Python''')
          speak.Speak(f"option A {z[0]}..   option b..  {z[1]}.. option .. c  {z[2]} and option d is....  {z[3]}")
          h = input("Enter answer: ")
          if(h == "d" or h == "D"):
            print("\n")
            print("\n")
            print('''                                                            Sahi Jawab!... bht aache bhaishab..taliyan''')
            speak.Speak("Sahi Jawab!...Nice job!")
            win_price = win_price + 70000
            print('''                                                                                                                        winning amount:''',win_price)

          elif(h == "quit"):
            print('''                         WIN amount is:''',win_price)
            exit

          else:
            print('''                                                            Ye galat jawab hai.... dhumtana dhumtana''')
            speak.Speak("Yeh galat jawab hai.... dhumtana dhumtana")
            print("\n")
            print('''                                                                          you lost!''')
            speak.Speak("you lost!")
            print("\n")
            print('''                                                         aaj aap yaha se dhanrashi lekr ja rhe h:''',win_price-10000)
            exit
        print("\n")
        print("\n")
        print("\n")
        print('''            THANKYOU FOR PLAYING MY KBC GAME HOPE SO YOU ENJOYED IT..
                        THANKYOU AGAIN. ''')
        speak.speak("THANKYOU FOR PLAYING MY KBC GAME HOPE SO YOU ENJOYED IT..THANKYOU AGAIN. ")
#completed my KBC game successfully