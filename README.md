# Textual-Analysis-in-Finance

## Step 1 - Automatically Downloading 10-Ks from SEC/Edgar
I use the Python file code "Edgar_Forms_02.py" to automatically download 10-Ks from the first quarter in each year from 2005-2021. 
For each year a folder is created, in which the respective 10-Ks can be found.

## Step 2 - Parsing 10-Ks to get textual analysis measures
For this the folders from the first step have to be selected. 
The Python code used here is the file "Generic_Parser_Dictionary_Readability.py" together with "Load_MasterDictionary.py". This file computes dictionary-based measures as defined by Loughran & McDonald (2011) and also readability measures. The file "Generic_Parser_Dictionary_Readability.py" outputs one excel for each year, in which the variables are computed for each 10-K in the respective year folder. The rows in the outputted excel represent a unique company, and the columns represent a textual variable. The files "2005.csv", ..., "2019.csv" show the calculated textual analysis values for all the companies in each year.

## Step 3 - Downloading Stock price infromation from CapitalIQ
I then download yearly stock price returns of stocks listed on major U.S. stock exchanges between 1st March 2006 to 1st March 2021


## Step 4 - Condcting statistical analysis with R 

