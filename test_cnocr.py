from cnocr import CnOcr
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-im', '--image_path', default='', type=str, help='image_path for testing')
args = vars(parser.parse_args())
img_fp = args['image_path']

def replacing(a: str):
    result = a.replace('q', '9')
    result = result.replace('o', '0')
    result = result.replace('O', '0')
    result = result.replace('Q', '0')
    result = result.replace('I', '1')
    result = result.replace('i', '1')
    return result

# img_fp = '/home/tigran/Datasets/vincut/13.jpg'
ocr = CnOcr(det_model_name='en_PP-OCRv3_det', rec_model_name='en_PP-OCRv3')
out = ocr.ocr(img_fp)
print(out)
assert len(out) > 0, "The model can't read VIN from your image, please load another image"
if len(out) == 1:
    vin = replacing(out[0]['text'])
    score = out[0]['score']
    print(f'Result: {vin}\t Confidence: {score}')
else:
    for item in out:
        vin = replacing(item['text'])
        score = item['score']
        print(f'Result: {vin}\t Confidence: {score}')
        print('\n')
