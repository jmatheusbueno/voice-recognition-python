import speech_recognition as sr
import time as tm

r = sr.Recognizer()
with sr.Microphone() as font:

    print('Hello, how can I help you?')
    useraudio = 'Empty';
    while useraudio != 'Não':
        tm.sleep(2)
        audio = r.listen(font)

        try:
            text = r.recognize_google(audio, language='pt-BR')
            useraudio = text.capitalize()
            if(useraudio == 'Sair' or useraudio == 'Não'):
                print('You: ' + useraudio)
                tm.sleep(1)
                print('\nOk im leaving now.\n')
                break

            elif("NÃO" in useraudio.upper()):
                print('You: ' + useraudio)
                tm.sleep(1)
                print('\nOk im leaving now.\n')
                break

            else:
                print('You: ' + useraudio)
                tm.sleep(1)
                print('\nCan I help with something else?')       
                
        except:
            print('\nSorry I cant understand.\n')
            break



       




