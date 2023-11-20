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
   "execution_count": 209,
   "id": "74c865b0-b5d0-4cd5-8595-6117e8fbf140",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''Importation of webscraping and datascience packages'''\n",
    "#!pip install -q lxml\n",
    "import numpy as np\n",
    "import bs4 #BeautifulSoup4 for scraping\n",
    "import lxml\n",
    "import pandas #datascience library\n",
    "import urllib #scraping\n",
    "import time\n",
    "import requests #scraping\n",
    "import random\n",
    "import yaml #to use yml files\n",
    "from urllib import request #to get the html source code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "id": "2338ea85-c283-4982-bf63-e5eb39ebdfff",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/tmp/ipykernel_308/3182924863.py:3: FutureWarning: Passing literal html to 'read_html' is deprecated and will be removed in a future version. To read from a literal string, wrap it in a 'StringIO' object.\n",
      "  proxy_list = pandas.read_html(response.text)[0]\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>IP Address</th>\n",
       "      <th>Port</th>\n",
       "      <th>Code</th>\n",
       "      <th>Country</th>\n",
       "      <th>Anonymity</th>\n",
       "      <th>Google</th>\n",
       "      <th>Https</th>\n",
       "      <th>Last Checked</th>\n",
       "      <th>url</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>213.212.220.210</td>\n",
       "      <td>8080</td>\n",
       "      <td>EG</td>\n",
       "      <td>Egypt</td>\n",
       "      <td>elite proxy</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>6 secs ago</td>\n",
       "      <td>http://213.212.220.210:8080</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>203.74.125.18</td>\n",
       "      <td>8888</td>\n",
       "      <td>TW</td>\n",
       "      <td>Taiwan</td>\n",
       "      <td>anonymous</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>6 secs ago</td>\n",
       "      <td>http://203.74.125.18:8888</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>190.63.35.30</td>\n",
       "      <td>9812</td>\n",
       "      <td>EC</td>\n",
       "      <td>Ecuador</td>\n",
       "      <td>elite proxy</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>6 secs ago</td>\n",
       "      <td>http://190.63.35.30:9812</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>191.96.100.33</td>\n",
       "      <td>3128</td>\n",
       "      <td>AE</td>\n",
       "      <td>United Arab Emirates</td>\n",
       "      <td>elite proxy</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>6 secs ago</td>\n",
       "      <td>http://191.96.100.33:3128</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>165.227.0.192</td>\n",
       "      <td>80</td>\n",
       "      <td>US</td>\n",
       "      <td>United States</td>\n",
       "      <td>elite proxy</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>26 secs ago</td>\n",
       "      <td>http://165.227.0.192:80</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        IP Address  Port Code               Country    Anonymity Google Https  \\\n",
       "0  213.212.220.210  8080   EG                 Egypt  elite proxy     no   yes   \n",
       "1    203.74.125.18  8888   TW                Taiwan    anonymous     no   yes   \n",
       "2     190.63.35.30  9812   EC               Ecuador  elite proxy     no   yes   \n",
       "3    191.96.100.33  3128   AE  United Arab Emirates  elite proxy     no   yes   \n",
       "4    165.227.0.192    80   US         United States  elite proxy    yes    no   \n",
       "\n",
       "  Last Checked                          url  \n",
       "0   6 secs ago  http://213.212.220.210:8080  \n",
       "1   6 secs ago    http://203.74.125.18:8888  \n",
       "2   6 secs ago     http://190.63.35.30:9812  \n",
       "3   6 secs ago    http://191.96.100.33:3128  \n",
       "4  26 secs ago      http://165.227.0.192:80  "
      ]
     },
     "execution_count": 210,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''We get a list of proxies from the website free-proxy-list.net to avoid being detected as a robot by the website'''\n",
    "response = requests.get(\"https://free-proxy-list.net/\")\n",
    "proxy_list = pandas.read_html(response.text)[0]\n",
    "proxy_list[\"url\"] = \"http://\" + proxy_list[\"IP Address\"] + \":\" + proxy_list[\"Port\"].astype(str)\n",
    "proxy_list.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 211,
   "id": "3e383cc9-078f-4353-a95c-388290a1034a",
   "metadata": {},
   "outputs": [],
   "source": [
    "https_proxies = proxy_list[proxy_list[\"Https\"] == \"yes\"] #We only keep the proxies working with https"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "id": "ef2cbe67-18d2-45fe-9046-714d5362c755",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''We use a user-agent and other headers also to avoid being detected'''\n",
    "'''We open the file headers in which we have different headers (for Chrome,Firefox...) and save them in browser_headers'''\n",
    "with open(\"headers.yml\") as f_headers:\n",
    "    browser_headers = yaml.safe_load(f_headers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "id": "12bba5cc-3f03-4a37-a7df-89573b2ee3bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Proxy http://191.96.100.33:3128 OK, added to good_proxy list\n",
      "Proxy http://167.71.41.76:8080 OK, added to good_proxy list\n"
     ]
    }
   ],
   "source": [
    "'''We only keep valid proxies thanks to this algorithm'''\n",
    "url = \"https://httpbin.org/ip\" #This will return the ip address we are using\n",
    "good_proxies = set()\n",
    "for proxy_url in https_proxies[\"url\"]:\n",
    "    proxies = {\n",
    "        \"http\": proxy_url,\n",
    "        \"https\": proxy_url,\n",
    "    }\n",
    "    \n",
    "    try:\n",
    "        response = requests.get(url, headers=list(browser_headers.values())[random.randint(0,len(list(browser_headers.values())-1)], proxies=proxies, timeout=2)\n",
    "        good_proxies.add(proxy_url)\n",
    "        print(f\"Proxy {proxy_url} OK, added to good_proxy list\")\n",
    "    except Exception:\n",
    "        pass\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
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
   "execution_count": 215,
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
   "execution_count": 218,
   "id": "2aa3085b-a24c-4280-9bd4-8a314355c137",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''We scrap the marks for each arrondissement thanks to a loop on the page urls of each arrondissement'''\n",
    "for i in range(20):\n",
    "    headers=list(browser_headers.values())[random.randint(0,len(list(browser_headers.values()))-1)]\n",
    "    '''Getting the source code of the arrondissement page'''\n",
    "    url_arr = urls[i] #url of the arrondissement page to scrap\n",
    "    request_text = requests.get(url_arr,proxies={\"http\": list(good_proxies)[random.randint(0,len(good_proxies)-1)],\"https\": list(good_proxies)[random.randint(0,len(good_proxies)-1)]},headers=headers).text #getting the html source code\n",
    "    '''Create a Python object from the web page with BeautifulSoup4 to facilitate html data retrieval'''\n",
    "    page_arr = bs4.BeautifulSoup(request_text, \"lxml\")\n",
    "    '''Getting the global mark of the arrondissement'''\n",
    "    global_mark = page_arr.find('p', {'id' : 'ng'})\n",
    "    '''Getting the table of marks for the 9 criterias + the global mark as a dataframe of one row and 10 columns'''\n",
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
    "    df_marks_arrondissements=pandas.concat([df_marks_arrondissements,df_marks])# We finally add this line to the final DataFrame\n",
    "    time.sleep(random.randint(1,5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 219,
   "id": "202ffd6b-2903-4b4d-9d1d-5787221c5d8a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Environnement</th>\n",
       "      <th>Transports</th>\n",
       "      <th>Sécurité</th>\n",
       "      <th>Santé</th>\n",
       "      <th>Sports et loisirs</th>\n",
       "      <th>Culture</th>\n",
       "      <th>Enseignement</th>\n",
       "      <th>Commerces</th>\n",
       "      <th>Qualité de vie</th>\n",
       "      <th>Note Globale</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Paris 9e</th>\n",
       "      <td>5,14</td>\n",
       "      <td>8,50</td>\n",
       "      <td>6,24</td>\n",
       "      <td>7,62</td>\n",
       "      <td>6,17</td>\n",
       "      <td>8,50</td>\n",
       "      <td>7,24</td>\n",
       "      <td>8,55</td>\n",
       "      <td>7,26</td>\n",
       "      <td>7,25</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Environnement Transports Sécurité Santé Sports et loisirs Culture  \\\n",
       "Paris 9e          5,14       8,50     6,24  7,62              6,17    8,50   \n",
       "\n",
       "         Enseignement Commerces Qualité de vie Note Globale  \n",
       "Paris 9e         7,24      8,55           7,26         7,25  "
      ]
     },
     "execution_count": 219,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''We obtain this final table of marks for all arrondissements'''\n",
    "df_marks_arrondissements"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 198,
   "id": "a5e3d5b9-ec9d-417c-81db-39a8cd1706f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''We save this dataframe in a excel file \"Notes_arrondissements\" '''\n",
    "writer=pandas.ExcelWriter(\"Notes_arrondissements.xlsx\")\n",
    "df_marks_arrondissements.to_excel(writer)"
   ]
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
