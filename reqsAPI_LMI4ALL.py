import requests
import pandas as pd


r = requests.get("http://api.lmiforall.org.uk/api/v1/vacancies/search?keywords=cook")

print (r.text) # check what we got. its everything together so a bit messy!

json_r = r.json()    #parse the text into json


#try to flatten json into csv. This is an initial try. 
#if its really nested (date info in this case) 
#more preprocessing needed here.


df=pd.DataFrame.from_records(json_r)

#

print(df)
