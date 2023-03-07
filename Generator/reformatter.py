import csv

def reformat(row):
    return (
        row[0],
        int(row[1]) - int(row[11]),
        int(row[1]) * int(row[11]),
        int(row[2]) - int(row[12]),
        int(row[2]) * int(row[12]),
        int(row[3]) - int(row[13]),
        int(row[3]) * int(row[13]),
        int(row[4]) - int(row[14]),
        int(row[4]) * int(row[14]),
        int(row[5]) - int(row[15]),
        int(row[5]) * int(row[15]),
        int(row[6]) - int(row[16]),
        int(row[6]) * int(row[16]),
        int(row[7]) - int(row[17]),
        int(row[7]) * int(row[17]),
        int(row[8]) - int(row[18]),
        int(row[8]) * int(row[18]),
        int(row[9]) - int(row[19]),
        int(row[9]) * int(row[19]),
        int(row[10]) - int(row[20]),
        int(row[10]) * int(row[20]),
        row[21]
    )

def main():
    reader = csv.reader(open(f'Arquivos_Tot/tobodo_training_data_reduce_7b1.csv', 'r'), csv.excel)
    writer = csv.writer(open(f'Arquivos_Tot/reformatted_7b1.csv', 'w'))
    for row in reader:
        if not row:
            continue
        writer.writerow(reformat(row))
    
if (__name__ == '__main__'):
    main()