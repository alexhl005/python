#def 1
def email(mail):
    for i in range(len(mail)):
        for j in range(len(mail[i])):
            if mail[i][j] == "@":
                return(mail[i])
            
def dominio(domain):
    mail_domain = email(domain)
    for i in range(len(mail_domain)):
        if mail_domain[i] == "@":
            return(mail_domain[i+1:])

def main(args):
    usuario = ("alex", "asir05", "192.168.8.15","alexherrera@gmail.com")
    mai = email(usuario)
    print(mai)
    dom = dominio(usuario)
    print(dom)
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))