from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse

def set_format(detail):
  detail = hex(detail).upper()
  detail =  ':'.join(a + b for a, b in zip(detail[::2], detail[1::2]))
  detail = detail.replace('X', '0', 1)
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
    "Modulus": set_format(public_key.n),
    "Public Exponent": public_key.e
  }
  return key_details

def private_key_details(private_key):
  '''
  Función que retorna las propiedades de una llave privada
  '''
  key_details = {
    "Modulus": set_format(private_key.n),
    "Public Exponent": private_key.e,
    "Private Exponent": set_format(private_key.d),
    "First Prime": set_format(private_key.p),
    "Second Prime": set_format(private_key.q),
    "First Exponent": set_format(private_key.d % (private_key.p - 1)),
    "Second Exponent": set_format(private_key.d % (private_key.q - 1)),
    "Coefficient": set_format(inverse(private_key.q, private_key.p))
  }
  return key_details

def get_details(key_type, pem_file):
  key = load_key(pem_file)
  key_type = str(key_type).lower()
  if key_type == "private":
    details_dic = private_key_details(key)
    return details_dic
  elif key_type == "public":
    details_dic = public_key_details(key)
    return details_dic

def is_validate(pem_file):
  # Convertimos de bytes a string
  content = pem_file.decode("utf-8")
  try:
    # Obtenemos el objeto RSA key
    key = RSA.importKey(content)
    return [True, ""]
  except:
    return [False, "Formato inválido de la llave RSA"]