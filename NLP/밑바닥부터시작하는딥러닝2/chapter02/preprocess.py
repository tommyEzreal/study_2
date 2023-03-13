# make raw text into copus, word_to_id:dict, id_to_word:dict


def preprocess(text):
    text = text.lower() # do lower case
    text = text.replace('.', ' .') # 맞춤표 사이 공백 만들기
    
    words = text.split(' ') # 공백 기준 단어단위 분절 

    # word to index 
    word_to_id = {}
    id_to_word = {}

    for word in words:
        if word not in word_to_id:
            new_id = len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word

    # 입력 text의 id array 생성 
    corpus = np.array([word_to_id[w] for w in words])

    return corpus, word_to_id, id_to_word
