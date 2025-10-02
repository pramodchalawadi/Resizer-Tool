import os
from tkinter import Tk, filedialog
from PIL import Image

def resize_image(input_file, output_folder, size=(800, 600), output_format="PNG"):
    """
    Resize and convert a single image.

    Args:
        input_file (str): Path to the input image
        output_folder (str): Path to save the resized image
        size (tuple): Desired image size (width, height)
        output_format (str): Output format (e.g., "PNG", "JPEG")
    """
    try:
        img = Image.open(input_file)
        resized_img = img.resize(size)

        base_name = os.path.splitext(os.path.basename(input_file))[0]
        new_filename = f"{base_name}.{output_format.lower()}"

        save_path = os.path.join(output_folder, new_filename)
        resized_img.save(save_path, output_format.upper())

        print(f"✅ {input_file} resized and saved as {save_path}")
    except Exception as e:
        print(f"❌ Error processing {input_file}: {e}")


if __name__ == "__main__":
    # Hide root Tkinter window
    root = Tk()
    root.withdraw()

    print("🖼️ Please select an image to resize...")
    input_file = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )

    if not input_file:
        print("❌ No image selected. Exiting...")
        exit()

    print("💾 Please select the output folder...")
    output_folder = filedialog.askdirectory(title="Select Output Folder")

    if not output_folder:
        print("❌ No output folder selected. Exiting...")
        exit()

    # Ask user for size & format
    width = int(input("📏 Enter width: "))
    height = int(input("📏 Enter height: "))
    output_format = input("🖼️ Enter output format (PNG/JPEG/BMP/GIF): ").strip().upper()

    resize_image(input_file, output_folder, size=(width, height), output_format=output_format)
