import pandas as pd
import matplotlib.pyplot as plt
'''
def get_name():
    name = "Ørjan"
    return name

# Call the above function
name = get_name()
print(name)
'''


def get_spectrum(table):
    #table = pd.read_csv(file_name)
    frequency = table["frequency"].values
    amplitude = table["amplitude"].values
    return frequency, amplitude
    #print(table)


def spectrum_label():
    x_label = "Frequency [Hz]"
    y_label = "Amplitude [g]"
    return x_label, y_label

#call the function

file_name = "frequency_spectrum.csv"
table = pd.read_csv(file_name)
frequency, amplitude = get_spectrum(table)
#plt.plot(frequency, amplitude)
#plt.show()
