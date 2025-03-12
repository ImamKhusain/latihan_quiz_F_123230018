import streamlit as st

# Soal 1: Field untuk input data diri
st.title("Latihan Kuis 🤩")
st.write("Selamat datang di Latihan Kuis 😎")

# Input data diri
nama = st.text_input("Nama:")
nim = st.text_input("NIM:")
kelas = st.text_input("Kelas:")

# Validasi input
if not nama or not nim or not kelas:
    st.warning("Silakan lengkapi data diri Anda terlebih dahulu.")
else:
    st.subheader("Data Diri Anda:")
    st.write(f"Nama: {nama}")
    st.write(f"NIM: {nim}")
    st.write(f"Kelas: {kelas}")


# Soal 2: Fitur Hitungan Menggunakan Expander

# Fungsi untuk menghitung BMI
def hitung_bmi(berat, tinggi):
    tinggi_m = tinggi / 100
    bmi = berat / (tinggi_m ** 2)
    return bmi

def main():
    st.title("Fitur Aplikasi Akademik")

    # Membuat expander sebagai kotak fitur
    with st.expander("Fitur", expanded=True):
        tab1, tab2 = st.tabs(["📌 Hitung BMI", "📝 Hitung Nilai Akhir"])

        # TAB 1: HITUNG BMI
        with tab1:
            st.subheader("Hitung BMI")
            st.write("Ini fitur untuk menghitung BMI Anda.")

            # Input berat & tinggi
            berat = st.number_input("Masukkan Berat Badan (kg):", min_value=1, max_value=200, value=60)
            tinggi = st.number_input("Masukkan Tinggi Badan (cm):", min_value=50, max_value=250, value=170)

            if st.button("Hitung BMI"):
                bmi = hitung_bmi(berat, tinggi)

                # Kategori BMI
                if bmi < 18.5:
                    kategori = "Underweight (Kurus)"
                    warna = "#FFC107"
                elif 18.5 <= bmi < 24.9:
                    kategori = "Normal (Ideal)"
                    warna = "#4CAF50"
                elif 25 <= bmi < 29.9:
                    kategori = "Overweight (Kelebihan Berat Badan)"
                    warna = "#2196F3"
                else:
                    kategori = "Obesitas"
                    warna = "#F44336"

                # Menampilkan hasil
                st.success(f"Nilai BMI Anda: {bmi:.2f}")
                st.markdown(
                    f"<div style='border-radius:5px;padding:10px;background-color:{warna};color:white;font-weight:bold;text-align:center;padding:10px;'>{kategori}</div>",
                    unsafe_allow_html=True
                )

        # TAB 2: HITUNG NILAI AKHIR
        with tab2:
            st.subheader("Hitung Nilai Akhir")
            st.write("Ini fitur untuk menghitung nilai akhir mahasiswa.")

            # Input nilai
            tugas = st.number_input("Nilai Tugas", min_value=0, max_value=100, value=80)
            uts = st.number_input("Nilai UTS", min_value=0, max_value=100, value=75)
            uas = st.number_input("Nilai UAS", min_value=0, max_value=100, value=85)

            # Tombol hitung
            if st.button("Hitung Nilai Akhir"):
                nilai_akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

                # Menentukan grade
                if nilai_akhir >= 85:
                    grade = "A (Baik)"
                    warna = "#4CAF50"
                elif nilai_akhir >= 75:
                    grade = "B (Cukup)"
                    warna = "#2196F3"
                elif nilai_akhir >= 60:
                    grade = "C (Kurang)"
                    warna = "#FFC107"
                else:
                    grade = "D (Buruk)"
                    warna = "#F44336"

                # Menampilkan hasil
                st.success(f"Nilai Akhir Anda: {nilai_akhir:.2f}")
                st.markdown(
                    f"<div style='border-radius:5px;padding:10px;background-color:{warna};color:white;font-weight:bold;text-align:center;padding:10px;'>{grade}</div>",
                    unsafe_allow_html=True
                )

if __name__ == "__main__":
    main()



