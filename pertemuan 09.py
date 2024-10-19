# Dewo dzaki_2409076022
# Judul program : "Program menentukan Umur pengguna"
print('=' *36 )
print("MASUKAN DATA SESUAI AKTE KELAHIRAN!") # Judul program
print("contoh: 22/09/2004") # Format contoh input data 
print('-' *36 )

a = int (input("tanggal lahir mu: ")) # Input data pengguna
b = int (input("bulan lahir mu  : ")) # Input data pengguna
c = int (input("Tahun lahir mu  : ")) # Input data pengguna

print('-' *36 )
print(a,b,c) # Print hasil input pengguna
hasil = 2024 - c # Menghitung umur berdasarkan input dari pengguna
print("UMURMU SEKARANG: ", hasil) # Menampilkan hasil proses dari program

if hasil <= 18: # "if":adalah percabangan yang menyatakan kondisi "true", jika hasil menunjukan <= 18 maka akan menamilkan pesan-pesan dibawah ini
   print('-' *36 ) # jika hasil menunjukan <= 18 maka akan menamilkan pesan-pesan ini
   print("Kamu masih Remaja") # jika hasil menunjukan <= 18 maka akan menamilkan pesan-pesan ini
   print("Umurmu masih muda kawan gunakan waktu sebaik-baiknya") # jika hasil menunjukan <= 18 maka akan menamilkan pesan-pesan ini
   print('=' *36 ) # jika hasil menunjukan <= 18 maka akan menamilkan pesan-pesan ini

elif hasil <= 40 : # "elif" : adalah percabangan yang menyatakan kondisi "false", jika hasil menunjukan <= 40 maka akan menamilkan pesan-pesan dibawah ini
   print('-' *36 ) # jika hasil menunjukan <= 40 maka akan menamilkan pesan-pesan ini
   print("Kau telah Dewasa")# jika hasil menunjukan <= 40 maka akan menamilkan pesan-pesan ini
   print("Bersikaplah bagaikan orang dewasa, Saling terima dan memaafkan")# jika hasil menunjukan <= 40 maka akan menamilkan pesan-pesan ini
   print('=' *36 ) # jika hasil menunjukan <= 40 maka akan menamilkan pesan-pesan ini

else: # "else" : adalah opsi percabangan yang menyatakan kondis alternatif, jika hasil menunjukan >= 40 maka akan menamilkan pesan-pesan dibawah ini
   print('-' *36 ) # jika hasil menunjukan >= 40 maka akan menamilkan pesan-pesan dibawah ini
   print("Kamu sudah Lansia kawan") # jika hasil menunjukan >= 40 maka akan menamilkan pesan-pesan dibawah ini
   print("Gunakan sisa usiamu dengan memperbanyak waktu dengan keluarga") # jika hasil menunjukan >= 40 maka akan menamilkan pesan-pesan dibawah ini
   print('=' *36 ) # jika hasil menunjukan >= 40 maka akan menamilkan pesan-pesan dibawah ini
