def main():
    file_ext(input("File name: ").strip().lower())


def file_ext(s):
    file_dict = {
        "gif" : "image/gif",
        "jpg" : "image/jpeg",
        "jpeg" : "image/jpeg",
        "png" : "image/png",
        "pdf" : "application/pdf",
        "txt" : "text/plain",
        "zip" : "application/zip",
    }
    #rsplit to split on final "." for file names such as 'appl.fruit.pdf'
    #iterate across dict on extension split
    F, E = s.rsplit(".", 1)
    try:
        print(file_dict[E])
    except KeyError: #utilize key error for other category
        print("application/octet-stream")
    else:
        return


        
main()