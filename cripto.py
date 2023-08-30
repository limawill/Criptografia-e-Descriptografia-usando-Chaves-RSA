# Importar as bibliotecas necessárias
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Geração de chave RSA
key = RSA.generate(2048)

# Salvar a chave privada em um arquivo
private_key = key.export_key()
with open('private_key.pem', 'wb') as f:
    f.write(private_key)

# Salvar a chave pública em um arquivo
public_key = key.publickey().export_key()
with open('public_key.pem', 'wb') as f:
    f.write(public_key)

# Criptografar uma mensagem usando a chave pública
def encrypt_message(message, public_key_file):
    """
    Criptografa uma mensagem usando a chave pública fornecida.

    Args:
        message (str): A mensagem a ser criptografada.
        public_key_file (str): Caminho para o arquivo contendo a chave pública.

    Returns:
        bytes: Mensagem criptografada.
    """
    with open(public_key_file, 'rb') as f:
        public_key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

# Entrada da mensagem para criptografar
message = input("Digite a mensagem para criptografar: ")

# Criptografar a mensagem
encrypted_message = encrypt_message(message, 'public_key.pem')

# Codificar a mensagem criptografada em base64
rsa_base64 = base64.b64encode(encrypted_message).decode('utf-8')

# Imprimir a mensagem criptografada em base64
print("Mensagem criptografada:", rsa_base64)

