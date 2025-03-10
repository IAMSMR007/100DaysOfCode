student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


#TODO 1. Create a dictionary in this format:{"A": "Alfa", "B": "Bravo"}

with open(r"C:\Users\MOHAMMAD SAMEER\PY\100DaysOfCode\Day 26\NATO-alphabet-start\nato_phonetic_alphabet.csv") as file:
    data = pandas.read_csv(file)

nato_phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_phonetic_alphabet)



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
output_list=[nato_phonetic_alphabet[letter] for letter in user_input]
print(output_list)
