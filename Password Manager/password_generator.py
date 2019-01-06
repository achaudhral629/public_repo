import hashlib
import binascii

def generate_salt_one(website,user_name,version):
    return website + user_name + version

def generate_salt_two(website,master_password,version):
    return website + master_password + version

def key_stretch_one(salt_one,master_password):
    return decode_utf(hashlib.pbkdf2_hmac
                            ("sha256", encode_utf(master_password),
                                                encode_utf(salt_one), 100000, 32))
def key_stretch_two(salt_two,ver_one, length):
    return decode_utf(binascii.hexlify(hashlib.pbkdf2_hmac
                            ("sha256", encode_utf(ver_one),
                                                encode_utf(salt_two), 100000, length))) #.decode() instead ?
def decimal_to_alphabet(ver_two, length,alphabet):
    num_elements = len(alphabet)
    chars = []
    while len(chars) < length:
        ver_two, index = divmod(ver_two, num_elements)
        chars.append(alphabet[index])
    ver_two = ''.join(chars)
    return ver_two
    
def encode_utf(txt):
    return txt.encode("utf-8")

def decode_utf(txt):
    return txt.decode("utf-8",'ignore')

def generate_password(website, user_name, master_password, version, length,alphabet):
    salt_one = generate_salt_one(website,user_name,version)
    salt_two = generate_salt_two(website,master_password,version)
    middle = length
    ver_one = key_stretch_one(salt_one,master_password)
    ver_two = key_stretch_two(salt_two,ver_one,length)
    ver_two = ver_two[:middle]
    ver_two = Decimal_to_hexdecimal(ver_two)
    ver_three = decimal_to_alphabet(ver_two, length,alphabet)
    return ver_three
    
def Decimal_to_hexdecimal(Dec):
    return int(Dec,16)

