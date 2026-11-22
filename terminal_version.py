import csv
import os

def check_file_exist(file):
    if not os.path.exists(file) :
        with open(file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([f"the {file} did not exist, but I created this file ✔️"])
            return True
    return True
    
def read_csv_file(file):
    if check_file_exist(file) == True:
        with open(file, "r", encoding="utf-8") as f :
            reader = csv.reader(f)
            for row in reader:
                if row :
                    print(row)
    else:
        print(f"the {file} not exist ❌")

read_csv_file("TodoList.csv")
