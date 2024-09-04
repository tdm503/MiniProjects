import wave

obj = wave.open('/home/minh/Desktop/docs/MiniProjects/SpeechToText/you-know-what-im-talking.wav','rb')

print(f'number of channer {obj.getnchannels()}')
print(f'number of parameter {obj.getparams()}')