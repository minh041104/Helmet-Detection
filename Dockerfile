FROM python:3.10-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Cài đặt các thư viện hệ thống cần thiết
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Sao chép file yêu cầu và cài đặt các thư viện phụ thuộc
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Chuyển đến thư mục chứa ứng dụng
WORKDIR /app/src/inference

# Mở cổng 8000
EXPOSE 8000

# Chạy ứng dụng
CMD ["python", "app.py"]
