"""
#This code is provided by Loughran & McDonald (https://sraf.nd.edu/textual-analysis/code/)
#I have adjusted the code, to account for readability measures. 

Program to provide generic parsing for all files in user-specified directory.
The program assumes the input files have been scrubbed,
  i.e., HTML, ASCII-encoded binary, and any other embedded document structures that are not
  intended to be analyzed have been deleted from the file.

Dependencies:
    Python:  Load_MasterDictionary.py
    Data:    LoughranMcDonald_MasterDictionary_XXXX.csv

The program outputs:
   1.  File name
   2.  File size (in bytes)
   3.  Number of words (based on LM_MasterDictionary
   4.  Proportion of positive words (use with care - see LM, JAR 2016)
   5.  Proportion of negative words
   6.  Proportion of uncertainty words
   7.  Proportion of litigious words
   8.  Proportion of modal-weak words
   9.  Proportion of modal-moderate words
  10.  Proportion of modal-strong words
  11.  Proportion of constraining words (see Bodnaruk, Loughran and McDonald, JFQA 2015)
  12.  Number of alphanumeric characters (a-z, A-Z)
  13.  Number of digits (0-9)
  14.  Number of numbers (collections of digits)
  15.  Average number of syllables
  16.  Average word length
  17.  Vocabulary (see Loughran-McDonald, JF, 2015)

  ND-SRAF
  McDonald 2016/06 : updated 2018/03
"""
import csv
import glob
import re
import string
import sys
import time
sys.path.append('C:/Users/Kaan Abudak/Desktop/Code_SentimentAnalysis')  # Modify to identify path for custom modules
import Load_MasterDictionary as LM
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from bs4 import BeautifulSoup
import unicodedata

    
# User defined directory for files to be parsed
TARGET_FILES = r'D:/Python_10K_Analysis/Test01/Forms/*.*'
# User defined file pointer to LM dictionary
MASTER_DICTIONARY_FILE = r'C:/Users/Kaan Abudak/Desktop/Code_SentimentAnalysis/' + \
                         'LoughranMcDonald_MasterDictionary_2018.csv'
# User defined output file
OUTPUT_FILE = r'D:/Python_10K_Analysis/Test01/Forms/Parser.csv'
# Setup output
OUTPUT_FIELDS = ['file name,', 'file size,', 'number of words,', '% positive,', '% negative,',
                 '% uncertainty,', '% litigious,', '% modal-weak,', '% modal moderate,',
                 '% modal strong,', '% constraining,', '# of alphabetic,', '# of digits,',
                 '# of numbers,', 'avg # of syllables per word,', 'average word length,', 'vocabulary', 'Fog_Index', 'Flesch_Index', 'Flesch-Kncaid', 'Lix-Index', 'Rix-Index']

lm_dictionary = LM.load_masterdictionary(MASTER_DICTIONARY_FILE, True)


def main(year):
    
    #specify the output directory
    f_out = open('D:/Python_10K_Analysis/Test01/Final_Parsed_Documents/' + str(year) + '.csv', 'w')
    wr = csv.writer(f_out, lineterminator='\n')
    wr.writerow(OUTPUT_FIELDS)
    
    #specify your input files, i.e. the 10-K txt files that were previously downloaded from the EDGAR server
    file_list = glob.glob('D:/Python_10K_Analysis/Test01/' + str(year) + '/*.*')
    for file in file_list:
        with open(file, 'r', encoding='UTF-8', errors='ignore') as f_in:
            doc = f_in.read()
        doc_len = len(doc)
        doc = re.sub('(May|MAY)', ' ', doc)  # drop all May month references
        doc = doc.upper()  # for this parse caps aren't informative so shift

        output_data = get_data(doc)
        output_data[0] = file
        output_data[1] = doc_len
        wr.writerow(output_data)
        print(file)


def get_data(doc):

    vdictionary = {}
    
    #_odata will correspond to the columns (varaibles) in the excel output files 
    _odata = [0] * 22
    total_syllables = 0
    word_length = 0
    
    #clean html structure 
    html_text = BeautifulSoup(doc, features="lxml")
    doc = html_text.get_text()
    for table in html_text.find_all("table"):
        table.extract()
    #only analyse the first 50k characters and start at the 1000 character    
    doc = (doc[1000:50000])    
    
    _odata[2] = 1
    tokens = re.findall('\w+', doc)  # Note that \w+ splits hyphenated words   
    for token in tokens:
        if not token.isdigit() and len(token) > 1 and token in lm_dictionary:
            _odata[2] += 1  # word count
            word_length += len(token)
            if token not in vdictionary:
                vdictionary[token] = 1
            #calculates dictionary-based measures
            if lm_dictionary[token].positive: _odata[3] += 1
            if lm_dictionary[token].negative: _odata[4] += 1
            if lm_dictionary[token].uncertainty: _odata[5] += 1
            if lm_dictionary[token].litigious: _odata[6] += 1
            if lm_dictionary[token].weak_modal: _odata[7] += 1
            if lm_dictionary[token].moderate_modal: _odata[8] += 1
            if lm_dictionary[token].strong_modal: _odata[9] += 1
            if lm_dictionary[token].constraining: _odata[10] += 1
            total_syllables += lm_dictionary[token].syllables
            if lm_dictionary[token].syllables >=3: _odata[17] +=1
            if len(token) > 6: _odata[20] +=1
            if len(token) > 6: _odata[21] +=1
              
  
    _odata[11] = len(re.findall('[A-Z]', doc))
    
    _odata[12] = len(re.findall('[0-9]', doc))
    
    doc = re.sub('(?!=[0-9])(\.|,)(?=[0-9])', '', doc)
    phrases = sent_tokenize(str(doc))
    sentences = (len(phrases)
    total_words_sentence = (_odata[2]/sentences) 
    
    #Readability Measures 
    #Fog Index
    _odata[17] = 0.4*(total_words_sentence+ 100*(_odata[17] / _odata[2]))
    
    #Flesch_Index
    _odata[18] = 206.385 - 1.015*(total_words_sentence) - 84.6*(total_syllables / _odata[2])
    
    #Flesch-Kincaid Index
    _odata[19] = -15.58 + 0.39 * total_words_sentence + 11.8*(total_syllables / _odata[2])
    
    #Lix Index 
    _odata[20] = total_words_sentence + 100 * _odata[20]/_odata[2]
    
    #Rix Index 
    _odata[21] = _odata[21]/((doc.count(".")+sentences)/2)
    
    doc = doc.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))
    
    _odata[13] = len(re.findall(r'\b[-+\(]?[$€£]?[-+(]?\d+\)?\b', doc))
    
    _odata[14] = total_syllables / _odata[2]
    
    _odata[15] = word_length / _odata[2]
    
    _odata[16] = len(vdictionary)
 
    
    # Convert counts to %
    for i in range(3, 10 + 1):
        _odata[i] = (_odata[i] / _odata[2]) * 100
    # Vocabulary
    
        
    return _odata


if __name__ == '__main__':
    print('\n' + time.strftime('%c') + '\nGeneric_Parser.py\n')
    #Run the function
    for year in range(2006, 2021):
        main(year)
    print('\n' + time.strftime('%c') + '\nNormal termination.')
