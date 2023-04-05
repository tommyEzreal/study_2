# word to vec 연산

# man - woman + king = ? 

def normalize(x):
    if x.ndim ==2:
        s = np.sqrt((x*x).sum(1))
        x /= s.reshape((s.shape[0],1))

    elif x.ndim==1:
        s = np.sqrt((x*x).sum(0))
        x /= s
    
    return x


def analogy(a,b,c, word_to_id, id_to_word, word_matrix, top=5):
    for word in (a,b,c):
        if word not in word_to_id:
            print("can not find word in list") 
        return
    
    print('\n[analogy]' + a + ':' + b + '=' + c + ':?')

    a_vec, b_vec, c_vec = word_matrix[word_to_id[a], 
                                      word_matrix[word_to_id[b]],
                                      word_matrix[c]]

    query_vec = normalize(b_vec - a_vec + c_vec)
    
    similarity = np.dot(word_matrix, query_vec)

    print("->" + answer + ':' + str(np.dot(word_matrix[word_to_id[answer]], query_vec)))


    count = 0
    for i in (-1*similarity).argsort():
        if np.isnan(similarity[i]):
            continue
        if id_to_word[i] in (a,b,c):
            continue
        print(f'{id_to_word[i]}: {similarity[i]}')

        count += 1
        if count >= top:
            return
