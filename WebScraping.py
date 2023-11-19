{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "47b9c91d-ef49-4b5b-bfd4-d943e6146e15",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'We want to scrap the marks that citizens of Paris have given to their arrondissement in the website ville-ideale.fr . The marks are out of 10 and the global mark is :(mean of 8 criterias + quality of life criteria) / 2  . '"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''We want to scrap the marks that citizens of Paris have given to their arrondissement in the website ville-ideale.fr . The marks are out of 10 and the global mark is :(mean of 8 criterias + quality of life criteria) / 2  . '''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "74c865b0-b5d0-4cd5-8595-6117e8fbf140",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''Importation of webscraping and datascience packages'''\n",
    "#!pip install -q lxml\n",
    "import numpy as np\n",
    "import bs4 #BeautifulSoup4\n",
    "import lxml\n",
    "import pandas\n",
    "import urllib\n",
    "\n",
    "from urllib import request #to get the html source code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "1de85270-e475-4dec-ab62-05b9f8ac0c37",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''Getting the source code of Paris 1 page'''\n",
    "url_Paris_1 = \"https://www.ville-ideale.fr/paris-1er-arrondissement_75101\" #url of the page to scrap\n",
    "    \n",
    "request_text = request.urlopen(url_Paris_1).read() #getting the html source code\n",
    "#print(request_text[:1000])   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "28487502-3a64-47d2-9ceb-efc5b609f39e",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''Create a Python object from the web page with BeautifulSoup4 to facilitate html data retrieval'''\n",
    "page_Paris_1 = bs4.BeautifulSoup(request_text, \"lxml\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "cd9938fa-6eda-46ce-93b3-6eef0393f62d",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''Getting the global mark of the arrondissement'''\n",
    "global_mark = page_Paris_1.find('p', {'id' : 'ng'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "cfdd8c01-560b-4885-bb87-13139cfc7f90",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'NoneType' object has no attribute 'find_all'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[96], line 3\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;124;03m'''Getting the table of marks for the 9 criterias + the global mark as a dataframe of one line and 10 columns'''\u001b[39;00m\n\u001b[1;32m      2\u001b[0m table_marks \u001b[38;5;241m=\u001b[39m page_Paris_1\u001b[38;5;241m.\u001b[39mfind(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtable\u001b[39m\u001b[38;5;124m'\u001b[39m, {\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m'\u001b[39m : \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtablonotes\u001b[39m\u001b[38;5;124m'\u001b[39m})\n\u001b[0;32m----> 3\u001b[0m rows_marks \u001b[38;5;241m=\u001b[39m \u001b[43mtable_marks\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mfind_all\u001b[49m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtr\u001b[39m\u001b[38;5;124m'\u001b[39m) \u001b[38;5;66;03m#Getting the lines of the table\u001b[39;00m\n\u001b[1;32m      4\u001b[0m df_marks\u001b[38;5;241m=\u001b[39mpandas\u001b[38;5;241m.\u001b[39mDataFrame()\n\u001b[1;32m      5\u001b[0m \u001b[38;5;66;03m#We will create two lists: one for criterias and one for corresponding marks using each row of the table\u001b[39;00m\n",
      "\u001b[0;31mAttributeError\u001b[0m: 'NoneType' object has no attribute 'find_all'"
     ]
    }
   ],
   "source": [
    "'''Getting the table of marks for the 9 criterias + the global mark as a dataframe of one line and 10 columns'''\n",
    "table_marks = page_Paris_1.find('table', {'id' : 'tablonotes'})\n",
    "rows_marks = table_marks.find_all('tr') #Getting the lines of the table\n",
    "df_marks=pandas.DataFrame()\n",
    "#We will create two lists: one for criterias and one for corresponding marks using each row of the table\n",
    "criteria_list=[]\n",
    "marks_list=[]\n",
    "for row in rows_marks:\n",
    "    criteria_list.append(row.find('th').text.strip())\n",
    "    marks_list.append(row.find('td').text.strip())\n",
    "    \n",
    "df_marks=pandas.DataFrame(marks_list).transpose() #We create a 1 line dataframe with the marks for the 9 criterias\n",
    "df_marks.columns=criteria_list #We assign the names of the criterias to the columns\n",
    "df_marks[\"Note Globale\"]=global_mark.text.strip()[:4] #We add the global mark (one column more)\n",
    "df_marks.index=[\"Paris 1er\"] #We give the line the name of the arrondissement\n",
    "df_marks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "72f61244-5ef1-482a-8e2b-a96a39995454",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''We first create lists for name of arrondissement and for postal codes to find the corresponding web page on the website ville-ideale.fr'''\n",
    "arrondissements_list= [\"1er\"]+[str(i) + \"e\" for i in range(2,21)]\n",
    "postal_codes_list=[\"751\"+\"0\"+ str(i) if i in range(1,10) else \"751\"+str(i) for i in range(1,21)]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "0c089330-a285-4803-958c-80788b04862a",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''We create a list of the url of the web pages of each arrondissement on the website ville-ideale.fr'''\n",
    "arrondissements_table=[[arrondissements_list[i],postal_codes_list[i]] for i in range(20)]\n",
    "urls=[\"https://www.ville-ideale.fr/paris-\"+arr[0]+\"-arrondissement_\"+ arr[1] for arr in arrondissements_table]\n",
    "'''We initialise the final DataFrame that will contain all the marks for all arrondissements'''\n",
    "df_marks_arrondissements=pandas.DataFrame()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "2aa3085b-a24c-4280-9bd4-8a314355c137",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.ville-ideale.fr/paris-1er-arrondissement_75101\n",
      "b''\n",
      "None\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'NoneType' object has no attribute 'find_all'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[77], line 15\u001b[0m\n\u001b[1;32m     13\u001b[0m table_marks \u001b[38;5;241m=\u001b[39m page_arr\u001b[38;5;241m.\u001b[39mfind(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtable\u001b[39m\u001b[38;5;124m'\u001b[39m, {\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m'\u001b[39m : \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtablonotes\u001b[39m\u001b[38;5;124m'\u001b[39m})\n\u001b[1;32m     14\u001b[0m \u001b[38;5;28mprint\u001b[39m(table_marks)\n\u001b[0;32m---> 15\u001b[0m rows_marks \u001b[38;5;241m=\u001b[39m \u001b[43mtable_marks\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mfind_all\u001b[49m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtr\u001b[39m\u001b[38;5;124m'\u001b[39m) \u001b[38;5;66;03m#Getting the lines of the table\u001b[39;00m\n\u001b[1;32m     16\u001b[0m df_marks\u001b[38;5;241m=\u001b[39mpandas\u001b[38;5;241m.\u001b[39mDataFrame()\n\u001b[1;32m     17\u001b[0m \u001b[38;5;66;03m#We will create two lists: one for criterias and one for corresponding marks using each row of the table\u001b[39;00m\n",
      "\u001b[0;31mAttributeError\u001b[0m: 'NoneType' object has no attribute 'find_all'"
     ]
    }
   ],
   "source": [
    "'''We scrap the marks for each arrondissement thanks to a loop on the page urls of each arrondissement'''\n",
    "for i in range(20):\n",
    "    '''Getting the source code of the arrondissement page'''\n",
    "    url_arr = urls[i] #url of the arrondissement page to scrap\n",
    "    request_text = request.urlopen(url_arr).read() #getting the html source code\n",
    "    '''Create a Python object from the web page with BeautifulSoup4 to facilitate html data retrieval'''\n",
    "    page_arr = bs4.BeautifulSoup(request_text, \"lxml\")\n",
    "    '''Getting the global mark of the arrondissement'''\n",
    "    global_mark = page_arr.find('p', {'id' : 'ng'})\n",
    "    '''Getting the table of marks for the 9 criterias + the global mark as a dataframe of one line and 10 columns'''\n",
    "    table_marks = page_arr.find('table', {'id' : 'tablonotes'})\n",
    "    rows_marks = table_marks.find_all('tr') #Getting the lines of the table\n",
    "    df_marks=pandas.DataFrame()\n",
    "    #We will create two lists: one for criterias and one for corresponding marks using each row of the table\n",
    "    criteria_list=[]\n",
    "    marks_list=[]\n",
    "    for row in rows_marks:\n",
    "        criteria_list.append(row.find('th').text.strip())\n",
    "        marks_list.append(row.find('td').text.strip())\n",
    "    \n",
    "    df_marks=pandas.DataFrame(marks_list).transpose() #We create a 1 line dataframe with the marks for the 9 criterias\n",
    "    df_marks.columns=criteria_list #We assign the names of the criterias to the columns\n",
    "    df_marks[\"Note Globale\"]=global_mark.text.strip()[:4] #We add the global mark (one column more)\n",
    "    df_marks.index=[\"Paris \"+arrondissements_list[i]] #We give the line the name of the arrondissement\n",
    "    df_marks_arrondissements=pandas.concat([df_marks_arrondissements,df_marks])# We finally add this line to the final DataFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "202ffd6b-2903-4b4d-9d1d-5787221c5d8a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['1er', '2e', '3e', '4e', '5e', '6e', '7e', '8e', '9e', '10e',\n",
       "       '11e', '12e', '13e', '14e', '15e', '16e', '17e', '18e', '19e',\n",
       "       '20e'], dtype='<U5')"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_marks_arrondissements"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "a5e3d5b9-ec9d-417c-81db-39a8cd1706f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''We save this dataframe in a excel file \"Notes_arrondissements\" '''\n",
    "writer=pandas.ExcelWriter(\"Notes_arrondissements.xlsx\")\n",
    "df_marks_arrondissements.to_excel(writer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33a6b150-a1ba-432c-ab4e-a1a91eebfcef",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
