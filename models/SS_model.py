from abc import ABC, abstractmethod
import random
import os
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

class InitMeta(type):
    def __call__(cls, *args, **kwargs):
        if cls is SS_Model:
            raise TypeError(f"Can't instantiate abstract class {cls.__name__}")
        instance = super().__call__(*args, **kwargs)
        if not hasattr(instance, '__init__') or instance.__init__ == SS_Model.__init__:
            raise NotImplementedError(f"Subclass {cls.__name__} must implement its own __init__ method.")
        return instance

class SS_Model(ABC):
    @abstractmethod
    def predict(self):
        pass

    def get_metrics(self, debug=False):
        pc = []
        tc = []
        ntc = []
        # Extract data [(pc, tc, ntc), ...]
        for tuple in self.classes_predicted:
            _pc, _tc, _ntc = zip(tuple)
            pc.append(_pc)
            tc.append(_tc)
            ntc.append(_ntc)

        # Compute accuracy
        accuracy = accuracy_score(tc, pc)

        # Compute precision, recall, and F1-score
        precision = precision_score(tc, pc, average='weighted')
        recall = recall_score(tc, pc, average='weighted')
        f1 = f1_score(tc, pc, average='weighted')

        # Classification report
        class_report = classification_report(tc, pc)

        # Confusion matrix
        conf_matrix = confusion_matrix(tc, pc)

        if debug:
            # Display metrics
            print(f"Accuracy: {accuracy}")
            print(f"Precision: {precision}")
            print(f"Recall: {recall}")
            print(f"F1-score: {f1}")
            print(f"Classification Report:\n{class_report}")
            print(f"Confusion Matrix:\n{conf_matrix}")

        return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}

    def select_test_data(debug=False):
        # Define the dataset folder path
        dataset_folder = 'dataset'

        # Retrieve the list of folders inside the dataset folder that start with 'n'
        folders = [folder for folder in os.listdir(dataset_folder) if folder.startswith('n') and os.path.isdir(os.path.join(dataset_folder, folder))]

        # Define the number of files you want to randomly select
        num_files_to_select = 20

        # List to store the tuples with file paths and folder names
        selected_files = []

        # Iterate through each folder, select random files, and save their paths along with folder names
        while len(selected_files) < num_files_to_select:
            n_files = random.randrange(0, min((num_files_to_select - len(selected_files)),5))
            if n_files == 0:
                n_files += 1
            
            folder = folders[random.randrange(0,len(folders))]
            folder_path = os.path.join(dataset_folder, folder)
            files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.lower().endswith('.jpeg')]
            selected_files.extend([(file, folder) for file in random.sample(files, n_files)])

        # if debug:
        #     # Print the selected file paths and their respective folder names
        #     for file_path, folder_name in selected_files:
        #         print(f"File: {file_path}, Class: {folder_name}")
        
        return selected_files