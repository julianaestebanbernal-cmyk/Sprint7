# "Primer Punto"

"""from PIL import Image
im = Image.open("/home/juli/Documentos/Proyecto VS/Sprint7/tripleten_logo.jpeg")
print(im.size)

rotated = im.rotate(90)
rotated.save("/home/juli/Documentos/Proyecto VS/Sprint7/tripleten_logo.png")
"""

# "Segundo Punto"
"""
from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("output_file")
parser.add_argument("angle", type=int)
args = parser.parse_args()

im = Image.open(args.input_file)
print(im.size)

rotated = im.rotate(args.angle, expand=True)
rotated.save(args.output_file)
print(rotated.size)
"""


# "tercer punto"
"""
from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="ruta del archivo de imagen de entrada")
parser.add_argument("output_file", help="ruta del archivo de imagen de salida")
parser.add_argument("--angle", "-a", type=int, default=90, help="ángulo de rotación")
args = parser.parse_args()

im = Image.open(args.input_file)
print(im.size)

rotated = im.rotate(args.angle)
rotated.save(args.output_file)
print(rotated.size)
"""

# "Cuarto punto"
"""
from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("output_file")
parser.add_argument("--angle", "-a", type=int, default=90)
parser.add_argument("-i", "--info", action="store_true")
args = parser.parse_args()

im = Image.open(args.input_file)
if args.info:
    print("dimensiones de la imagen de entrada:", im.size)

rotated = im.rotate(args.angle)
rotated.save(args.output_file)
"""

# Ejercicio 5

from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='ruta del archivo de entrada')
parser.add_argument('output_file', help='ruta del archivo de salida')
parser.add_argument('width', help='ancho deseado', type=int)
parser.add_argument('height', help='altura deseada', type=int)
args = parser.parse_args()

im = Image.open(args.input_file)
new_size = (args.width, args.height)
resized = im.resize(new_size)
resized.save(args.output_file)
im.close()
