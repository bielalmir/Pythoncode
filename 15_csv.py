import csv
import pandas as pd

with open('records.csv' , mode ='w', newline='') as rec_file:
    csv_writer = csv.writer(rec_file)

    csv_writer.writerows([['abcd', 'bsdk', 'bdsm', 69], ['mars', 'Dominance', 'bkl', '123']])

    csv_writer.writerow(['abcd', '20', 'bdsmjh', '6.9'])

    

with open('records.csv',mode="r", newline='') as file2:
    reader1= csv.reader(file2)
    pd= pd.DataFrame(reader1)
print(pd) 