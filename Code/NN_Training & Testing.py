# Prior Training we have to setup loss fuction & optimizer
lossfn = nn.L1Loss()                                               # Loss fuction used is mean absolute error (MAE) 
optimizer = torch.optim.SGD(model_0.parameters(), lr=0.01)         # Optimizer is useing 


# In this section we have trained our model using gradient descent and back propogation with 200+ epochs

torch.manual_seed(99)
epochs = 225                                        # No of loop for the data 

for epoch in range(epochs):
  model_0.train()                                   # Puts the model in training mode

  y_prediction = model_0(X_train)                   # We have inputed the trainning data to our Fw pass predicting 'y'
  loss = lossfn(y_prediction, y_train)              # Calculating loss brtween predicted - actual 
  optimizer.zero_grad()                             # Clears the gradient of parameters
  loss.backward()                                   # Perform Backpropagation based on loss observed
  optimizer.step()                                  # Update parameters on computed gradients


# Testing the Model
  model_0.eval()                                    # Puts the model in evaluation i.e. testing/validation set
  with torch.inference_mode():
     ytest_preds = model_0(X_test)                  # Inputed the testing data to our Fw pass

     test_loss = lossfn(ytest_preds, y_test)        # Calculating loss
 
 
 ---------------------------------------------------------------
  # following section can we use to see the trend in loss fuctions

loss_v = []
testl_v = []
epoch_c = []

if epoch % 10 == 0:
  epoch_c.append(epoch)
  loss_v.append(loss.detach().numpy())
  testl_v.append(test_loss.detach().numpy())
  print (f"Epoc: {epoch}, Loss: {loss},  test loss: {test_loss}") 
    
