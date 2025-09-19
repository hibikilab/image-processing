from image_utils import image_to_rgb_arrays, rgb_arrays_to_image, grayscale_array_to_image

# 入力画像のパス
img_path = "images/hana.png"

# RGB分解
R, G, B = image_to_rgb_arrays(img_path)

# # RGBから画像再構成
reconstructed = rgb_arrays_to_image(R, G, B)
reconstructed.show()
reconstructed.save("output/hana.png")


# ==============
# グレー画像の生成
# ==============

image_array = [[255, 0, 0, 0, 0],
            [0, 255, 0, 0, 0],
            [0, 0, 255, 0, 0],
            [0, 0, 0, 255, 0],
            [0, 0, 0, 0, 255],
            ]

gray_img = grayscale_array_to_image(image_array)
gray_img.show()
gray_img.save("output/out.png")
