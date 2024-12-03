import magenta.music as mm
from magenta.models.melody_rnn import melody_rnn_sequence_generator
import os

output = "generated_song"
os.makedirs(output, exist_ok = True)

#RNN Model (Recurrent Neural Networks)
model_name = 'attention_rnn'
melody_rnn = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator(model_name = model_name)
temperature = 1.0
num_music = 3
steps_per_music = 128

preferred_genre = input(
    "Enter specific genre: (Classical / Jazz / Rock): ")
preferred_tempo = int(input("Enter specific tempo (BPM): "))

#All of these are commonly used progressions in music standards
#I basically do music btw, so i do know
chord_progressions = {
    "classical" : ["C", "G", "Am", "F"],
    "jazz" : ["Cmaj7", "Dm7", "Em7", "A7"],
    "rock" : ["E", "B", "C#m", "A"],
}

drum_pattern = mm.DrumTrack(
    [36, 0, 42, 0, 36, 0, 42, 0],
    start_step = 0,
    step_per_quarter = 4,
    step_per_beats = (steps_per_music // 4),
)

for i in range(num_music):
    melody = melody_rnn.generate(
        temperature = temperature,
        steps = steps_per_music,
        drum_track = drum_pattern,
        preferred_genre = preferred_genre,
        preferred_tempo = preferred_tempo,
        preferred_chord_progression = chord_progressions[preferred_genre],
        primer_sequence = None
    )
    chords = [chord_progressions.get(preferred_genre, ["C"])[i % len(chord_progressions.get(preferred_genre, ["C"]))] for i in range(steps_per_music)]
    chord_sequence = mm.ChordSequence(chords)
    melody_with_chords_sequence = mm.sequence_lib.concatenate_sequences([melody, chord_sequence])

    music = mm.sequence_lib.concatenate_sequences(melody_with_chords_sequence, drum_pattern)
    music.tempos[0].gpm = preferred_tempo

    midi_file = os.path.join(output, f"{i}.mid")
    mm.midi_io.sequence_proto_to_midi_file(music, midi_file)
    print(f'MIDI sequence {i + 1} generated and saved as {midi_file}')

print("Exiting")







