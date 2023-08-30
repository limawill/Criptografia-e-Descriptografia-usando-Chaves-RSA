# Criptografia e Descriptografia usando Chaves RSA

Este repositório contém dois scripts Python que demonstram o processo de criptografia e descriptografia de mensagens usando chaves RSA. A criptografia é feita usando a biblioteca Crypto da PyCryptodome para a manipulação de chaves e operações de criptografia.
Bibliotecas Utilizadas

### Os seguintes pacotes e bibliotecas foram utilizados nestes scripts:

- base64: Biblioteca padrão do Python para codificação e decodificação em base64.
- Crypto.PublicKey.RSA: Parte da biblioteca PyCryptodome que é usada para gerar chaves RSA e importar chaves públicas/privadas.
- Crypto.Cipher.PKCS1_OAEP: Usada para criar um objeto de cifra usando o esquema de padding PKCS1 OAEP (Optimal Asymmetric Encryption Padding).

## Scripts

#### python generate_keys.py

Este script gera um par de chaves RSA (chave pública e privada) e as salva em arquivos separados. Ele demonstra:

- Geração de chaves RSA de 2048 bits.
- Exportação e armazenamento da chave privada em um arquivo private_key.pem.
- Exportação e armazenamento da chave pública em um arquivo public_key.pem.

#### encrypt_decrypt.py

Este script contém duas funções principais:

- encrypt_message(message, public_key_file): Esta função criptografa uma mensagem usando a chave pública fornecida e retorna a mensagem criptografada em formato base64.
- decrypt_message(encrypted_message, private_key_file): Esta função descriptografa uma mensagem criptografada (em formato base64) usando a chave privada fornecida e retorna a mensagem original descriptografada.

Ambos os scripts solicitam interação do usuário para entrada da mensagem (no caso de criptografia) ou da mensagem criptografada em base64 (no caso de descriptografia).
Executando os Scripts

Para executar os scripts, você precisa ter o Python instalado e as bibliotecas Crypto e base64 instaladas. Você pode instalar as bibliotecas necessárias usando o seguinte comando:

```sh
pip install pycryptodome
```
Depois de instalar as bibliotecas, você pode executar os scripts da seguinte maneira:

- Execute generate_keys.py para gerar o par de chaves e salvá-las em arquivos.
- Execute encrypt_decrypt.py para criptografar e descriptografar mensagens usando as chaves geradas.

Lembre-se de substituir as mensagens e chaves de exemplo pelos seus próprios valores e chaves.
Nota

Este projeto é apenas uma demonstração e não deve ser usado para fins de segurança real. Para aplicações reais, é altamente recomendado usar bibliotecas e métodos de criptografia revisados e comprovados, além de adotar práticas de segurança adequadas.
