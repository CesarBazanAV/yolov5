# import PIL
# from PIL import ImageDraw
import argparse
import easyocr

from utils.general import colorstr


def run(source='data/images'  # file/dir/URL/glob, 0 for webcam
        ):
    bounds = reader.readtext(source)
    print(f"Bounds: {bounds}")
    for bound in bounds:
        print(bound)


def load_model():
    print(f"Loading easyocr model")
    reader = easyocr.Reader(['es', 'en'])  # need to run only once to load model into memory


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='data/images', help='file/dir/image')
    opt = parser.parse_args()
    return opt


def main(opt):
    print(colorstr('detect: ') + ', '.join(f'{k}={v}' for k, v in vars(opt).items()))
    # check_requirements(exclude=('tensorboard', 'thop'))
    load_model()
    run(**vars(opt))


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
