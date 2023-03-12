# Sigmoid 역전파 계층

class Sigmoid:
    def __init__(self):
        self.params, self.grads=[],[]
        self.out = None
    
    def forward(self,x):
        out = 1 / (1+np.exp(-x))
        self.out = out
        return out
    
    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out # y(1-y)
        return dx
      
# Affine Layer   
class Affine:
    def __init__(self, W, b):
        self.params = [W,b]
        self.grads = [np.zeros_like(W), np.zeros_like(b)]
        self.x = None
    
    def forward(self,x):
        W,b = self.params
        out = np.matmul(x,W) + b
        self.x = x
        return out

    def backward(self, dout):
        W, b = self.params
        dx = np.matmul(dout, W.T)
        dW = np.matmul(self.x.T, dout)
        db = np.sum(dout, axis=0)

        self.grads[0][...] = dW
        self.grads[1][...] = db
        return dx
