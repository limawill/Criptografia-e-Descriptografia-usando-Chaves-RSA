import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def decrypt_message(encrypted_message, private_key_file):
    """
    Descriptografa uma mensagem criptografada usando a chave privada fornecida.

    Args:
        encrypted_message (str): A mensagem criptografada em formato base64.
        private_key_file (str): Caminho para o arquivo contendo a chave privada.

    Returns:
        str: Mensagem descriptografada.
    """
    with open(private_key_file, 'rb') as f:
        private_key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode()

# Entrada da mensagem criptografada em base64
mensagem = input("Digite a chave: ")

# Decodificar a mensagem criptografada de base64
rsa_byte = base64.b64decode(mensagem)
print(rsa_byte)

# Descriptografar a mensagem
decrypted_message = decrypt_message(mensagem, 'private_key.pem')

# Imprimir a mensagem descriptografada
print("Mensagem descriptografada:", decrypted_message)

