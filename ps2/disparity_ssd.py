import numpy as np
import cv2
import os

def disparity_ssd(L, R, window_size=5):
    """Compute disparity map D(y, x) such that: L(y, x) = R(y, x + D(y, x))

    Params:
    L: Grayscale left image
    R: Grayscale right image, same size as L

    Returns: Disparity map, same size as L, R
    """

    disparity = np.zeros_like(L)
    img_row, img_col = L.shape
    tpl_row = tpl_col = window_size

    for r in range(tpl_row / 2, img_row - tpl_row / 2 + 1):
        strip_top = r - tpl_row
        strip_btm = r + tpl_row
        R_strip = R[strip_top:strip_btm, :].astype(np.float32)
        d = cv2.matchTemplate(R_strip, cv2.TM_SQDIFF_NORMED)

if __name__ == "__main__":
    L = cv2.imread(os.path.join('input', 'pair0-L.png'), 0) * (1.0 / 255.0)  # grayscale, [0, 1]
    R = cv2.imread(os.path.join('input', 'pair0-R.png'), 0) * (1.0 / 255.0)
    D_L = disparity_ssd(L, R)
