import pandas as pd
from datetime import datetime

col_list = ["imagen"]
fullDf = pd.read_csv("lubricantesDemo.csv", sep=";")
fullDf.drop_duplicates(inplace=True)

df = pd.read_csv("lubricantesDemo.csv", usecols=col_list,
                 sep=';')  # dataframe variable
df.drop_duplicates(inplace=True)
timeNow = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
fileName = 'CleanData/cleanedData' + timeNow + '.csv'
image_list = df["imagen"]

# An invalid link looks like wwww. without the https scheme change all links that do not adhere to woocommerce guidelines
for link in image_list:
    if link.startswith('www.'):
        fullDf["imagen"].replace(
            to_replace=link, value="https://" + link, inplace=True)

print(fullDf)
fullDf.to_csv(fileName,
              index=False)
