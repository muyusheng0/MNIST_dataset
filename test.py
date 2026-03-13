def read_pic_from_file(filename):
    f = open(filename, 'rb')
    magic = int.from_bytes(f.read(4), 'big')
    num = int.from_bytes(f.read(4), 'big')
    width = int.from_bytes(f.read(4), 'big')
    height = int.from_bytes(f.read(4), 'big')

    dataset = []
    for i in range(num):
        pic = []
        for i in range(width * height):
            pic.append(int.from_bytes(f.read(1), 'big'))
        dataset.append(pic)
        # show_pic(pic)
    return dataset

train_data_list = read_pic_from_file('./downloads/train-images-idx3-ubyte')
test_data_list = read_pic_from_file('./downloads/t10k-images-idx3-ubyte')

def read_label_from_file(filename):
    f = open(filename, 'rb')
    magic = int.from_bytes(f.read(4), 'big')
    num = int.from_bytes(f.read(4), 'big')
    
    labels = []
    for i in range(num):
        labels.append(int.from_bytes(f.read(1), 'big'))
    return labels

train_label_list = read_label_from_file('./downloads/train-labels-idx1-ubyte')
test_label_list = read_label_from_file('./downloads/t10k-labels-idx1-ubyte')


train_data = torch.tensor(train_data_list, dtype=torch.float, device='cuda')
train_label = torch.tensor(train_label_list, device='cuda')

test_data = torch.tensor(test_data_list, dtype=torch.float, device='cuda')
test_label = torch.tensor(test_label_list, device='cuda')
