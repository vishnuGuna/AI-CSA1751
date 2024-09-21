import math
import random

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        self.weights_input_hidden = [[random.random() for _ in range(hidden_size)] for _ in range(input_size)]
        self.weights_hidden_output = [[random.random() for _ in range(output_size)] for _ in range(hidden_size)]
        self.bias_hidden = [random.random() for _ in range(hidden_size)]
        self.bias_output = [random.random() for _ in range(output_size)]

    def feedforward(self, X):
        hidden_layer = [0] * self.hidden_size
        output_layer = [0] * self.output_size

        for i in range(self.hidden_size):
            for j in range(self.input_size):
                hidden_layer[i] += X[j] * self.weights_input_hidden[j][i]
            hidden_layer[i] += self.bias_hidden[i]
            hidden_layer[i] = sigmoid(hidden_layer[i])

        for i in range(self.output_size):
            for j in range(self.hidden_size):
                output_layer[i] += hidden_layer[j] * self.weights_hidden_output[j][i]
            output_layer[i] += self.bias_output[i]
            output_layer[i] = sigmoid(output_layer[i])

        return output_layer

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [[0], [1], [1], [0]]

nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)

for x in X:
    output = nn.feedforward(x)
    print(f"Input: {x} Output: {output}")
