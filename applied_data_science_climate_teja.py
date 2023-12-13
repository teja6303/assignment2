
pip install wbgapi

import pandas as pd
import wbgapi as wb
import seaborn as sns
import matplotlib.pyplot as plt

#Pandas function definition to read the dataset values from World Indicator data
def read_data (df):
  c=pd.read_csv(df)
  return c

#Calling reading dataset function
text=read_data('/content/World_Bank_Data.csv')

#Printing the initial rows and columns
text.head(6)

#Index set function
text1=text.set_index('economy')

#Printing the initial rows and columns in transpose format
text1.T.head(8)

#Forming the economic and climate indicators
cntry_nmes = ['CHN','ARG','BGD','BGR','PAK','FRA','JPN','AUS']
ecn_vrbl = ['SP.POP.TOTL','NE.DAB.TOTL.ZS','NY.GDP.MKTP.CD','SL.UEM.1524.NE.ZS']
clm_vrbl=['EN.ATM.PM25.MC.T1.ZS','EG.ELC.RNWX.KH','EN.ATM.GHGT.KT.CE','EN.ATM.CO2E.GF.KT']
ECONMY  = wb.data.DataFrame(ecn_vrbl, cntry_nmes, mrv=7)
CLMT = wb.data.DataFrame(clm_vrbl, cntry_nmes, mrv=7)


#SP.POP.TOTL: Current population of a country
#NE.DAB.TOTL.ZS: Current expenditure of a country
#NY.GDP.MKTP.CD: Current GDP as USD of a country
#SL.UEM.1524.NE.ZS: Current youth unemployment of country
#EN.ATM.PM25.MC.T1.ZS: Value of PM2.5 pollution, exceeding WHO Interim Target-1
#EG.ELC.RNWX.KH: Production of energy from Renewable sources
#EN.ATM.GHGT.KT.CE: Emissions of Greenshouse gases
#EN.ATM.CO2E.GF.KT: Emission of CO2 using gaseous fuel

# Economic indicators over the years
ECONMY.columns = [r.replace('YR','') for r in ECONMY.columns]
ECONMY=ECONMY.stack().unstack(level=1)
ECONMY.index.names = ['Country_Name', 'Year']
ECONMY.columns
ECONMY.fillna(0)
ECONMY.head(8)

# Climate indicators over the years
CLMT.columns = [r.replace('YR','') for r in CLMT.columns]
CLMT=CLMT.stack().unstack(level=1)
CLMT.index.names = ['Country_Name', 'Year']
CLMT.columns
CLMT.fillna(0)
CLMT.head(8)

#Forming dataframes for economic and climatic indicators
e1=ECONMY.reset_index()
c1=CLMT.reset_index()
e2=e1.fillna(0)
c2=c1.fillna(0)

#Final dataframe with climate and economic variables
finl = pd.merge(e2, c2)
finl.head(6)

# Descriptive statistics summary for China
t1=finl[(finl['Country_Name']=='CHN')]
t1.describe()

"""**The average total expenditure for China is 98.18**"""

#Line plot visualisation for Emissions of Greenshouse gases in China
plt.plot(t1["Year"], t1["EN.ATM.GHGT.KT.CE"],color="purple")
plt.xlabel("Year")
plt.ylabel("EN.ATM.GHGT.KT.CE")
plt.show()

# Descriptive statistics summary for Argentina
t2=finl[(finl['Country_Name']=='ARG')]
t2.describe()

"""**The average total population of Argentina is lower than China. The average youth unemployment of Argentina is higher than China**"""

#Line plot visualisation for total expenditure in Argentina
plt.plot(t2["Year"], t2["NE.DAB.TOTL.ZS"],color="purple")
plt.xlabel("Year")
plt.ylabel("NE.DAB.TOTL.ZS")
plt.show()

# Descriptive statistics summary for Bangladesh
t3=finl[(finl['Country_Name']=='BGD')]
t3.describe()

"""**The average total electricity production from renewable sources in Bangladesh is lower than Aregntina and China. The average total population of Bangladesh is higher than Argentina but lower than China**"""

#Bar plot visualisation for current market GDP in Bangladesh
t3.plot(x="Year", y="NY.GDP.MKTP.CD", kind="bar",color="purple")

# Descriptive statistics summary for Bulgaria
t4=finl[(finl['Country_Name']=='BGR')]
t4.describe()

"""**The average Value of PM2.5 pollution, exceeding WHO Interim Target-1 in Bulgaria is lower than Argentina and Bangladesh. The average total expenditure of Bulgaria is lower than Argentina and Bangladesh.**"""

# Scatter plot visualisation for youth unemployment in Bulgaria
t4.plot(x="Year", y="SL.UEM.1524.NE.ZS", kind="scatter",color="purple")

# Descriptive statistics summary for Pakistan
t5=finl[(finl['Country_Name']=='PAK')]
t5.describe()

"""**The average total expenditure of Pakistan is higher than Bulgaria and Bangladesh. The average greenhouse gas emissions of Pakistan is higher than Bulgaria and Bangladesh.**"""

#Scatter plot visualisation for greenhouse gas emission in Pakistan
t5.plot(x="Year", y="EN.ATM.GHGT.KT.CE", kind="scatter",color="purple")

# Descriptive statistics summary for France
t6=finl[(finl['Country_Name']=='FRA')]
t6.describe()

"""**The average youth unemployment in France is higher than Pakistan and Bulgaria. The average electricity production from renewable source in France is higher than Pakistan and Bulgaria**"""

#Bar plot visualisation for youth unemployment in France
t6.plot(x="Year", y="SL.UEM.1524.NE.ZS", kind="bar",color="purple")

# Descriptive statistics summary for Japan
t7=finl[(finl['Country_Name']=='JPN')]
t7.describe()

"""**The average current GDP of Japan is higher than France and Pakistan. The total youth unemployment in Japan is lower than than France and Pakistan.**"""

# Scatter plot visualisation for total expenditure in Japan
t7.plot(x="Year", y="NE.DAB.TOTL.ZS", kind="scatter",color="purple")

# Descriptive statistics summary for Australia
t8=finl[(finl['Country_Name']=='AUS')]
t8.describe()

"""**The average total population of Australia is lower than Japan and France.**"""

#Bar plot visualisation for current GDP of Australia
t8.plot(x="Year", y="NY.GDP.MKTP.CD", kind="bar",color="purple")

"""**CORRELATION ANALYSIS - Bulgaria**"""

plt.plot(t4["NY.GDP.MKTP.CD"], t4["NE.DAB.TOTL.ZS"],color="purple")
plt.xlabel("NY.GDP.MKTP.CD")
plt.ylabel("NE.DAB.TOTL.ZS")
plt.show()

plt.plot(t4["SP.POP.TOTL"], t4["NE.DAB.TOTL.ZS"],color="purple")
plt.xlabel("SP.POP.TOTL")
plt.ylabel("NE.DAB.TOTL.ZS")
plt.show()

"""**CORRELATION ANALYSIS - CHINA**"""

plt.plot(t1["SP.POP.TOTL"], t1["NE.DAB.TOTL.ZS"],color="purple")
plt.xlabel("SP.POP.TOTL")
plt.ylabel("NE.DAB.TOTL.ZS")
plt.show()

plt.plot(t1["SP.POP.TOTL"], t1["NY.GDP.MKTP.CD"],color="purple")
plt.xlabel("SP.POP.TOTL")
plt.ylabel("NY.GDP.MKTP.CD")
plt.show()

"""**HEATMAP PICTURE**"""

#Heatmap for Pakistan
import warnings
with warnings.catch_warnings(record=True):
    a=finl[((finl['Country_Name']=='PAK'))]
    fig,axs = plt.subplots(figsize=(6, 6))
    sns.heatmap(a.corr(), annot = True, fmt= '.2f',cmap='summer')
    plt.show()
