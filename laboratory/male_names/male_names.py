import torch
import sys

# Loading tensors
V = torch.load('V.pt')
W1 = torch.load('W1.pt')
b1 = torch.load('b1.pt')
W2 = torch.load('W2.pt')
b2 = torch.load('b2.pt')

with open('possible_chars.txt', 'r') as f:
    possible_chars = f.read().splitlines()

def encode(x):
    return possible_chars.index(x)

# Generating 1 name
softmax = torch.nn.Softmax(dim=0)
n_names = int(sys.argv[1])
new_names_list = []

for i in range(n_names):
    content_block = '...' 
    new_name = ''

    while True:
        start_char_encoded = [encode(c) for c in content_block]
        start_char_vector = V[start_char_encoded].view(-1)

        h1 = (start_char_vector @ W1 + b1).tanh()
        out = h1 @ W2 + b2

        probabilities = softmax(out)
        next_char_index = torch.multinomial(probabilities, num_samples=1, replacement=True).item()
        next_char = possible_chars[next_char_index]
        if next_char == '.':
            break
        else:
            content_block = content_block[1:] + next_char
            new_name += next_char
    new_names_list.append(new_name)

print(new_names_list)