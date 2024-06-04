import win32com.client as wc

speaker = wc.Dispatch("SAPI.SpVoice")

speaker.Speak("hello")

def main():
 while 1:
  s = input("Enter the word you want to speak it out by computer: ")
  speaker.Speak(s)

if __name__ == '__main__':
	main()
# To stop the program press
# ctrl + c

# print(help(wc))