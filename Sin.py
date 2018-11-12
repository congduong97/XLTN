import numpy as np
import matplotlib.pyplot as plt
import matplotlib

class SinFFT:
    def __init__(self):
        self.nfft = 512
        # Sampling Frequency
        self.rate = 2000
        # Sine frequency
        self.F0 = 200

    def create_sin(self):
        self.datasin = np.zeros(self.nfft)
        #Timinig axe
        self.time = np.linspace(0, 2.0 * np.pi * self.F0 * self.nfft / self.rate, num = self.nfft)
        self.datasin = np.sin(self.time)
        self.hamming = np.hamming(self.nfft)
        self.data = np.multiply(self.datasin, self.hamming)

    def plot_signal(self):
        SMALL_SIZE = 14
        matplotlib.rc('font', size = SMALL_SIZE)
        matplotlib.rc('axes', titlesize = SMALL_SIZE)
        plt.subplot(311)
        plt.xlim(self.time[0], self.time[-1])
        plt.ylim(np.min(self.datasin), np.max(self.datasin))
        plt.fill_between(self.time, np.min(self.datasin), np.max(self.datasin), color = 'k')
        plt.plot(self.time, self.datasin, color = '#00E100')
        plt.grid(color = 'w')
        plt.xlabel('Time in second')
        plt.ylabel('Bien do')
        plt.subplot(312)
        plt.xlim(self.time[0], self.time[-1])
        plt.ylim(np.min(self.data), np.max(self.data))
        plt.fill_between(self.time, np.min(self.data), np.max(self.data), color = 'k')
        plt.plot(self.time, self.data, color = '#00E100')
        plt.grid(color = 'w')
        plt.xlabel('Time in Second')
        plt.ylabel('Bien do')

    def _calculate_frequencies(self, data):
        data_freq = np.fft.fft(data, self.nfft)
        magSpectrum = np.abs(data_freq)
        self.magDb = 20.0 * np.log10(magSpectrum / max(magSpectrum))
        return self.magDb

    def plot_spectrum(self):
        plt.subplot(313)
        magDb = self._calculate_frequencies(self.data)
        minDb = min(magDb)
        maxDb = max(magDb)
        #Frequency axe scalar
        frequency = np.linspace(0, (self.rate / 2), num = (self.nfft) /2 -1)
        #Background in Black
        plt.fill_between(frequency, minDb, maxDb, color = 'k')
        plt.plot(frequency, magDb[0:int(self.nfft/2) -1], color = '#00E100')
        plt.xlim(0, self.rate / 2.0)
        plt.ylim(minDb, maxDb)
        plt.grid(color = 'w')
        plt.xlabel('Frequency in Hz')
        plt.ylabel('Magnitude in  dB')
        plt.show()

if __name__ == "__main__":
    specsin = SinFFT()
    creates = specsin.create_sin()
    drawsin = specsin.plot_signal()
    plotspec = specsin.plot_spectrum()