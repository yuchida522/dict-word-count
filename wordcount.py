# put your code here.

def word_count_dict(filename):

    poem = open(filename)
    
    word_count = {}

    for line in poem:
        poem_words = line.rstrip("\n!?.(),").split(" ")
        # print(poem_words)
    
        for word in poem_words:
            word_count[word.lower()] = word_count.get(word, 0) + 1

    for key, value in word_count.items():
       print(f"{key} {value}")

    poem.close()

word_count_dict('test.txt')
