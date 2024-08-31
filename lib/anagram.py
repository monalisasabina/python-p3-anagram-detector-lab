class Anagram:
      def __init__(self, word):
        self.word_letters = sorted([letter for letter in word])

      def match(self, word_list):
        match_word_list = []

        for word in word_list:
            if sorted([letter for letter in word]) == self.word_letters:
                match_word_list.append(word)

        return match_word_list
      
anagram_checker = Anagram("listen") 
print(anagram_checker.match(["enlist", "google", "inlets", "banana"]))  # Output: ['enlist', 'inlets']


    
# class Anagram:
#     def __init__(self,word):
#         self.word = word

#     def match(self,other_word):
#         return sorted(self.word) == sorted(other_word)   

# anagram_checker = Anagram("listen") 
# print(anagram_checker.match("silent"))
# print(anagram_checker.match("enlist"))  
# print(anagram_checker.match("hello")) 