import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


#text_file = open("/Users/adwitasingh/Documents/GitHub/cb20ML/eng.txt", "r")
#text = text_file.read()
#text_file.close()
#print(text)

def summarize(text, per):
    nlp = spacy.load('en_core_web_sm')
    document= nlp(text)
    tokenizing=[token.text for token in document]
    word_frequencies={}
    for word in document:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    sentence_tokens= [sent for sent in document.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():                            
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent]+=word_frequencies[word.text.lower()]
    select_length=int(len(sentence_tokens)*per)
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    final_summary=[word.text for word in summary]
    summary=''.join(final_summary)
    return summary

GeneratedSum = summarize(text,per)    

#with open('summariser.pkl', 'wb') as file:
#    pickle.dump(GeneratedSum, file)

#f= open("generatedsummary.txt","w+")
#f.write(summarize(text, 1.5))
#f.close()

#def print_data(data):
 #   print(data)

#def output_file(filename, data):
#    file = open(filename, "w+")
#    file.write(data)
#    file.close()

#def main():
#    generatedsummary = summarize(text, 0.5)
#    print_data(generatedsummary)
#    output_file("generatedsummary.txt", generatedsummary)

#if  __name__ == '__main__':
#    main()