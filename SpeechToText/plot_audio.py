import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open('/home/minh/Desktop/docs/MiniProjects/SpeechToText/you-know-what-im-talking.wav','rb')

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

t_audio = n_samples/sample_freq

print(t_audio)
