from neural_io import neuralIO

io = neuralIO(ip='127.0.0.1',input='input.yaml',output='output.yaml')
print(io.getInputStates())
print(io.getOutputStates())
