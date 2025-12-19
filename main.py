# from flask import Flask, render_template

# # Membuat instance (objek) aplikasi Flask
# # __name__ adalah variabel Python yang memberikan nama modul
# app = Flask(__name__)

# # Ini adalah 'route' (rute)
# # Ini memberi tahu Flask URL apa yang harus memicu fungsi di bawahnya
# @app.route('/')
# def hello_world():
#     name = 'Ardhi'
#     # Fungsi ini akan dieksekusi ketika pengguna mengakses URL dasar (/)
#     return render_template('Beranda.html', name=name, fluskL='flusk')

# @app.route('/TebakUsia', methods=['GET', 'POST'])
# def TebakUsia():
#     if request.method == 'POST':
#         tahun_lahir = int(request.form['tahun'])
#         tahun_sekarang = 2024
#         usia = tahun_sekarang - tahun_lahir
#         return render_template('cek_usia.html', usia=usia)        
#     return render_template('TebakUsia.html', usia=none)    

# @app.route('/Gplan')
# def Gplan():
#     return '<h1>Ini Halaman Gplan</h1> <br/> <a href="/">Kembali Ke Beranda<a/>'     

# @app.route('/About')
# def About():
#     return '<h1>Ini Halaman About</h1> <br/> <a href="/">Kembali Ke Beranda<a/>'    

# # Untuk menjalankan aplikasi
# if __name__ == '__main__':
#     # debug=True memungkinkan server untuk me-reload secara otomatis
#     # ketika Anda membuat perubahan pada kode.
#     app.run(debug=True)


from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)