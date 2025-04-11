# Jewelry Product Normalizer

A full-stack app to normalize jewelry product data from multiple manufacturers (CSV/XLSX) and output WooCommerce-ready CSV files. Built with FastAPI + React, deployable via Docker or DigitalOcean App Platform.

---

## 🚀 Features
- Upload files with mismatched vendor formats
- Map fields to WooCommerce schema
- Download clean CSV for import
- Frontend: Drag-and-drop uploader
- Backend: FastAPI for normalization
- Nginx for static file routing

---

## 📦 Quick Start (Local)
```bash
git clone https://github.com/your-repo/normalize-jewelry
cd normalize-jewelry
docker-compose up --build
```

Visit: `http://localhost`

---

## 🌐 Deploy to DigitalOcean App Platform
1. Push this repo to GitHub
2. Create App in DigitalOcean → connect GitHub repo
3. Use Dockerfile as the build source
4. Add a static route: `/static → ./static`
5. Enable HTTPS and custom domain (optional)

---

## 📁 File Structure
```
├── main.py               # FastAPI backend
├── normalize_jewelry_data.py  # Normalization logic (add this file)
├── static/               # Output CSV storage
├── frontend/             # React uploader component
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
├── requirements.txt
└── .gitignore
```

---

## ✍️ Author
Built by [Your Name / Team] — Jewelry Tech Solutions

---

## 📬 License
MIT License
