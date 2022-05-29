#get the english word list

englistfile = open("words.txt","r")
loklist_i = []
loklist_i = englistfile.readlines()
loklist = []
for word in loklist_i:
    loklist.append(word.strip())

#group the english word list in a dictionary by length of the words

engdict = {loklist[i]:len(loklist[i]) for i in range(0,len(loklist))}
lendict = {}
for key,val in engdict.items():
    lendict[val] = [key] if val not in lendict.keys() else lendict[val] + [key]

# Anagram function 1 : list of word concatanated into a single word
def list_to_word(lst):
    word = "".join(lst)
    return(word)

# Anagram function 2 : function that does the swapping of words on the same principle as nPr calculation
def swapper(wchar,wlen):
    initlist = []
    for step in range(1,wlen):
        for pos in range(0,wlen):

            if pos + step >= wlen:
                reppos = wlen - (pos+step)
            else:
                reppos = pos + step
                
            wchar[pos],wchar[reppos] = wchar[reppos],wchar[pos]
            newword = list_to_word(wchar)
            initlist.append(newword)
    initlist = list(set(initlist))
    return(initlist)


# Anagram function 3 : get inital values and then create combinations further still to get the final complete jumble
def permutate(word):
    
    allnpn = [word]
    wchar = sorted(word)
    wlen = len(word)
    
    initlist = swapper(wchar,wlen)
    
    for combo in initlist:
        combol = list(combo)
        comboout = swapper(combol,wlen)
        allnpn.extend(comboout)
            
    allnpn = list(set(allnpn))
    return(allnpn)

#the main function

def anagramer(word):
    anagrams = []
    allcombo = set(permutate(word))
    lokset = set(lendict[len(word)])
    anagrams = lokset.intersection(allcombo)
    return(anagrams)