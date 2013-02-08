from collections import Counter
infile = open("MYSTERY.IN", mode="r")
decrypted = open("MYSTERY_DECRYPT.OUT", mode="r")
outfile = open("RESULT.OUT", mode="a")


def decrypt(file):
    lines = file.readlines()
    for line in lines:
        for i in line:
            decrypt.write(chr(ord(i) - 5))

def most_common_3():
    word_list = []
    for line in decrypted.readlines():
        for word in line.split(" "): #extract words from lines
            word_list.append(word)

    counter = 0
    for i in Counter(word_list).most_common()[:20]: #python library function
        if counter == 3:
            break
        elif len(i[0]) > 4: #removing non-nouns (eg. a, the, we)
            print(i[0] + " ")
            counter = counter + 1
most_common_3()
infile.close()
decrypted.close()
outfile.close()
