from pyaudio import PyAudio, paFloat32
import numpy as np


class Audio:
    def __init__(self):
        self.RATE = 44100
        self.BPM = 100
        self.L1 = (60 / BPM * 4) * self.RATE
        self.L2 = self.L1 / 2
        self.L4 = self.L1 / 4
        self.L8 = self.L1 / 8
        self.stream = None

    def open(self):
        self.stream = PyAudio().open(format=paFloat32,
                                     channels=1,
                                     rate=self.RATE,
                                     frames_per_buffer=1024,
                                     output=True)

    def play(self, freq, length):
        t = float(freq) * np.pi * 2 / self.RATE
        s = np.sin(np.arange(length) * t)
        self.stream.write(s.astype(np.float32).tostring())

    def close(self):
        self.stream.close()
