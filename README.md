# Image Upscaling
<h2>Team Details</h2>
<b>Team Number: </b><p>24AACR13</p>
<b>Senior Mentor: </b><p>Abhiram Dodda</p>
<b>Junior Mentor: </b><p>Siddharth Mahesh, Ekanth Sai</p>
<b>Team Member: </b><p>Hemanth Nag Bitra</p>

---

## Table of Contents
- [Introduction](#introduction)  
- [Requirements](#requirements)  
- [How to Use](#installation-and-usage)  
- [Preview](#preview)  
- [Contribution](#contribution)  

---

## Introduction
This project focuses on **Single Image Super-Resolution (SISR)**, utilizing the **Enhanced Deep Super-Resolution (EDSR)** model to upscale images by **4x**. By leveraging deep learning techniques, it achieves high-quality image restoration with improvements measured using **PSNR (Peak Signal-to-Noise Ratio)** and **SSIM (Structural Similarity Index)**.

---

## Requirements
| Package | Version |  
|----------|------|  
| [Python](https://www.python.org/downloads/) | 3.10.14|  
| [PyTorch](https://pytorch.org/) | 2.4.0|
| [Torchvision](https://github.com/pytorch/vision/) | 0.19.0|
| [Pillow](https://pypi.org/project/pillow/) | 10.3.0|
| [Matplotlib](https://matplotlib.org) | 3.7.5|
| [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) |  12.6|  

---

## Installation and Usage

Follow these steps to set up the project and perform image upscaling:

### Step 1: Clone the Repository
```bash
git clone https://github.com/AAC-Open-Source-Pool/Image-Upscaling
```
### Step 2: Install requirements.txt
```bash
pip install -r requirements.txt
```
#### Dataset Link: [https://data.vision.ee.ethz.ch/cvl/DIV2K/](https://data.vision.ee.ethz.ch/cvl/DIV2K/)
### Step 3: To train the model yourself
    1. Download the dataset from the given link, and place it appropriately in the dataset directory
    2. Run training.ipynb
    3. The model and plots will be saved to Models directory
### Step 4: To upscale the images of your own
    1. Place the model in "Models" directory
    2. Place the set of images to upscale in "Input" directory
    3. Run upscale.py
    4. Find the upscaled images in "Upscaled" directory

## Preview
<h3>The below are the images upscaled using the model: <br><br>
<div align="center">
<img src="https://i.imgur.com/yrLE4cw.png"> <br>
 Fig.1 (Left - Original, Right - Upscaled) <br><br><br>
<img src="https://i.imgur.com/4j1fNe7.png"> <br>
 Fig.2 (Left - Original, Right - Upscaled) <br><br><br>
<img src="https://i.imgur.com/vwtZFkk.png"> <br>
 Fig.3 (Left - Original, Right - Upscaled) <br><br>
</h3>

## Contribution
This section provides instructions and details on how to submit a contribution via a pull request. It is important to follow these guidelines to make sure your pull request is accepted.
1. Before choosing to propose changes to this project, it is advisable to go through the readme.md file of the project to get the philosophy and the motive that went behind this project. The pull request should align with the philosophy and the motive of the original poster of this project.
2. To add your changes, make sure that the programming language in which you are proposing the changes should be the same as the programming language that has been used in the project. The versions of the programming language and the libraries(if any) used should also match with the original code.
3. Write a documentation on the changes that you are proposing. The documentation should include the problems you have noticed in the code(if any), the changes you would like to propose, the reason for these changes, and sample test cases. Remember that the topics in the documentation are strictly not limited to the topics aforementioned, but are just an inclusion.
4. Submit a pull request via [Git etiquettes](https://gist.github.com/mikepea/863f63d6e37281e329f8)

