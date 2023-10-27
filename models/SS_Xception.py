from keras.applications.xception import Xception
from keras.preprocessing import image
from keras.applications.xception import preprocess_input, decode_predictions
import numpy as np

# class inheritance
from models.SS_model import SS_Model

class SS_Xception(SS_Model):
    def __init__(self):
        super().__init__() # very important

        self.model = Xception(weights='imagenet')

        img_path = 'samples/african_elephant.jpg'
        img = image.load_img(img_path, target_size=(150, 150))
        self.x = image.img_to_array(img)
        self.x = np.expand_dims(self.x, axis=0)
        self.x = preprocess_input(self.x)
    
    def predict(self):
        self.preds = self.model.predict(self.x)

    def correct_result(self):
        # decode the results into a list of tuples (class, description, probability)
        # (one such list for each sample in the batch)
        # print('Predicted:', decode_predictions(preds, top=1)[0])

        expected = 'African_elephant'

        return decode_predictions(self.preds, top=1)[0][0][1] == expected
        