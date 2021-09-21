# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 23:19:59 2021

@author: Ashish Anand
"""

import numpy as np
import matplotlib.pyplot as plt
#import soundfile as sf
#import librosa

def genSine(f0, fs, dur):
    samples = dur * fs
    t = np.arange(samples)
    sinusoid = np.sin(2*np.pi*t*(f0/fs))    
    return sinusoid

fs = 16000
# analog freq in Hz
F = 200
dur = 0.1 # seconds
x1 = genSine(F, fs, dur)
x2 = genSine(700, fs, dur)
x3 = genSine(1000, fs, dur)
#plt.stem(x)

x = np.concatenate((x1,x2,x3))
xa = np.concatenate((x3,x2,x1))

time = np.arange(x.size)/fs
plt.subplot(211)
plt.plot(time,x)

plt.subplot(212)
plt.plot(time,xa)
plt.xlabel('time')
plt.show()

# plot the spectrum
m = np.size(time)/3
X = (2/m)*np.abs(np.fft.fft(x))
freq = np.fft.fftfreq(x.shape[-1],d=1/fs)
plt.plot(freq,X)
plt.xlabel('Frequency (in Hz)')
plt.show()

#Xa = (2/m)*np.abs(np.fft.fft(xa))
#freq = np.fft.fftfreq(xa.shape[-1],d=1/fs)
#plt.plot(freq,Xa)
#plt.xlabel('Hz')
#plt.show()

fs = 500
x1 = genSine(F, fs, dur)
x2 = genSine(700, fs, dur)
x3 = genSine(1000, fs, dur)

x = np.concatenate((x1,x2,x3))
xa = np.concatenate((x3,x2,x1))

time = np.arange(x.size)/fs
plt.subplot(211)
plt.plot(fs*time,x)

plt.subplot(212)
plt.plot(fs*time,xa)
plt.show()

# plot the spectrum
m = np.size(time)/3
X = (2/m)*np.abs(np.fft.fft(x))
freq = np.fft.fftfreq(x.shape[-1],d=1/fs)
plt.plot(freq,X)
plt.xlabel('Frequency (in Hz)')
plt.show()



fs = 1500
x1 = genSine(F, fs, dur)
x2 = genSine(700, fs, dur)
x3 = genSine(1000, fs, dur)

x = np.concatenate((x1,x2,x3))
xa = np.concatenate((x3,x2,x1))

time = np.arange(x.size)/fs
plt.subplot(211)
plt.plot(fs*time,x)

plt.subplot(212)
plt.plot(fs*time,xa)
plt.show()

# plot the spectrum
m = np.size(time)/3
X = (2/m)*np.abs(np.fft.fft(x))
freq = np.fft.fftfreq(x.shape[-1],d=1/fs)
plt.plot(freq,X)
plt.xlabel('Frequency (in Hz)')
plt.show()



fs = 3000
x1 = genSine(F, fs, dur)
x2 = genSine(700, fs, dur)
x3 = genSine(1000, fs, dur)

x = np.concatenate((x1,x2,x3))
xa = np.concatenate((x3,x2,x1))

time = np.arange(x.size)/fs
plt.subplot(211)
plt.plot(fs*time,x)

plt.subplot(212)
plt.plot(fs*time,xa)
plt.show()

# plot the spectrum
m = np.size(time)/3
X = (2/m)*np.abs(np.fft.fft(x))
freq = np.fft.fftfreq(x.shape[-1],d=1/fs)
plt.plot(freq,X)
plt.xlabel('Frequency (in Hz)')
plt.show()