import csv
import itertools
import collections
import numpy as np
import random

def main(validate):
    reader = csv.reader(open('Arquivos_Tot/Training_data_comparation_1.csv', 'r'), csv.excel)
    data = [tuple(int(i) for i in (*row[0].split('_vs_'), row[-1])) for row in reader if len(row) > 0]

    print('t0')

    zeros = {(row[0], row[1]) for row in data if row[-1] == 0}
    ones = {(row[0], row[1]) for row in data if row[-1] ==  1}
    twos = {(row[0], row[1]) for row in data if row[-1] == 2}

    print('t1')

    if (validate):
        assert len(twos) == len(ones)
        for a, b in ones:
            assert (b, a) in twos
            assert (a, b) not in zeros
            assert (b, a) not in zeros
        for b, a in twos:
            assert (a, b) in ones
            assert (a, b) not in zeros
            assert (b, a) not in zeros
        for a, b in zeros:
            assert (a, b) not in ones
            assert (b, a) not in ones
            assert (a, b) not in twos
            assert (b, a) not in twos

    print('t2')

    id_set = set(row[0] for row in data)

    equivalent_sets = [{i} for i in id_set]
    for i, j in zeros:
        ith_set = [s for s in equivalent_sets if i in s][0]
        jth_set = [s for s in equivalent_sets if j in s][0]
        if (ith_set != jth_set):
            equivalent_sets.remove(ith_set)
            jth_set.update(ith_set)
    
    print('t3')

    if (validate):
        for cls in equivalent_sets:
            for a in cls:
                for b in cls:
                    assert (a, b) not in ones
                    assert (b, a) not in ones
                    assert (a, b) not in twos
                    assert (b, a) not in twos
                    assert (a, b) in zeros
                    assert (b, a) in zeros

    print('t4')

    representative_sets = [(first(s), s) for s in equivalent_sets]
    representatives = {t[0] for t in representative_sets}
    sub_data = [row for row in ones if row[0] in representatives and row[1] in representatives]
    counter = {s: len([sub for sub in sub_data if s in sub]) for s in representatives}
    sorted_equivalent_sets = list(l[1] for l in sorted(representative_sets, key=lambda s: counter[s[0]]))

    print('t5')

    if validate:
        l = len(sorted_equivalent_sets)
        for i in range(l-1):
            for j in range(i+1, l):
                bfr = sorted_equivalent_sets[0]
                aft = sorted_equivalent_sets[1]
                for bfr_el in bfr:
                    for aft_el in aft:
                        assert (bfr_el, aft_el) in twos

    print('t6')

def first(s: set):
    return next(iter(s))


def reduce_part_1():
    reader = csv.reader(open('Arquivos_Tot/Training_data_comparation_1.csv', 'r'), csv.excel)
    writer = csv.writer(open('Arquivos_Tot/Data_reduce_v1.csv', 'w'), csv.excel)

    sample = collections.deque()
    count = 0
    for row in reader:
        if len(row) == 0:
            continue
        simple_row = (*row[0].split('_vs_'), row[-1])
        sample.append(simple_row)
        if len(sample) >= 25_000:
            writer.writerows(sample)
            count += len(sample)
            sample.clear()
            print(count)
    writer.writerows(sample)
    count += len(sample)
    print(count)

def reduce_part_2():
    reader = csv.reader(open('Arquivos_Tot/Data_reduce_v1.csv', 'r'), csv.excel)
    zero_writer = csv.writer(open('Arquivos_Tot/Data_reduce_v2_zero.csv', 'w'), csv.excel)
    one_writer = csv.writer(open('Arquivos_Tot/Data_reduce_v2_one.csv', 'w'), csv.excel)
    two_writer = csv.writer(open('Arquivos_Tot/Data_reduce_v2_two.csv', 'w'), csv.excel)

    zero_sample = collections.deque()
    one_sample = collections.deque()
    two_sample = collections.deque()
    counter = 0
    for row in reader:
        if len(row) == 0:
            continue
        simple = (row[0], row[1])
        result = row[2]
        if (result == '0'):
            zero_sample.append(simple)
        elif (result == '1'):
            one_sample.append(simple)
        else:
            two_sample.append(simple)
        
        if (len(zero_sample) >= 25_000):
            zero_writer.writerows(zero_sample)
            counter += len(zero_sample)
            zero_sample.clear()
            print(counter)
        if (len(one_sample) >= 25_000):
            one_writer.writerows(one_sample)
            counter += len(one_sample)
            one_sample.clear()
            print(counter)
        if (len(two_sample) >= 25_000):
            two_writer.writerows(two_sample)
            counter += len(two_sample)
            two_sample.clear()
            print(counter)
        
    zero_writer.writerows(zero_sample)
    counter += len(zero_sample)
    one_writer.writerows(one_sample)
    counter += len(one_sample)
    two_writer.writerows(two_sample)
    counter += len(two_sample)
    print(counter)


def big_read(reader):
    acumulators = collections.deque(maxlen=10_000)
    cur = collections.deque(maxlen=25_000)
    for row in reader:
        if (len(row) == 0):
            continue
        cur.append(tuple(map(int, row)))
        if len(cur) >= 25_000:
            acumulators.append(cur)
            cur = collections.deque(maxlen=25_000)
            print(10_000 * len(acumulators))
    acumulators.append(cur)
    return np.fromiter(itertools.chain(*acumulators), dtype=tuple)


def reduce_part_2_validate():

    print('t-1')

    zero_reader = csv.reader(open('Arquivos_Tot/Data_reduce_v2_zero.csv', 'r'), csv.excel)
    zeros = big_read(zero_reader)
    print('.')
    one_reader = csv.reader(open('Arquivos_Tot/Data_reduce_v2_one.csv', 'r'), csv.excel)
    ones = big_read(one_reader)
    print('.')
    two_reader = csv.reader(open('Arquivos_Tot/Data_reduce_v2_two.csv', 'r'), csv.excel)
    twos = big_read(two_reader)
    print('.')

    print('t0')

    assert len(twos) == len(ones)
    for a, b in ones:
        assert (b, a) in twos
        assert (a, b) not in zeros
        assert (b, a) not in zeros
    print('t1')
    for b, a in twos:
        assert (a, b) in ones
        assert (a, b) not in zeros
        assert (b, a) not in zeros
    print('t2')
    for a, b in zeros:
        assert (a, b) not in ones
        assert (b, a) not in ones
        assert (a, b) not in twos
        assert (b, a) not in twos
    print('t3')


def reduce_part_3():
    
    zero_reader = csv.reader(open('Arquivos_Tot/Data_reduce_v2_zero.csv', 'r'), csv.excel)
    one_reader = csv.reader(open('Arquivos_Tot/Data_reduce_v2_one.csv', 'r'), csv.excel)
    two_reader = csv.reader(open('Arquivos_Tot/Data_reduce_v2_two.csv', 'r'), csv.excel)

    equivalent_sets = list()
    for row in zero_reader:
        if not row:
            continue
        a, b = int(row[0]), int(row[1])
        sub_a = [s for s in equivalent_sets if a in s]
        sub_b = [s for s in equivalent_sets if b in s]
        if (not sub_a):
            equivalent_sets.append({a})
        if (not sub_b):
            equivalent_sets.append({b})
            continue
        if (not sub_a):
            continue
        ath = sub_a[0]
        bth = sub_b[0]
        if id(ath) == id(bth):
            continue
        equivalent_sets.remove(ath)
        bth.update(ath)
        print(len(equivalent_sets))
    print(len(equivalent_sets))
    writer = csv.writer(open(f'Arquivos_Tot/Data_reduce_v3.csv', 'w'), csv.excel)
    writer.writerows(equivalent_sets)


def bigger(r1, r2):
    print(r1, r2)
    one_reader = csv.reader(open('Arquivos_Tot/Data_reduce_v2_one.csv', 'r'), csv.excel)
    keys = (r1, r2)
    it = iter(one_reader)
    row = None
    while not row or int(row[1]) not in keys:
        row = next(it)
    print('.')
    while not row or int(row[1]) not in keys:
        row = next(it)
        if int(row[0]) == r1:
            if int(row[1]) == r2:
                return True
            else:
                continue
        if int(row[1]) == r1:
            if int(row[0]) == r2:
                return False
            else:
                continue


def reduce_part_4():
    reader = csv.reader(open(f'Arquivos_Tot/Data_reduce_v3.csv', 'r'), csv.excel)
    representative_set = [(min(map(int, row)), row) for row in reader if row]

    l = len(representative_set)
    for i in range(0, l-1):
        for j in range(i+1, l):
            print('.....')
            if bigger(representative_set[i][0], representative_set[j][0]):
                print('swap')
                swap = representative_set[i]
                representative_set[i] = representative_set[j]
                representative_set[j] = swap
    writer = csv.writer(open(f'Arquivos_Tot/Data_reduce_v4.csv', 'w'), csv.excel)
    writer.writerows((r[1] for r in representative_set))


def reduce_part_5():
    validation_reader = csv.reader(open('D:\Mestrado\MasterMedicalDecisionSupport\Generator\Arquivo Antigo\Validações.csv', 'r'))
    data = []
    acum = []
    user = None
    for row in validation_reader:
        if not row:
            continue
        row = row[0].split(';')
        if (row[3] == 'neurological'):
            continue
        if (user and user != row[0]):
            data.append(acum)
            acum = []
        user = row[0]

        simple = [
            row[3],
            row[5],
            row[7],
            row[9],
            row[11],
            row[13],
            row[15],
            row[17],
            row[19],
            row[20]
        ]
        acum.append(simple)
    data.append(acum)

    rec = itertools.count()
    reader = csv.reader(open(f'Arquivos/arg_space.csv'))
    for row in reader:
        if not row:
            continue
        identifier = str(next(rec))
        for group in data:
            l = len(group)
            for i in range(l):
                item = group[i]
                if item == row:
                    group[i] = identifier
    data = [[item for item in group if type(item) == str] for group in data]
    writer = csv.writer(open(f'Arquivos_Tot/Data_reduce_v5_with_data_medical.csv', 'w'), csv.excel)
    writer.writerows(data)


def reduce_part_6():
    val_reader = csv.reader(open(f'Arquivos_Tot/Data_reduce_v5_with_data_medical.csv', 'r'), csv.excel)
    validation_data = [tuple(t) for t in val_reader if t]
    total_validation = tuple(itertools.chain(*validation_data))

    order_reader = csv.reader(open(f'Arquivos_Tot/Data_reduce_v4.csv', 'r'), csv.excel)
    order_writer = csv.writer(open(f'Arquivos_Tot/Data_reduce_v6_all_data.csv', 'w'), csv.excel)

    for group in order_reader:
        breaking_item = None
        for item in group:
            if item in total_validation:
                breaking_item = item
                break
        else:
            order_writer.writerow(group)
            continue
        print(breaking_item)
        validation_gorup = None
        for possible_validation_group in validation_data:
            if breaking_item in possible_validation_group:
                validation_gorup = possible_validation_group
                break

        for item in validation_gorup:
            group.remove(item)
        breaking_item = validation_gorup[len(validation_gorup)//2]
        for item in validation_gorup:
            if (item == breaking_item):
                order_writer.writerow(group + [item])
            else:
                order_writer.writerow([item])

        
def reduce_part_7():
    order_reader = csv.reader(open(f'Arquivos_Tot/Data_reduce_v6_all_data.csv', 'r'), csv.excel)
    medical_reader = csv.reader(open(f'Arquivos_Tot/Data_reduce_v5_with_data_medical.csv', 'r'), csv.excel)

    medical = list(itertools.chain(*medical_reader))
    order = [row for row in order_reader if row]

    def compare(a, b):
        for group in order:
            if a in group:
                return '1' if b not in group else '0'
            if b in group:
                return '2'
    
    cnt = itertools.count()
    arg_space_reader = csv.reader(open(f'Arquivos/arg_space.csv'))
    arg_space = {(str(next(cnt)), *row) for row in arg_space_reader if row}


    qtd = 5000

    sub_arg_space = []
    sub_arg_space.append(set(random.sample(arg_space, qtd)))
    sub_arg_space[0] = {p for p in arg_space if p[0] in medical or p in sub_arg_space[0]}
    sub_arg_space.append(set(random.sample(arg_space-sub_arg_space[0], qtd)))
    sub_arg_space.append(set(random.sample(arg_space-sub_arg_space[0]-sub_arg_space[1], qtd)))
    sub_arg_space.append(set(random.sample(arg_space-sub_arg_space[0]-sub_arg_space[1]-sub_arg_space[2], qtd)))

    p = [(0, 1), (2,3)]

    for i, j in p:

        arg_space_1 = sub_arg_space[i]
        arg_space_2 = sub_arg_space[j]
        
        training_writer = csv.writer(open(f'Arquivos_Tot/Database_training_reduce_7_{i}{j}.csv', 'w'), csv.excel)

        acum = collections.deque(maxlen=25_000)
        tot = 0
        for pac_a in arg_space_1:
            for pac_b in arg_space_2 :
                if (pac_a[0] in medical or pac_b[0] in medical):
                    for i in range(2):
                        acum.append([f'{pac_a[0]}_vs_{pac_b[0]}', *pac_a[1:], *pac_b[1:], compare(pac_a[0], pac_b[0])])
                if (compare(pac_a[0], pac_b[0]) != '0' or i == 2):
                    acum.append([f'{pac_a[0]}_vs_{pac_b[0]}', *pac_a[1:], *pac_b[1:], compare(pac_a[0], pac_b[0])])
                if len(acum) >= 25_000:
                    training_writer.writerows(acum)
                    tot += len(acum)
                    acum.clear()
                    print(tot)
        training_writer.writerows(acum)

        
def reduce_part_7b():
    order_reader = csv.reader(open(f'Arquivos_Tot/Data_reduce_v6_all_data.csv', 'r'), csv.excel)
    order = [row[1:min(len(row), 9)-1] for row in order_reader if row]
    ordered_set = list(itertools.chain(*order))
    def compare(a, b):
        for group in order:
            if a in group:
                return '1' if b not in group else '0'
            if b in group:
                return '2'
    
    cnt = itertools.count()
    arg_space_reader = csv.reader(open(f'Arquivos/arg_space.csv'))
    arg_space = [(str(next(cnt)), *row) for row in arg_space_reader if row]
    arg_space = [arg for arg in arg_space if arg[0] in ordered_set]

    training_writer = csv.writer(open(f'Arquivos_Tot/Database_training_reduce_7b.csv', 'w'), csv.excel)

    acum = collections.deque(maxlen=25_000)
    tot = 0
    for pac_a in arg_space:
        for pac_b in arg_space:
            acum.append([f'{pac_a[0]}_vs_{pac_b[0]}', *pac_a[1:], *pac_b[1:], compare(pac_a[0], pac_b[0])])
            if len(acum) >= 25_000:
                training_writer.writerows(acum)
                tot += len(acum)
                acum.clear()
                print(tot)
    training_writer.writerows(acum)

        
def reduce_part_7c():
    order_reader = csv.reader(open(f'Arquivos_Tot/Data_reduce_v6_all_data.csv', 'r'), csv.excel)
    order = [row for row in order_reader if row]
    ordered_set = list(itertools.chain(*order))
    def compare(a, b):
        for group in order:
            if a in group:
                return '1' if b not in group else '0'
            if b in group:
                return '2'
    
    cnt = itertools.count()
    arg_space_reader = csv.reader(open(f'Arquivos/arg_space.csv'))
    arg_space = [(str(next(cnt)), *row) for row in arg_space_reader if row]
    arg_space = [arg for arg in arg_space if arg[0] in ordered_set]

    training_writer = csv.writer(open(f'Arquivos_Tot/Database_training_reduce_7c.csv', 'w'), csv.excel)

    acum = collections.deque(maxlen=25_000)
    tot = 0
    for pac_a in arg_space:
        for pac_b in arg_space:
            if (compare(pac_a[0], pac_b[0]) == '0'):
                continue
            acum.append([f'{pac_a[0]}_vs_{pac_b[0]}', *pac_a[1:], *pac_b[1:], compare(pac_a[0], pac_b[0])])
            if len(acum) >= 25_000:
                training_writer.writerows(acum)
                tot += len(acum)
                acum.clear()
                print(tot)
    training_writer.writerows(acum)


if __name__ == '__main__':
    reduce_part_1()
    reduce_part_2()
    reduce_part_3()
    reduce_part_4()
    reduce_part_5()
    reduce_part_6()
    reduce_part_7()