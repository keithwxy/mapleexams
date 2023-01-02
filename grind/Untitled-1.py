import hashlib


abc = "0894375830497850938475289739079324908734\n"
pos = 0

for i in abc:
    ii = int(i)
    for x in range (0, 10):
        if ii == 9:
            ii = 0
        else:
            ii += 1
        newstr = abc[:pos] + str(ii) + abc[pos + 1:]
        #print(newstr)
        sha_1 = hashlib.sha1(newstr.encode('utf-8'))
        #print(sha_1.hexdigest())
        if sha_1.hexdigest() == "819daf53aad4a6a605d40d21a0b578049a110447":
            print(newstr)
    pos += 1