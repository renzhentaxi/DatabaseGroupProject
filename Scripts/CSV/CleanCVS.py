import shutil
import os
#cleans the default csv folder
print("Cleaning the csv folder")
if os.path.exists("./data/csv"):
    shutil.rmtree("./data/csv")
print('Done')