import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
while True:
    reproducir = input("in tro ")
    speaker.Speak(reproducir)
    if reproducir =="1":
        break