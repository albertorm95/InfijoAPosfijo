N=100
#pila=[0 for i in range(N)]
pila=[]

global tope
tope=0

def llena():
    if(tope==(N-1)):
        return True
    return False

def vacia():
    if(tope==-1):
        return True
    return False

def push(dato):
    if(llena()!=True):
        global tope
        tope=tope+1
        #pila[tope]=dato
        pila.insert(tope,dato)

def pop():
    if(vacia()!=True):
        global tope
        aux=pila[tope]
        del pila[tope]
        tope=tope-1
        return aux
    else:
        return -9999

eistring=raw_input('Ingrese Operacion sin espacios: ')
EI=list(eistring)
print EI
EPOS=''
while (EI!=EPOS):                       #while 1
    if (EI[tope]=='('):                 #si 1
        push(EI[tope])
    else:                               #si no 1
        if(EI[0]==')'):                 #si 2
            while (pila[tope]!='('):    #while 2
                EPOS=EPOS+pop()
            pop()
        else:                           #si no 2
            if(EI[tope]=='+' or EI[tope]=='-' or EI[tope]=='*' or EI[tope]=='/' or EI[tope]=='^'):
                EPOS=EPOS+EI[tope]
            else:                       #si no 3
                while (
       

