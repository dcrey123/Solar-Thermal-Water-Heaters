#This code reads in hourly irradiance ("global horizontal irradiance" or GHI) & ground reflection ("surface albedo") data from every state and calculates that data into monthly average irradiation and ground reflection
#State data was gathered from the National Renewable Energy Laboratory (NREL) website into 50 csv files to be read.
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import numpy as np
from scipy import stats
import pandas as pd


# In[2]:


def get_data(filename):
    month = []
    GHI = []
    albedo = []
    
    #open file
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter = ",", quotechar="|")
        for col in spamreader:
            month.append(col[1]) #get month data
            GHI.append(col[5]) #get GHI
            albedo.append(col[6]) #get albedo
        
    month=month[3:]
    GHI=GHI[3:]
    albedo=albedo[3:]

    month_new=[]
    GHI_new=[]
    albedo_new=[]
    for i in range(0, len(GHI)):
        #month_new.append(float(month[i]))
        GHI_new.append(float(GHI[i]))
        albedo_new.append(float(albedo[i]))
        
    all_months=[] # array to store all sums
    tot1=[]
    for j in range(0, 744):
        #print(j, month[j], GHI_new[j])
        tot1.append(GHI_new[j])

    val1=np.sum(tot1)
    val1=val1*3600/1e6
    val1=val1/31.0
    #print(val1)
    all_months.append(val1)
    
    tot2=[]
    for j in range(744, 1416):
        #print(j, month[j], GHI_new[j])
        tot2.append(GHI_new[j])

    val2=np.sum(tot2)
    val2=val2*3600/10e6
    val2=val2/28.0
    #print(tot2)
    all_months.append(val2)

    tot3=[]
    for j in range(1416, 2160):
        #print(j, month[j], GHI_new[j])
        tot3.append(GHI_new[j])

    val3=np.sum(tot3)
    val3=val3*3600/1e6
    val3=val3/31.0
    
    #print(tot3)
    all_months.append(val3)

    tot4=[]
    for j in range(2160, 2880):
        #print(j, month[j], GHI_new[j])
        tot4.append(GHI_new[j])

    val4=np.sum(tot4)
    val4=val4*3600/1e6
    val4=val4/30.0
    
    #print(tot4)
    all_months.append(val4)
    
    tot5=[]
    for j in range(2880, 3624):
        #print(j, month[j], GHI_new[j])
        tot5.append(GHI_new[j])

    val5=np.sum(tot5)
    val5=val5*3600/1e6
    val5=val5/31.0
    #print(tot5)
    all_months.append(val5)
    
    tot6=[]
    for j in range(3624, 4344):
        #print(j, month[j], GHI_new[j])
        tot6.append(GHI_new[j])

    val6=np.sum(tot6)
    val6=val6*3600/1e6
    val6=val6/30.0
    #print(tot6)
    all_months.append(val6)
    
    tot7=[]
    for j in range(4344, 5088):
        #print(j, month[j], GHI_new[j])
        tot7.append(GHI_new[j])

    val7=np.sum(tot7)
    val7=val7*3600/1e6
    val7=val7/31.0
    #print(tot7)
    all_months.append(val7)
    
    tot8=[]
    for j in range(5088, 5832):
        #print(j, month[j], GHI_new[j])
        tot8.append(GHI_new[j])

    val8=np.sum(tot8)
    val8=val8*3600/1e6
    val8=val8/31.0
    #print(tot8)
    all_months.append(val8)
    
    tot9=[]
    for j in range(5832, 6552):
        #print(j, month[j], GHI_new[j])
        tot9.append(GHI_new[j])

    val9=np.sum(tot9)
    val9=val9*3600/1e6
    val9=val9/30.0
    #print(tot9)
    all_months.append(val9)
    
    tot10=[]
    for j in range(6552, 7296):
        #print(j, month[j], GHI_new[j])
        tot10.append(GHI_new[j])

    val10=np.sum(tot10)
    val10=val10*3600/1e6
    val10=val10/31.0
    #print(tot10)
    all_months.append(val10)
    
    tot11=[]
    for j in range(7296, 8016):
        #print(j, month[j], GHI_new[j])
        tot11.append(GHI_new[j])

    val11=np.sum(tot11)
    val11=val11*3600/1e6
    val11=val11/30.0
    #print(tot11)
    all_months.append(val11)
    
    tot12=[]
    for j in range(8016, 8760):
        #print(j, month[j], GHI_new[j])
        tot12.append(GHI_new[j])

    val12=np.sum(tot12)
    val12=val12*3600/1e6
    val12=val12/31.0
    #print(tot12)
    all_months.append(val12)
    
    avg = np.sum(albedo_new)/len(albedo_new) 
    
    return all_months, avg


# In[3]:


alabama = "alabama.csv"
alaska = "alaska.csv"
arizona = "arizona.csv"
arkansas = "arkansas.csv"
california = "california.csv"
colorado = "colorado.csv"
connecticut = "connecticut.csv"
delaware = "delaware.csv"
florida = "florida.csv"
georgia = "georgia.csv"
hawaii = "hawaii.csv"
idaho = "idaho.csv"
illinois = "illinois.csv"
indiana = "indiana.csv"
iowa = "iowa.csv"
kansas = "kansas.csv"
kentucky = "kentucky.csv"
louisiana = "louisiana.csv"
maine = "maine.csv"
maryland = "maryland.csv"
massachusetts = "massachusetts.csv"
michigan = "michigan.csv"
minnesota = "minnesota.csv"
mississippi = "mississippi.csv"
missouri = "missouri.csv"
montana = "montana.csv"
nebraska = "nebraska.csv"
nevada = "nevada.csv"
newhampshire = "newhampshire.csv"
newjersey = "newjersey.csv"
newmexico = "newmexico.csv"
newyork = "newyork.csv"
northcarolina = "northcarolina.csv"
northdakota = "northdakota.csv"
ohio = "ohio.csv"
oklahoma = "oklahoma.csv"
oregon = "oregon.csv"
pennsylvania = "pennsylvania.csv"
rhodeisland = "rhodeisland.csv"
southcarolina = "southcarolina.csv"
southdakota = "southdakota.csv"
tennessee = "tennessee.csv"
texas = "texas.csv"
utah = "utah.csv"
vermont = "vermont.csv"
virginia = "virginia.csv"
washington = "washington.csv"
westvirginia = "westvirginia.csv"
wisconsin = "wisconsin.csv"
wyoming = "wyoming.csv"


# In[4]:


#Store all states' sums
all_state_sum =[]
all_state_albedo =[]

get_sum, avg = get_data(alabama)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(alaska)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(arizona)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(arkansas)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(california)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(colorado)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(connecticut)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(delaware)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(florida)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(georgia)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(hawaii)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(idaho)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(illinois)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(indiana)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(iowa)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(kansas)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(kentucky)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(louisiana)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(maine)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(maryland)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(massachusetts)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(michigan)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(minnesota)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(mississippi)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(missouri)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(montana)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(nebraska)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(nevada)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(newhampshire)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(newjersey)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(newmexico)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(newyork)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(northcarolina)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(northdakota)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(ohio)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(oklahoma)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(oregon)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(pennsylvania)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(rhodeisland)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(southcarolina)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(southdakota)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(tennessee)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(texas)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(utah)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(vermont)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(virginia)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(washington)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(westvirginia)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg  = get_data(wisconsin)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)

get_sum, avg = get_data(wyoming)
all_state_sum.append(get_sum)
all_state_albedo.append(avg)


# In[5]:


all_state_sum
len(all_state_sum)

len(all_state_albedo)


# In[6]:


len(all_state_albedo)


# In[7]:


results = pd.DataFrame(data=all_state_sum)
results.to_csv("avgmondailyrad.csv")


# In[8]:


results1 = pd.DataFrame(data=all_state_albedo)
results1.to_csv("albedo.csv")


# In[ ]:




