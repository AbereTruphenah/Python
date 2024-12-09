"""Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C.
Store the paragraph above in a variable named text. Split the paragraph into sentences by looking for the dot followed by a space. Store the result in a variable named sentences. Loop through the sentences and for each sentence search for the word temperature and print the sentence where it is found."""
# Store the paragraph in a variable
text = ("Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C.")

# Split the paragraph into sentences
sentences = text.split('. ')

# Loop through the sentences and search for the word 'temperature'
for sentence in sentences:
    if 'temperature' in sentence.lower():
        print(sentence)
