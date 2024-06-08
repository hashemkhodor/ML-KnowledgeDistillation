
# Knowledge Distillation in Neural Networks

## 1. About

### 1.1. Knowledge Distillation
Knowledge Distillation is a technique in machine learning and AI where a smaller model (student) is trained to emulate the behavior of a larger, pre-trained model (teacher). This method is beneficial for deploying deep learning models in environments where computational resources are limited. By distilling the knowledge of a cumbersome model into a more manageable one, we can achieve comparable performance with significantly reduced computational overhead. This project, part of an AI summer school at Texas A&M University in Doha, Qatar, provides an implementation of knowledge distillation techniques using neural networks built with Keras. Much of the inspiration for this project comes from the seminal paper ["Distilling the Knowledge in a Neural Network"](https://arxiv.org/abs/1503.02531).


### 1.2. DataSet and Model
For this project, the CIFAR-10 dataset was employed, using a convolutional neural network. The architecture is based on a model from [this GitHub repository](https://github.com/MelihGulum/CIFAR-10-CNN-FLASK-Deployment/blob/main/CIFAR_10.ipynb). We distilled a large model with 2.2 million parameters into a much smaller model with only 330K parameters.

### 1.3. Results
The following results demonstrate the effectiveness of our knowledge distillation approach:
- **Average Accuracy**:
  - Teacher: 89%
  - Distilled Student: 86%
  - Non-Distilled Student: 79%
- **Average Precision**:
  - Teacher: 89%
  - Distilled Student: 87%
  - Non-Distilled Student: 80%
- **Average Recall**:
  - Teacher: 89%
  - Distilled Student: 86%
  - Non-Distilled Student: 79%

The optimal results were achieved with an alpha value of 0.8.

## 2. Setup

### Requirements
- Python 3.10 or higher
- All necessary libraries are listed in `requirements.txt`

### Commands
- Create a virtual environment named "Venv":
  ```
  python -m venv Venv
  ```
- Activate the virtual environment:
  ```
  source Venv/bin/activate  # On Unix/macOS
  Venv\Scripts\activate  # On Windows
  ```
- Install the required packages:
  ```
  pip install -r requirements.txt
  ```

## 3. Presentation Link
View the detailed presentation of our project [here](https://www.canva.com/design/DAGHDQk5gsc/qSqwTggxset_vPRi-wPDCw/edit?utm_content=DAGHDQk5gsc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton).

## 4. Team
- **Angiero Tani**, Polito - taniangiero@gmail.com
- **Khater Christopher**, AUB - christopherkhater@hotmail.com
- **Khodor Hashem**, AUB - hashemkhoder1@gmail.com
- **Sayfiddinov Mukhammad Ali**, Polito - muhammadalisayfiddinov@gmail.com

