def burbula_kartosana(masivs):
    n = len(masivs)
    for i in range(n):
        #iet cauri visiem elementiem
        for j in range(n-1):
            if masivs[j]> masivs[j+1]:
                masivs[j], masivs[j+1] = masivs[j+1], masivs[j]
                print(masivs)
            else:
                #print('Nav nepieciešama maiņa')
                pass
            
    print('Sakārtotais saraksts: ', masivs)

nesakartots = [45, 15, 2, 9, 100, 1]

print("nesakartots saraksts: ", nesakartots)
print(type(nesakartots))

burbula_kartosana(nesakartots)