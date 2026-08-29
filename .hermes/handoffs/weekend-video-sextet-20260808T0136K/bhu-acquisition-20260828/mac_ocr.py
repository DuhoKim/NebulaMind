import Quartz
import Vision
from Foundation import NSURL
import sys

def ocr_image(image_path):
    url = NSURL.fileURLWithPath_(image_path)
    image = Quartz.CIImage.imageWithContentsOfURL_(url)
    
    request = Vision.VNRecognizeTextRequest.alloc().init()
    request.setRecognitionLevel_(Vision.VNRequestTextRecognitionLevelAccurate)
    
    handler = Vision.VNImageRequestHandler.alloc().initWithCIImage_options_(image, None)
    success, error = handler.performRequests_error_([request], None)
    
    if success:
        results = request.results()
        text = "\n".join([result.topCandidates_(1)[0].string() for result in results])
        return text
    else:
        return f"Error: {error}"

if __name__ == '__main__':
    for i in range(1, 13):
        path = f"page_{i}.png"
        print(f"\n--- Page {i} ---")
        print(ocr_image(path))
