def characters():
    fin = open("words.txt")
    for line in fin:
        words = line.strip()
        if len(words) > 19:
            print(words)
