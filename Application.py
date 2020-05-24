import wave
import pyaudio
import speech_recognition

SECONDS = 5

AUDIO_FILE = "d:/male.wav"

# initialize pyAudio class
pAudio = pyaudio.PyAudio()

RECOGNIZER = speech_recognition.Recognizer()

with speech_recognition.AudioFile(AUDIO_FILE) as source:
    totalAudioLength = source.DURATION

    while SECONDS <= totalAudioLength:
        # read initial SECONDS from audio
        audioDataInstance = RECOGNIZER.record(source, 5)
        SECONDS += 5

        speechToTextData = RECOGNIZER.recognize_google(audioDataInstance)
        print(">>> " + speechToTextData)

        # open wave file
        waveAudio = wave.open(AUDIO_FILE)

        # construct a pyAudio stream object using wave properties
        stream = pAudio.open(format=pAudio.get_format_from_width(waveAudio.getsampwidth()),
                             channels=waveAudio.getnchannels(),
                             rate=waveAudio.getframerate(),
                             output=True)

        stream.write(audioDataInstance.get_raw_data())

stream.stop_stream()
stream.close()
pAudio.terminate()
