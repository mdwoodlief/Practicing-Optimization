def main():
    plate = input("Plate: ".upper().strip())
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (
        range_check(s)
        and char_start(s)
        and FN_Check(s)
        and permitted(s)
        and Suf_Check(s)
    ):
        return True


# check range requirement
def range_check(s):
    if len(s) > 6 or len(s) < 2:
        return False
    else:
        return True


# check first 2 characters are alpha
def char_start(s):
    if len(s) >= 2:
        if not s[0].isalpha() or not s[1].isalpha():
            return False
        else:
            return True


# check permitted characters only
def permitted(s):
    if "." in s:
        return False
    elif " " in s:
        return False
    elif "!" in s:
        return False
    elif "?" in s:
        return False
    else:
        return True


# first number check
def FN_Check(s):
    FN = None
    for char in s:
        if char.isdigit():
            FN = char
        if FN != None:
            if FN == "0":
                return False
            else:
                return True
        if s.isalpha():
            return True


# check for alpha after firstnum
def Suf_Check(s):
    position = None
    for char in s:
        if char.isdigit():
            position = s.index(char)
        if char.isdigit():
            break
    if not s.isalpha():
        if s[position:].isdigit():
            return True

        if s[position:].isalpha():
            return False
    else:
        return True


if __name__ == "__main__":
    main()
