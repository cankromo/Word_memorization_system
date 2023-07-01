# Vocabulary Learning Algorithm

This algorithm is designed to help users learn vocabulary in two languages - Spanish and Turkish. It presents a random word in Spanish and asks the user to provide its Turkish translation. The algorithm provides feedback on the correctness of the translation and keeps track of the user's progress.

# Define the word list:
The word list contains pairs of words, where the first word is in Spanish and the second word is in Turkish. You can add or modify the word pairs according to your needs.

word_list = [
    ("La Palabra", "Kelime"),
    ("El Hambre", "Açlık"),
    ("El Olor", "Koku"),
    ...
]
# Requirements

The following libraries are required to run the algorithm:

random: Used for generating random words from the word list.

gtts: Used for text-to-speech conversion and saving audio files.

pygame: Used for playing the generated audio files.

os: Used for removing temporary audio files.

Make sure you have these libraries installed before running the algorithm.

# Additional Features

There is commented code provided in the algorithm that allows the user to learn Spanish words by providing their Turkish translations. If you want to use this feature, uncomment the code and follow the same steps as for the Spanish to Turkish translation.

Note: You can modify the code as per your requirements and add more features to enhance the learning experience.

# Acknowledgements
This project was made possible thanks to the hard work and dedication of my friend [Ahmet Yusuf Demir](https://github.com/ahmetdem). Thank you for your contributions and for making this project a reality!
