def main():
    text=input("Waiting for user input: ")
    newtext=convert(text)
    print(newtext)

def convert(str):
    str_replace = str.replace(":)","🙂").replace(":(","🙁")
    return str_replace
    
main()