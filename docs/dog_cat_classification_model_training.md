# Dog cat classification model training tutorial
This tutorial covers how to use **ComfyUI Data Analysis** to train an image classification model with your own image dataset.  
We'll use a **dog and cat image dataset** created specifically for this tutorial, which is available publicly on [my GitHub repo](https://github.com/HowToSD/dog_and_cat_dataset).  

Once you complete the tutorial, you can experiment with your own images.

**Disclaimer:** The model architecture is a traditional convolutional neural network (CNN) and is **not state-of-the-art**. This choice keeps the model small, enabling faster training and easier explanation.

---

## Overview of Steps

1. Downloading the dog and cat dataset from the GitHub repo
2. Edit the training workflow  
3. Run the training workflow  
4. Edit the evaluation workflow
5. Run the evaluation workflow

---

## 1. Download the Dog & Cat Dataset  

Visit [the GitHub repo](https://github.com/HowToSD/dog_and_cat_dataset) and go to the **Releases** page.  
Click **"Source code (zip)"** to download the zip that contains all the images.  
Extract the ZIP file using an unarchiver.  

The dataset follows this directory structure:  

```
dog_and_cat
  train
    cats
    dogs

  val
    cats
    dogs
```


Take note of the **full paths** to the `train` and `val` directories, as you'll need them in the next step.

---

## 2. Editing the Training Workflow

Drag and drop the below file into ComfyUI:  
```
examples/workflow/dog_cat_classification_train_model.json
```
Some nodes will be marked red, indicating they require edits.  
The only required changes are the **train** and **val** dataset paths.  
Replace them with the paths noted earlier.

---

## 3. Running the Training Workflow  

Click **Queue** to start training.  

Monitor the console for errors. If training runs smoothly, you should see output like this:

```
Epoch (train) 1/20, Loss: 0.6865
Epoch (val) 1/20, Loss: 0.6801
Epoch (train) 2/20, Loss: 0.6216
Epoch (val) 2/20, Loss: 0.5710
Epoch (train) 3/20, Loss: 0.4998
Epoch (val) 3/20, Loss: 0.4716
Epoch (train) 4/20, Loss: 0.3827
Epoch (val) 4/20, Loss: 0.4045
Epoch (train) 5/20, Loss: 0.2897
Epoch (val) 5/20, Loss: 0.3297
Epoch (train) 6/20, Loss: 0.2243
Epoch (val) 6/20, Loss: 0.2925
Epoch (train) 7/20, Loss: 0.1603
Epoch (val) 7/20, Loss: 0.2916
Epoch (train) 8/20, Loss: 0.1102
Epoch (val) 8/20, Loss: 0.3216
Epoch (train) 9/20, Loss: 0.0916
Epoch (val) 9/20, Loss: 0.2706
Epoch (train) 10/20, Loss: 0.0522
Epoch (val) 10/20, Loss: 0.2220
Epoch (train) 11/20, Loss: 0.0481
Epoch (val) 11/20, Loss: 0.2820
Epoch (train) 12/20, Loss: 0.0228
Epoch (val) 12/20, Loss: 0.2899
Epoch (train) 13/20, Loss: 0.0130
Epoch (val) 13/20, Loss: 0.3056
Epoch (train) 14/20, Loss: 0.0137
Epoch (val) 14/20, Loss: 0.3070
Epoch (train) 15/20, Loss: 0.0200
Epoch (val) 15/20, Loss: 0.2714
Epoch (train) 16/20, Loss: 0.0313
Epoch (val) 16/20, Loss: 0.3108
Epoch (train) 17/20, Loss: 0.0125
Epoch (val) 17/20, Loss: 0.3388
Epoch (train) 18/20, Loss: 0.0174
Epoch (val) 18/20, Loss: 0.2989
Epoch (train) 19/20, Loss: 0.0017
Epoch (val) 19/20, Loss: 0.3165
Epoch (train) 20/20, Loss: 0.0009
Epoch (val) 20/20, Loss: 0.3582
Prompt executed in 253.64 seconds
```

If you encounter an error:  
- Ensure dataset paths are correct.  
- Reduce **batch size** if your GPU runs out of memory (OOM error).  

Once training completes, a **line chart** displaying training progress will appear at the bottom right of the canvas. You don’t need to interpret it initially.

---

## 4. Editing the Evaluation Workflow
Now, let's verify if the model was trained correctly. In this step, we'll feed the validation data into the trained model and compute metrics to assess its performance.

Drag and drop the below file into ComfyUI:  
```
examples/workflow/dog_cat_classification_eval_model.json
```

into **ComfyUI**.  

Update the **val dataset path**.

---

## 5. Running the Evaluation Workflow  

Click **Queue**. The evaluation process runs much faster than training.  

Check the **Accuracy** node—it should display a value around **0.9**, confirming successful model training.

Congratulations! You’ve successfully trained a machine learning model from scratch without writing a single line of code.

Now, you can use your own images to train the model in the same way.