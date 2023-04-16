count_word={}

    text = input("Text:")
    words=text.split()
    for i in words:
        number = count_word.get(i,0)
        count_word[i] = number + 1
    words = list(count_word.keys())
    words.sort()
    max_length=max((len(i) for i in words))
    for i in words:
        print("{:{}} : {}".format(i, max_length, count_word[i]))



