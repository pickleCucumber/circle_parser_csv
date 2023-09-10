import pandas as pd
import os
import glob

# use glob to get all the csv files
# in the folder
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.csv"))

# loop over the list of csv files
for f in csv_files:
    # read the csv file
    df = pd.read_csv(f, sep=';', encoding='PT154', comment='#')

    # print the location and filename
    print('Location:', f)
    print('File Name:', f.split("\\")[-1])

    # print the content
    print('Content:')
    print(df.head(10))
    print()


---------------------------------------------------------------------------------

def df_list():
    filename_list = current_stage_files(PATH)
    df_list = []
    for file in filename_list:
        df = pd.read_csv(PATH+file)
        df.name = file
        df_list.append(df)
    return df_list
