def main(args):
    f = open("interfaces.txt", "r")
    p = open("nuevofir.txt", "w")
    for i in f:
        if "gateway" in i:
            p.write(i)
    p.close()
    f.close()
    
    p = open("nuevofir.txt", "r")
    print(p.read())

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))