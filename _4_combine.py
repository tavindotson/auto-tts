# Will recombine all split files and put them in /files/audio/combined

import os
import shutil
import time

def combine_audio_parts(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):
        if filename.endswith(".mp3"):
            base_filename, part_number = filename.rsplit('_', 1)
            part_number = part_number.split('.')[0]
            if base_filename not in audio_files:
                audio_files[base_filename] = []
            audio_files[base_filename].append((int(part_number), filename))

    for base_filename, parts in audio_files.items():
        parts.sort(key=lambda x: x[0])
        combined_filepath = os.path.join(destination_dir, f"{base_filename}.mp3")
        if os.path.exists(combined_filepath):
            print(f"Combined file {combined_filepath} already exists. Skipping...")
            continue
        with open(combined_filepath, 'wb') as combined_file:
            for _, part_filename in parts:
                part_filepath = os.path.join(source_dir, part_filename)
                with open(part_filepath, 'rb') as part_file:
                    shutil.copyfileobj(part_file, combined_file)

source_directory = "./files/audio"
destination_directory = "./files/audio/combined"
audio_files = {}

combine_audio_parts(source_directory, destination_directory)

print("Combining audio parts complete.")
