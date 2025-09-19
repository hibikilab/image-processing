from PIL import Image
import numpy as np
from pathlib import Path

def image_to_rgb_arrays(image_path):
    """
    画像ファイルを読み込み、R, G, Bの2次元配列に分解する。

    Parameters:
        image_path (Path or str): 入力画像のパス

    Returns:
        tuple: R, G, B の numpy.ndarray（2次元配列）
    """
    image_path = Path(image_path)
    img = Image.open(image_path).convert('RGB')
    img_array = np.array(img)

    # R = img_array[:, :, 0]
    # G = img_array[:, :, 1]
    # B = img_array[:, :, 2]
    R = np.array(img_array[:, :, 0], dtype=np.int64)
    G = np.array(img_array[:, :, 1], dtype=np.int64)
    B = np.array(img_array[:, :, 2], dtype=np.int64)

    return R, G, B

def rgb_arrays_to_image(R, G, B, save_path=None):
    """
    R, G, Bの2次元配列から画像を生成する。

    Parameters:
        R, G, B: 各色チャネルの2次元配列（リストやnp.ndarrayなど）
        save_path (Path or str, optional): 保存先のパス。指定しない場合は画像を返すのみ。

    Returns:
        PIL.Image: 生成された画像
    """
    R = np.array(R, dtype=np.uint8)
    G = np.array(G, dtype=np.uint8)
    B = np.array(B, dtype=np.uint8)

    rgb_array = np.stack((R, G, B), axis=-1)
    img = Image.fromarray(rgb_array, mode='RGB')

    if save_path:
        save_path = Path(save_path)
        img.save(save_path)

    return img

def grayscale_array_to_image(gray_array, save_path=None):
    """
    グレースケールの2次元配列から画像を生成する。

    Parameters:
        gray_array: グレースケールの2次元配列（リストやnp.ndarrayなど）
        save_path (Path or str, optional): 保存先のパス。指定しない場合は画像を返すのみ。

    Returns:
        PIL.Image: 生成された画像
    """
    gray_array = np.array(gray_array, dtype=np.uint8)
    img = Image.fromarray(gray_array, mode='L')

    if save_path:
        save_path = Path(save_path)
        img.save(save_path)

    return img
