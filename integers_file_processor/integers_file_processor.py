def process_integers():
    with open("integers_file_processor/integers.txt", "r") as infile:
        numbers = [int(line.strip()) for line in infile if line.strip()]
    
    with open("double.txt", "w") as f:
        for n in numbers:
            if n % 2 == 0:
                f.write(f"{n * n}\n")
    
    with open("triple.txt", "w") as f:
        for n in numbers:
            if n % 2 == 1:
                f.write(f"{n * n * n}\n")

# siguraduhing na‑call
print("Processing...")   # para makita mo talaga napapatakbo
process_integers()
print("Done! Check double.txt and triple.txt.")