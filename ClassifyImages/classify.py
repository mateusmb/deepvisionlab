# Source from Alexey Spizhevoy and Aleksandr Rybnikov OpenCV 3 Computer Vision with Python Cookbook

import cv2
import numpy as np

# Function to classify frames from video capture
def classify(video_src, net, in_layer, out_layer, mean_val, 
             category_names, swap_channels=False):
    capture = cv2.VideoCapture(video_src)

    t = 0

    while True:
        has_frame, frame = capture.read()
        if not has_frame:
            break

        # Transform frame to tensor/blob
        if isinstance(mean_val, np.ndarray):
            tensor = cv2.dnn.blobFromImage(frame, 1.0, (224, 224),
                                           1.0, False)
            tensor -= mean_val
        else:
            tensor = cv2.dnn.blobFromImage(frame, 1.0, (224, 224),
                                           mean_val, swap_channels)

        # Feeds tensor to deep network
        net.setInput(tensor, in_layer)
        prob = net.forward(out_layer)

        prob = prob.flatten()

        r = 1

        # Selects five categories with highest probability
        for i in np.argsort(prob)[-5:]:
            txt = '"%s"; probability: %.2f' % (category_names[i], prob[i])
            cv2.putText(frame, txt, (0, frame.shape[0] - r*40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
            r += 1

        cv2.imshow('classification', frame)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()
    capture.release()

# Open file with category names
with open('../res/imagenet_comp_graph_label_strings.txt') as f:
    class_names = [l.rstrip() for l in f.readlines()]

# Load a GoogleNet trained model from TensorFlow and call classify
googlenet_tf = cv2.dnn.readNetFromTensorflow('../res/tensorflow_inception_graph.pb')

classify(0, googlenet_tf, 'input', 'softmax2', 117, class_names, True)

