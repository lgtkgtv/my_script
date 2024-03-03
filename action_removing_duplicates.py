import os
import hashlib

def calculate_file_hash(file_path, block_size=65536):
    """Calculate hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(block_size)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def detect_duplicate_files(files):
    """Detect duplicate files by comparing their hashes."""
    file_hashes = {}
    duplicates = {}
    for file in files:
        file_hash = calculate_file_hash(file)
        if file_hash not in file_hashes:
            file_hashes[file_hash] = file
        else:
            if file_hash not in duplicates:
                duplicates[file_hash] = [file_hashes[file_hash]]
            duplicates[file_hash].append(file)
    return duplicates

def remove_duplicates(files):
    """Remove duplicate files based on user selection."""
    new_files = []
    duplicates = detect_duplicate_files(files)
    for file_hash, dup_list in duplicates.items():
        print(f"Duplicate files with hash '{file_hash}':")
        for idx, dup_file in enumerate(dup_list):
            print(f"{idx + 1}. {dup_file}")
        
        keep_idx = int(input("Enter the index of the file you want to keep: "))
        keep_file = dup_list[keep_idx - 1]
        new_files.append(keep_file)
        for dup_file in dup_list:
            if dup_file != keep_file:
                os.remove(dup_file)
                print(f"Removed duplicate file: {dup_file}")
    return new_files
