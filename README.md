# py_linevim
![Screenshot Statusline](./img/Picsart_25-06-14_13-55-53-067.jpg)
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
{'F28-none/py_linevim',
    build='UpdateRemotePlugins'
}
```
## Default Config
this is an example configuration
```lua
vim.fn.Py_line_config({
--     icon_mode = '#', -- icon for mode 
--     border_left = '∆', -- icon for border_left
--     border_right = '§', -- icon for border_right
--     icon_branch = '', -- icon for branch
--     icon_file = '#', -- icon for file 
--     file_bg = '#e0601b', -- baground for file section
--     separator = '•', -- icon for separator
--     branch_bg = '#1b70e0',-- baground for branch section
    mode_bg = {
       Normal='#6f03fc',
       Insert='#000000',
       Visual='#888888',
       VisualLine='#888888',
       VisualBlock='#888888',
       Command='#000000',
       Replace='#888888',
       Terminal='#888888',
       Select='#888888',
    },
})
