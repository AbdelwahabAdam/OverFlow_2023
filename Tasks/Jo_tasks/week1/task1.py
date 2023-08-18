from letter_patterns import letter_patterns

def print_name_sideways(name):
    lines = [""] * 5
    for letter in name:
        if letter in letter_patterns:
            pattern = letter_patterns[letter]
            for i in range(5):
                lines[i] += " ".join("*" if dot == 1 else " " for dot in pattern[i]) + "  "
        else:
            print("Letter not found (what a strange name!): ", letter)
    
    for line in lines:
        print(line)

def main():
    name = input("Enter your name: ")
    print_name_sideways(name)

if __name__ == "__main__":
    main()
