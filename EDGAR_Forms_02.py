# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 08:38:52 2021

@author: Kaan Abudak
"""
import os
import requests


def download_masterindex(year, qtr, flag=False):
    # Download Master.idx from EDGAR
    # Loop accounts for temporary server/ISP issues
    # ND-SRAF / McDonald : 201606

    from urllib.request import Request, urlopen

    PARM_ROOT_PATH = 'https://www.sec.gov/Archives/edgar/full-index/'
    
    append_path = str(year) + '/QTR' + str(qtr) + '/master.idx'  # /master.idx => nonzip version
   
    sec_url = PARM_ROOT_PATH + append_path

    req = Request(sec_url, headers={'User-Agent': 'Mozilla/5.0'})

    records = urlopen(req).read().decode('utf-8', 'ignore').splitlines()[10:]

        
    return records

#Creating base_URL 
base_url = 'https://www.sec.gov/Archives/'

for year in range(2005, 2021):
         
        #creating new folder              
        #directory
        directory = str(year)
        
        # Parent Directory path
        parent_dir = "D:/Python_10K_Analysis/Test01"
        
        # Path
        path = parent_dir + '/' +  directory
        print(path)
        # Create the directory
        # 'GeeksForGeeks' in
        # '/home / User / Documents'
        try: 
            os.mkdir(path) 
        except OSError as error: 
           print(error)  
           
        #Creating the masterindex containing all URL in that year for 10Ks
        masterindex = (download_masterindex(year = year, qtr= 1, flag=False))
        
        dict_list = {}
        
        for item in masterindex[1:]:
        
             components = item.split('|')

             if "10-K" in components:
        
                 components_norm = components[-1].replace("-", "")
        
                 url_components = components[-1].split("/")
        
                 first_term_url = url_components[0]
        
                 second_term_url = url_components[1]
        
                 third_term_url = url_components[2]
        
                 fourth_term_for_url = components_norm.split("/")[-1].split(".")[0]
        
                 fifth_term_for_url = url_components[3]
        
                 full_url = base_url + first_term_url + '/' + second_term_url + '/' + third_term_url + '/' + fourth_term_for_url + '/' + fifth_term_for_url 
        
                 if url_components[2] not in dict_list:
                     
                     dict_list[url_components[2]] = full_url
               
                 myfile = requests.get(full_url)

                 created_file = open(str(path) + '/' + str(third_term_url) + '.txt', 'wb').write(myfile.content)
                 
                 size = os.path.getsize(str(path) + '/' + str(third_term_url) + '.txt')
                 
                 if size < 10000:
                     os.remove(str(path) + '/' + str(third_term_url) + '.txt')
        
  
print(len(dict_list))






