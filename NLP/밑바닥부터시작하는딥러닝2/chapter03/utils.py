# from corpus, return contexts and target 
def create_contexts_target(corpus, window_size=1):
    target = corpus[window_size: -window_size]
    
    contexts = []
    for idx in range(window_size, len(corpus) - window_size):
        cs = []
        for t in range(-window_size, window_size+1):
            if t==0:
                continue
            cs.append(corpus[idx]+t)
        contexts.append(cs)
    return np.array(contexts), np.array(target)


# word idx into one hot
def convert_one_hot(corpus, vocab_size):
    """
    corpus: word id list 
    """

    N = corpus.shape[0] # shape = (batch, sequence), N=sequence

    if corpus.ndim == 1: # for target vector
        one_hot = np.zeros((N, vocab_size), dtype=np.int32) # sequence,vocab_size matrix
        for idx, word_id in enumerate(corpus):
            one_hot[idx, word_id] = 1 # [seuqence, word_id]
    
    elif corpus.ndim ==2: # for context vectors of target 
        C = corpus.shape[1] # dim 
        one_hot = np.zeros((N,C,vocab_size), dtype=np.int32) #(dim, seq, vocab)
        for idx_0, word_ids in enumerate(corpus):
            for idx_1, word_id in enumerate(word_ids):
                one_hot[idx_0, idx_1, word_id] = 1 #
    return one_hot
