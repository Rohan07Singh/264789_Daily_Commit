def is_word_present(sentence, word):
    s=sentence.split(" ")
    for i in s:
        if(i==word):
            print("True")
    print("False")
s=input("Enter a  sentence")
word=input("Enter the word to be searched")
is_word_present(s,word)