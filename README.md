<div align="center">

# ⌚ Joybasket

**A Django-powered online watch shop, currently under construction.**

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.x-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=for-the-badge)

</div>

---

## 📖 About

Joybasket started from the BootstrapMade **LeadPage** template and is being turned into a watch-selling website. The template pages are wired into Django, the contact form saves to a database, and the shop features (products, categories, ordering) are coming next.

> 🚧 **Work in progress.** Some page content is still template placeholder text and will be replaced.

## 📑 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Pages and URLs](#-pages-and-urls)
- [Viewing Contact Messages](#-viewing-contact-messages)
- [Project Structure](#-project-structure)
- [Roadmap](#-roadmap)
- [Notes](#-notes)
- [Credits](#-credits)

## ✨ Features

- 🏠 Responsive landing page served through Django
- 📄 Starter, service details and portfolio details pages
- 📬 Contact form that saves every submission to the database
- 🛠️ Contacts viewable and manageable in the Django admin
- 📰 Newsletter signup form *(currently prints to the terminal, not saved yet)*
- 🗄️ SQLite database for local development

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Framework | Django 6 |
| Database | SQLite |
| Front end | HTML, CSS, JavaScript, Bootstrap |

## 🚀 Getting Started

**1. Clone the repository**

```bash
git clone <repository-url>
cd Joybasket
```

**2. Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install Django**

```bash
pip install django
```

**4. Create the database tables**

```bash
python manage.py migrate
```

**5. Create an admin user**

```bash
python manage.py createsuperuser
```

**6. Run the development server**

```bash
python manage.py runserver
```

Then open **http://127.0.0.1:8000/** in your browser. 🎉

## 🔗 Pages and URLs

| URL | Page |
|---|---|
| `/` | Homepage |
| `/starter/` | Starter page |
| `/services/` | Service details |
|
