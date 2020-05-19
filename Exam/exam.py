def boyer_moore(input_data, dictionary):
    length = len(input_data)
    symbols = ['?', '-', '(', ')', '#', '*', '', ' ', '.', ',', '!']
    for word in dictionary:
        word_length = len(word)
        i = word_length - 1
        j = word_length - 1
        while True:
            if word[j] == input_data[i]:
                if j == 0:
                    if i == 0 or input_data[i - 1] in symbols and input_data[i + len(word)] in symbols:
                        dictionary[word] = True
                        break
                    else:
                        i = i + word_length - min(j, 1 + word.rfind(input_data[i]))
                        j = word_length - 1
                else:
                    i -= 1
                    j -= 1
            else:
                i = i + word_length - min(j, 1 + word.rfind(input_data[i]))
                j = word_length - 1
            if i > length - 1:
                break
    return dictionary


def read_to_dictionary(path):
    dictionary = {}
    symbols = '?().,!-"":\n '
    with open(path, 'r', encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                tmp1 = word.strip(symbols)
                tmp1 = tmp1.lower()
                tmp2 = tmp1
                if tmp2 not in dictionary and tmp1 != "":
                    dictionary[tmp2] = False
    file.close()
    return dictionary


def read_input_data(path):
    with open(path, 'r', encoding="utf-8") as file:
        input_data = file.read()
    input_data = input_data.lower()
    file.close()
    return input_data


def results(words_file1, words_file2):
    unique_words1 = 0
    duplicates = 0
    for word in words_file1:
        if words_file1[word]:
            duplicates += 1
        elif not words_file1[word]:
            unique_words1 += 1
    unique_words2 = int(len(words_file2)) - duplicates

    # print("Count of words in file 1 (without duplicates): " + str(len(words_file1)))
    # print("Count of words in file 2 (without duplicates): " + str(len(words_file2)))
    # print("Count of unique words in file 1: " + str(unique_words1))
    # print("Count of unique words in file 1: " + str(unique_words2))
    # print("Count of words from file 1 found in file 2:" + str(duplicates))

    save_results_to_file(words_file1, len(words_file2), unique_words1, unique_words2, duplicates)


def save_results_to_file(words_file1, words_file2, unique_words1, unique_words2, matches):
    file = open("results.txt", "w", encoding="utf-8")

    file.write("Results: \n")
    file.write("____________________________________________________________________________________________\n")
    file.write("Count of words in file 1 (without duplicates): " + str(len(words_file1)) + "\n")
    file.write("Count of words in file 2 (without duplicates): " + str(words_file2) + "\n")
    file.write("Unique words in file 1: " + str(unique_words1) + "\n")
    file.write("Unique words in file 2: " + str(unique_words2) + "\n")
    file.write("Count of words from file 1 found in file 2: " + str(matches) + "\n")

    file.write(
        "Words from file 1 not found in file 2:: \n")
    i = 1
    for word in words_file1:
        if not words_file1[word]:
            file.write(str(i) + ". " + str(word.strip().capitalize()) + "\n")
            i += 1

    file.close()


# MAIN
results(boyer_moore(read_input_data("file1.txt"), read_to_dictionary("file1.txt")), read_to_dictionary("file2.txt"))


#https://www.overleaf.com/project/5ec03273d57fc20001ff084b