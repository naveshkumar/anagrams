def list_to_word(lst):
    word = "".join(lst)
    return(word)

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
