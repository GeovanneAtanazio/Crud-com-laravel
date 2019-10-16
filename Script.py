import os
import shutil

def tratarEndereco(endereco):
    endereco=endereco.replace('\u005C','\u002F')
    return endereco


def criarProjetoLaravel(endereco,nomeProjeto):
    os.chdir(enderecoProjeto)
    os.system('composer create-project --prefer-dist laravel/laravel '+nomeProjeto)

def criarCrudBase(enderecoLocal,enderecoProjeto,nomeProjeto):
    enderecoProjeto = enderecoProjeto+'/'+nomeProjeto
    os.chdir(enderecoProjeto) #abre o diretório do projeto
    os.system('php artisan make:command CrudGenerator') #cria crud
    
    os.chdir(enderecoProjeto+'/resources')
    os.system('md stub')
    
    shutil.copyfile(enderecoLocal+'/stub/Controller.stub', enderecoProjeto+'/resources/stub/Controller.stub')  #copia arquivo Controller
    shutil.copyfile(enderecoLocal+'/stub/Model.stub',enderecoProjeto+'/resources/stub/Model.stub')   #copia arquivo Model
    shutil.copyfile(enderecoLocal+'/stub/Request.stub',enderecoProjeto+'/resources/stub/Request.stub') #copia arquivo Request

    shutil.copyfile(enderecoLocal+'/CrudGenerator.php',enderecoProjeto+'/app/Console/Commands/CrudGenerator.php')    #copia arquivo Crud

    shutil.copyfile(enderecoLocal+'/AppServiceProvider.php',enderecoProjeto+'/app/Providers/AppServiceProvider.php')


if __name__ == "__main__":
    enderecoLocal = os.getcwd() #pega o ondereço local
    enderecoLocal = tratarEndereco(enderecoLocal)
    enderecoProjeto = input("Digite o endereço do projeto: ")
    enderecoProjeto = tratarEndereco(enderecoProjeto)

    nomeProjeto = input('Digite o nome do projeto: ')

    criarProjetoLaravel(enderecoProjeto,nomeProjeto)
    criarCrudBase(enderecoLocal,enderecoProjeto,nomeProjeto)
