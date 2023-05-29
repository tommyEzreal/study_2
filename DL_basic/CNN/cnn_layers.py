import numpy as np

def Conv1D(num_inputs, input_acts, filter_size, stride, weights):
    '''
    Args:
    num_inputs : int 
    input_acts : 1d array 
    filter_size : int
    stride : int
    weights: 1d array 
    '''


    output_acts = []
    for i in range(0, num_inputs - filter_size + 1, stride):
        
        sliced_input = input_acts[i:i+filter_size]
        
        output = 0
        for j in range(len(sliced_input)):
            output += sliced_input[j] * weights[j]
        
        '''
        <or>
        output = np.sum(sliced_input * weights)
        '''
        
        output_acts.append(output)
    
    return output_acts

#or

def Conv1D(num_inputs, input_acts, filter_size, stride, weights):
    
    output_len = (num_inputs - filter_size)//stride + 1
    
    output_acts = []
    for j in range(output_len):
        out = 0
        for k in range(filter_size):
            out += input_acts[j*stride + k] * weights[k]
        output_acts.append(out)
    return output_acts


# 2 dim Convolution 
def Conv2D(input_acts, weights, stride):
    '''
    Args:
    input_acts: 2d array (input_h, input_w)
    stride : int 
    weights : 2d array(filter_h, filter_w)
    '''
    
    input_h, input_w = input_acts.shape
    filter_h, filter_w = weights.shape
    output_h, output_w = (input_h - filter_h)//stride + 1, (input_w - filter_w)//stride + 1
    
    output_act = np.zeros((output_h, output_w))
    for i in range(0, input_h - filter_h + 1, stride):
        for j in range(0, input_w - filter_w + 1, stride):
            
            sliced_input = input_acts[i:i+filter_h, j:j+filter_w]

            output = 0
            for k in range(len(sliced_input[0])):
                for l in range(len(sliced_input[1])):
                    output += sliced_input[k,l] * weights[k,l]

            output_act[i//stride, j//stride] = output

            '''
            <or>
            output_act[i//stride, j//stride] = np.sum(sliced_input * weights)


            # ! wrong !
            # output_act[i//stride, j//stride] = np.sum(np.dot(weights.T, sliced_input))
            # !       !   
            '''    
    return output_act


# contains input channel 
def Conv2D_w_C(input_acts, weights, stride):
    '''
    Args:
    input_acts: 3d array (input_channels, input_h, input_w)
    stride : int 
    weights : 4d array (num_filters, input_channels, filter_h, filter_w)
    num_filters: int (개별 입력 채널에 대한 필터의 개수) == output_channels
    '''

    input_c, input_h, input_w = input_acts.shape
    num_filters, input_c, filter_h, filter_w = weights.shape

    output_h = (input_h - filter_h)//stride + 1
    output_w = (input_w - filter_w)//stride + 1

    output_act = np.zeros((num_filters, output_h, output_w))
    for nf in range(num_filters):
        for h in range(0, input_h - filter_h + 1 , stride):
            for w in range(0, input_w - filter_w + 1, stride):

                sliced_input = input_acts[:, h:h+filter_h, w:w+filter_w]
                output = np.sum(sliced_input * weights[nf])

                output_act[nf, h//stride, w//stride] = output
    
    return output_act
