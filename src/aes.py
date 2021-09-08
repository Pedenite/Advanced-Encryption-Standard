from util.args_helper import str2bool
import util.passphrase
import argparse
import os
import sys
from symmetric.cipher import Cipher
from symmetric.decipher import Decipher

parser = argparse.ArgumentParser(description='Cifra e decifra dados usando a cifra de bloco AES simétrica.', formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('mensagem', type=argparse.FileType('rb'), help='Arquivo com a mensagem a ser cifrada/decifrada')
parser.add_argument('-k', nargs='?', type=argparse.FileType('rb'), help='Arquivo com a chave de criptografia. Se não informado, será gerada uma chave automaticamente que será salva no arquivo \'keys/key[tamanho da chave]\'', metavar='chave')
parser.add_argument('-o', type=argparse.FileType('w'), help='Arquivo de saída', metavar='output', required=True)
parser.add_argument('-d', nargs='?', type=str2bool, const=True, default=False, help='Especifica que a mensagem deve ser decifrada na execução (padrão: cifrar)', metavar='decifrar')
parser.add_argument('-r', nargs='?', type=int, default=10, help='Quantidade de rodadas', metavar='rounds')

args = parser.parse_args()

os.chdir(os.path.dirname(sys.argv[0]))

if args.r <= 0:
    print("Quantidade de rounds inválida!")
    exit()

msg = pswd = []
with args.mensagem as f:
    byte = f.read(1)
    while byte != b"":
        msg.append(ord(byte))
        byte = f.read(1)

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

res = Decipher(msg, pswd, args.r) if args.d else Cipher(msg, pswd, args.r)

with args.o as file:
    print(res, end='', file=file)
