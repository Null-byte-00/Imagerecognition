# Image Recognition
![alt text](https://github.com/Null-byte-00/Imagerecognition/blob/main/imagerec.gif)
A simple Image recognition program using pytorch
This is a simple convolutional neural network capable of recognizing 3 different shapes (house, smiling face and fish)<br>
[you can download full version from here](https://drive.google.com/file/d/1CN_dbHrfiZctm-eJKfEIBof6HHYs1SjA/view?usp=drive_link)
## The model 
the model is a a small convolutional neural network with two convolution/maxpool and 2 linear layers. the input is a square 500x500 2d array (because all pixels in my datase images are whether (0,0,0) or (255,255,255) it shoul be 
a 2d array of 0s and 1s). It gives 3 different numbers as output that are then passed through a softmax function to get the probabilities for 3 different shapes
## The dataset
the dataset consists of 243 pictures I drew (81 samples for each shape)<br>
create_dataset.py turns all thesepictures intoa hdf file<br>
[here you can download raw images](https://drive.google.com/file/d/1k1mj3IhPsY-ZmQHdGsiiAwm3iMY7Zt4R/view?usp=drive_link)
## Training 
the model is trained by stochastic gradient descent and mean square error loss function.<br>
[here you can download the trained model pth file]()
## how to use
first import the conda enviroment
```
conda env create -f environment.yml
```
activate the enviroment
```
conda activate imagerecognition
```
create a directory named models then download the trained model from [here](https://drive.google.com/file/d/15cgj57P1yLuC7fwWc9u_2omlSK4DFuKl/view?usp=drive_link) and copy it in models directory
now run:
```
python main.py
```
the window will open and you can draw. press 'c' on the keyboard to get the results like this:
```
tensor([-160.3708,  134.9981,   40.6356])
house: tensor(0., grad_fn=<MulBackward0>)
smilingface: tensor(100., grad_fn=<MulBackward0>)
fish: tensor(1.0445e-39, grad_fn=<MulBackward0>)
```
these are probability percentages for each shape 
