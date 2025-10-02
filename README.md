 Image Resizer Tool
 Project Overview

The Single Image Resizer Tool is a Python application that allows users to select a particular image from their device, resize it to a custom width and height, and save it in a chosen format (PNG, JPEG, BMP, or GIF). The user selects both the input image and the output folder using a simple file dialog, making the tool user-friendly and professional.

 Features

Select a single image file using a file picker dialog.

Choose an output folder to save the resized image.

Specify custom width and height for resizing.

Convert images into multiple formats (PNG, JPEG, BMP, GIF).

Clean and professional script with error handling.

 Tools & Libraries

Python 3.x

Pillow (PIL) → For image processing.

Tkinter → For file/folder selection dialogs.

 Project Structure
image_resizer/
│── image_resizer.py   # Main script
│── README.md          # Project documentation

 Installation

Clone or download the repository.

Install required dependencies:

pip install pillow


(Tkinter comes pre-installed with Python, no need to install separately on most systems.)

 Usage

Run the script:

python image_resizer.py


A file dialog will appear → Select the image you want to resize.

A folder dialog will appear → Choose where to save the resized image.

Enter the desired width & height.

Enter the output format (PNG/JPEG/BMP/GIF).

The resized image will be saved in the selected folder.

 Example Run
 Please select an image to resize...
 Please select the output folder...
 Enter width: 500
 Enter height: 400
 Enter output format (PNG/JPEG/BMP/GIF): JPEG

 myphoto.jpg resized and saved as C:/Users/Output/myphoto.jpeg

 Outcome

A lightweight, automated tool to resize and convert a single selected image with just a few clicks.
