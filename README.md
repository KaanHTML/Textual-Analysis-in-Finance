# Textual-Analysis-in-finance
The four steps listed below show an overview of how I conducted a textual analysis of annual reports (10-Ks). In each of the programming files you can find a more detailed description of each step. 

## Step 1 - Automatically downloading 10-Ks from SEC/Edgar
I use the Python file code "Edgar_Forms_02.py" to automatically download 10-Ks from the first quarter in each year from 2005-2021. 
For each year a folder is created, in which the respective 10-Ks can be found as text files (those text files are not included in the repository).

## Step 2 - Parsing 10-Ks to get textual analysis measures
To parse the 10-Ks, the text files the folders from the first step have to be selected. 
The Python code used here is the file "Generic_Parser_Dictionary_Readability.py" together with "Load_MasterDictionary.py". This file computes dictionary-based measures as defined by Loughran & McDonald (2011) and also readability measures. The file "Generic_Parser_Dictionary_Readability.py" outputs one excel for each year, in which the variables are computed for each 10-K in the respective year folder. The rows in the outputted excel represent a unique company, and the columns represent a textual variable. The files "2006.csv", ..., "2019.csv" show the calculated textual analysis values for all the companies in each year.

## Step 3 - Downloading stock price infromation from CapitalIQ
I then download yearly stock price returns of stocks listed on major U.S. stock exchanges on CapitalIQ.

## Step 4 - Condcting statistical analysis with R 
Having all data ready to analyse, I use R to merge the datasets: I first merge the yearly textual analysis data. Finally I merge this dataset with the stock price information downloaded from CapitalIQ. Having the final dataset, I am able to condcut several analysis such as development of readability measures over time, adjustment of the language in 10-Ks in uncertain economic times, and correlation of textual measures to the subsequent stock price measures. You can find the detailed coud in the file "Updated_SentimentAnalysis_TestCode02.Rmd"

