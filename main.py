def AnagramChecking(s1, s2, s3):
    # check if the size of each string is equal
    if len(s1) == len(s2) and len(s1) == len(s3):
        # if so create a list of dictionaries for each string
        # each dictionary will contain letters with their corresponding quantity in given text
        dicts = list()
        # create a list of strings for easy management of the code (no need to write same code 3 times)
        texts = [s1, s2, s3]

        # for each given string
        for i in range(3):
            # create an  empty dictionary
            mydic = dict()
            # and for each letter in that string
            for j in texts[i]:
                # check if that letter is already in the dictionary
                if j in mydic:
                    # if so then add one more appearance
                    mydic[j] += 1
                else:
                    # if not then add it to dictionary and set number of appearances to 1
                    mydic[j] = 1
            # append to list of dictionaries created dictionary
            dicts.append(mydic)
        
        # create a dictionary that contains only common letters with identical number of appearances as in all created dictionaries 
        common_letters = {k: dicts[0][k] for k in dicts[0] if k in dicts[1] and dicts[0][k] == dicts[1][k] and k in dicts[2] and dicts[0][k] == dicts[2][k]}
        
        # if length of created dictionary is same as any other then return true
        if len(common_letters) == len(dicts[0]):
            return True
    
    # any other case - return false
    return False

def main():
    print("Result for 'kasia', 'asia', 'basia' is " + str(AnagramChecking('kasia', 'asia', 'basia')))
    print("Result for 'kasia', 'asiak', 'askia' is " + str(AnagramChecking('kasia', 'asiak', 'askia')))
    print("Result for 'kasia', 'asiak', 'asial' is " + str(AnagramChecking('kasia', 'asiak', 'asial')))
    print("Result for 'kasia', 'asiak', 'asmia' is " + str(AnagramChecking('kasia', 'asiak', 'asmia')))

if __name__ == "__main__":
    main()