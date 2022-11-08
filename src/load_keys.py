from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse

def set_format(detail):
  detail = hex(detail).upper()
  detail =  ':'.join(a + b for a, b in zip(detail[::2], detail[1::2]))
  return detail

def load_key(pem_file):
  '''
  Función que recibe el archivo PEM en bytes y retorna un objeto RSA key
  '''
  # Convertimos de bytes a string
  content = pem_file.decode("utf-8")
  # Obtenemos el objeto RSA key
  key = RSA.importKey(content)
  return key

def public_key_details(public_key):
  '''
  Función que retorna las propiedades de una llave pública
  '''
  key_details = {
    "modulus": set_format(public_key.n),
    "public_exponent": public_key.e
  }
  return key_details

def private_key_details(private_key):
  '''
  Función que retorna las propiedades de una llave privada
  '''
  key_details = {
    "modulus": set_format(private_key.n),
    "public_exponent": private_key.e,
    "private_exponent": set_format(private_key.d),
    "first_prime": set_format(private_key.p),
    "second_prime": set_format(private_key.q),
    "first_exponent": set_format(private_key.d % (private_key.p - 1)),
    "second_exponent": set_format(private_key.d % (private_key.q - 1)),
    "coefficient": set_format(inverse(private_key.q, private_key.p))
  }
  return key_details