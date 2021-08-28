# caleb
attempt to create a mind for a machine body(works better if you speak both portuguese and english)
################################################################
#############tentativa inicial de documentação##################
################################################################
voltei depois de alguns meses ao projeto CALEB e me deparei com
varios arquivos bagunçados e decidi tentar mapear quais arquivos
se relacionam uns com os outros, e quais ainda faltam ser
implementados.

Reconhecimento de voz:

1)transcritor.py
importa o arquivo decisao, que chama algum shell script com uma
ação pro linux.

2)decisao.py
um monte de if e elif, que vai fazer o python rodar o shell
script, que geralmente é auto explicativo pelo nome. se não for
auto explicativo, consulte a documentação, se houver alguma
alem dessa.
implementar mais decisoes no futuro

3)audiorecording.txt
log escrito de todo o audio que for analisado quando o arquivo
transcritor.py for executado.
implementar metodos e atributos que permitam maior privacidade
e anonimato ao usuario final.
