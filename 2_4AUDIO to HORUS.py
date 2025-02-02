from scipy.io import wavfile
import pandas as pd
import matplotlib.pyplot as plt

# Function to display audio info and plot the signal
def show_audio_info(audio_name, audio_data, rate):
    print(f"Audio: {audio_name}")
    print(f"Rate: {rate}")
    print(f"Shape: {audio_data.shape}")
    print(f"Min, Max: {audio_data.min()}, {audio_data.max()}")
    plot_audio(audio_name, audio_data, rate)

# Function to plot the audio signal
def plot_audio(audio_name, audio_data, rate):
    plt.title(f"Signal Wave - {audio_name} at {rate} Hz")
    for c in range(audio_data.shape[1]):
        plt.plot(audio_data[:, c], label=f"Ch{c+1}")
    plt.legend()
    plt.show()

# Function to process and save audio data
def process_audio(input_file, output_file, channels):
    rate, data = wavfile.read(input_file)
    show_audio_info(channels, data, rate)
    df = pd.DataFrame(data, columns=[f"Ch{i+1}" for i in range(data.shape[1])])
    df.to_csv(output_file, index=False)

# Process multiple audio files
audio_files = [
    ("C:/VKHCG/05-DS/9999-Data/2ch-sound.wav", "Audio-to-HORUS-outputG-2ch.csv", "2 channel"),
    ("C:/VKHCG/05-DS/9999-Data/4ch-sound.wav", "Audio-to-HORUS-outputG-4ch.csv", "4 channel"),
    ("C:/VKHCG/05-DS/9999-Data/6ch-sound.wav", "Audio-to-HORUS-outputG-6ch.csv", "6 channel"),
    ("C:/VKHCG/05-DS/9999-Data/8ch-sound.wav", "Audio-to-HORUS-outputG-8ch.csv", "8 channel")
]

for input_file, output_file, channels in audio_files:
    print(f"Processing: {input_file}")
    process_audio(input_file, output_file, channels)

print("Audio to HORUS - Done")
