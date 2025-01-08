#Variant page 86
#calculate thi final score after removing the lowest two values
def finalScore(s) :
    min_s = min(s)
    for element in s :
        if element == min_s :
            s.remove(element)
    return s

def main() :
    scores = [8, 4, 7, 9, 9, 7, 5, 10]
    flist = finalScore(scores)
    flist2 = finalScore(flist)
    summ = sum(flist2)
    print("Final Score:",summ)

main()
