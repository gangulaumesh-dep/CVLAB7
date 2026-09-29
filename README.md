# Canny Edge Detection

## Introduction

This experiment implements the **Canny Edge Detection** technique on a grayscale image using Python, OpenCV, NumPy, and Matplotlib.

## Objective

To detect significant edges in an image using smoothing, Sobel operators, non-maximum suppression, and hysteresis thresholding.

## Technologies Used

* Python
* OpenCV
* NumPy
* Matplotlib
* Google Colab

## Methodology

1. Convert the input image to grayscale.
2. Apply average filtering for smoothing.
3. Calculate horizontal and vertical gradients using Sobel operators.
4. Calculate gradient magnitude and orientation.
5. Quantize the orientation into 0°, 45°, 90°, and 135°.
6. Apply Non-Maximum Suppression.
7. Apply Hysteresis Thresholding.
8. Display the final Canny edge image.

## Output

The program displays:

* Original Grayscale Image
* Gradient Magnitude
* Non-Maximum Suppressed Image
* Canny Edges

## Result

The significant edges of the input image were successfully detected using the Canny edge detection process.

## Conclusion

Thus, Canny edge detection was successfully implemented using smoothing, Sobel gradient calculation, non-maximum suppression, and hysteresis thresholding.


#OUTPUT:-

<img width="1415" height="345" alt="image" src="https://github.com/user-attachments/assets/b0cb06a6-ca68-4deb-b6f0-3d4585ec50dc" />
