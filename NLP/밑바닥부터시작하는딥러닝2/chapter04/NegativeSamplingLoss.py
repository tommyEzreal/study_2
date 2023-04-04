#NegativeSamplingLoss
from common.layers import SigmoidWithLoss


class NegativeSamplingLoss:
    def __init__(self, W, corpus, power=0.75,sample_size=5):
        self.sample_size = sample_size
        self.sampler = UnigramSampler(corpus, power, sample_size)

        self.loss_layers = [SigmoidWithLoss() for _ in range(sample_size+1)]
        self.embed_dot_layers = [EmbeddingDot(W) for _ in range(sample_size+1)]
        """
        sample_size for negative sample, one for positive sample
        """

        self.params, self.grads = [], []
        for layer in self.embed_dot_layers:
            self.params += layer.params
            self.grads += layer.grads

    def forward(self, h, target):

        batch_size = target.shape[0]

        negative_sample = self.sampler.get_negative_sample(target)

        #positive sample : one
        correct_label = np.ones(batch_size, dtype=np.int32)
        score = self.embed_dot_layers[0].forward(h,target)
        loss = self.loss_layers[0].forward(score, correct_label)

        #negative sample : sample_size
        negative_label = np.zeros(batch_size, dtype=np.int32)   
        for i in range(self.sample_size):
            negative_target = negative_sample[:, i]# first sample , second_sample .. ith sample 


            score = self.embed_dot_layers[i+1].forward(h, negative_target) # embed_dot_layers[0] is for positive label
            loss += self.loss_layers[i+1].forward(score, negative_label)
            
        return loss

    def backward(self, dout = 1):
        dh = 0
        for l0, l1 in zip(self.loss_layers, self.embed_dot_layers):
            dscore = l0.backward(dout)
            dh += l1.backward(dscore)
        
        return dh 
