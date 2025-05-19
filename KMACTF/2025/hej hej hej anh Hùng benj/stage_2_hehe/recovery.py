hehe_enc = open('hehe.txt.[B04883D6[decryptprof@mailfence.com].Sup', 'rb').read()
huh_enc = open('huh.txt[B04883D6[decryptprof@mailfence.com].Sup', 'rb').read()

key = open('key.bin', 'rb').read()
with open('hehe.txt', 'w') as he, open('huh.txt', 'w') as huh:
    for i in range(len(hehe_enc)):
        he.write(chr((hehe_enc[i] ^ key[i]) & 0xFF))
    for j in range(len(huh_enc)):
        huh.write(chr((huh_enc[j] ^ key[j]) & 0xFF))