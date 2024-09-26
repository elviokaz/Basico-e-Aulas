import io

import numpy as np
import tensorflow as tf

# Carregar o modelo de geração de imagens
model = tf.keras.models.load_model("model.h5")

# Criar um prompt de texto para a imagem
prompt = "Uma paisagem de montanha com um lago e árvores"

# Gerar a imagem
image = model.generate_image(prompt, image_size=(512, 512))

# Converter a imagem para um formato que possa ser exibido
image = tf.keras.preprocessing.image.array_to_img(image)
image_bytes = io.BytesIO()
image.save(image_bytes, format="png")

# Exibir a imagem
from IPython.display import display
display(image_bytes)
