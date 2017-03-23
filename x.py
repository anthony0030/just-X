def main():
    import numpy as np
    import tkinter as tk
    from tkinter import filedialog


    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    #print(file_path)

    xyz = []
    X=0
    Y=0
    Z=0
    m=0

    a,b,c,d,e,f,g,h,i,j = np.genfromtxt(file_path,delimiter=',', unpack=True)
    n = (len(c))
    #print("L\t","W\t","Q\t")
    for i in range(0,n):
            if (c[i] > 0 and c[i] < 1000) :



                    X = int(c[i]*10)
                    Y = int(e[i]*10)
                    Z = int(h[i])
                    
                    #print(X,"\t",Y,"\t",Z)

                    
                    xyz.append([int(X),int(Y),int(Z)])
                    m=m+1
                    

    #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    #print("PANELS: ",m,"aray entrys: ", n)
   # print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    #for i in range(0,m):
            #print(xyz[i])
    np.savetxt("out.csv", xyz,fmt='%10.0f', delimiter=',', header='LENGTH,#WIDTH,#QUANTITY')


main()
