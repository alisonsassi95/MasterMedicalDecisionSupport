- README GIT HUB
    
    ### Objetivo Geral:
    
    - Desenvolver um modelo computacional que através de variáveis informadas, possa fazer uma listagem por ordem de gravidade dos pacientes que precisam de unidade de tratamento intensivo. Desta forma, facilitar a decisão que o profissional de saúde  recisa tomar na escolha de quem ocupará os leitos.
    
    ### Objetivos Específicos:
    
    - [X]  Extrair os critérios necessários do protocolo AMIB para produção do modelo computacional;
    - [X]  Propor o algoritmo de aprendizado de máquina supervisionado capaz de interpretar
    os critérios;
    - [X]  Codificar a forma de captura dos dados e validação do modelo;
    - [X]  Treinar o algoritmo com os dados dos critérios extraídos;
    - [ ]  Realizar a validação do modelo construído;
    - [ ]  Qualificar a validação reajustando se necessário.
    
    ### Hipótese:
    
    - A tecnologia oferece soluções para problemas complexos, utilizando algoritmos de Inteligencia Artificial, em companhia com a modelagem matemática, é possível criar um modelo computacional baseado no protocolo AMIB 2020 com assertividade e  transparência, conforme critérios predefinidos e treinados, resultando em uma lista de pacientes sugerida pelo modelo desenvolvido, afim de apoiar o profissional da saúde.
    
    ### **MedicalDecisionSupport**:
    
    - É o **nome do sistema** que está sendo desenvolvido para a utilização do Trabalho.

# Passo a passo

```
git clone https://github.com/rg3915/django-auth-tutorial.git
cd django-auth-tutorial
git branch base origin/base
git checkout base

[] Criar ambiente virtual: 
* Criar um ambiente virtual: python -m venv venv
* Ativar: .\venv\Scripts\activate

pip install -U pip
[] Rodar comando para as dependências:
* Instalar todos as dependencias: pip install -r requirements.txt
pip install ipdb

python contrib/env_gen.py

[] Banco de dados:
* Rodar o MakeMigrations: python manage.py makemigrations
* Rodar o Migrate: python manage.py migrate

python manage.py createsuperuser --username="admin" --email="admin@email.com"

- Comandos
* Gerar o arquivo requeriments: pip freeze > requirements.txt
python manage.py shell_plus
```
Step by Step Comands

INICIALIZAR AMBIENTE
[] Iniciar servidor:
* Iniciar Servidor: python manage.py runserver