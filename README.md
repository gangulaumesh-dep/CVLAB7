# Image Filtering and Edge Suppression (Custom Implementation)

This script contains a custom Python implementation of spatial image filtering (convolution) with padding and stride support, along with the foundational steps for Non-Maximum Suppression and Double Thresholding (commonly used in Canny Edge Detection).

## Prerequisites

Ensure you have the required Python libraries installed:

    pip install opencv-python matplotlib numpy

## How to Use

1. Update the image path in the script. It currently reads from `/content/drive/MyDrive/dove.jpg`. Change this to your local image path:
       
       img = cv2.imread('path/to/your/image.jpg')
       
2. Run the script in your terminal or Python environment.
### Note: You can directly open the `.ipynb` file in Colab or Jupyter Notebook.

## How it Works

1. **Custom Convolution**: The `image_filtering` function implements mathematical convolution with customizable padding (`p`) and stride (`s`) parameters, returning the filtered image array.
2. **Kernel Operations**: Initializes a 9x9 normalized Box Filter (Average Filter) and applies it to the image.
3. **Non-Maximum Suppression (NMS)**: Contains the logic to thin edges by comparing pixel gradients across discrete orientation angles (Note: depends on gradient magnitude and orientation arrays).
4. **Hysteresis Thresholding**: Defines Strong and Weak edges using high and low threshold values (`Th` and `Tl`), isolating the most distinct structural edges in the image.
