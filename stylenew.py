import paddle
import os
import sys

sys.path.insert(0, os.getcwd())
from ppgan.apps import LapStylePredictor
import argparse


def envirstyle(input_path:str,style_chose:str):
    """
    input_path:目标图像文件
    style_chose:选择风格迁移模型
    """

    predictor = LapStylePredictor(output='output_dir',
                                style=style_chose,
                                weight_path=None,
                                style_image_path=None)
    predictor.run(input_path)

# envirstyle('./image/guanzhou.jpg','stars')
