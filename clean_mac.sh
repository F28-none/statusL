#!/bin/bash

echo "🔧 Menghapus Xcode..."
sudo rm -rf /Applications/Xcode.app
sudo rm -rf /Library/Developer/CommandLineTools
sudo rm -rf ~/Library/Developer
sudo rm -rf /Library/Developer
rm -rf ~/Library/Caches/com.apple.dt.Xcode
rm -rf ~/Library/Developer/Xcode/DerivedData
rm -rf ~/Library/Developer/CoreSimulator

echo "🍺 Menghapus Homebrew..."
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"

echo "🧹 Menghapus sisa Homebrew..."
sudo rm -rf /usr/local/Homebrew
sudo rm -rf /usr/local/Caskroom
sudo rm -rf /usr/local/bin/brew
sudo rm -rf /opt/homebrew
rm -rf ~/Library/Caches/Homebrew
rm -rf ~/Library/Logs/Homebrew

echo "✅ Pengecekan akhir..."
echo "Cek brew: $(which brew)"
echo "Cek Xcode path: $(xcode-select -p 2>/dev/null || echo 'Tidak ditemukan')"

echo "🚀 Pembersihan selesai!"

