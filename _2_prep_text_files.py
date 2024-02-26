# This script splits files larger than 4096 characters
# and (optional) will do special formatting for numbers in-between "- X -"

import os
import time

print("Large files in /files will be split up. (4096 char limit)")
print("You can recombine them after TTS processing.")
time.sleep(3)

def split_large_files(folder_path='./files', max_size=4096):
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath) and filename.endswith('.txt'):
            with open(filepath, 'r') as file:
                content = file.read()
            if len(content) > max_size:
                chunks = []
                start = 0
                while start < len(content):
                    end = start + max_size
                    if end >= len(content):
                        end = len(content)
                    else:
                        while end > start and content[end] != '\n':
                            end -= 1
                    chunks.append(content[start:end])
                    start = end + 1 if end < len(content) else end
                for i, chunk in enumerate(chunks):
                    new_filename = f"{os.path.splitext(filename)[0]}_{i+1}{os.path.splitext(filename)[1]}"
                    new_filepath = os.path.join(folder_path, new_filename)
                    with open(new_filepath, 'w') as new_file:
                        new_file.write(chunk)
                os.remove(filepath)

split_large_files()

def normalize_filename(filename):
    parts = filename.split(" - ")
    if len(parts) < 3:
        return filename
    middle_part = parts[1].strip()
    try:
        middle_number = int(middle_part)
        normalized_middle_part = '{:03d}'.format(middle_number)
        parts[1] = normalized_middle_part
        return " - ".join(parts)
    except ValueError:
        return filename

def main():
    current_dir = './files'
    txt_files = [f for f in os.listdir(current_dir) if f.endswith('.txt')]
    
    for filename in txt_files:
        old_path = os.path.join(current_dir, filename)
        new_filename = normalize_filename(filename)
        new_path = os.path.join(current_dir, new_filename)
        
        os.rename(old_path, new_path)
        print(f"Renamed '{filename}' to '{new_filename}'")

if __name__ == "__main__":
    print("Attempting to normalize file names.")
    time.sleep(2)
    main()
