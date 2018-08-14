import codecs
import base64

hex_str='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
final_answer='SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
answer = base64.b64encode(codecs.decode(hex_str,'hex')).decode() #Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
print(answer == final_answer)