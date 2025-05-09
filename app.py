import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageFilter, ImageOps, ImageEnhance, ImageChops

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Imagens")

        self.image = None  # A imagem original
        self.modified_image = None  # A imagem modificada
        self.image_path = None
        self.original_image = None

        # Interface Gráfica
        self.canvas = tk.Canvas(root, width=1000, height=500)
        self.canvas.pack()

        # Botões
        self.load_button = tk.Button(root, text="Carregar Imagem", command=self.load_image)
        self.load_button.pack()

        self.gray_button = tk.Button(root, text="Escala de Cinza", command=self.apply_grayscale)
        self.gray_button.pack()

        self.invert_button = tk.Button(root, text="Inverter Cores", command=self.invert_colors)
        self.invert_button.pack()

        self.contrast_button = tk.Button(root, text="Aumento de Contraste", command=self.apply_contrast)
        self.contrast_button.pack()

        self.blur_button = tk.Button(root, text="Blur", command=self.apply_blur)
        self.blur_button.pack()

        self.sharpen_button = tk.Button(root, text="Nitidez", command=self.apply_sharpen)
        self.sharpen_button.pack()

        self.edges_button = tk.Button(root, text="Detecção de Bordas", command=self.apply_edges)
        self.edges_button.pack()

        self.save_button = tk.Button(root, text="Salvar Imagem", command=self.save_image)
        self.save_button.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Arquivos de Imagem", "*.jpg;*.png;*.jpeg")])
        if file_path:
            self.image_path = file_path
            self.image = Image.open(self.image_path)
            self.original_image = self.image.copy()
            self.modified_image = self.image.copy()  # Inicializa a imagem modificada
            self.show_images(self.original_image, self.modified_image)

    def resize_image(self, image):
        # Redimensiona as imagens para se ajustar ao tamanho do canvas (500x500)
        max_width = 500
        max_height = 500
        img_width, img_height = image.size

        # Calcular o fator de escala para manter a proporção
        scale_factor = min(max_width / img_width, max_height / img_height)
        
        # Calcular o novo tamanho da imagem
        new_width = int(img_width * scale_factor)
        new_height = int(img_height * scale_factor)
        
        # Redimensionar a imagem
        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        return resized_image

    def show_images(self, image1, image2):
        # Redimensiona as imagens para caber dentro do editor
        resized_image1 = self.resize_image(image1)
        resized_image2 = self.resize_image(image2)

        # Convertendo as imagens redimensionadas para um formato adequado para exibição no tkinter
        self.tk_image1 = ImageTk.PhotoImage(resized_image1)
        self.tk_image2 = ImageTk.PhotoImage(resized_image2)

        # Limpa o canvas antes de desenhar as imagens
        self.canvas.delete("all")

        # A primeira imagem será a original e a segunda será a modificada
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image1)  # Imagem original à esquerda
        self.canvas.create_image(500, 0, anchor=tk.NW, image=self.tk_image2)  # Imagem modificada à direita

    def apply_grayscale(self):
        if self.image:
            gray_image = self.image.convert("L")
            self.modified_image = gray_image  # Atualiza a imagem modificada
            self.show_images(self.original_image, self.modified_image)
        else:
            messagebox.showerror("Erro", "Nenhuma imagem carregada")

    def invert_colors(self):
        if self.image:
            inverted_image = ImageOps.invert(self.image.convert("RGB"))
            self.modified_image = inverted_image  # Atualiza a imagem modificada
            self.show_images(self.original_image, self.modified_image)
        else:
            messagebox.showerror("Erro", "Nenhuma imagem carregada")

    def apply_contrast(self):
        if self.image:
            enhancer = ImageEnhance.Contrast(self.image)
            contrast_image = enhancer.enhance(2)  # Aumenta o contraste em 2x
            self.modified_image = contrast_image  # Atualiza a imagem modificada
            self.show_images(self.original_image, self.modified_image)
        else:
            messagebox.showerror("Erro", "Nenhuma imagem carregada")

    def apply_blur(self):
        if self.image:
            blurred_image = self.image.filter(ImageFilter.GaussianBlur(5))  # Desfoque
            self.modified_image = blurred_image  # Atualiza a imagem modificada
            self.show_images(self.original_image, self.modified_image)
        else:
            messagebox.showerror("Erro", "Nenhuma imagem carregada")

    def apply_sharpen(self):
        if self.image:
            sharpened_image = self.image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))  # Nitidez
            self.modified_image = sharpened_image  # Atualiza a imagem modificada
            self.show_images(self.original_image, self.modified_image)
        else:
            messagebox.showerror("Erro", "Nenhuma imagem carregada")

    def apply_edges(self):
        if self.image:
            edges_image = self.image.filter(ImageFilter.FIND_EDGES)  # Detecção de bordas
            self.modified_image = edges_image  # Atualiza a imagem modificada
            self.show_images(self.original_image, self.modified_image)
        else:
            messagebox.showerror("Erro", "Nenhuma imagem carregada")

    def save_image(self):
        if self.modified_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
            if save_path:
                self.modified_image.save(save_path)  # Salva a imagem modificada
        else:
            messagebox.showerror("Erro", "Nenhuma imagem modificada para salvar")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()
