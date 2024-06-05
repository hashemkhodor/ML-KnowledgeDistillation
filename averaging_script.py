import os
import json
import numpy as np
import matplotlib.pyplot as plt
import argparse

def load_data(directory, folder_prefix, start, end):
    val_accuracies = []
    filename = "history.json"
    for i in range(start, end + 1):
        foldername = f"{folder_prefix}-{i}"
        file_path = os.path.join(directory, foldername, filename)
        with open(file_path, 'r') as file:
            data = json.load(file)
            val_accuracies.append(data['val_accuracy'])
    return np.array(val_accuracies)

def compute_averages(data):
    return np.mean(data, axis=0)

def save_averages(averages, output_filename):
    with open(output_filename, 'w') as file:
        for index, value in enumerate(averages):
            file.write(f"Index {index}: {value}\n")

def plot_averages(averages, plot_filename):
    plt.figure(figsize=(10, 5))
    plt.plot(averages, marker='o', linestyle='-', color='b')
    plt.title('Index-wise Averages of Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Average Validation Accuracy')
    plt.grid(True)
    plt.savefig(plot_filename)
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Process JSON data for validation accuracy.')
    parser.add_argument('--directory', type=str, required=True, help='Directory containing the JSON files')
    parser.add_argument('--folder_prefix', type=str, required=True, help='Prefix of the folder names')
    parser.add_argument('--start', type=int, required=True, help='Start index of the folders')
    parser.add_argument('--end', type=int, required=True, help='End index of the folders')
    args = parser.parse_args()

    data = load_data(args.directory, args.folder_prefix, args.start, args.end)
    averages = compute_averages(data)
    output_filename = "average_val_accuracy.txt"
    plot_filename = "average_val_accuracy_plot.png"

    save_averages(averages, output_filename)
    print(f"Index-wise averages of val_accuracy saved to {output_filename}")
    plot_averages(averages, plot_filename)

if __name__ == "__main__":
    main()
