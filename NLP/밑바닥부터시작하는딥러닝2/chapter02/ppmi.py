# PPMI
# improve statistical method -> pointwise mutual information method -> max(0, pmi(x,y)) = PPMI

def ppmi(C, verbose=False, eps=1e-8):
    M = np.zeros_like(C, dtype=np.float32) 
    N = np.sum(C) # Num corpus
    S = np.sum(C, axis=0) # num each word appearance
    total = C.shape[0] * C.shape[1]
    
    cnt = 0
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            pmi = np.log2(C[i,j] * N / (S[j] * S[i]) + eps)
            M[i,j] = max(0,pmi) # PPMI

            if verbose:
                cnt +=1
                if cnt % (total // 100) ==0:
                    print('%.1f%% complete' % (100*cnt/total)) # 100번째마다 출력 
    return M
