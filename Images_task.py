from PIL import Image

matrix = Image.open('word_matrix.png')
mask = Image.open('mask.png')

print('matrix dimentions: ', matrix.size)
print('mask dimentions: ', mask.size)

w = 1015
h = 559
matrix.putalpha(150)
new_mask = mask.resize((w, h))
print(new_mask.size)
new_mask.show()
new_mask.paste(im=matrix, box=(0, 0), mask=matrix)
new_mask.show()