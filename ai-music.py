import magenta.music as mm
from magenta.models.melody_rnn import melody_rnn_sequence_generator
import numpy as np
import random
import os
from typing import List, Dict, Optional

class MusicGenerator:
    CHORD_PROGRESSIONS = {
        "classical": [
            ["C", "G", "Am", "F"],
            ["Em", "Am", "F", "G"],
            ["D", "Bm", "G", "A"]
        ],
        "jazz": [
            ["Cmaj7", "Dm7", "Em7", 'A7'],
            ["Fmaj7", "Bb7", "Eb", "Am7"],
            ["Gmaj7", "C7", "Dm7", "Em7"]
        ],
        "rock": [
            ["E", "B", "C#m", "A"],
            ["G", "D", "Em", "C"],
            ["A", "D", "Bm", "F#m"] 
        ],
        "electronica": [
            ["Am", "F", "G", "C"],
            ["Dm", "Bb", "F", "C"],
            ["Em", "C", "G", "D"]
        ]
    }

    DRUM_PATTERNS = {
        "classical": [
            [36, 0, 42, 0, 36, 0, 42, 0],
            [36, 42, 0, 36, 0, 42, 36, 0]
        ],
        "jazz": [
            [36, 0, 42, 0, 36, 0, 42, 0],
            [36, 42, 0, 36, 0, 42, 36, 0]
        ],
        "rock": [
            [36, 0, 42, 0, 36, 0, 42, 0],
            [36, 42, 0, 36, 0, 42, 36, 0]
        ],
        "electronica": [
            [36, 0, 42, 0, 36, 0, 42, 0],
            [36, 42, 0, 36, 0, 42, 36, 0]
        ]
    }

    def __init__(self, 
            model_name: str = 'attention_rnn',
            output_dir: str = 'generated_music',
            temperature: float = 1.0,
            num_compositions: int = 5,
            steps_per_composition: int = 256):
        
        """
        Initialize the music generator with customizable parameters
        :param model_name: Name of RNN model to use
        :param output_dir: Directory to save generated music
        :param temperature: Randomness of generation
        :param num_compositions: Number of compositions to generate
        :param steps_per_composition: Musical steps in each comp.
        """

        self.model_name = model_name
        self.output_dir = output_dir
        self.temperature = temperature
        self.num_compositions = num_compositions
        self.steps_per_composition = steps_per_composition

        os.makedirs(self.output_dir, exist_ok = True)
        self.melody_rnn = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator(
            model_name = self.model_name
        )
    def _select_genre_details(self,
            preferred_genre: Optional[str] = None,
            preferred_tempo: Optional[int] = None) -> tuple:

        """
        Dynamically selects a genre and tempo if needed
        :param preferred_genre: User-specified genre
        :param preferred_tempo: User-specified tempo
        :return: Tuple of (genre, tempo)
        """

        if not preferred_genre:
            genres = list(self.CHORD_PROGRESSIONS.keys())
            preferred_genre = random.choice(genres)
        if not preferred_tempo:
            tempo_ranges = {
                "classical": (60, 120),
                "jazz": (80, 160),
                "rock": (100, 180),
                "electronic": (120, 200)
            }
            min_tempo, max_tempo = tempo_ranges.get(preferred_genre, (80, 140))
            preferred_tempo = random.randint(min_tempo, max_tempo)
        return preferred_genre, preferred_tempo

    def generate_drum_pattern(self, genre: str) -> mm.DrumTrack:

        """
        Generates a drum pattern based on genre
        :param genre: Music genre
        :return: Drum sequence
        """

        pattern = random.choice(self.DRUM_PATTERNS.get(genre, self.DRUM_PATTERNS['rock']))
        return mm.DrumTrack(
            pattern,
            start_step = 0,
            step_per_quarter = 4,
            step_per_beats = (self.steps_per_composition // 4)
        )

    def generate_music(self,
                preferred_genre: Optional[str] = None,
                preferred_tempo: Optional[int] = None) -> List[str]:
        
        """
        Generate multiple music compositions

        :param preferred_genre: User-specified genre
        :param preferred_tempo: User-specified tempo
        :return: List of generated MIDI file paths
        """
        genre, tempo = self._select_genre_details(preferred_genre, preferred_tempo)
        generated_files = []
        for i in range(self.num_compositions):
            chord_progressions = random.choice(self.CHORD_PROGRESSIONS[genre])
            drum_pattern = self.generate_drum_pattern(genre)
            melody = self.melody_rnn.generate(
                temperature = self.temperature,
                steps = self.steps_per_composition,
                drum_track = drum_pattern,
                preferred_genre = genre,
                preferred_tempo = tempo,
                preferred_chord_progression = chord_progressions,
                primer_sequences = None
            )
            chords = [chord_progressions[i % len(chord_progressions)] for i in range(self.steps_per_composition)]
            chord_sequence = mm.ChordSequence(chords)

            melody_with_chords = mm.sequence_lib.concatenate_sequences([melody, chord_sequence])
            music = mm.sequence_lib.concatenate_sequences(melody_with_chords, drum_pattern)
            midi_file = os.path.join(self.output_dir, f"{genre}_{i+1}.mid")
            mm.midi_io.sequence_proto_to_midi_file(music, midi_file)
            generated_files.append(midi_file)
            print(f'MIDI sequence {i + 1} generated and saved as {midi_file}')

        return generated_files

def main():
    print("AI Music Generator")
    print()

    print("Available Genres:", ", ".join(MusicGenerator.CHORD_PROGRESSIONS.keys()))
    genre_choice = input("Enter genre (or press Enter for random): ").strip() or None

    try:
        tempo_choice = int(input("Enter tempo (or press Enter for random): ") or 0)
    except ValueError:
        tempo_choice = None
    
    music_generator = MusicGenerator(
        num_compositions = 3,
        temperature = 1.2,
        steps_per_composition = 256
    )

    generated_files = music_generator.generate_music(
        preferred_genre = genre_choice,
        preferred_tempo = tempo_choice
    )
    print("\nGeneration complete!")
    print("Generated MIDI files: ", generated_files)

if __name__ == "__main__":
    main()






