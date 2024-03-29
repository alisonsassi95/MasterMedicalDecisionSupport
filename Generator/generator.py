import typing as tp
import random
import csv
import multiprocessing
import itertools

class Paciente(tp.NamedTuple):
    neuro: int
    cardi: int
    respi: int
    coagu: int
    hepat: int
    renal: int
    icc: int
    ecog: int

    @classmethod
    def __make(cls, neuro: int, cardi: int, respi: int, coagu: int, hepat: int, renal: int, icc: int, ecog: int,):
        if not (0 <= neuro <= 4):
            raise Exception('neuro invalida')
        if not (0 <= cardi <= 4):
            raise Exception('cardi invalida')
        if not (0 <= respi <= 4):
            raise Exception('respi invalida')
        if not (0 <= coagu <= 4):
            raise Exception('coagu invalida')
        if not (0 <= hepat <= 4):
            raise Exception('hepat invalida')
        if not (0 <= renal <= 4):
            raise Exception('renal invalida')
        if 0 != icc != 3:
            raise Exception('icc invalida')
        if not (0 <= ecog <= 4):
            raise Exception('ecog invalida')
        # Quando Cardio = 1: "PAM < 70mmHg  e Sem uso de vasopressor " o Respiratório tem que ser maior que 0: "PaO2 > 400 em ar ambiente"
        if (cardi==1) and (respi == 0):
            raise Exception('Provav Morte')
        # Quando Neuro (3 ou 4) o Respiratório tem que ser 3 ou 4
        if (respi >= 3) and (neuro < 3) or (neuro >= 3) and (respi < 3):
            raise Exception('validacao invalida')
        #Nao factível quando o ECOG completamente ativo (0) mas esta com glasgow menor que 6
        if (neuro >= 3) and (ecog == 0):
            raise Exception('validacao invalida')
        
        return cls(neuro, cardi, respi, coagu, hepat, renal, icc, ecog,)
    
    @classmethod
    def make(cls):
        r = random.randint
        while True:
            try:
                return cls.__make(*tuple(r(0, 4) for i in range (6)), r(0, 3), r(0, 4))
            except:
                #print('tem que otmizar isso depois')
                pass

def sofa(pac: Paciente) -> int:
    return sum(pac[0:5])

def amib_total(pac: Paciente) -> int:
    s = sofa(pac)
    s_ = 1 if s <= 8 else 2 if s <= 11 else 3 if s <= 14 else 4

    ecog = pac.ecog
    ecog_ = 1 if ecog <= 1 else pac.ecog

    return s_ + pac.icc

def compare_amib(pac_1: Paciente, pac_2: Paciente) -> tp.Optional[Paciente]:
    if (amib_total(pac_1) < amib_total(pac_2)):
        return pac_1
    if (amib_total(pac_1) > amib_total(pac_2)):
        return pac_2
    if (pac_1.icc < pac_2.icc):
        return pac_1
    if (pac_1.icc > pac_2.icc):
        return pac_2
    if (sofa(pac_1) < sofa(pac_2)):
        return pac_1
    if (sofa(pac_1) > sofa(pac_2)):
        return pac_2
    return None


def compare_amib_alpha(pac_1: Paciente, pac_2: Paciente) -> int:
    if (amib_total(pac_1) < amib_total(pac_2)):
        return amib_total(pac_2) - amib_total(pac_1)
    if (amib_total(pac_1) > amib_total(pac_2)):
        return amib_total(pac_1) - amib_total(pac_2)
    if (pac_1.icc < pac_2.icc):
        return pac_2.icc - pac_1.icc
    if (pac_1.icc > pac_2.icc):
        return pac_1.icc - pac_2.icc
    if (pac_1.ecog < pac_2.ecog):
        return pac_2.ecog - pac_1.ecog
    if (pac_1.ecog > pac_2.ecog):
        return pac_1.ecog - pac_2.ecog
    if (sofa(pac_1) < sofa(pac_2)):
        return sofa(pac_2) - sofa(pac_1)
    if (sofa(pac_1) > sofa(pac_2)):
        return sofa(pac_1) - sofa(pac_2)

    return 0.00001

def inercia(data: tp.Sequence[tp.Tuple[int]]) -> float:
    center: tp.Tuple[float] = tuple(sum(a[i] for a in data)/len(data) for i in range(len(data[0])))
    return sum(sum((a[i]-center[i])**2 for a in data) for i in range(len(data[0])))


def sum_alpha(data: tp.Sequence[Paciente]) -> int:
    return sum(compare_amib_alpha(pac_1, pac_2) for pac_1 in data for pac_2 in data)


def  inercia_per_alpha(pac: Paciente, data: tp.Sequence[Paciente]) -> float:
    sub_data = [p for p in data if p != pac or pac == None]
    ine = inercia(sub_data)
    alpha = sum_alpha(sub_data)
    return (ine / alpha)

def pro(n):
    print(n, 'start')
    max_ipa = 1
    data: tp.List[Paciente] = [Paciente.make() for i in range(5)]
    ipa: float = inercia_per_alpha(None, data)
    for _ in range(10000):
        data_2 = list()
        for pac in data:
            ipa_pac = inercia_per_alpha(pac, data)
            if ipa_pac > ipa:
                data_2 = [p for p in data if p != pac]
        c = iter(range(10000))
        while len(data_2) < 1000 and next(c) < 1000:
            pac = Paciente.make()
            if pac in data:
                break
            if (ipa < inercia_per_alpha(None, data_2 + [pac])):
                data_2.append(pac)
                data = data_2
                break
        random.shuffle(data)
        ipa: float = inercia_per_alpha(None, data)
        if ipa > max_ipa:
            break
    print(n, 'stop')
    
    wirter = csv.writer(open(f'Arquivos/temp_{n}.csv', 'w'), csv.excel)
    data_final = [p + (sofa(p), amib_total(p)) for p in data]
    wirter.writerows(data_final)

def __main__2():
    # max inertia, minimizar alpha
    with multiprocessing.Pool() as pool:
        for _ in pool.imap_unordered(pro, range(100), chunksize=1):
            pass
    
preset = set()

def make100(_):
    global preset
    return {Paciente.make() for _ in range(1_000)} - preset

def __main__():
    pool_size = 72_500  # 77.500 registros
    pool = set()
    print('start main loop')
    while len(pool) < pool_size:
        print(len(pool))
        global preset
        preset = pool
        with multiprocessing.Pool() as worerPool:
            acumulator = [pool]
            for d in worerPool.imap_unordered(make100, range(12)):
                acumulator.append(d)
                print('.')
            pool = set(itertools.chain(*acumulator))
            print(len(pool))
    print('end main loop')
    writer = csv.writer(open('Arquivos/arg_space.csv', 'w'), csv.excel)
    data_final = [p + (sofa(p), amib_total(p)) for p in pool]
    writer.writerows(data_final)

if (__name__ == '__main__'):
    print('start main')
    __main__()
    print('end main')