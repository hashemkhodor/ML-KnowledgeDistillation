

# Knowledge Distillation in Neural Networks

## Introduction

Knowledge distillation is a technique used to transfer the knowledge from a larger, more complex model (teacher model) to a smaller, simpler model (student model). This method is beneficial for deploying deep learning models in environments where computational resources are limited. By distilling the knowledge of a cumbersome model into a more manageable one, we can achieve comparable performance with significantly reduced computational overhead. This repository provides an implementation of knowledge distillation techniques using neural networks built with Keras.

## Requirements

To run the scripts and notebooks in this repository, you will need:

- Python 3.9 or higher
- Keras

## Setup

Follow these steps to set up your local environment and run the models:

1. **Create a Virtual Environment:**
   ```bash
   python -m venv Venv
   ```
   Activate the virtual environment:
   - Windows:
     ```bash
     .\Venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source Venv/bin/activate
     ```

2. **Install Requirements:**
   Install the required Python packages using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Notebooks:**
   Launch Jupyter Notebook or JupyterLab in your environment:
   ```bash
   jupyter notebook
   ```
   Navigate to the directory containing the notebooks and open them to run the experiments.

# Presentation Link

Access the presentation here: [presentation](https://www.canva.com/design/DAGHDQk5gsc/qSqwTggxset_vPRi-wPDCw/edit).

## Contributions

Contributions to this project are welcome! If you have improvements or bug fixes, please feel free to fork this repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.


