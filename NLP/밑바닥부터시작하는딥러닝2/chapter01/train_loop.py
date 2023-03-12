# train loop

import sys
sys.path.append('..')
from common.optimizer import SGD
import matplotlib
matplotlib.rc('font', family='AppleGothic')

# hyperparams
max_epoch = 300
batch_size = 30
hidden_size = 10
learning_rate = 1.0

# load data
x,t = spiral.load_data()

# model, optim
model = TwoLayerNet(input_size=2, hidden_size = hidden_size, output_size = 3)
optimizer = SGD(lr = learning_rate)

data_size = len(x)
max_iters = data_size // batch_size

total_loss = 0
loss_count = 0
loss_list = []

# loop
for epoch in range(max_epoch):
    idx = np.random.permutation(data_size) # shuffle data / 0-datasize까지 무작위 순서 생성 
    x = x[idx] # ex: [7,6,8,3,5,0,4,1,2,9] 
    t = t[idx]
    # epoch 단위로 데이터를 섞고 앞에서부터 순서대로 뽑아내어 사용 
    for iters in range(max_iters):
        batch_x = x[iters * batch_size : (iters+1)*batch_size]
        batch_t = t[iters * batch_size : (iters+1)*batch_size]
        
        # get grad and update 
        loss = model.forward(batch_x, batch_t)
        model.backward()
        optimizer.update(model.params, model.grads) # step

        total_loss += loss
        loss_count +=1

        if (iters+1) % 10 ==0:
            avg_loss = total_loss / loss_count
            print('epoch: %d | iters: %d / %d | loss %.2f'
                    % (epoch +1, iters + 1, max_iters, avg_loss))
            loss_list.append(avg_loss)
            total_loss, loss_count = 0,0
