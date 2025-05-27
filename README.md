# 🤖 CI/CD Cho AI Với GitHub Actions & AI Agent

Đây là một dự án demo minh hoạ cách thiết lập quy trình **CI/CD cho mô hình AI** sử dụng **GitHub Actions**, đồng thời tích hợp một **AI Agent** để tự động chọn mô hình tốt nhất dựa trên kết quả huấn luyện từ MLflow.

---

## 🎯 Mục tiêu

* Hiểu vai trò của CI/CD trong phát triển AI.
* Tự động hóa việc test, train, đánh giá mô hình bằng GitHub Actions.
* Sử dụng AI Agent để phân tích metric và chọn mô hình tốt nhất để deploy.

---

## 📁 Cấu trúc thư mục dự án

```
ai-cicd-pipeline/
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml           # Pipeline CI/CD với GitHub Actions
├── agents/
│   └── model_selector_agent.py       # AI Agent chọn mô hình tốt nhất
├── train.py                          # Script huấn luyện mô hình
├── test_model.py                     # File test đơn giản
├── requirements.txt                  # Thư viện phụ thuộc
├── README.md                         # Mô tả dự án
└── model_to_deploy.txt               # (tùy chọn) Kết quả chọn model
```

---

## ⚙️ Cách hoạt động

1. Mỗi lần **push code lên branch `main`**
2. GitHub Actions sẽ:

   * Cài thư viện cần thiết.
   * Chạy `test_model.py`
   * Chạy `train.py` để huấn luyện và log kết quả vào MLflow
   * Chạy `model_selector_agent.py` để chọn mô hình tốt nhất

---

## 🚀 Hướng dẫn chạy thủ công (local)

1. Cài đặt thư viện:

```bash
pip install -r requirements.txt
```

2. Chạy test:

```bash
python test_model.py
```

3. Huấn luyện và log mô hình:

```bash
python train.py
```

4. AI Agent chọn model tốt nhất:

```bash
python agents/model_selector_agent.py
```

---

## 📦 Yêu cầu

* Python >= 3.10
* `mlflow`, `pandas`

---

## 🧠 Ghi chú mở rộng

* Kết quả MLflow được lưu trong thư mục `mlruns/`
* Có thể chạy `mlflow ui` để xem metric trực quan:

```bash
mlflow ui
```

---

## 🏁 Kết quả mong đợi

> Mỗi lần push code mới, pipeline CI/CD sẽ tự động chạy và AI Agent sẽ chọn mô hình có độ chính xác cao nhất dựa trên log từ MLflow.

---

Tài liệu học MLOps thực chiến ✨
