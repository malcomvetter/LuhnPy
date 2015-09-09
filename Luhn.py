def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10
 
def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0
 
i = 0
with open("cc.txt") as f:
        for line in f:
                if (str(int(line)) != "0000000000000000"):
                        if (str(int(line)) != "8888888888888888"):
                                if  (len(str(int(line))) == 16):
                                        if (is_luhn_valid(int(line))):
                                                i = i + 1
                                                print str(i) + ": " + str(int(line))
 
