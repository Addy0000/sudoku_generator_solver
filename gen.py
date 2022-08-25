
import numpy as np      

#generator

def gen(mask_rate=0.5):
    while True:
        n=9
        puzzle=np.zeros((n,n),np.int)
        random=np.arange(1,n+1)
        puzzle[0,:]=np.random.choice(random,n,replace=False)
        try:
            for r in range (1,n):
                for c in range (n):
                    col_rest=np.setdiff1d(random,puzzle[:r,c])
                    row_rest=np.setdiff1d(random,puzzle[r,:c])

                    uni1=np.intersect1d(col_rest,row_rest)

                    r_start=(r//3)*3
                    c_start=(c//3)*3

                    uni2=np.setdiff1d(np.arange(0,n+1),puzzle[r_start:(r_start+1),c_start:(c_start+1)].ravel())

                    uni=np.intersect1d(uni1,uni2)
                    puzzle[r,c]=np.random.choice(uni,size=1)
            break
        except ValueError:
            pass

    puzzle1 = puzzle.copy()
    puzzle1[np.random.choice([True, False], size=puzzle.shape, p=[mask_rate, 1 - mask_rate])] = 0 
    print(puzzle(delimiter=",")) 
    return puzzle1 

board=gen()