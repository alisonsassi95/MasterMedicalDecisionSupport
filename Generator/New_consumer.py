import csv
import typing as tp
import generator

def __main__():
    data = list()
    comparation_set = list()

    pac_1_ = generator.Paciente.make()
    print(pac_1_)

    pac_2_ = generator.Paciente()
    print(pac_2_)


    comparation_set.append((
            
            *pac_1_[1][:8],
            generator.sofa(pac_1_),
            generator.amib_total(pac_1_),
            *pac_2_[1][:8],
            generator.sofa(pac_2_),
            generator.amib_total(pac_2_),
            compare(pac_1_, pac_2_)
    ))
    

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
    __main__()