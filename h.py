# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:36:16 2021

@author: Ashish Anand
"""
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
#import librosa
#import librosa.display
#from scipy.fftpack import fft

dur = 5  #duration of sinusoid (in sec)
fs = 10000    #sinusoid generation frequency (sampling frequency at which it is generated) (in Hz)
f0=100   #frequency of sinusoid (in Hz)

samples = dur * fs
t = np.linspace(0,dur,samples)

sinusoid = np.sin(2*np.pi*f0*t)   
plt.subplot(211) 
plt.xlabel('t (in sec)')
plt.plot(t,sinusoid)
plt.xlabel('t (in sec)')
plt.title('Continuous time sinusoid signal')
sf.write('sinct.wav',sinusoid,fs,subtype='PCM_24')  #continuous time signal

#plotting spectrum
m = np.size(t)
X = (2/m)*np.abs(np.fft.fft(sinusoid))
freq = np.fft.fftfreq(sinusoid.shape[-1],d=1/fs)
plt.subplot(212)
plt.plot(freq,X)
plt.xlabel('Frequency (in Hz)')
plt.show()


fs1 = 50
samples_dt1 = dur * fs1
n1 = np.linspace(0,dur,samples_dt1)
sinusoid_dt50 = np.sin(2*np.pi*f0*n1)    
plt.subplot(211)
plt.plot(n1*fs1,sinusoid_dt50)
plt.title('Discrete time sinusoid sampled at 50 Hz')
plt.xlabel('n (integer values)')
sf.write('sindt50.wav',sinusoid_dt50,fs1,subtype='PCM_24')  #discrete time signal sampled at Fs=50 Hz

m1 = np.size(n1)
X1 = (2/m1)*np.abs(np.fft.fft(sinusoid_dt50))
freq1 = np.fft.fftfreq(sinusoid_dt50.shape[-1],d=1/fs1)
plt.subplot(212)
plt.plot(freq1,X1)
plt.xlabel('Frequency (in Hz)')
plt.show()


fs2 = 100
samples_dt2 = dur * fs2
n2 = np.linspace(0,dur,num=samples_dt2)
sinusoid_dt100 = np.sin(2*np.pi*f0*n2)
plt.subplot(211)
plt.plot(n2*fs2,sinusoid_dt100)
plt.title('Discrete time sinusoid sampled at 100 Hz')
plt.xlabel('n (integer values)')
sf.write('sindt100.wav',sinusoid_dt100,fs2,subtype='PCM_24') #discrete time signal sampled at Fs=100 Hz

m2 = np.size(n2)
X2 = (2/m2)*np.abs(np.fft.fft(sinusoid_dt100))
freq2 = np.fft.fftfreq(sinusoid_dt100.shape[-1],d=1/fs1)
plt.subplot(212)
plt.plot(freq2,X2)
plt.xlabel('Frequency (in Hz)')
plt.show()



fs3 = 200
samples_dt3 = dur * fs3
n3 = np.linspace(0,dur,num=samples_dt3)
sinusoid_dt200 = np.sin(2*np.pi*f0*n3)
plt.subplot(211)
plt.plot(n3*fs3, sinusoid_dt200)
plt.title('Discrete time sinusoid sampled at 200 Hz')
plt.xlabel('n (integer values)')
sf.write('sindt200.wav',sinusoid_dt200,fs3,subtype='PCM_24') #discrete time signal sampled at Fs=200 Hz

m3 = np.size(n3)
X3 = (2/m3)*np.abs(np.fft.fft(sinusoid_dt200))
freq3 = np.fft.fftfreq(sinusoid_dt200.shape[-1],d=1/fs3)
plt.subplot(212)
plt.scatter(freq3,X3)
plt.xlabel('Frequency (in Hz)')
plt.show()


fs4=400
samples_dt4 = dur * fs4
n4 = np.linspace(0,dur,num=samples_dt4)
sinusoid_dt400 = np.sin(2*np.pi*f0*n4)
plt.subplot(211)
plt.plot(n4*fs4, sinusoid_dt400)
plt.title('Discrete time sinusoid sampled at 400 Hz')
plt.xlabel('n (integer values)')
sf.write('sindt400.wav',sinusoid_dt400,fs4,subtype='PCM_24') #discrete time signal sampled at Fs=100 Hz

m4 = np.size(n4)
X4 = (2/m4)*np.abs(np.fft.fft(sinusoid_dt400))
freq4 = np.fft.fftfreq(sinusoid_dt400.shape[-1],d=1/fs4)
plt.subplot(212)
plt.plot(freq4,X4)
plt.xlabel('Frequency (in Hz)')
plt.show()
