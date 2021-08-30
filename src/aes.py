from util.args_helper import str2bool
import util.passphrase
import argparse
import os
import sys

parser = argparse.ArgumentParser(description='Cifra e decifra dados usando a cifra de bloco AES simétrica.', formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('mensagem', type=argparse.FileType('r'), help='Arquivo com a mensagem a ser cifrada/decifrada')
parser.add_argument('-k', nargs='?', type=argparse.FileType('rb'), help='Arquivo com a chave de criptografia. Se não informado, será gerada uma chave automaticamente que será salva no arquivo \'key[tamanho da chave]\'', metavar='chave')
parser.add_argument('-o', type=argparse.FileType('w'), help='Arquivo de saída', metavar='output', required=True)
parser.add_argument('-d', nargs='?', type=str2bool, const=True, default=False, help='Especifica que a mensagem deve ser decifrada na execução (padrão: cifrar)', metavar='decifrar')

args = parser.parse_args()

os.chdir(os.path.dirname(sys.argv[0]))

msg = pswd = ''
with args.mensagem as file:
    msg = file.read()

if args.k == None:
    if args.d:
        print("É necessário informar uma chave para decifrar!")
        exit()
    pswd = util.passphrase.generate_key()
else:
    try:
        pswd = util.passphrase.parse_key(args.k)
    except Exception as e:
        print(e)

res = "Saida"#cifra(msg, pswd, args.d)

with args.o as file:
    print(res, end='', file=file)
