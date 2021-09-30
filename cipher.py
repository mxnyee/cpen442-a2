import math, itertools, timeit, functools
import secrets, string

NUM_LETTERS = 26
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cipher1 = 'SNKTQUSGPARNATRIKRUMPEMMPRKMPRQUNZTOKMHRGNGMSKXQEHNZMSMVNLLEQNZIKNUGPRPEODZSMRYNFXNMMRKMPROZVPRGGHQMPSGMSLRVNLLEEKOUEGETSMMTRGMEFMTROUPRKGPRPREFOPRFBNSVRVTNGRMNPRFREFONMQNZFRMPSKISKXEHNZMGNLRMPSKXVNLLELQOREFVNLLEEKOMPEMLEIRGQNZYNFXRMMNMETIONMSVEKMMRTTQNZJZGMKNUUPEMMPRLNFETNYMPEMSGVNLLEHZMSGPETTFRLRLHRFSMSKEHSMONMARFPEAGSMPEGKMNKRVNLLEETSVRBRKMZFROMNFRLEFIONMMZMVNLLEMZMVNLLEVPSTOGESOMPROZVPRGGONMRBRFQMPSKXGXNMELNFETVNLLESYNKTQQNZVEKYSKOSM'
cipher2 = 'RAVMWBGUKNOPMHYNKNSFKNISVBSFLZSCVFTLOPONTMQVVWTAPZNHOSSUETZVVCCIOPOHVPNIIBYMMKZPEPCKILPRKBXNQIWVAWWBGCOPFEGUPEEFFBIZQVZNFZPQLIILGSWYBWVFUVVCCAIBMGFIWIQVXAIUDAAWCONIQPOHVPSFBOQVVCTMIUDAAWRAVMWBGUKNOPMHYNTGZSTMHFNFSIUYOSNPWBMUOPSWPIWNDCPEKBWNKBZTTMQPNSVQSFPVEZPVVUSFBOYNGMPIIPVCBWVSSUIUNIWDVIHLSCYTTEZXCMQHYREPZVEGLIIUDAAWWBGDKRMYCMWKSFPVSFHFRFSFBOHFQGIPBOWYSFQIHFQGVUVUNKSFSNUHMGSFPQWBGUEPUMHUBWCMIPEOQVDCPEKBXNWVAWNXDYVSQVOSVNCIOPSVYMRNWCISGLOPAHPVVIZVGSOPVNXUGQVITLOPVSZVDSWVAWWBGCOPCMVHQYBPRUNVSCIFSFBOKNPVVUINONVWFCIUDAAWRAOTIBOLQKEFUNWVAWSDEVGDKRMYCMWKSFPVIUDAAWWBRCQZVETLOPNWILYSYNPRFIILRXHFDSEFSFPIVUCLOQBKBKNWNRCQFSUZHUSNBIFIIFNHNVIUDAAWWBRUBOYNIWISCIOPEPYNINEHTEQVPAKBPFSNVFUVOHGSWCQVFIOPBKFDOPXQWVAWUWBIOPNXVBIFSFLIHEHOSFBOKNPVIUDAAWWBRCNWVNCIHIWHVPVUNLFCUWBIMKZPEPCKILNXVBDHCACSTMHFCKIFOSRNOPOHWCRUSNNSGFNYCMZVEGLIKBPGOCIBMQKSOPVSZVMGFISFPBVSCTPINHYNWBVMXSWVAWWBRCOPATBOIUDAAWHOIUHDIPIUDAAWUWUVCVSIVUINOPWYMXQKGLOPONTMQVVWTAPZNPVHFDFSQPOHVPOPDSWVAWWBRCOPNYCVKNOTYPCKSFKNSFVEMHSCRTPSHFQGQPISQVWBGCOPHPWHFQMQLIVPKNQVYNSFPZWYGCVPKNQVDCPEKBXNWVAWWBXUGMHEBPVCCIOPVSZVMGFIQWNGKRMYCMWKSFPVBEBZVQRUYMXQWVAWOHYSLZIBFNOPVWTAPZNHHFQGGMHUCSCIOPVSZVMHSIFSOPSVONTMNIEVXQWVAWWBXDOQBKBKNYCVXZSCMUHVGUHVSFBVKBIHIHSFKNMKZPEPCKILOTBWQKPKPRYMQVSFBVIUDAAWWIIUCMSIEICIWYCKSFBOSCVLGDWIZLHPPSHFQGVZPVKWILMGFISYQZLINVPISFPQCVVCTMHOSFVINBPVHOSFLVFEVQCTYBVUCKSFSNNXRSXMQPBIAWVQOHMYOBXUVCTMRYPIBICKIFDCPEKBXNWVAWWBVCISCYNYCVIFWYZVIUNISFPBVSCTPIPSKBOWPVZTTMVUDGFIHOIUHDIPRAVMWBGUKNOPMYCMKBGLOPFIOPMDWIZLHPKNWIIQKMVPQVIFSFQIWIVCISWIIUDAAWWBGCWYISPSHUSIWYQYBPCNSFKNOBYMLISYQZLINVPISFPIBKZVIHTLOPHUIBVHTLOPVFQGBINXQSWVAWUWHIIVZVYSBVXAQPVUNKCMUWKNQPNXVBHOSFBVYNZLXUVUVHSFXSWVAWUWHWXMQPBIVMBZLGZSCIPVPIILVCCIOPNIHVXRFIDCPEKBWMVETMSFLOSVNIHUIBVHTLOPVFQGBINXQSWVAWVPBEEVGCOPVWTAPZIUDAAWOPNWNIOPOTYPCKIFBKHSSNONPSPIHQWIHCVUNKPSSNPMCVQIHFQGIWNLBZGSOPNSRFIFOFNTWVAWOPNXQKEPXCNYQKGLHWNVSCSFLOHVPINKTLPVOPWYGDYMVSQVOPMYCMHVVQVPXCNYBFXANIFZQZPBUWPVPIOPIUFQMCVZPVKMZNCNLIPZPIWIWNSCVLGDWIZLXSWVAWUWSTWUBOPVLVBKGCUVUIWVAWOHMHBOPVBZQKBKHGZNVUOWPVVUCKSFSNNWNYQKBFQZVZPVWYGCUVHFCITESFLVFEVQCTYBOLQKETCIFIOPWYCMIHTLOPONTXQVONITWHTLOPOBNIIUDAAWUWWVXMQOIPCNBKZVSFBOSCZTPIIUDAAWWBMXTLPVNWMGGMEZVIYONVIPGTHFIFTLOPBKCMHOSFBOPICGFIIWFNOPVFQGBINXESPHHFYPIUDAAWWBGCSYQZLINVPIZHFWZMLIOPVSRFCKIFBKAKZHHDONPSPIHQWIHCVUNKNIOPVWTAPZZTTMOTCSPSQVOSCYNIHVXRHVFISHEFFZQVVUNBWBRCWNSFLVVPBIIUDAAWPSSCSCMFKBPTHOSFQZBVPVKBXQSIAPLOHVLIOPDGFIPSBOWIVQVPMXCKSFPVYBCVTGTVFSHOSFBVWIZLHPIUDAAWQWNFYNKGXMSFVEHFMSPZNWIHZVMGFISFPISGWBVLSDBZCFVPCYIPCKSFLIMYZVEPYPVUNBNXVPOFQKPKQPOHVPSFLVKNVITLOPTSSKIUDAAWSFLZSCMLHUQVEFFNUVHVFISHIUDAAWWBGCOPTWEPHNONTLPKWNXAIUDAAWOHQKEFOBMQAXQKPFSNMWCM'

cipher = cipher2
N = len(cipher)


# shift cipher
def shift_letter(char, shift):
    offset = ord(char) - ord('A')
    new_offset = ((offset - shift) % NUM_LETTERS) + ord('A')
    return chr(new_offset)

def run_shift():
    for shift in range(NUM_LETTERS):
        output = ''
        for char in cipher:
            output += shift_letter(char, shift)
        
        print(shift)
        print(output)


# letter frequency
def run_hist(input = cipher):
    hist = {}
    for char in input:
        if char in hist:
            hist[char] = hist[char] + 1
        else:
            hist[char] = 1
    ranking = sorted(hist.items(), key=lambda tuple: tuple[1], reverse=True)
    
    map = {}
    for item in ranking:
        letter = item[0]
        percent = round(hist[letter] / len(input) * 100, 2)
        map[letter] = percent
    return map


# word frequency
def run_hist2():
    word_length = 3
    hist = {}
    for i in range(word_length - 1, N):
        word = cipher[i - word_length:i]
        if word in hist:
            hist[word] = hist[word] + 1
        else:
            hist[word] = 1
    ranking = sorted(hist.items(), key=lambda tuple: tuple[1], reverse=True)
    
    for item in ranking:
        print(item)


# digraph frequency
def run_hist3(input = cipher):
    hist = {}
    for i in range(len(input) - 1):
        pair = input[i:i+2]
        if pair in hist:
            hist[pair] = hist[pair] + 1
        else:
            hist[pair] = 1
    ranking = sorted(hist.items(), key=lambda tuple: tuple[1], reverse=True)
    
    map = {}
    for item in ranking:
        pair = item[0]
        percent = round(hist[pair] / (len(input) - 1) * 100, 2)
        map[pair] = percent
    return map

# polyalphabetic
def decrypt_poly(shift_word):
    output = ''
    for i in range(N):
        j = i % len(shift_word)
        letter_shift = shift_word[j]

        output += shift_letter(cipher[i], letter_shift)

    print(shift_word)
    print(output)

def run_poly():
    for n in range(2, 33):
        hist = {}
        for i in range(N):
            offset = i % n
            char = cipher[i]

            if offset in hist:
                if char in hist[offset]:
                    hist[offset][char] = hist[offset][char] + 1
                else:
                    hist[offset][char] = 1
            else:
                hist[offset] = { char: 1 }
        
        shift_word = []
        for offset in hist.keys():
            ranking = sorted(hist[offset].items(), key=lambda tuple: tuple[1], reverse=True)
            result = (ord(ranking[0][0]) - ord('A')) - (ord('E') - ord('A')) % NUM_LETTERS
            shift_word.append(result)

        decrypt_poly(shift_word)


# codebook
code = {
    'V': 'C',
    'N': 'O',
    'L': 'M',
    'E': 'A',
    'R': 'E',
    'M': 'T',
    'S': 'I',
    'K': 'N',
    'G': 'S',
    'P': 'H',
    'F': 'R',
    'O': 'D',

    'U': 'W',
    'I': 'K',
    'X': 'G',
    'B': 'V',
    'Y': 'F',
    'T': 'L',
    'Q': 'Y',
    'Z': 'U',
    'H': 'B',
    'D': 'Q',
    'J': 'J',
    'A': 'P',

    'C': '_',
    'W': '_',
}
def run_code():
    output = ''
    for char in cipher:
        if char in code:
            output += code[char]
        else:
            output += '_'
    print(output)


# brute force
FREQUENCY = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
HIST = 'MNREPLSKGOFTVZQUHXIYABDJCW'
known = {
    'V': 'C',
    'N': 'O',
    'L': 'M',
    'E': 'A',
}
ignore = 'TVZQUHXIYABDJCW'
m0 = 'ETINSHRD'

def run_brute():
    substr = cipher
    letters = list(filter(lambda c: c not in known and c not in ignore, ALPHABET))
    perms = itertools.permutations(letters)
    print('perms for ', letters)
    for perm in perms:
        output = ''
        for char in substr:
            if char in known:
                output += known[char]
            elif char in ignore:
                output += '_'
            else:
                index = perm.index(char)
                output += m0[index]
            
        if 'THE' in output:
            print(''.join(perm))
            print(output)



# playfair

def pair_letters(input = cipher):
    out = ''
    arr = []
    for i in range(len(input)):
        if i % 2 == 0:
            out += input[i]
        else:
            out += input[i] + ' '
            pair = input[i-1:i+1]
            arr.append(pair)
    return arr

# http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/
letter_freq = {
    'A':  8.55,
    'K':  0.81,
    'U':  2.68,
    'B':  1.60,
    'L':  4.21,
    'V':  1.06,
    'C':  3.16,
    'M':  2.53,
    'W':  1.83,
    'D':  3.87,
    'N':  7.17,
    'X':  0.19,
    'E': 12.10,
    'O':  7.47,
    'Y':  1.72,
    'F':  2.18,
    'P':  2.07,
    'Z':  0.11,
    'G':  2.09,
    'Q':  0.10,
    'H':  4.96,
    'R':  6.33,
    # 'I':  7.33,
    'I':  7.55, # combine I and J
    'S':  6.73,
    # 'J':  0.22,
    'T':  8.94,
}
bigram_freq = {'TH': 2.71, 'HE': 2.33, 'IN': 2.03, 'ER': 1.78, 'AN': 1.61, 'RE': 1.41, 'ES': 1.32, 'ON': 1.32, 'ST': 1.25, 'NT': 1.17, 'EN': 1.13, 'AT': 1.12, 'ED': 1.08, 'ND': 1.07, 'TO': 1.07, 'OR': 1.06, 'EA': 1.0, 'TI': 1.0, 'AR': 0.98, 'TE': 0.98, 'NG': 0.89, 'AL': 0.88, 'IT': 0.88, 'AS': 0.87, 'IS': 0.86, 'HA': 0.83, 'ET': 0.76, 'SE': 0.73, 'OU': 0.72, 'OF': 0.71, 'LE': 0.7, 'SA': 0.7, 'VE': 0.68, 'RO': 0.68, 'RA': 0.66, 'RI': 0.65, 'HI': 0.64, 'NE': 0.63, 'ME': 0.63, 'DE': 0.63, 'CO': 0.62, 'TA': 0.6, 'EC': 0.6, 'SI': 0.61, 'LL': 0.57, 'SO': 0.55, 'NA': 0.54, 'LI': 0.54, 'LA': 0.54, 'EL': 0.53, 'MA': 0.5, 'DI': 0.52, 'IC': 0.5, 'RT': 0.5, 'NS': 0.49, 'RS': 0.49, 'IO': 0.55, 'OM': 0.49, 'CH': 0.47, 'OT': 0.46, 'CA': 0.46, 'CE': 0.46, 'HO': 0.46, 'BE': 0.45, 'TT': 0.45, 'FO': 0.44, 'TS': 0.44, 'SS': 0.44, 'NO': 0.44, 'EE': 0.43, 'EM': 0.42, 'AC': 0.41, 'IL': 0.41, 'DA': 0.41, 'NI': 0.43, 'UR': 0.4, 'WA': 0.39, 'SH': 0.39, 'EI': 0.4, 'AM': 0.37, 'TR': 0.37, 'DT': 0.36, 'US': 0.36, 'LO': 0.36, 'PE': 0.36, 'UN': 0.35, 'NC': 0.35, 'WI': 0.35, 'UT': 0.35, 'AD': 0.34, 'EW': 0.34, 'OW': 0.34, 'GE': 0.33, 'EP': 0.32, 'AI': 0.34, 'LY': 0.32, 'OL': 0.32, 'FT': 0.32, 'OS': 0.31, 'EO': 0.31, 'EF': 0.31, 'PR': 0.31, 'WE': 0.3, 'DO': 0.3, 'MO': 0.3, 'ID': 0.3, 'IE': 0.32, 'MI': 0.28, 'PA': 0.28, 'FI': 0.28, 'PO': 0.28, 'CT': 0.27, 'WH': 0.27, 'IR': 0.27, 'AY': 0.27, 'GA': 0.26, 'SC': 0.25, 'KE': 0.25, 'EV': 0.24, 'SP': 0.24, 'IM': 0.24, 'OP': 0.24, 'DS': 0.24, 'LD': 0.24, 'UL': 0.24, 'OO': 0.24, 'SU': 0.23, 'IA': 0.27, 'GH': 0.23, 'PL': 
0.23, 'EB': 0.23, 'IG': 0.22, 'VI': 0.22, 'IV': 0.21, 'WO': 0.21, 'YO': 0.21, 'RD': 0.21, 'TW': 0.21, 'BA': 0.21, 'AG': 0.2, 'RY': 0.2, 'AB': 0.2, 'LS': 0.2, 'SW': 0.2, 'AP': 0.2, 'FE': 0.2, 'TU': 0.2, 'CI': 0.2, 'FA': 0.19, 'HT': 0.19, 'FR': 0.19, 'AV': 0.19, 'EG': 0.19, 'GO': 0.19, 'BO': 0.19, 'BU': 0.19, 'TY': 0.19, 'MP': 0.18, 'OC': 0.18, 'OD': 0.18, 'EH': 0.17, 'YS': 0.17, 'EY': 0.17, 'RM': 0.17, 'OV': 0.17, 'GT': 0.17, 'YA': 0.17, 'CK': 0.17, 'GI': 0.17, 'RN': 0.16, 'GR': 0.16, 'RC': 0.16, 'BL': 0.16, 'LT': 0.16, 'YT': 0.16, 'OA': 0.15, 'YE': 0.15, 'OB': 0.14, 'DB': 0.14, 'FF': 0.14, 'SF': 0.14, 'RR': 0.14, 'DU': 0.14, 'KI': 0.14, 'UC': 0.13, 'IF': 0.13, 'AF': 0.13, 'DR': 0.13, 'CL': 0.13, 'EX': 0.13, 'SM': 0.13, 'PI': 0.13, 'SB': 0.13, 'CR': 0.13, 'TL': 0.12, 'OI': 0.14, 'RU': 0.12, 'UP': 0.12, 'BY': 0.12, 'TC': 0.12, 'NN': 0.12, 'AK': 0.12, 'SL': 0.11, 'NF': 0.11, 'UE': 0.11, 'DW': 0.11, 'AU': 0.11, 'PP': 0.11, 'UG': 0.11, 'RL': 0.11, 'RG': 0.11, 'BR': 0.11, 'CU': 0.11, 'UA': 0.11, 'DH': 0.11, 'RK': 0.1, 'YI': 0.11, 'LU': 0.1, 'UM': 0.1, 'BI': 0.11, 'NY': 0.1, 'NW': 0.1, 'QU': 0.1, 'OG': 0.1, 'SN': 0.1, 'MB': 0.1, 'VA': 0.1, 'DF': 0.09, 'DD': 0.09, 'MS': 0.09, 'GS': 0.09, 'AW': 0.09, 'NH': 0.09, 'PU': 0.09, 'HR': 0.09, 'SD': 0.09, 'TB': 0.09, 'PT': 0.09, 'NM': 0.09, 'DC': 0.09, 'GU': 0.09, 'TM': 0.09, 'MU': 0.09, 'NU': 0.09, 'MM': 0.09, 'NL': 0.09, 'EU': 0.08, 'WN': 0.08, 'NB': 0.08, 'RP': 0.08, 'DM': 0.08, 'SR': 0.08, 'UD': 0.08, 'UI': 0.08, 'RF': 0.08, 'OK': 0.08, 'YW': 0.08, 'TF': 0.08, 'IP': 0.08, 'RW': 0.08, 'RB': 0.08, 'OH': 0.08, 'KS': 0.07, 'DP': 0.07, 'FU': 0.07, 'YC': 0.07, 'TP': 0.07, 'MT': 0.07, 'DL': 0.07, 'NK': 0.07, 'CC': 0.07, 'UB': 0.07, 'RH': 0.07, 'NP': 0.07, 'FL': 0.07, 'DN': 0.07, 'KA': 0.07, 'PH': 0.07, 'HU': 0.06, 'LF': 0.06, 'YB': 0.06, 'RV': 0.06, 'OE': 0.06, 'IB': 0.06, 'IK': 0.06, 'YP': 0.06, 'GL': 0.06, 'LP': 0.06, 'YM': 0.06, 'LB': 0.06, 'HS': 0.06, 'DG': 0.06, 'GN': 0.06, 'EK': 0.06, 'NR': 0.06, 'PS': 0.05, 'TD': 0.05, 'LC': 0.05, 'SK': 0.05, 'YF': 0.05, 'YH': 0.05, 'VO': 0.05, 'AH': 0.05, 'DY': 0.05, 'LM': 0.05, 'SY': 0.05, 'NV': 0.05, 'YD': 0.05, 'FS': 0.05, 'SG': 0.05, 'YR': 0.05, 'YL': 0.05, 'WS': 0.05, 'MY': 0.05, 'OY': 0.04, 'KN': 0.04, 'IZ': 0.04, 'XP': 0.04, 'LW': 0.04, 'TN': 0.04, 'KO': 0.04, 'AA': 0.04, 'ZE': 0.04, 'FC': 0.04, 'GW': 0.04, 'TG': 0.04, 'XT': 0.03, 'FH': 0.03, 'LR': 0.03, 'YN': 0.03, 'GG': 0.03, 'GF': 0.03, 'EQ': 0.03, 'HY': 0.03, 'KT': 0.03, 'HC': 0.03, 'BS': 0.03, 'HW': 0.03, 'HN': 0.03, 'CS': 0.03, 'HM': 0.03, 'HH': 0.03, 'WT': 0.03, 'GC': 0.03, 'LH': 0.03, 'FM': 0.03, 'DV': 0.03, 'LV': 0.03, 'WR': 0.03, 'GP': 0.03, 'FP': 0.03, 'GB': 0.03, 'GM': 0.03, 'HL': 0.03, 'LK': 0.03, 'CY': 0.03, 'MC': 0.03, 'YG': 0.02, 'XI': 0.02, 'HB': 0.02, 'FW': 0.02, 'GY': 0.02, 'HP': 0.02, 'MW': 0.02, 'PM': 0.02, 'ZA': 0.02, 'LG': 0.02, 'IW': 0.02, 'XA': 0.02, 'FB': 0.02, 'SV': 0.02, 'GD': 0.02, 'IX': 0.02, 'KL': 0.02, 'HF': 0.02, 'HD': 0.02, 'AE': 0.02, 'SQ': 0.02, 'FY': 0.02, 'AZ': 0.02, 'LN': 0.02, 'AO': 0.02, 'FD': 0.02, 'KW': 0.02, 'MF': 0.02, 'MH': 0.02, 'UF': 0.02, 'TV': 0.02, 'XC': 0.02, 'YU': 0.02, 'BB': 0.02, 'WW': 0.02, 'AX': 0.02, 'MR': 0.02, 'WL': 0.02, 'XE': 0.02, 'KH': 0.02, 'OX': 0.02, 'UO': 0.02, 'ZI': 0.02, 'FG': 0.01, 'IH': 0.01, 'TK': 0.01, 'II': 0.01, 'IU': 0.08, 'MN': 0.01, 'WY': 0.01, 'KY': 0.01, 'KF': 0.01, 'FN': 0.01, 'UY': 0.01, 'PW': 0.01, 'DK': 0.01, 'UK': 0.01, 'KR': 0.01, 'KU': 0.01, 'WM': 0.01, 'KM': 0.01, 'MD': 0.01, 'ML': 0.01, 'EZ': 0.01, 'KB': 0.01, 'WC': 0.01, 'WD': 0.01, 'HG': 0.01, 'BT': 0.01, 'ZO': 0.01, 'KC': 0.01, 'PF': 0.01, 'YV': 0.01, 'PC': 0.01, 'PY': 0.01, 'WB': 0.01, 'YK': 0.01, 'CP': 0.01, 'KP': 0.01, 'PB': 0.01, 'CD': 0.01, 'UW': 0.01, 'UH': 0.01, 'WF': 0.01, 'YY': 0.01, 'WP': 0.01, 'BC': 0.01, 'AQ': 0.01, 'CB': 0.01, 'IQ': 0.01, 'CM': 0.01, 'MG': 0.01, 'DQ': 0.01, 'TZ': 0.01, 'KD': 0.01, 'PD': 0.01, 'CF': 0.01, 'NZ': 0.01, 'CW': 0.01, 'FV': 0.01, 'VY': 0.01, 'FK': 0.01, 'OZ': 0.01, 'ZZ': 0.01, 'NQ': 0.01, 'UV': 0.0, 'XO': 0.0, 'PG': 0.0, 
'HK': 0.0, 'KG': 0.0, 'VS': 0.0, 'HV': 0.0, 'BM': 0.0, 'CN': 0.0, 'GV': 0.0, 'CG': 0.0, 'WU': 0.0, 'XH': 0.0, 'GK': 0.0, 'TQ': 0.0, 'CQ': 0.0, 'RQ': 0.0, 
'BH': 0.0, 'XS': 0.0, 'UZ': 0.0, 'WK': 0.0, 'XU': 0.0, 'UX': 0.0, 'BD': 0.0, 'BW': 0.0, 'WG': 0.0, 'MV': 0.0, 'PN': 0.0, 'XM': 0.0, 'OQ': 0.0, 'BV': 0.0, 
'XW': 0.0, 'KK': 0.0, 'BP': 0.0, 'ZU': 0.0, 'RZ': 0.0, 'XF': 0.0, 'MK': 0.0, 'ZH': 0.0, 'BN': 0.0, 'ZY': 0.0, 'HQ': 0.0, 'IY': 0.0, 'DZ': 0.0, 'VR': 0.0, 
'ZS': 0.0, 'XY': 0.0, 'CV': 0.0, 'XB': 0.0, 'XR': 0.0, 'YQ': 0.0, 'VD': 0.0, 'PK': 0.0, 'VU': 0.0, 'ZL': 0.0, 'SZ': 0.0, 'YZ': 0.0, 'LQ': 0.0, 'BF': 0.0, 
'NX': 0.0, 'QA': 0.0, 'QI': 0.0, 'KV': 0.0, 'ZW': 0.0, 'WV': 0.0, 'UU': 0.0, 'VT': 0.0, 'VP': 0.0, 'XD': 0.0, 'GQ': 0.0, 'XL': 0.0, 'VC': 0.0, 'CZ': 0.0, 
'LZ': 0.0, 'ZT': 0.0, 'WZ': 0.0, 'SX': 0.0, 'ZB': 0.0, 'VL': 0.0, 'PV': 0.0, 'FQ': 0.0, 'ZM': 0.0, 'VW': 0.0, 'ZC': 0.0, 'BG': 0.0, 'XG': 0.0, 'RX': 0.0, 
'HZ': 0.0, 'XX': 0.0, 'VM': 0.0, 'XN': 0.0, 'QW': 0.0, 'VN': 0.0, 'ZD': 0.0, 'ZR': 0.0, 'FZ': 0.0, 'XV': 0.0, 'ZP': 0.0, 'VH': 0.0, 'VB': 0.0, 'ZF': 0.0, 
'GZ': 0.0, 'TX': 0.0, 'VF': 0.0, 'DX': 0.0, 'QB': 0.0, 'BK': 0.0, 'ZG': 0.0, 'VG': 0.0, 'ZK': 0.0, 'ZN': 0.0, 'UQ': 0.0, 'VV': 0.0, 'MQ': 0.0, 'QS': 0.0, 
'FX': 0.0, 'PQ': 0.0, 'MZ': 0.0, 'YX': 0.0, 'QT': 0.0, 'WQ': 0.0, 'LX': 0.0, 'GX': 0.0, 'ZV': 0.0, 'MX': 0.0, 'KQ': 0.0, 'XK': 0.0, 'QM': 0.0, 'QH': 0.0, 
'VK': 0.0, 'KZ': 0.0, 'QC': 0.0, 'PZ': 0.0, 'QL': 0.0, 'QO': 0.0, 'QF': 0.0, 'QD': 0.0, 'BZ': 0.0, 'HX': 0.0, 'PX': 0.0, 'QP': 0.0, 'QE': 0.0, 'QR': 0.0, 
'ZQ': 0.0, 'BQ': 0.0, 'XQ': 0.0, 'CX': 0.0, 'KX': 0.0, 'WX': 0.0, 'QY': 0.0, 'QV': 0.0, 'QN': 0.0, 'VX': 0.0, 'BX': 0.0, 'VZ': 0.0, 'QG': 0.0, 'QQ': 0.0, 
'ZX': 0.0, 'XZ': 0.0, 'QK': 0.0, 'VQ': 0.0, 'QX': 0.0, 'QZ': 0.0}

test_plaintext = 'Likemostpremoderneracipherstheplayfairciphercanbeeasilycrackedifthereisenoughtext'.upper()
test_ciphertext = 'DQRKHSTOAOFKQCKWKGWEDHCOKWTOKCLAYBEYKQDHCOKWEPTGFWKEQMABEOPERKIQGSKCWKMQGKUPCNRGZS' # key = 'PLAY'

PF_ALPHABET = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' # no J
M_DIM = 5 # 5x5 matrix

def create_matrix(key):
    # form string that goes in matrix
    s = ''
    for i in range(len(key)):
        c = key[i]
        if c == 'J': # replace J with I
            c = 'I'
        if c not in s: # remove dups in key
            s += c
    # add rest of alphabet
    for i in range(len(PF_ALPHABET)):
        c = PF_ALPHABET[i]
        if c not in s:
            s += c
    
    # fill matrix
    m = [None] * M_DIM
    for i in range(M_DIM):
        m[i] = s[i * M_DIM:(i + 1) * M_DIM]
    return m


def find_in_matrix(m, c):
    for row in range(len(m)):
        if c in m[row]:
            return [row, m[row].index(c)]
    print('error!!!', c, 'not found in matrix', m)


def decrypt_playfair(ciphertext, key):
    m = create_matrix(key)    

    # decode digrams
    plaintext = ''
    ciphertext_arr = pair_letters(ciphertext)
    for pair in ciphertext_arr:
        c0 = pair[0]
        c1 = pair[1]
        row0, col0 = find_in_matrix(m, c0)
        row1, col1 = find_in_matrix(m, c1)
        if row0 == row1: # left
            plaintext += m[row0][(col0 + M_DIM - 1) % M_DIM]
            plaintext += m[row1][(col1 + M_DIM - 1) % M_DIM]
        elif col0 == col1: # up
            plaintext += m[(row0 + M_DIM - 1) % M_DIM][col0]
            plaintext += m[(row1 + M_DIM - 1) % M_DIM][col1]
        else: # corner of same row
            plaintext += m[row0][col1]
            plaintext += m[row1][col0]
    
    # remove X's
    result = ''
    for c in plaintext:
        if c != 'X':
            result += c
    
    return result


def encrypt_playfair(plaintext, key):
    m = create_matrix(key)

    # prepare plaintext
    p_str = ''
    # sep dups with X if needed
    for i in range(len(plaintext)):
        c = plaintext[i]
        if i > 1 and c == plaintext[i - 1]:
            p_str += 'X' + c
        else:
            p_str += c
    # add X on end of needed
    if len(p_str) % 2 != 0:
        p_str += 'X'
    # pair letters
    p_arr = pair_letters(p_str)

    # encode digrams
    ciphertext = ''
    for pair in p_arr:
        c0 = pair[0]
        c1 = pair[1]
        row0, col0 = find_in_matrix(m, c0)
        row1, col1 = find_in_matrix(m, c1)
        if row0 == row1: # right
            ciphertext += m[row0][(col0 + 1) % M_DIM]
            ciphertext += m[row1][(col1 + 1) % M_DIM]
        elif col0 == col1: # down
            ciphertext += m[(row0 + 1) % M_DIM][col0]
            ciphertext += m[(row1 + 1) % M_DIM][col1]
        else: # corner of same row
            ciphertext += m[row0][col1]
            ciphertext += m[row1][col0]
    
    return ciphertext


def fitness(ciphertext, key):
    alpha = 0.3
    beta = 1 - alpha

    # decrypt ciphertext using key and count frequencies
    plaintext = decrypt_playfair(ciphertext, key)
    letter_hist = run_hist(plaintext)
    bigram_hist = run_hist3(plaintext)

    letter_sum = 0;
    for l in letter_freq:
        if (l == 'J'):
            continue
        val = 0
        if l in letter_hist:
            val = letter_hist[l]
        letter_sum += abs(letter_freq[l] - val) ** 2

    bigram_sum = 0;
    for b in bigram_freq:
        if (b[0] == 'J' or b[1] == 'J'):
            continue
        val = 0
        if b in bigram_hist:
            val = bigram_hist[b]
        bigram_sum += abs(bigram_freq[b] - val) ** 2
    
    return round(alpha * letter_sum + beta * bigram_sum, 2)


def random_string(length):
    # https://stackoverflow.com/a/63485691
    letters = string.ascii_uppercase
    str = ''
    while len(str) < length:
        rand_letter = secrets.choice(letters)
        if rand_letter not in str:
            str += rand_letter
    return str


def random_crossover(k0, k1):
    prob_c = 1
    option = secrets.randbelow(100)
    if option < (prob_c * 100):
        option = secrets.choice([1, 2])
        i = secrets.randbelow(len(k0) - 1) + 1
        if option == 1:
            # swap end
            out0 = k0[:i] + k1[i:]
            out1 = k1[:i] + k0[i:]
            return [out0, out1]
        else:
            # swap beginning
            out0 = k1[:i] + k0[i:]
            out1 = k0[:i] + k1[i:]
            return [out0, out1]
    return [k0, k1]


def random_mutation(k):
    prob_m = 0.05
    option = secrets.randbelow(100)
    if option < (prob_m * 100):
        
        option = secrets.choice([1, 2])
        if option == 1:
            i = secrets.randbelow(len(k) - 1) + 1
            # switch parts
            out = k[i:] + k[:i]
            return out
        else:
            i = secrets.randbelow(len(k))
            j = secrets.randbelow(len(k))
            while j == i:
                j = secrets.randbelow(len(k))
            # switch chars
            smaller = min(i, j)
            larger = max(i, j)
            out = k[:smaller] + k[larger] + k[smaller+1:larger] + k[smaller] + k[larger+1:]
            return out

    return k

def run_gapfc(input = cipher, key_len = 5):
    # key_len = 5 # probably 3-10
    gen_num = 1000 # 1000-2000, larger = better
    key_num = 200 # 40-200, up to 1000-2000?
    best = 0.04 # 4-5%
    ciphered_text = input

    initial_pop = [random_string(key_len) for i in range(key_num)]
    # calculate fitness of each key and sort by fitness asc
    fitnesses = [[key, fitness(ciphered_text, key)] for key in initial_pop]
    
    for g in range(gen_num):
        
        fitnesses.sort(key=lambda item: item[1])
        avg_fitness = round(functools.reduce(lambda sum, item: sum + item[1], fitnesses, 0) / len(fitnesses), 2)

        # best is a percentage so apply it to the population size
        best_num = math.ceil(len(fitnesses) * best)
        
        # eliminate worst keys
        fitnesses = fitnesses[2*best_num:]

        # stochastic selection https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_parent_selection.htm
        mating_pool = []
        sum_fitness = math.floor(functools.reduce(lambda sum, item: sum + item[1], fitnesses, 0))
        while len(mating_pool) * 2 < best_num:
            rand1 = secrets.randbelow(sum_fitness)
            rand2 = secrets.randbelow(sum_fitness)
            running_sum = 0
            chosen1 = ''
            chosen2 = ''
            i = 0
            while running_sum < rand1 or running_sum < rand2:
                running_sum += fitnesses[i][1]
                if running_sum > rand1 and not chosen1:
                    chosen1 = fitnesses[i][0]
                    j = i
                    while chosen1 in mating_pool or chosen1 == chosen2:
                        j += 1
                        chosen1 = fitnesses[j][0]
                if running_sum > rand2 and not chosen2:
                    chosen2 = fitnesses[i][0]
                    j = i
                    while chosen2 in mating_pool or chosen1 == chosen2:
                        j += 1
                        chosen2 = fitnesses[j][0]
                i += 1
            mating_pool.append([chosen1, chosen2])

        # print(g, mating_pool, avg_fitness)

        # mate pairs in paired mating pool
        for k0, k1 in mating_pool:
            # cross
            new0, new1 = random_crossover(k0, k1)
            
            # mutate
            existing_keys = list(map(lambda item: item[0], fitnesses))
            new0 = random_mutation(new0)
            while new0 in existing_keys:
                new0 = random_string(key_len)

            new1 = random_mutation(new1)
            while new1 in existing_keys or new1 == new0:
                new1 = random_string(key_len)

            # add mutated keys to pop with their fitnesses
            fitnesses.append([new0, fitness(ciphered_text, new0)])
            fitnesses.append([new1, fitness(ciphered_text, new1)])

        # add best_num new random keys with their fitnesses
        existing_keys = list(map(lambda item: item[0], fitnesses))
        for i in range(best_num):
            rand_key = random_string(key_len)
            while rand_key in existing_keys:
                rand_key = random_string(key_len)
            fitnesses.append([rand_key, fitness(ciphered_text, rand_key)])
        
    # after all generations, select best fitting keys and decrypt
    fitnesses.sort(key=lambda item: item[1])

    top = 5
    for key, fit in fitnesses[-top:]:
        print(key, fit)
        plaintext = decrypt_playfair(ciphered_text, key)
        if 'THE' in plaintext and 'AND' in plaintext:
            print(plaintext)



# run_hist()
# run_hist2()
# run_hist3()
# run_shift()
# run_poly()
# run_code()
# run_brute()

# print(encrypt_playfair(test_plaintext, 'PLAY'))
# print(test_ciphertext)
# print(decrypt_playfair(test_ciphertext, 'PLAY'))
# print(test_plaintext)

# print(random_crossover('ABCDEFG', 'TUVWXYZ'))
# print(random_mutation('ABCDEFGHIJKLMNOP'))
start = timeit.default_timer()
num_runs = 1
for i in range(num_runs):
    run_gapfc(cipher2, 5)
stop = timeit.default_timer()
print('Time: ', stop - start)
