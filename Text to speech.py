import pyttsx3


def welcome(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def txt_speech(word):
    engine=pyttsx3.init()
    engine.say(word)
    engine.runAndWait()


def main():
    text="What do you want me to say??"
    welcome(text) 

    word=input("What do you want me to say??\n")
    txt_speech(word)
    

if __name__=='__main__':
    main()