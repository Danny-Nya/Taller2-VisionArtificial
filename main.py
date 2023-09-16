import cv2
import numpy as np

# Cargar la imagen de entrada
input_image = cv2.imread('input_image.jpg')

# Definir las transformaciones
translation_matrix = np.float32([[1, 0, 42], [0, 1, -37]])
rotation_angle = 65
scale_factor = 0.75

# Método 1: Usando funciones de OpenCV

# Aplicar la traslación usando la función warpAffine
translated_image_cv = cv2.warpAffine(input_image, translation_matrix, (input_image.shape[1], input_image.shape[0]))
cv2.imwrite('translated_image_cv_function.jpg', translated_image_cv)
# Aplicar la rotación y el escalamiento usando la función warpAffine
rotation_matrix = cv2.getRotationMatrix2D((input_image.shape[1] / 2, input_image.shape[0] / 2), rotation_angle, scale_factor)
cv2.imwrite('rotated_image_cv_function.jpg', rotation_matrix)
rotated_scaled_image_cv = cv2.warpAffine(input_image, rotation_matrix, (input_image.shape[1], input_image.shape[0]))
cv2.imwrite('rotated_scaled_image_cv_function.jpg', rotated_scaled_image_cv)
# Método 2: Calculando la matriz compuesta y aplicándola

# Calcular la matriz compuesta de transformación
combined_matrix = np.matmul(np.float32([[np.cos(np.radians(rotation_angle)), -np.sin(np.radians(rotation_angle)), 0],
                                       [np.sin(np.radians(rotation_angle)), np.cos(np.radians(rotation_angle)), 0]]),
                            np.float32([[scale_factor, 0],
                                       [0, scale_factor], [0, 0]]))
combined_matrix = np.matmul(combined_matrix, translation_matrix)

# Aplicar la matriz de transformación combinada a la imagen
transformed_image_combined = cv2.warpAffine(input_image, combined_matrix, (input_image.shape[1], input_image.shape[0]))

# Guardar las imágenes resultantes
cv2.imwrite('translated_image_cv.jpg', translated_image_cv)
cv2.imwrite('rotated_scaled_image_cv.jpg', rotated_scaled_image_cv)
cv2.imwrite('transformed_image_combined.jpg', transformed_image_combined)

