#-----------------------------------------------------------
#-----------------------------------------------------------
def saveh5py(varsave, istep,fname):

    import numpy as np
    import h5py

    # save to h5 file
    if istep == 0:
        h5fu = h5py.File(fname+'.h5', 'w')
    else:
        h5fu = h5py.File(fname+'.h5', 'a')
    
    h5fu.create_dataset(str(istep)+'step', data=varsave)
    h5fu.close()

    return
#-----------------------------------------------------------
#-----------------------------------------------------------
def serial_train(data_in, data_out, istep):

    import torch
    import torch.nn.functional as F

    import numpy as np
    import h5py

    print(type(data_out))
    print(type(data_in))
    print('step = ',istep)

    print("shape in",np.shape(data_in))
    print("shape expect",np.shape(data_out))
    
    din_flat  = data_in.flatten()
    dout_flat = data_out.flatten()

    # set variables
    path_mod = './ModelCheckpoint.pt'
    path_loss = './ModelLoss.h5'

    # N is batch size; D_in is input dimension;
    # H is hidden dimension; D_out is output dimension.
    N = 36
    D_in = int(len(din_flat)/N)
    H = 100
    D_out = D_in
   
    # Create torch Tensors to hold inputs and outputs
    x = din_flat.reshape(N,D_in)
    y = dout_flat.reshape(N,D_out)
    x = torch.from_numpy(x).float()
    y = torch.from_numpy(y).float()
    
    # create model
    class TheModelClass(torch.nn.Module):
        def __init__(self):
            super(TheModelClass, self).__init__()
            self.fc1 = torch.nn.Linear(D_in, H)
            self.fc2 = torch.nn.Linear(H, D_out)
    
        def forward(self, x):
            x = F.relu(self.fc1(x))
            x = self.fc2(x)
            return x
    
    # create or load model based on current time step (istep)
    if istep == 0:
        model = TheModelClass()
    else:
        model = TheModelClass()
        model.load_state_dict(torch.load(path_mod))
        model.eval()
        
    # The nn package also contains definitions of popular loss functions; in this
    # case we will use Mean Squared Error (MSE) as our loss function.
    loss_fn = torch.nn.MSELoss(reduction='sum')
    
    learning_rate = 1e-4
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    loss_results = []
    
    for t in range(1000):
        # Forward pass: compute predicted y by passing x to the model. Module objects
        # override the __call__ operator so you can call them like functions. When
        # doing so you pass a Tensor of input data to the Module and it produces
        # a Tensor of output data.
        y_pred = model(x)
    
        # Compute and print loss. We pass Tensors containing the predicted and true
        # values of y, and the loss function returns a Tensor containing the
        # loss.
        loss = loss_fn(y_pred, y)
        loss_results.append(loss.item())
        if t % 100 == 99:
            print(t, loss.item())
    
        optimizer.zero_grad()
    
        # Backward pass: compute gradient of the loss with respect to model
        # parameters
        loss.backward()
    
        # Calling the step function on an Optimizer makes an update to its
        # parameters
        optimizer.step()
       
    # save model parameters    
    torch.save(model.state_dict(), path_mod)

    # save loss results
    # TODO: overwrites an existing filename's h5 file at istep=0, then adds next steps' losses
    if istep == 0:
        h5f = h5py.File(path_loss, 'w')
    else:
        h5f = h5py.File(path_loss, 'a')
    
    h5f.create_dataset(str(istep), data=loss_results)
    h5f.close()

    return
