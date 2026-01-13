# Kea – Inventory Management System

[![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.16-A30000?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)

**Kea** is a professional backend inventory management system designed for small to medium-sized businesses. It provides a robust set of APIs to manage categories, items, pricing, and stock transactions with built-in reporting.

---

## 🚀 Features

- **Hierarchical Categories**: Organize items in a structured manner.
- **Stock Management**: Track stock levels (IN/OUT) with automatic balance calculations.
- **Dynamic Pricing**: Manage item pricing over time.
- **Comprehensive Reporting**:
  - Item lists with real-time balances.
  - Full transaction ledger.
  - Stock levels by specific dates.
- **Built-in API Documentation**: Interactive Swagger and Redoc interfaces.

---

## 🛠️ Tech Stack

- **Framework**: Django 6.0 & Django REST Framework
- **Database**: SQLite (Default) | MySQL / PostgreSQL supported
- **Auth**: JWT (JSON Web Token)

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.10+
- `pip` or `pipenv`

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/natnael-mata/Kea_Inventory.git
   cd Kea_Inventory
   ```

2. **Setup Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory (see `.env.example`).
   ```bash
   DEBUG=True
   SECRET_KEY=your-secret-key
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

---

## 📖 API Documentation

Once the server is running, you can access the interactive documentation at:

- **Swagger UI**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) (Mapped to root for convenience)
- **Redoc**: [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)
- **Schema (YAML)**: [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

Please refer to [COMMIT_CONVENTIONS.md](./COMMIT_CONVENTIONS.md) for commit message guidelines.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👤 Author

**Natnael Samuel** - [GitHub](https://github.com/natnael-mata)
