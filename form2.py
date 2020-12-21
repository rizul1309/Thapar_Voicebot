from flask import Flask, render_template, request, jsonify, Response,flash
import requests
import speech_recognition as sr     # import the library
import subprocess
from gtts import gTTS
from playsound import playsound
import os
import random


app=Flask(__name__)
output=[]#("message stark","hi")]
@app.route('/')
def home_page():
    return render_template("IY_Home_page.html",result=output)

@app.route('/result',methods=["POST","GET"])
def Result():
    if request.method=="POST":
        print(list(request.form.values()))
        result=list(request.form.values())[0]
        if result.lower()=="restart" or result.lower()=="cls":
            output.clear()
        elif result.lower()=="voice":
            r = sr.Recognizer()  # initialize recognizer
            with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
                print("Speak Anything :")
                audio = r.listen(source)  # listen to the source
                try:
                    message = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
                    print("You said : {}".format(message))

                except:
                    print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
            
            print("Sending message now...")

            r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

            print("Bot says, ",end=' ')
            
            for j in r.json():
                bot_message = j['text']
                print(f"{bot_message}")
            bot_message4="Bot says "+bot_message
            myobj = gTTS(text=bot_message4)
            num1 = random.randint(0, 1000)
            file = str(str(num1)+".mp3")
            myobj.save(file)
            output.extend([("message parker",message),("message stark",bot_message)])
            if message.lower()=="restart" or message.lower()=="cls":
                output.clear()
            print('saved')
            # Playing the converted filewelcome.mp3
            playsound(file)
            os.remove(file)

        else:
            try:
                r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": result})
                print("Bot says, ")
                for i in r.json():
                    bot_message = i['text']
                    print(f"{i['text']}")
                output.extend([("message parker",result),("message stark",bot_message)])
                myobj = gTTS(text=bot_message)
                num1 = random.randint(0, 1000)
                file = str(str(num1)+".mp3")
                myobj.save(file)

                print('saved')
                # Playing the converted filewelcome.mp3
                playsound(file)
                os.remove(file)
                
            except:
                output.extend([("message parker", result), ("message stark", "We are unable to process your request at the moment. Please try again...")])
                bot_message2="Try again later"
                myobj = gTTS(text=bot_message2)
                num1 = random.randint(0, 1000)
                file = str(str(num1)+".mp3")
                myobj.save(file)

                print('saved')
                # Playing the converted filewelcome.mp3
                playsound(file)
                os.remove(file)
        print(output)
        return render_template("IY_Home_page.html",result=output)

if __name__=="__main__":
    app.run(debug=True)#,host="192.168.43.161")
