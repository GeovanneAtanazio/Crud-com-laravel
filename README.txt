Criar projeto laravel: 
	composer create-project --prefer-dist laravel/laravel nome_do_projeto
Criar CRUD:
	php artisan make:command CrudGenerator

ADCIONAR O DIRETÓRIO /stub E OS ARQUIVOS CONTIDOS NELE NO DIRETÓRIO /resouces

MUDAR O ARQUIVO CrudGenerator.php NO DIRETÓRIO app/Console/Commands

CONFIGURE O BANCO NO ARQUIVO .env

Criar um Controller para uma tabela:
	php artisan crud:generator nome_do_controller

Cria uma migration para uma tabela:
	php artisan make:migration create_NOME-DA-TABELA_table --create=NOME-DA-TABELA

INSERE AS COLUNAS NO METODO up DA MIGATION CRIADA

MUDAR O ARQUIVO AppServiceProvider.php NO DIRETÓRIO app/Providers

Criar a tabela no banco:
	php artisan migrate
