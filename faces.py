def convert():
    str = (input(""))
    if ":)" in str and ":(" in str:
        print(str.replace(":)","🙂").replace(":(","🙁"))
    elif ":)" in str:
        print(str.replace(":)","🙂"))
    elif ":(" in str:
        print(str.replace(":(","🙁"))
    else:
        print(str)

convert()
