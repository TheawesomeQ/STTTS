# This is a sample Python script.
import speech_recognition as sr
import pyttsx3
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Speech Recognition engine init
    r = sr.Recognizer()
    r.dynamic_energy_threshold = False
    r.pause_threshold = 0.8
    phrase_max_time = 10
    ambient_init_period = 2

    # Text to speech engine init
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')
    tts.setProperty('voice', voices[1].id)

    with sr.Microphone() as source:
       # print("Device: " + source.device_index)

        r.adjust_for_ambient_noise(source, duration=ambient_init_period)
        while True:
            print("Say something:")
            audio = r.listen(source, phrase_time_limit=phrase_max_time)
            print("Sample duration: " + str((len(audio.frame_data)/audio.sample_width)/audio.sample_rate) + "s")
            print("Attempting recognition...")
            try:
                #print("Sphinx: " + r.recognize_sphinx(audio))
                result = r.recognize_google(audio)
                print("Google: " + result)
                print("Attempting TTS reading...")
                try:
                    tts.say(result)
                    tts.runAndWait()
                except Exception:
                    print("TTS Failed.")
            except LookupError:
                print("Lookup error.")
            except sr.RequestError as e:
                print("Couldn't access recognition engine.")
            except sr.UnknownValueError as e:
                print("Couldn't understand.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
