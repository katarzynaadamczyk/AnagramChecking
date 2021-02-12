def AnagramChecking(s1, s2, s3):
    # check if the size of each string is equal
    if len(s1) == len(s2) and len(s1) == len(s3):
        dicts = list()
        texts = [s1, s2, s3]
        for i in range(3):
            mydic = dict()
            for j in texts[i]:
                if j in mydic:
                    mydic[j] += 1
                else:
                    mydic[j] = 1
            dicts.append(mydic)
        common_letters = {k: dicts[0][k] for k in dicts[0] if k in dicts[1] and dicts[0][k] == dicts[1][k] and k in dicts[2] and dicts[0][k] == dicts[2][k]}
        if len(common_letters) == len(dicts[0]):
            return True

    return False

def main():
    print("Result for 'kasia', 'asia', 'basia' is " + str(AnagramChecking('kasia', 'asia', 'basia')))
    print("Result for 'kasia', 'asiak', 'askia' is " + str(AnagramChecking('kasia', 'asiak', 'askia')))
    print("Result for 'kasia', 'asiak', 'asia' is " + str(AnagramChecking('kasia', 'asiak', 'asia')))

if __name__ == "__main__":
    main()