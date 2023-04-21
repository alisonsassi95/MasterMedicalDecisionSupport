- README GIT HUB
    
    ### Objetivo Geral:
    
    - Desenvolver um modelo computacional que através de variáveis informadas, possa fazer uma listagem por ordem de gravidade dos pacientes que precisam de unidade de tratamento intensivo. Desta forma, facilitar a decisão que o profissional de saúde  recisa tomar na escolha de quem ocupará os leitos.
    ### Hipótese:
    
    - A tecnologia oferece soluções para problemas complexos, utilizando algoritmos de Inteligencia Artificial, em companhia com a modelagem matemática, é possível criar um modelo computacional baseado no protocolo AMIB 2020 com assertividade e  transparência, conforme critérios predefinidos e treinados, resultando em uma lista de pacientes sugerida pelo modelo desenvolvido, afim de apoiar o profissional da saúde.

    
    ### Divisão das pastas
     # Diretório "Generator" é o lugar onde é gerado os arquivos.
        Não será possível replicar totalmente este trabalho pelas validações médicas realizadas.

        Porém existe o arquivo com as 2 milhões de linhas para rodar a Inteligência Artificial.

        * OBS: Conversor dos dados para texto ( melhor visualização)


        Existe o conversor dos dados: Ele serve para deixar mais visual os dados. Então realizei um DE:PARA de cada dados do paciente, para que fique uma visualização melhor. "\Generator\Conversor_fileIA_vs_names_variavel.py"

        * Gerador de dados ( iníco do algoritmo)
            No arquivo "\Generator\generator.py" é onde crio os dados dos pacientes. Resultando em um arquivo: "Arquivos/arg_space.csv"
            
            É nesse arquivo que tem as regras do AMIB e os dados de geração.
        
        * Comparador de dados (segundo algoritmo)
            No arquivo "\Generator\consumer.py" é onde consome o arquivo anterior e cria uma comparação de todos contra todos.
            
            Gerando um arquivo de comparação final.

        * Comparador de dados (terceiro algoritmo)
            No arquivo "\Generator\reducer.py" é onde é gerado uma sequencia de dados, como se trabalha com muitos dados eu reduzi 


     # Diretório "Jupter Notebook" terá um README para orientação.  
        Nesses algoritmos você vai encontrar os arquivos .CSV (Se o GitHub não excluir) e os algoritmos utilizados no trabalho. 

        

     # Diretórios restantes
     ### **MedicalDecisionSupport**:
    - É o **nome do sistema** que está sendo desenvolvido para a utilização do Trabalho.

        São o sistema que utilizei para a validação dos médicos. 
            Foi utilizado o Heroku para hospedagem. Link: https://mediclasystemdecision.herokuapp.com/accounts/login/
            User:teste_github
            Senha:compartilhado
        
        É criado em cima do Framework Django.
        Na pasta "myproject" encontrará todos os arquivos de rotas e páginas necessário.

        Deixo aqui o arquivo "/patient/importCSV.py" para subir no sistema os dados gerados para mais testes.
    
    
    
# Passo a passo para subir o projeto do Django

```
git clone LINK_DO_PROJETO

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



# Heroku
pip install django-on-heroku
pip install pywin32==302
pip install pipwin
pywin32==302; platform_system=="Windows"
pywin32==223; sys_platform == "win32"

# git

git add .
git commit -m "..."
git push
git push heroku