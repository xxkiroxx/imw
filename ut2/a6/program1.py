import sys

sentence = sys.argv[1]


def count_words(sentence):
    summary = {}
    words = sentence.split()
    for palabra in words:
        if palabra in summary:
            summary[palabra] += 1
        else:
            summary[palabra] = 1
    return summary
for word, count in count_words(sentence).items():
    print(f"{word} : {count}")
