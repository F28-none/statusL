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
```
## Default Config
```lua
vim.fn.Py_line_config({
    file_bg = '#e0601b', -- baground color file
    pipe= '••', -- baground color file
    branch_bg = '#1b70e0',-- baground color file
    --mode baground harus tabel lua
    mode_bg = {
        ['\x16']= '#e01b3c', -- for visual block mode
        n = '#09e644', -- for normal mode
        i = '#82e609',-- for insert mode
        v = '#09e6bd',-- for visual mode
        V = '#e609cf',-- for visual line mode
        c = '#e62709',-- for command mode
        R = '#e62709',-- for replace mode
        t = '#1b53e0',-- for terminal mode
    },
})
