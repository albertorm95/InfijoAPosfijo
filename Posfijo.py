N=20
#pila=[0 for i in range(N)]
pila=[]

global tope
tope=-1

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

def operando(i, EI):
    abcd='abcdefghijklmnopqrstuvxyz'
    abcd=list(abcd)
    for j in range(len(abcd)):
        if(EI[i]==abcd[j]):
            return True
    return False

def parentesis(i, EI):
    if(EI[i]!=')'):
        return True
    else:
        return False
    
#Ope    PriInf  PriPila
#^      4       3
#*      2       2
#/      2       2
#+      1       1
#-      1       1
#(      5       0
#)      NONE    NONE
    
def infijo(i, EI):
    if(EI[i]=='^'):
        prioridadop=4
        return prioridadop
    elif(EI[i]=='*'):
        prioridadop=2
        return prioridadop
    elif(EI[i]=='/'):
        prioridadop=2
        return prioridadop
    elif(EI[i]=='+'):
        prioridadop=1
        return prioridadop
    elif(EI[i]=='-'):
        prioridadop=1
        return prioridadop
    elif(EI[i]=='('):
        prioridadop=5
        return prioridadop

def pripila(pila):
    if(pila[tope]=='^'):
        prioridadpi=3
        return prioridadpi
    elif(pila[tope]=='*'):
        prioridadpi=2
        return prioridadpi
    elif(pila[tope]=='/'):
        prioridadpi=2
        return prioridadpi
    elif(pila[tope]=='+'):
        prioridadpi=1
        return prioridadpi
    elif(pila[tope]=='-'):
        prioridadpi=1
        return prioridadpi
    elif(pila[tope]=='('):
        prioridadpi=0
        return prioridadpi


#eistring=raw_input('Ingrese Operacion sin espacios: ')
#EI=list(eistring.lower())
EI=['a','*','b','/','(','a','+','c',')']
EP=[]
for i in range(len(EI)):
    print 'PILA'
    print pila
    print 'EI'
    print EI
    print 'EP'
    print EP
    print '------------------'
    if(operando(i, EI)==True):
        EP.append(EI[i])
    elif(parentesis(i, EI)==True):
        if (tope==-1):
            push(EI[i])
        elif(tope>=0):
            if(infijo(i,EI)>pripila(pila)):
                push(EI[i])
                print 'lol'
            
            
            
           




       

