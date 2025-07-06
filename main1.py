from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFont, ImageDraw

save_path = None


def add_text():
    global save_path
    if not save_path:
        save_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All Files", "*.*")],
            title="Save watermarked image as..."
        )
        if not save_path:
            return

    base = Image.open(image_path).convert("RGBA")
    txt_layer = Image.new("RGBA", base.size, (255, 255, 255, 0))

    text_to_add = entry_box.get()
    text_font = ImageFont.truetype("arial.ttf", 60)

    draw = ImageDraw.Draw(txt_layer)
    draw.text((base.width - 300, base.height - 100), text_to_add, fill=(255, 255, 255, 100), font=text_font)

    watermarked = Image.alpha_composite(base, txt_layer)
    final_image = watermarked.convert("RGB")

    final_image.save(save_path)
    image_label.after(1000, show_pic)


def show_pic():
    if save_path:
        new_img = Image.open(save_path)
        new_img.show()


def choose_image():
    global image_path, image_tk, image_label, save_path
    save_path = None

    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp")]
    )
    if not file_path:
        return

    image_path = file_path
    image = Image.open(image_path)
    im = image.resize((300, 200))
    image_tk = ImageTk.PhotoImage(im)

    image_label.config(image=image_tk)
    image_label.image = image_tk

    entry_box.pack(pady=20)
    button.pack(pady=20)


window = Tk()
window.title('Image Watermarker')

choose_button = Button(window, text='Choose Image', command=choose_image, font=("Helvetica", 14))
choose_button.pack(pady=20)

image_label = Label(window)
image_label.pack(pady=20)

entry_box = Entry(window, font=('Helvetica', 14))
button = Button(window, text='Add Watermark and Save', command=add_text, font=("Helvetica", 14))

window.mainloop()
