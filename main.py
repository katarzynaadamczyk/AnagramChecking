# as I undestand uppercase is different than the lowercase as it is a different character
# in ASCII or UNICODE
# if you consider them as same then it is needed to change the below code so that each
# character is firstly changed to lowercase and then added / checked in the dictionary
# and comparison of strings in line 10 should be also in lowercase

def are_anagrams(s1, s2, s3):
    # check if the size of each string is equal 
    # and the strings are different
    if len(s1) == len(s2) and len(s1) == len(s3) and not (s1 == s2 or s1 == s3 or s2 == s3):
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
    print("Result for 'kasia', 'kasia', 'Kasia' is " + str(are_anagrams('kasia', 'kasia', 'Kasia')))
    print("Result for 'kasia', 'asiak', 'askia' is " + str(are_anagrams('kasia', 'asiak', 'askia')))
    print("Result for 'kasia', 'asiak', 'asial' is " + str(are_anagrams('kasia', 'asiak', 'asial')))
    print("Result for 'kasia', 'asiak', 'asmia' is " + str(are_anagrams('kasia', 'asiak', 'asmia')))
    print("Result for 'kasia', 'asiak', 'kasia' is " + str(are_anagrams('kasia', 'asiak', 'kasia')))

if __name__ == "__main__":
    main()