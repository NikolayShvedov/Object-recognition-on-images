from imageai.Detection import ObjectDetection
import os

exec_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(
    exec_path, "resnet50_coco_best_v2.1.0.h5")
)
detector.loadModel()

list = detector.detectObjectsFromImage(
    input_image=os.path.join(exec_path, "test_images/objects.jpg"),
    output_image_path=os.path.join(exec_path, "new_objects.jpg")
)