import codecs
import binascii
hex='1c0111001f010100061a024b53535009181c'
xor_against='686974207468652062756c6c277320657965'
final_answer = '746865206b696420646f6e277420706c6179'
hex_decoded = codecs.decode(hex,'hex').decode()#.decode() Always operate on raw bytes, ne
xor_against_decoded = codecs.decode(xor_against,'hex').decode()
l = [ord(a) ^ ord(b) for a,b in zip(hex_decoded,xor_against_decoded)]
answer = binascii.hexlify(bytearray(l)).decode()
print(answer == final_answer)