#turn an IP into binary
#233.233.233.233
#this is the first program i've ever made in py

IP = str(input(""))
hex_list = IP.split('.')

hex1 = hex_list[0]
hex2 = hex_list[1]
hex3 = hex_list[2]
hex4 = hex_list[3]

#print (hex_list)
#print (hex1)
#print (hex2)
#print (hex3)
#print (hex4)

Hex1 = int(hex1)
Hex2 = int(hex2)
Hex3 = int(hex3)
Hex4 = int(hex4)

# 128   64  32  16  8   4   2   1

loop = 1
while loop < 5:
    if loop == 1:
        math = Hex1
    elif loop == 2:
        math = Hex2
    elif loop == 3:
        math = Hex3
    elif loop == 4:
        math = Hex4    

    if math >= 128:
            bin1 = 1
            math = math - 128
    else: 
            bin1 = 0
    
    if math >= 64:
            bin2 = 1
            math = math - 64
    else:
            bin2 = 0
    if math >= 32:
            bin3 = 1
            math = math - 32
    else:
            bin3 = 0
    if math >= 16:
            bin4 = 1
            math = math - 16
    else:
            bin4 = 0
    if math >= 8:
            bin5 = 1
            math = math - 8
    else:
            bin5 = 0
    if math >= 4:
            bin6 = 1
            math = math - 4
    else:
            bin6 = 0
    if math >= 2:
            bin7 = 1
            math = math - 2
    else:
            bin7 = 0
    if math >= 1:
            bin8 = 1
    else:
            bin8 = 0
            
    if loop == 1:
        Bin1 = bin1, bin2, bin3, bin4, bin5, bin6, bin7, bin8
    elif loop == 2:
        Bin2 = bin1, bin2, bin3, bin4, bin5, bin6, bin7, bin8
    elif loop == 3:
        Bin3 = bin1, bin2, bin3, bin4, bin5, bin6, bin7, bin8
    elif loop == 4:
        Bin4 = bin1, bin2, bin3, bin4, bin5, bin6, bin7, bin8
    loop += 1
    if loop == 5:
        continue
     
print(Bin1)
print(Bin2)
print(Bin3)
print(Bin4)     
     
