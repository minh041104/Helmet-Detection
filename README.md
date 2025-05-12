# 🪖 Helmet Detection

Ứng dụng phát hiện người đội mũ bảo hiểm trong hình ảnh và video, sử dụng mô hình huấn luyện trên Roboflow và giao diện Gradio thân thiện với người dùng.

---

## 🚀 Tính năng

- 📸 Phát hiện mũ bảo hiểm trong **ảnh**
- 🎥 Phát hiện mũ bảo hiểm trong **video**
- ✅ Giao diện dễ dùng, chạy trực tiếp bằng trình duyệt
- ⚙️ Dễ dàng cấu hình với file `config.yaml`

---

## ⚙️ Cài đặt và chạy

### 1. Tạo môi trường ảo và cài đặt thư viện

```bash
git clone https://github.com/minh041104/Helmet-Detection.git
cd Helmet-Detection
pip install -r requirements.txt
```

### 2. Cấu hình Roboflow trong config.yaml

### 3. Chạy ứng dụng
```bash
cd .\src\inference\
python run.py
