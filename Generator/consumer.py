import csv
import itertools
import generator
import random
from multiprocessing import Pool

def __main__():
    data = list()
    reader = csv.reader(open(f'Arquivos/arg_space.csv'))
    sec = itertools.count()
    for l in reader:
        if l:
            data.append((f'{next(sec)}', tuple(int(i) for i in l)))
    comparation_set = list()
    print(len(data))
    leading = data#random.sample(data, 1_000)
    trailing = data#random.sample(data, 1_000)

    writer = csv.writer(open('Arquivos_Tot/Training_data_comparation_1.csv', 'w'))
    for l in leading:
        print(leading.index(l))
        for l_2 in trailing:
            pac_1_ = generator.Paciente(*l[1][0:8])
            pac_2_ = generator.Paciente(*l_2[1][0:8])
            comparation_set.append((
                    f'{l[0]}_vs_{l_2[0]}',
                    *l[1][:8],
                    generator.sofa(pac_1_),
                    generator.amib_total(pac_1_),
                    *l_2[1][:8],
                    generator.sofa(pac_2_),
                    generator.amib_total(pac_2_),
                    compare(l, l_2)
            ))
        if (len(comparation_set) > 2_000_000):
            writer.writerows(comparation_set)
            comparation_set = list()

def compare(pac_1, pac_2):
    pac_1_ = generator.Paciente(*pac_1[1][0:8])
    pac_2_ = generator.Paciente(*pac_2[1][0:8])
    comparation = generator.compare_amib(pac_1_, pac_2_)
    if comparation is None:
        return '0'
    if comparation == pac_1_:
        return '1'#pac_1[0]
    return '2'#pac_2[0]


if __name__ == '__main__':
    with Pool(200) as p:
        __main__()
