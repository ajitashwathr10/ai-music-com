# Music Generation with Magenta RNN

[![GitHub stars](https://img.shields.io/github/stars/ajitashwathr10/music-magenta-rnn?style=social)](https://github.com/ajitashwathr10/music-magenta-rnn/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ajitashwathr10/music-magenta-rnn?style=social)](https://github.com/ajitashwathr10/music-magenta-rnn/network)
[![Issues](https://img.shields.io/github/issues/ajitashwathr10/music-magenta-rnn)](https://github.com/ajitashwathr10/music-magenta-rnn/issues)
[![MIT License](https://img.shields.io/github/license/ajitashwathr10/music-magenta-rnn)](LICENSE)

## Introduction
This Python based script generates music using the `Magenta` library, specifically utilizing the Melody RNN model. The script allows users to specify a preferred genre and tempo, and it outputs MIDI files based on these inputs.

## Prerequisites
Before running the script, ensure you have the necessary packages installed:
```bash
pip install magenta
```

## Components
### Libraries
- `Magenta`: An open-source research project exploring the role of machine learning in the process of creating art and music.
- `os`: A standard Python library for interacting with the operating system.
  
### Key Parameters
- `model_name`: The name of the Melody RNN model used (attention_rnn).
- `temperature`: Controls the randomness of the generated music (default is 1.0).
- `num_music`: Number of music pieces to generate (default is 3).
- `steps_per_music`: Number of steps (notes) in each generated music piece (default is 128).

### User Inputs
- `preferred_genre`: The genre of music to generate (options: Classical, Jazz, Rock).
- `preferred_tempo`: The tempo of the music in beats per minute (BPM).

### Chord Progressions
- Predefined chord progressions for each genre:
  - Classical: `["C", "G", "Am", "F"]`
  - Jazz: `["Cmaj7", "Dm7", "Em7", "A7"]`
  - Rock: `["E", "B", "C#m", "A"]`
 
### Drum Pattern
- A simple drum pattern is defined to be included in the generated music.

## Script Overview
The script follows these main steps:
1. Imports necessary libraries.
2. Creates an output directory for the generated MIDI files.
3. Loads the Melody RNN model.
4. Prompts the user to input a preferred genre and tempo.
5. Defines chord progressions for different genres.
6. Defines a drum pattern.
7. Generates a specified number of music pieces using the Melody RNN model.
8. Saves each generated piece as a MIDI file.

## Usage
- Run the script.
- Enter the preferred genre when prompted (options: Classical, Jazz, Rock).
- Enter the preferred tempo (in BPM).
- The script will generate and save the specified number of MIDI files in the generated_song directory.

### Notes
- Ensure the `magenta` library is correctly installed and configured.
- The script generates MIDI files that can be played using any MIDI-compatible software.

## Acknowledgement
This script was created using the Magenta library, developed by the Magenta team at Google. Special thanks to the open-source community for providing the tools and frameworks necessary for developing such innovative applications.

For more information on Magenta and its capabilities, visit the [Magenta GitHub repository](https://github.com/magenta/magenta)



 
