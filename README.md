# django-ravena
Teste de endpoint

criar uma pasta para o projeto 
mkdir django-quati
cd django-quati

# instalar o Pyenv no Mac
1. brew install pyenv

Although not required, the pyenv wiki recommends installing some additional libraries.

brew install openssl readline sqlite3 xz zlib

https://binx.io/blog/2019/04/12/installing-pyenv-on-macos/

Shell	Config snippet	    Config file
bash	eval (pyenv init -)	~/.bash_profile or ~/.bashrc

Inserir no ~/.bash_profile or ~/.bashrc

editar o arquivo .bashrc e inserir esta linha abaixo. Restart no terminal (fecha e abre)
eval (pyenv init -)

2. na pasta /django-quati/ 

   pyenv install 3.6.6

3. pyenv local 3.6.6

4. python -V (3.6.6)

5. Criar o virtulenv 
python -m venv .venv

6. source .venv/bin/active

7. pip install -r requirements.txt

