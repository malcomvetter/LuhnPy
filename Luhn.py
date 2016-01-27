# Author: Tim MalcomVetter
# github.com/malcomvetter

import re, math, sys, getopt

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
 

def generate_CC(template):
    template = template.replace('X','x').replace('-','').replace(' ','')
    start = len(template)
    end = 0
    for m in re.finditer('x', template):
        if (m.start() < start):
            start = m.start()
        if (m.end() > end):
            end = m.end();	
    prefix = template[:start]
    suffix = template[end:]
    for x in xrange (0, int(math.pow(10, end-start))):
        padding = ''
        for y in xrange (len(str(x)), (end-start)):
            padding = padding + '0'
        cc = prefix + padding + str(x) + suffix
        if (is_luhn_valid(int(cc[:(len(cc) -1)]))):
            print cc
    return

def validate_file(filename):
    i = 0
    with open(filename) as f:
            for line in f:
                    if (str(int(line)) != "0000000000000000"):
                            if (str(int(line)) != "8888888888888888"):
                                    if  (len(str(int(line))) == 16):
                                            if (is_luhn_valid(int(line))):
                                                    i = i + 1
                                                    #print str(i) + ": " + str(int(line))
                                                    print str(int(line))

def printHeader():
    print 'Luhn.py - Tim MalcomVetter (@malcomvetter)'
    print '_' * 63
    print ' __                 __                                         '
    print '|  \\               |  \\                                        '
    print '| $$      __    __ | $$____   _______        ______   __    __ '
    print '| $$     |  \\  |  \\| $$    \\ |       \\      /      \\ |  \\  |  \\'
    print '| $$     | $$  | $$| $$$$$$$\\| $$$$$$$\\    |  $$$$$$\\| $$  | $$'
    print '| $$     | $$  | $$| $$  | $$| $$  | $$    | $$  | $$| $$  | $$'
    print '| $$_____| $$__/ $$| $$  | $$| $$  | $$ __ | $$__/ $$| $$__/ $$'
    print '| $$     \\\\$$    $$| $$  | $$| $$  | $$|  \\| $$    $$ \\$$    $$'
    print ' \\$$$$$$$$ \\$$$$$$  \\$$   \\$$ \\$$   \\$$ \\$$| $$$$$$$  _\\$$$$$$$'
    print '                                           | $$      |  \\__| $$'
    print '                                           | $$       \\$$    $$'
    print '                                            \\$$        \\$$$$$$ '
    print '_' * 63
    print

def printHelp():
    printHeader()
    print 'To validate a file of potential credit card numbers:'
    print 'luhn.py -i <inputfile>'
    print    
    print 'To generate a list of luhn-valid credit card numbers based on a template:'
    print 'luhn.py -t 411111xxxxxx1111'
    print


try:
    opts, args = getopt.getopt(sys.argv[1:],'hi:t:')
except getopt.GetoptError:
    printHelp()
    sys.exit(2)

if len(opts) == 0:
    printHelp()
    sys.exit(1)

for opt, arg in opts:
    if opt == '-h':
        printHelp()
        sys.exit()
    elif opt in ("-i"):
        validate_file(arg)
        sys.exit()
    elif opt in ("-t"):
        generate_CC(arg)
        sys.exit()

