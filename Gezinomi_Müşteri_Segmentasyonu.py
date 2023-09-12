
GÖREV_1
###############################Soru_1#####################################################
import numpy as np
import pandas as pd
df = pd.read_excel("datasets/miuul_gezinomi.xlsx")
df.head()
pd.set_option("display.float_format", lambda x: "%.2f" % x)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

def check_df(dataframe, head=5):
    print("###############Shape###############################")
    print(dataframe.shape)
    print("###############Dtypes###############################")
    print(dataframe.dtypes)
    print("###############Head################################")
    print(dataframe.head(head))
    print("###############tail################################")
    print(dataframe.tail(head))
    print("###############NA##################################")
    print(dataframe.isnull().sum())
    print("###############Quantiles############################")
    print(dataframe.describe([0, 0.05, 0.25, 0.50, 0.75, 0.95, 0.99]).T)

check_df(df)
###############################Soru_2#####################################################
df["SaleCityName"].nunique()
df["SaleCityName"].value_counts()
###############################Soru_3#####################################################
df["ConceptName"].nunique()
###############################Soru_4#####################################################
df["ConceptName"].value_counts()
###############################Soru_5#####################################################
df.groupby("SaleCityName").agg({"Price":"sum"})
df.groupby(by=["SaleCityName"]).agg({"Price":"sum"}) # by= birden fazla kategorik değişkene göre kırılım yapmak için by= daha uygun bir yöntem
df.groupby("SaleCityName")["Price"].sum()
###############################Soru_6#####################################################
df.groupby("ConceptName").agg({"Price":"sum"})
###############################Soru_7#####################################################
df.groupby("SaleCityName").agg({"Price":"mean"})
###############################Soru_8#####################################################
df.groupby("ConceptName").agg({"Price":"mean"})
###############################Soru_9#####################################################
df.groupby(by=["SaleCityName","ConceptName"]).agg({"Price":"mean"})
df.pivot_table("Price", "SaleCityName", "ConceptName")

GÖREV2
###########################################################################################
bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
label = ["Last_Minuters", "Potential_Planners", "Planners", "Early_Bookers"] #aralıklarla aynı sırada isimleri girilir

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=label)

df["SaleCheckInDayDiff"].max()
df.head()
df.tail()
df["EB_Score"].value_counts()
df["EB_Score"].isnull().sum()
df["SaleCheckInDayDiff"].isnull().sum()
type(df["EB_Score"].mode()) # pandas series
type(df["EB_Score"].mode()[0]) #str
# (0,7] --- "Last Minuters"
# (7,30] --- "Potential Planners"
# (30,90] --- "Planners"
# (90,max] --- "Early Bookers"

GÖREV3
########################################################################################
df.groupby(by=["SaleCityName", "ConceptName", "EB_Score"]).agg({"Price":["mean", "count"]})
pd.set_option("display.max_rows", None)
df.groupby(by=["SaleCityName", "ConceptName", "Seasons"]).agg({"Price":["mean", "count"]})
df["Seasons"].value_counts()
df.groupby(by=["SaleCityName", "ConceptName", "CInDay"]).agg({"Price":["mean", "count"]})

GÖREV4
########################################################################################
df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price":"mean"})
df["Price"].max()
agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price":"mean"}).sort_values("Price", ascending=False)
agg_df.head(20)

GÖREV5
########################################################################################
df.groupby(["SaleCityName", "ConceptName", "EB_Score"]).agg({"Price":["mean", "count"]}).reset_index(inplace=True)
df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price":["mean", "count"]}).reset_index(inplace=True)
df.groupby(["SaleCityName", "ConceptName", "CInDay"]).agg({"Price":["mean", "count"]}).reset_index(inplace=True)
#reset_index komutu index'teki isimleri değişken yapar ve indexi resetler(0,1,2,..)

GÖREV6
########################################################################################
agg_df.reset_index(inplace=True)
agg_df = agg_df.reset_index()
agg_df.head(20)
agg_df["sales_level_based"] = agg_df["SaleCityName"] + "_" + agg_df["ConceptName"] + "_" + agg_df["Seasons"]
## asistanın çözümü:

agg_df["sales_level_based"]= agg_df[["SaleCityName", "ConceptName", "Seasons" ]].agg(lambda x: "_".join(x).upper(),axis=1)

"_".join(["ahmet", "ali", "ayse"]).upper()

GÖREV7
########################################################################################
agg_df["Segment"] = pd.qcut(agg_df["Price"], 4, labels=["D","C","B","A"])
agg_df.groupby("Segment").agg({"Price":["mean", "max", "sum"]})

GÖREV8
########################################################################################
agg_df.sort_values(by="Price")
new_user = "Antalya_Herşey Dahil_High"
agg_df[agg_df["sales_level_based"] == new_user]
new_user2 = "Girne_Yarım Pansiyon_Low"
agg_df[agg_df["sales_level_based"] == new_user2]