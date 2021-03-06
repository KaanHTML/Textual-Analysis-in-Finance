# Textual-Analysis-in-finance
The four steps listed below show an overview of how I conducted a textual analysis of annual reports (10-Ks). In each of the programming files you can find a more detailed description. I use Python to download and parse the 10-Ks and R to conduct the statistical analysis. 

## Step 1 - Automatically downloading 10-Ks from SEC/EDGAR server
I use the Python file code "Edgar_Forms_02.py" to automatically download 10-Ks from the first quarter in each year from 2006-2019. 
For each year a folder is created, in which the respective 10-Ks can be found as text files (those text files are not uploaded in the repository).

## Step 2 - Parsing 10-Ks to get textual analysis measures
To parse the 10-Ks, the txt files in the folders (created in the first step) have to be selected. 
The Python code used for the parsing procedure is the file "Generic_Parser_Dictionary_Readability.py" together with "Load_MasterDictionary.py". This file computes dictionary-based measures as defined by Loughran & McDonald (2011) and also readability measures. The file "Generic_Parser_Dictionary_Readability.py" outputs a csv file for each year, in which the variables are computed for the 10-Ks in the respective year folder. The rows in the outputted csv file represent the unique companies, and the columns represent the textual variables. The files "2006.csv", ..., "2019.csv" show the calculated textual analysis values for all the companies in each year.

## Step 3 - Downloading stock price information from CapitalIQ
I then download yearly stock price returns of stocks listed on major U.S. stock exchanges on CapitalIQ. The corresponding csv file is the “Yearly_StockData.csv”.

## Step 4 - Conducting statistical analysis with R 
Having all data ready to analyse, I use R to merge the datasets: I first merge the yearly textual analysis data. Finally, I merge this dataset with the stock price information downloaded from CapitalIQ. Having the final dataset, I am able to conduct several analyses such as development of readability measures over time, adjustment of the language in 10-Ks according to the economic development, and correlation of textual measures to the subsequent stock price measures. You can find the detailed code of the statistical analysis in the file "Updated_SentimentAnalysis_TestCode02.Rmd". The code is structured as follows: 
  - line 14-207; Part 0: Preparing the Data 
  - line 211-259; Summary Statistics
  - line 262-358: Part 1 of empirical analysis: Adjustment of language in 10Ks according to economic development 
  - line 363-439: Part 2 of empirical analysis: Development of complexity of 10Ks
  - line 440-500: Part 3 of empirical analysis: Correlation between stock market return and textual measures

