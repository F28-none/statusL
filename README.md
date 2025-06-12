# py_linevim

**py_linevim** adalah plugin statusline Neovim berbasis Python yang menampilkan informasi seperti mode, nama file, posisi kursor, dan status Git branch dengan tampilan yang bisa dikustomisasi.

---

## ✨ Fitur

- Menampilkan mode Neovim (Normal, Insert, dsb) dengan warna yang berbeda
- Menampilkan nama file dan posisi kursor
- Integrasi dengan Git: menampilkan nama dan status branch saat ini
- Tampilan visual dengan simbol dekoratif (ikon, shape kiri/kanan, dll.)
- Warna statusline dapat dikonfigurasi
- Berbasis event (`VimEnter`, `ModeChanged`, dll.)

---

## ⚙️ Instalasi

Gunakan plugin manager **LAZY**
```lua
{'F28-none/py_linevim'}
