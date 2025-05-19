from pwn import *
from string import *

context.log_level = 'error'
charset = ascii_letters + digits + punctuation
flag = list('KCSC{') + ['a'] * 46
for i in range(5, 51):
    for c in charset:
        tmp = flag.copy()
        tmp[i] = c
        btmp = ''.join(tmp).encode()
        io = process(['python', './deob_proc.py'])
        io.recvuntil(b'Enter Flag: ')
        io.sendline(btmp)
        fs = io.recvall().decode().split('\n')[0]
        if fs[i] == '1':
            flag[i] = c
            io.close()
            break

print(''.join(flag))