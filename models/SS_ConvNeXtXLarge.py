from keras.applications.convnext import ConvNeXtXLarge
from keras.preprocessing import image
from keras.applications.convnext import preprocess_input, decode_predictions
import numpy as np

# class inheritance
from models.SS_model import SS_Model

class SS_ConvNeXtXLarge(SS_Model):
    def __init__(self):
        super().__init__() # very important

        self.model = ConvNeXtXLarge(weights='imagenet')

        # Select random samples from dataset
        self.selected_files = self.select_test_data()

        # Create prediction array
        self.classes_predicted = []
            
    def predict(self):
        for file in self.selected_files:
            img = image.load_img(file[0], target_size=(224, 224))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            
            preds = self.model.predict(x)
            d_preds = decode_predictions(preds, top=1)[0][0]
            class_pred = d_preds[0]
            name_pred = d_preds[1]
            
            self.classes_predicted.append((class_pred,file[1],name_pred))
            
            # # debug
            # print((class_pred,file[1],name_pred))