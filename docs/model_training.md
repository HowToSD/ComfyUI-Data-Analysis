# Model Training

Experimental PyTorch model training has been added.  
No coding is required. Training is as simple as a single click!  
Currently, only classification is supported.

The system is designed to be modular. For example, to switch from a linear model to a convolutional model, you only need to replace the model node (see screenshot below).

You can choose to:
* Use your own images
* Use a public dataset

## Using Your Own Images

Check out [the dog and cat classification tutorial](dog_cat_classification_model_training.md).

## Public Datasets

Currently, only Fashion MNIST has been tested. Other public datasets have not been verified yet, though they may work.  
If you try one and it doesn't work, please create an issue so I can investigate adding support.

To use the Fashion MNIST dataset, simply drag and drop the workflow files below into ComfyUI. The model will be downloaded automatically.

Linear model  
* Training: examples/fashion_mnist_train.json  
* Evaluation: examples/fashion_mnist_eval.json

Convolutional model  
* Training: examples/fashion_mnist_train_conv.json  
* Evaluation: examples/fashion_mnist_eval_conv.json

These training workflows train a FashionMNIST model from scratch effortlessly.

### Training workflow
**Linear model**
![Train](images/fashion_mnist_train.png)

**Conv model**
![Train](images/conv_train.png)

*Close up of the conv node*
![Train](images/conv_train2.png)

### Eval workflow
**Linear model**
![Eval](images/fashion_mnist_eval.png)

**Conv model**
![Eval](images/conv_eval.png)
