pt = open('./VSCodeUserSetup-x64.exe.[B04883D6[decryptprof@mailfence.com].Sup.Sup', 'rb').read()
ct = open('./VSCodeUserSetup-x64-1.63.2.exe', 'rb').read()
with open('key.bin', 'wb') as f:
    for i in range(8827448):
        f.write(bytes([pt[i] ^ ct[i]]))