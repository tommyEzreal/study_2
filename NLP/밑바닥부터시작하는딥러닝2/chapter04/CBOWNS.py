# CBOW with embedding & negative sampling 

class CBOWNS:
    def __init__(self, vocab_size, hidden_size, window_size, corpus):
        """
        window_size: foward_backward contexts
        corpus: word_id list 
        """
        V,H = vocab_size, hidden_size

        W_in = 0.01 * np.random.randn(V, H).astype('f')
        W_out = 0.01 * np.random.randn(V, H).astype('f')


        self.in_layers = []
        for _ in range(2*window_size):
            layer = Embedding(W_in) # embedding layer: if window_size==2, 2|2 4 
            self.in_layers.append(layer)
        self.ns_loss = NegativeSamplingLoss(W_out, corpus, power=0.75, sample_size=5)
        
        layers = self.in_layers + [self.ns_loss] 

        
        self.params, self.grads = [], []
        for layer in layers:
            self.params += layer.params
            self.grads += layer.grads

        self.word_vecs = W_in 

    def forward(self, contexts, target):

        h=0
        for i, layer in enumerate(self.in_layers): 
            # in layers에 모아둔 각 layer들 하나씩 꺼내서 forward 통과시키기
            h += layer.forward(contexts[:,i])            
        h *= 1 / len(self.in_layers)
        loss = self.ns_loss.forward(h, target)
        
        return loss

    def backward(self, dout=1):
        dout = self.ns_loss.backward(dout)
        dout *= 1 / len(self.in_layers)
        for layer in self.in_layers:
            layer.backward(dout)
        
        return None
