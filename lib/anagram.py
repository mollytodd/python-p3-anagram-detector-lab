class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        matched_words = []
        for word in word_list:
            if sorted(self.word) == sorted(word):
                matched_words.append(word)
        return matched_words if matched_words else []
