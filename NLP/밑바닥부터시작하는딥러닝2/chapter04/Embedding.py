# Embedding : from W, extract idx rows

class Embedding:
    def __init__(self, W):
        self.params = [W]
        self.grads = [np.zeros_like(W)]
        self.idx = None

    def forward(self, idx):
        W, = self.params 
        self.idx = idx
        out = W[idx]
        return out

    # backward
    # just pass grad from outlayer backward

    def backward(self,dout):
        dW, = self.grads
        dW[...] = 0 # all elements into zeros
        
        for i, word_id in enumerate(self.idx): # for duplicates 
            dW[word_id] += dout[i]

        # or 
        # np.add.at(dW, self.idx, dout) 
        # add dout to dW's self.idx row 
        return None
