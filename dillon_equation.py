import sympy as sp
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter, ImageEnhance

# Symbols for Dillon Creation Equation
c0, alpha, Psi, f_369, R, n = sp.symbols('c0 alpha Psi f_369 R n')

# Derive the Creation Equation
c_R = c0 * (1 + alpha * Psi / f_369 * R**n)

# Derive the Dillon Operator
dillon_op = sp.diff(c_R, R)

# Function to generate holographic image
def generate_holographic_image(equation_str, filename='dillon_holo.png'):
    fig, ax = plt.subplots(figsize=(8, 4), facecolor='black')
    ax.text(0.5, 0.5, equation_str, fontsize=20, color='white', ha='center', va='center')
    ax.axis('off')
    plt.savefig('temp.png', bbox_inches='tight', facecolor='black')
    plt.close()

    # Add holographic glow
    img = Image.open('temp.png')
    img = img.filter(ImageFilter.GaussianBlur(5))
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.5)
    img.save(filename)
    print(f"Holographic image saved as {filename}")

# Example usage
equation_str = f"c_R = {c_R}"
generate_holographic_image(equation_str)

print("Derived Dillon Creation Equation:", c_R)
print("Derived Dillon Operator:", dillon_op)
