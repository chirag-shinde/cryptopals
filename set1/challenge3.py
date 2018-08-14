import codecs
import string
import binascii
import re
hex_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# FREQ_TABLE = {
# "e":0.12702, 
# "t":0.09056,
# "a":0.08167,
# "o":0.07507,
# "i":0.06966,
# "n":0.06749,
# "s":0.06327,
# "h":0.06094,
# "r":0.05987,
# "d":0.04253,
# "l":0.04025,
# "c":0.02782,
# "u":0.02758,
# "m":0.02406,
# "w":0.02360,
# "f":0.02228,
# "g":0.02015,
# "y":0.01974,
# "p":0.01929,
# "b":0.01492,
# }

CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}
def get_frequency(answer):    
    score = 0
    for char in answer:
        if char.lower() in CHARACTER_FREQ:
            score += CHARACTER_FREQ[char.lower()]
    return score,answer

def single_byte_xor_cipher(hex_str):
    scores = []
    hex_decoded = codecs.decode(hex_str,'hex')
    for char in string.ascii_letters:
        l = [a ^ ord(char) for a in hex_decoded]
        answer = bytearray(l).decode()
        answer = re.sub(r'[\x00-\x1F]+', '', answer)
        scores.append(get_frequency(answer))
        l = []
    print(max(scores, key=lambda x: x[0]))
single_byte_xor_cipher(hex_str)