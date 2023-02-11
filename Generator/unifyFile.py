import csv
import os
from faker import Faker

faker = Faker()

NameFileExport = "NameFileExport.csv"
def __main__():

    exist = os.path.exists(NameFileExport)
    if not (exist):
        createFile()

    data = []
    patient = []
    for n in range(100):
        reader = csv.reader(open(f'../Arquivos/temp_{n}.csv'))
        for l in reader:
            if l:
                l.append(n)
                data.append(l)
    for R in data:
        patient.append(faker.name())

        patient.append(R[0])
        patient.append(neurologicalName(int(R[0])))

        patient.append(R[1])
        patient.append(cardiovascularName(int(R[1])))

        patient.append(R[2])
        patient.append(respiratoryName(int(R[2])))

        patient.append(R[3])
        patient.append(coagulationName(int(R[3])))

        patient.append(R[4])
        patient.append(hepaticName(int(R[4])))

        patient.append(R[5])
        patient.append(renalName(int(R[5])))

        patient.append(R[6])
        patient.append(SPICTName(int(R[6])))
        
        patient.append(R[7])
        patient.append(ecogName(int(R[7])))
        #SOFA
        patient.append(R[8])
        #AMIB
        patient.append(R[9])
        #GRUPO
        patient.append(R[10])
        
        File = str(patient).replace("'","").replace("[","'").replace("]","").replace("\u2264", "-").replace("'","")
        print(File)
        patient.clear()
        insertOneRegisterInFile(File)

def insertOneRegisterInFile(data_file):
    arq = open(NameFileExport,'a')
    arq.write('\n')
    arq.write(data_file)
    arq.close()

def neurologicalName(value):
        neurologicalName = {
            0: "15",
            1: "Entre 13 a 14",
            2: "Entre 10 a 12",
            3: "Entre 6 a 9",
            4: "Menor que 6"
        }
        return neurologicalName[value]

def cardiovascularName(value):
    cardiovascularName = {
            0: "PAM > 70mmHg e Sem uso de vasopressor",
            1: "PAM < 70mmHg  e Sem uso de vasopressor ",
            2: "Em uso de Dopamina ≤ 5 ou Dobutamina qualquer dose",
            3: "Em uso de Dopamina > 5 ou Noradrenalina ≤ 0.1",
            4: "Em uso de Dopamina > 15 ou Noradrenalina > 0.1"
        }
    return cardiovascularName[value]
def respiratoryName(value):
    respiratoryName = {
            0: "PaO2 > 400 em ar ambiente",
            1: "SpO2>92% com Cateter nasal O2 até 2l/min",
            2: "SpO2> 92% com Cateter nasal O2 até 5l/min",
            3: "SpO2>92% com ventilação mecânica com FiO2 até 40%",
            4: "SpO2> 92% com ventilação mecânica com FiO2> 40%"
        }
    return respiratoryName[value]
def coagulationName(value):
    coagulationName = {
            0: "Maior que 150",
            1: "Entre 100 a 149",
            2: "Entre 50 a 99",
            3: "Entre 20 a 49",
            4: "Menor que 20"

        }
    return coagulationName[value]
def hepaticName(value):
    hepaticName = {
            0: "Até 1.2",
            1: "Entre 1.2 e 1.9",
            2: "Entre 2 e 5.9",
            3: "Entre 6 e 11.9",
            4: "Maior que 12"
        }
    return hepaticName[value]

def renalName(value):
    renalName = {
            0: "Creatinina menor que 1.2",
            1: "Creatinina entre 1.2 a 1.9",
            2: "Creatinina entre 2.0 a 3.4",
            3: "Creatinina  entre 3.5 a 4.9 ou diurese entre 199 até 500ml/dia",
            4: "Creatinina  maior que 5.0 ou diurese menor que 200ml/dia"
        }
    return renalName[value]

def SPICTName(value):
    SPICTName = {
        0: "Paciente sem condições graves",
        3: "Pacientes com expectativa de sobrevida inferior a um ano"
    }
    return SPICTName[value]

def ecogName(value):
    ecogName = {
        0: "Completamente ativo",
        1: "Restricao a atividades físicas rigorosas",
        2: "Capaz de realizar auto-cuidados",
        3: "Auto-cuidados limitados",
        4: "Completamente incapaz"
    }
    return ecogName[value]

def createFile():
    arq = open(NameFileExport,'w')
    arq.write('NAME_PATIENT,NEUROLOGICAL,DESCR_NEUROLOGICAL,CARDIOVASCULAR,DESCR_CARDIOVASCULAR,RESPIRATORY,DESCR_RESPIRATORY,COAGULATION,DESCR_COAGULATION,HEPATIC,DESCR_HEPATIC,RENAL,DESCR_RENAL,SPICT,DESCR_SPICT,ECOG,DESCR_ECOG,SOFA,AMIB,GROUP')
    arq.close()

if __name__ == '__main__':
    __main__()











