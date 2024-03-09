import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung gaya gravitasi antara dua objek
def hitung_gaya_gravitasi(m1, m2, posisi1, posisi2, G=6.67430e-11):
    jarak = posisi2 - posisi1
    jarak_kuadrat = np.dot(jarak, jarak)
    
    if jarak_kuadrat == 0:
        return np.array([0, 0])
    
    gaya = G * m1 * m2 / jarak_kuadrat
    gaya_vektor = gaya * (jarak / np.sqrt(jarak_kuadrat))
    
    return gaya_vektor

# Fungsi untuk menghitung total gaya yang bekerja pada setiap objek dalam sistem
def hitung_total_gaya(masses, positions):
    n_objek = len(masses)
    total_gaya = np.zeros((n_objek, 2))
    
    for i in range(n_objek):
        for j in range(n_objek):
            if i != j:
                gaya_ij = hitung_gaya_gravitasi(masses[i], masses[j], positions[i], positions[j])
                total_gaya[i] += gaya_ij
    
    return total_gaya

# Fungsi untuk mengupdate posisi dan kecepatan menggunakan metode Verlet
def update_posisi_kecepatan(masses, positions, kecepatan, dt):
    n_objek = len(masses)
    total_gaya = hitung_total_gaya(masses, positions)
    
    percepatan = total_gaya / masses[:, np.newaxis]
    positions_baru = positions + kecepatan * dt + 0.5 * percepatan * dt**2
    
    total_gaya_baru = hitung_total_gaya(masses, positions_baru)
    percepatan_baru = total_gaya_baru / masses[:, np.newaxis]
    
    kecepatan_baru = kecepatan + 0.5 * (percepatan + percepatan_baru) * dt
    
    return positions_baru, kecepatan_baru

# Inisialisasi parameter dan posisi awal
masses = np.array([1.0, 1.0, 1.0])
positions = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
kecepatan = np.zeros((3, 2))
dt = 0.01
n_steps = 1000

# Inisialisasi plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal', 'box')

# Simulasi pergerakan objek dan plot hasilnya
for step in range(n_steps):
    positions, kecepatan = update_posisi_kecepatan(masses, positions, kecepatan, dt)
    ax.clear()
    ax.scatter(positions[:, 0], positions[:, 1])
    ax.set_title(f'Langkah waktu: {step+1}')
    plt.pause(0.01)

plt.show()
