# import PIL
# from PIL import ImageDraw
import argparse
import easyocr

from utils.general import colorstr


def load_model():
    print(f"Loading easyocr model")
    reader = easyocr.Reader(['es', 'en'])  # need to run only once to load model into memory
    return reader


def detect(source='data/images'):
    print(f"OCR active")
    t0 = time.time()
    bounds = reader.readtext(source)
    t1 = time_sync()
    table = [['Activity', 'Time', 'Unit'],
             ['OCR detection', total_process_time, 's'],
             ['Average detection', 1/total_process_time, 'FPS']]
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid', floatfmt=".3f"))
    for bound in bounds:
        print(bound)


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='data/images', help='file/dir/image')
    opt = parser.parse_args()
    return opt


def main(opt):
    print(colorstr('detect: ') + ', '.join(f'{k}={v}' for k, v in vars(opt).items()))
    # check_requirements(exclude=('tensorboard', 'thop'))
    detect(**vars(opt))


reader = load_model()

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
