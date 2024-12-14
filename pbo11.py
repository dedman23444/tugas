import pandas as pd
from collections import Counter

# Fungsi untuk menghitung probabilitas Naive Bayes
def naive_bayes(data, labels):
    # Menghitung jumlah total data
    total_count = len(data)
    
    # Menghitung frekuensi setiap kelas
    class_counts = Counter(labels)
    
    # Menghitung probabilitas prior untuk setiap kelas
    prior_prob = {cls: count / total_count for cls, count in class_counts.items()}
    
    # Menghitung probabilitas likelihood
    likelihood = {}
    for cls in class_counts:
        likelihood[cls] = {}
        subset = [data[i] for i in range(total_count) if labels[i] == cls]
        for feature in subset:
            if feature in likelihood[cls]:
                likelihood[cls][feature] += 1
            else:
                likelihood[cls][feature] = 1
    
    # Menghitung probabilitas posterior
    posterior_prob = {}
    for cls in class_counts:
        posterior_prob[cls] = prior_prob[cls]
        for feature in data:
            posterior_prob[cls] *= (likelihood[cls].get(feature, 0) + 1) / (class_counts[cls] + len(likelihood[cls]))
    
    return posterior_prob

# Inisialisasi list untuk menyimpan data dan label
data = []
labels = []

while True:
    # Meminta input dari pengguna
    user_input = input("Masukkan data (atau ketik 'exit' untuk keluar): ")
    
    # Memeriksa apakah pengguna ingin keluar
    if user_input.lower() == 'exit':
        break
    
    # Meminta label untuk data yang dimasukkan
    label = input("Masukkan label untuk data tersebut: ")
    
    # Menambahkan input ke dalam list
    data.append(user_input)
    labels.append(label)

# Menghitung probabilitas menggunakan Naive Bayes
posterior_prob = naive_bayes(data, labels)

# Menentukan kelas dengan probabilitas tertinggi (modus)
predicted_class = max(posterior_prob, key=posterior_prob.get)

# Menampilkan hasil
print("Probabilitas Posterior:")
print(posterior_prob)
print(f"Kelas yang diprediksi: {predicted_class}")
import pandas as pd
from collections import Counter

# Fungsi untuk menghitung probabilitas Naive Bayes
def naive_bayes(data, labels):
    # Menghitung jumlah total data
    total_count = len(data)
    
    # Menghitung frekuensi setiap kelas
    class_counts = Counter(labels)
    
    # Menghitung probabilitas prior untuk setiap kelas
    prior_prob = {cls: count / total_count for cls, count in class_counts.items()}
    
    # Menghitung probabilitas likelihood
    likelihood = {}
    for cls in class_counts:
        likelihood[cls] = {}
        subset = [data[i] for i in range(total_count) if labels[i] == cls]
        for feature in subset:
            if feature in likelihood[cls]:
                likelihood[cls][feature] += 1
            else:
                likelihood[cls][feature] = 1
    
    # Menghitung probabilitas posterior
    posterior_prob = {}
    for cls in class_counts:
        posterior_prob[cls] = prior_prob[cls]
        for feature in data:
            posterior_prob[cls] *= (likelihood[cls].get(feature, 0) + 1) / (class_counts[cls] + len(likelihood[cls]))
    
    return posterior_prob

# Inisialisasi list untuk menyimpan data dan label
data = []
labels = []

while True:
    # Meminta input dari pengguna
    user_input = input("Masukkan data (atau ketik 'exit' untuk keluar): ")
    
    # Memeriksa apakah pengguna ingin keluar
    if user_input.lower() == 'exit':
        break
    
    # Meminta label untuk data yang dimasukkan
    label = input("Masukkan label untuk data tersebut: ")
    
    # Menambahkan input ke dalam list
    data.append(user_input)
    labels.append(label)

# Menghitung probabilitas menggunakan Naive Bayes
posterior_prob = naive_bayes(data, labels)

# Menentukan kelas dengan probabilitas tertinggi (modus)
predicted_class = max(posterior_prob, key=posterior_prob.get)

# Menampilkan hasil
print("Probabilitas Posterior:")
print(posterior_prob)
print(f"Kelas yang diprediksi: {predicted_class}")