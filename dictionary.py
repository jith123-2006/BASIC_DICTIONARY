import nltk # pyright: ignore[reportMissingImports]

from nltk.corpus import wordnet  # pyright: ignore[reportMissingImports]



class dictionary:
    def __init__(self):
        pass
    def meaning(self,word):
        word = wordnet.synsets(word)
        from collections import Counter
        pos_counts = Counter([syn.pos() for syn in word])
    
    # Most common POS
        common_pos ,_= pos_counts.most_common(1)[0]
    
    # First synset of that POS
        main_synset = next(s for s in word if s.pos() == common_pos)
        return main_synset.definition()
    def synonyms(self,word):
        word=wordnet.synsets(word)
        return {synonyms.name() for sys in word for synonyms in sys.lemmas()}
    
    def antonyms(self,word):
        word=wordnet.synsets(word)
        return [ ant.name() for sys in word for lemma in sys.lemmas()  for ant in lemma.antonyms()]


if __name__ =="__main__":
    while True:
        word= input("enter the word to find meaning or press enter to exit : ")
        if word =="":
            print("Thank you 😊for using the dictionary")
            print("visit again!🤗")
            enter=input("Enter again to use the dictionary or press enter to exit :")
            if enter.lower()== "again":
                continue
            else:
                break
        dict_obj=dictionary()
        print("meaning: ",dict_obj.meaning(word) )
        print("synonyms: ",dict_obj.synonyms(word))
        print("antonyms: ",dict_obj.antonyms(word))
        
        

        