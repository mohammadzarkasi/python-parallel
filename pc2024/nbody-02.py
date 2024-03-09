import numpy as np
import tkinter as tk

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
    # n_objek = len(masses)
    total_gaya = hitung_total_gaya(masses, positions)
    
    percepatan = total_gaya / masses[:, np.newaxis]
    positions_baru = positions + kecepatan * dt + 0.5 * percepatan * dt**2
    
    total_gaya_baru = hitung_total_gaya(masses, positions_baru)
    percepatan_baru = total_gaya_baru / masses[:, np.newaxis]
    
    kecepatan_baru = kecepatan + 0.5 * (percepatan + percepatan_baru) * dt
    
    return positions_baru, kecepatan_baru

# Inisialisasi parameter dan posisi awal
masses = np.array([1000.0, 1000.0, 1000.0])
positions = np.array([[10.0, 10.0], [100.0, 10.0], [10.0, 100.0]])
kecepatan = np.zeros((3, 2))
# print(kecepatan)
# kecepatan = np.array([
#     [1,0],
#     [1,1],
#     [0,1],
# ])
dt = 0.01
dt = 1
n_steps = 1000

# Fungsi untuk menggambar objek pada canvas
def gambar_objek(canvas : tk.Canvas, positions, kecepatan, step):
    canvas.delete("all")
    info = ""
    info2 = ""
    counter = 0
    for posisi in positions:
        v = kecepatan[counter]
        counter += 1
        x, y = posisi
        vx, vy = v
        canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue")
        # canvas.create_text(x+50, y+20, text="x="+str(x) +"\ny="+str(y))
        info_ = str(counter) + ". x=" + str(x) +", y=" + str(y) + "\n"
        info2_ = str(counter) + ". vx=" + str(vx) + ", vy=" + str(vy) + "\n"
        info += info_
        info2 += info2_
    canvas.create_text(350, 10, text=str(step))
    canvas.create_text(200, 300, text=info)
    canvas.create_text(200, 350, text=info2)

# Fungsi untuk melakukan langkah waktu dan memperbarui gambar
def langkah_waktu(canvas: tk.Canvas, positions, kecepatan, dt, step):
    positions, kecepatan = update_posisi_kecepatan(masses, positions, kecepatan, dt)
    gambar_objek(canvas, positions, kecepatan, str(step*dt) + " detik")
    canvas.after(10, langkah_waktu, canvas, positions, kecepatan, dt, step+1)

# Inisialisasi window Tkinter
root = tk.Tk()
root.title("Simulasi Pergerakan Objek")

# Inisialisasi canvas
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Memulai simulasi
langkah_waktu(canvas, positions, kecepatan, dt, 0)

root.mainloop()
