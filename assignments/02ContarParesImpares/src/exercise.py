def main():
    #escribe tu código abajo de esta línea
    CajaV=list(input())
    while CajaV[0] != '*':
        CajaV.insert(0, input())

    Pares=0
    Impares=0
    for i in CajaV[1:]:
        i=int(i)
        if i%2 == 0:
            Pares += 1
        else:
            Impares += 1

    print('PARES=' + str(Pares))
    print('IMPARES=' + str(Impares))

if __name__=='__main__':
    main()
