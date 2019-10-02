import pandas as pd
import matplotlib.pyplot as plt

def print_message():
    """
    Function that prints a message
    """
    print("I am awesome")

def print_message2():
    """
    Function with variable
    """
    message = "I am awesome and boring"
    print(message)

def print_function_with_argument(message):
    """
    Function with one argument
    """
    print(message)

def plot_spectrum(file_name):
    """
    This frequency plots a frequency spectrum
    """
    table = pd.read_csv(file_name)
    #print(table)
    frequency = table["frequency"].values
    amplitude = table["amplitude"].values
    plt.plot(frequency,amplitude)
    plt.xlabel(" Frequency ")
    plt.ylabel(" Amplitude ")
    plt.title(" Frequency spectrum ")
    plt.show()

def plot_spectrum_w_arg(file_name, x_label, y_label, title):
        """
        Founction with four arguments
        This frequency plots a frequency spectrum with
        """
        table = pd.read_csv(file_name)
        #print(table)
        frequency = table["frequency"].values
        amplitude = table["amplitude"].values
        plt.plot(frequency,amplitude)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()


if __name__ == '__main__':
    file_name = "frequency_spectrum.csv"
    my_xlabel = " Frequency "
    my_ylabel = " Amplitude "
    my_title = " My frequency spectrum / envelope?  "
    plot_spectrum_w_arg(file_name, my_xlabel, my_ylabel, my_title)
