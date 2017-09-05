
# EventosApp
Projeto com o objetivo de criar uma plataforma online de eventos, onde pessoas podem publicar seus eventos para que outras pessoas possam participar. Didaticamente o projeto visa colocar em prática a construção de um design de classes coeso e claro, tal como a aplicação de testes de unidade, padrões de projetos e avaliar o trabalho de equipe.

## Como o projeto está estruturado?
- **Documentação :** Contém a modelagem das classes. Possui o arquivo de requisitos do projeto, e imagem + arquivo modelado( no software asta ) com o diagrama.
- **evento:** Contém os arquivos necessários para a execução da aplicação.  As pastas “appweb”, ”comum”, “core”, “inscricao”, “notificacao” referem-se a uma determinada parte da aplicação do software. A organização dos arquivos possui a estrutura do framework Django.
	- **.idea:** Contém arquivos em formato xml do projeto.
	- **.settings:** Contém arquivo que resolve conflitos de compatibilidade.
	- **.config:** Contém arquivos de configuração do banco de dados e urls.
- **requeriments.txt:** Script usado para baixar as dependencias necessárias para a execução da aplicação.
# Modelagem
- Diagrama de Classes
![Modelagem Design de Classes](/documentação/diagrama%20de%20classe/diagrama%20de%20classe.jpg)

- Diagrama de Caso de Uso
![Modelagem Caso de Uso](/documentação/diagrama%20de%20caso%20de%20uso/diagrama%20caso%20de%20uso.jpg)

![Modelagem Diagrama de objetos](documentação/diagrama%20de%20objetos/diagrama%20de%20objeto.jpg)

## Execução da aplicação:

O projeto não possui dependência. Então faça um git clone:
```
git clone https://github.com/fabiomsrs/EventosApp
cd Eventosapp
```
Vá no arquivo (/evento/config/settings.py) e configure seu banco de dados no campo DATABASES.
Execute o prompt de comando e vá até o diretorio (Eventosapp/evento) e execute o comando **manage.py migrate**.
Em apos as migrações estiverem completas execute o comando **manage.py runserver**. Vá até a seguinte linha **Starting development server at http://127.0.0.1:8000/** e copie a url e cole no seu navegador.

