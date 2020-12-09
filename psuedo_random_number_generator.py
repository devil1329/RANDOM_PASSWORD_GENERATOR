import string
import pickle as pi

def prng():
    if os.path.exists("prng.dat")==True:
        if os.path.getsize("prng.dat")!=0:
            f=open("prng.dat","rb")
            n=pi.load(f)
            f.close()
            seed=n
        else:
            seed=9856523498371
    else:
        seed=9856523498371
    t=[]
    for i in range(985):
        seed=((5*seed)+17)%1213
        t.append(seed)
        print(seed)
    f=open("prng.dat","wb")
    pi.dump(seed,f)
    f.close()
    return t


t=prng()
