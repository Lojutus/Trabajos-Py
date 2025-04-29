import openai
import speech_recognition as sr
import pyttsx3, pywhatkit 
import time 


# Initialize OpenAI API
openai.api_key = "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"
# Initialize the text to speech engine 
engine=pyttsx3.init()
name = "hola"


#Generar respuesta de chat gpt
def generate_response(prompt):
    response= openai.Completion.create(
        engine = "gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    print(response)
    return response ["choices"][0]["text"]

# Set Spanish voice for text-to-speech engine
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
spanish_voice = None

def speak_text(text):
    engine.say(text)
    engine.runAndWait()
def escuchar():
    recognizer=sr.Recognizer()
    transcription = ''
    try:
        with sr.Microphone() as source:
            
            print("Escuchando")
            
            
            audio=recognizer.listen(source,phrase_time_limit=5,)
            transcription = recognizer.recognize_google(audio, language="es")
            transcription = transcription.lower()
            print("Transcripcion completa")
            if name in transcription:
                print(transcription , ": Que quieres ")
                transcription=transcription.replace(name, '')
                print(transcription , ": 2")
               
    except:
         pass 
    return transcription 

def main():
    while True:
        try:
            
            transcripcion = escuchar()
            escuchar()
            print("///////////////////////")
            if 'reproduce' in transcripcion:
                music = transcripcion.replace('reproduce', '')
                print('Reproduciendo' + music)
                speak_text("Reoroduciendo" + music)
                pywhatkit.playonyt(music)
            if 'respóndeme'  in transcripcion:
            #Generate the response

                responder = transcripcion.replace('respóndeme','')
                response = generate_response(responder)
                print(response, "Ahi está")
                speak_text(response)
        except Exception as e:
            print("Ahhhhhh erroor : ".format(e) )
           
if __name__=="__main__":
    main()
        
"""def main():
    while True:
        #Waith for user say "genius"
        print("Di 'Hola' para empezar a grabar")
       
               
                    #record audio
                    filename ="input.wav"
                    print("Dime que quieres mozo")
                    with sr.Microphone() as source:
                        recognizer=sr.Recognizer()
                        source.pause_threshold=1
                        audio=recognizer.listen(source,phrase_time_limit=None,timeout=None)
                        with open(filename,"wb")as f:
                            f.write(audio.get_wav_data())
                    #transcript audio to test 
                    text=transcribe_audio_to_test(filename)
                    if text:
                        print(f"Yo {text}")
                        
                        #Generate the response
                        response = generate_response(text)
                        print(f"El bot ese dice: {response}")
                            
                        #read resopnse using GPT3
                        speak_text(response)"""
            
