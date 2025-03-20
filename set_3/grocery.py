def main():
    G_dict = {}
    while True:
        try:
            user_entry = input("").casefold()

        except EOFError:
            show_list(G_dict)
            break

        else:
            # ammend dict to 'add NEW key + value of 1' or
            # key errors caught by this if statement?
            if user_entry not in list(G_dict):
                user_entry = G_dict.setdefault(user_entry, 1)
            # update value of key += 1'
            elif user_entry in list(G_dict):
                G_dict[user_entry] += 1


def show_list(x):
    # sort dictionary alphabetically (dict becomes sorted tuples in list)
    # convert tuples to dict
    sort_L = dict(sorted(x.items()))
    # print values then keys
    for key in sort_L:
        print(sort_L[key], key.upper())


main()
