# Hough-Transform-and-Hough-Line-Transform-Using-OpenCV
Hough transform is a feature extraction method for detecting simple shapes such as circles, lines, etc in an image. Hough Transform and Hough Line Transform is implemented in OpenCV with two methods; the Standard Hough Transform and the Probabilistic Hough Line Transform.

The “simple” characteristic is derived by the shape representation in terms of parameters. A “simple” shape will be only represented by a few parameters, for example a line can be represented by its slope and intercept, or a circle which can be represented by x, y and radius.
## Detecting lines using OpenCV
In OpenCV, line detection using Hough Transform is implemented in the functions HoughLines and HoughLinesP (Probabilistic Hough Transform).
