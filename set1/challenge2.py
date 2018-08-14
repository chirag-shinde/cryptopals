import codecs
import binascii
hex_str='1c0111001f010100061a024b53535009181c'
xor_against='686974207468652062756c6c277320657965'
final_answer = '746865206b696420646f6e277420706c6179'

def fixed_xor(hex_str, xor_against):
    hex_decoded = codecs.decode(hex_str,'hex')#.decode() Always operate on raw bytes, ne
    xor_against_decoded = codecs.decode(xor_against,'hex')
    l = [a ^ b for a,b in zip(hex_decoded,xor_against_decoded)]
    answer = binascii.hexlify(bytearray(l)).decode('ascii')
    return answer

assert(fixed_xor(hex_str,xor_against) == final_answer)