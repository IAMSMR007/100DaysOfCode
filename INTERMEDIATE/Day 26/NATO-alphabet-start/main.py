import pandas

# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
with open("nato_phonetic_alphabet.csv") as file:
    data = pandas.read_csv(file)

nato_phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    
    try:
        if not user_input.isalpha():
            raise ValueError("Please enter only alphabetic characters.")
        
        output_list = []
        for letter in user_input:
            try:
                output_list.append(nato_phonetic_alphabet[letter])
            except KeyError:
                print(f"'{letter}' is not in the NATO phonetic alphabet. Skipping.")
        
        if output_list:
            print(output_list)
        else:
            print("No valid NATO phonetic codes were found.")
    except ValueError as ve:
        print(ve)
        generate_phonetic()  # Recursive call to give user another chance

# Run the program
generate_phonetic()

