from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw


def add_text():
    base = Image.open(image_path).convert("RGBA")
    txt_layer = Image.new("RGBA", base.size, (255, 255, 255, 0))

    text_to_add = entry_box.get()
    text_font = ImageFont.truetype("arial.ttf", 60)

    draw = ImageDraw.Draw(txt_layer)
    draw.text((base.width - 300, base.height - 100), text_to_add, fill=(255, 255, 255, 100), font=text_font)
    # White text with alpha=100 (out of 255) for transparency

    watermarked = Image.alpha_composite(base, txt_layer)

    # Convert back to RGB and save
    final_image = watermarked.convert("RGB")
    final_image.save(image_path)

    image_label.after(1000, show_pic)


def show_pic():
    new_img = Image.open(image_path)
    new_img = new_img.resize((300, 200))
    updated_tk_image = ImageTk.PhotoImage(new_img)
    image_label.config(image=updated_tk_image)
    image_label.image = updated_tk_image


def load_image_from_path():
    global image_path, image_tk, image_label

    image_path = image_path_box.get()
    if not image_path:
        return

    top.destroy()  # Close the popup

    image = Image.open(image_path)
    im = image.resize((300, 200))
    image_tk = ImageTk.PhotoImage(im)

    image_label = Label(window, image=image_tk)
    image_label.pack(pady=20)

    # Show entry and button
    entry_box.pack(pady=20)
    button.pack(pady=20)


window = Tk()
window.title('Image')

top = Toplevel(window)
top.title("Enter the image path")

Label(top, text="Enter full image path:").pack(pady=10)
image_path_box = Entry(top, width=50, font=('Helvetica', 12))
image_path_box.pack(pady=5)
Button(top, text="Load Image", command=load_image_from_path).pack(pady=10)

entry_box = Entry(window, font=('Helvetica', 14))

button = Button(window, text='Add text to image', command=add_text, font=("Helvetica", 14))

window.mainloop()