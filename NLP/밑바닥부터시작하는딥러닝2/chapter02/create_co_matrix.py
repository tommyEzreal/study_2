# make Co-occurence matrix for statistical approach 

def create_co_matrix(corpus, vocab_size, window_size=1):
    corpus_size = len(corpus)
    co_matrix = np.zeros((vocab_size, vocab_size), dtype=np.int32)

    for idx, word_id in enumerate(corpus):
        for i in range(1, window_size + 1):
            left_idx = idx-i # 오른쪽, 왼쪽 문맥 
            right_idx = idx+i    # window 만큼 칸수 이동한 범위 
            
            if left_idx >= 0: # word_id가 첫번째word가 아니라면 
                left_word_id = corpus[left_idx]
                co_matrix[word_id, left_word_id] +=1 
                # co_matrix의 (word_idx, 왼쪽 idx)성분 +1 

            if right_idx < corpus_size:
                right_word_id = corpus[right_idx]
                co_matrix[word_id, right_word_id] += 1 

    return co_matrix
