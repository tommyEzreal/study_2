# cosine similarity between word vecs

def cos_sim(x, y , eps=1e-8):
    nx = x / np.sqrt(np.sum(x**2)+ eps) # x_norm
    ny = y / np.sqrt(np.sum(y**2)+ eps) # y_norm

    return np.dot(nx,ny) # dot-product of xy
  
  
# similartiy rank (top k search_ )
def most_similar(query, word_to_id, id_to_word, word_matrix, top=5):
    if query not in word_to_id:
        print('not found error.' % query)
        return 

    print('\n[query]:' + query)
    query_id = word_to_id[query]
    query_vec = word_matrix[query_id]

    # calculate cosin-sim / all by once
    vocab_size = len(id_to_word)
    similarity = np.zeros(vocab_size)
    for i in range(vocab_size):
        similarity[i] = cos_sim(word_matrix[i], query_vec)
    
    count = 0
    # 내림차순 정렬 (-1* & argsort()) / array의 index 반환
    for i in (-1 * similarity).argsort():  # 유사도가 높은 값의 idx부터 접근 
        if id_to_word[i] == query: 
            continue # query와 같은 word의 index는 예외처리  
        
        print(' %s: %s' % (id_to_word[i], similarity[i]))
        count +=1
        if count >=top: # top 몇개 출력 여부에 따라 
            return 
