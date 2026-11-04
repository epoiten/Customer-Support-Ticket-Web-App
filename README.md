# MedTech Support Desk — Clinical & Medical Device Support Ticket Web App

## Course Information

* **Institution:** Digital4Business (D4B) Professional Master’s in Advanced Digital Technologies for Business

* **Course:** Business Programming (September 2026 Edition)

* **Selected Project Option:** Option A – Customer Support Ticket Web App

* **Submitted To:** Professor José Américo Rio

## Project Team & Roles

* **Roner Lamadrid Chichirita** — Backend Engineering, Database Schema & Flask Routing

* **Linda** — Front-End Architecture, Responsive UI/UX Styling & Template Design

* **Franz** — Client-Side JavaScript Validation, Interactive Character Counter & Quality Assurance Testing

## Overview & Business Problem

In acute hospital environments (surgical wards and intensive care units), medical device malfunctions—such as infusion pump occlusion alarms, vital monitor sensor faults, or electronic health record (EHR) workstation glitches—are frequently reported via unstructured phone calls, paper slips, or fragmented messaging apps. This leads to delayed biomedical engineering triage, lost fault records, and heightened patient safety risks.

The **MedTech Support Desk** is a lightweight, responsive Python/Flask web application designed to centralize incident reporting and tracking. It enables nursing and clinical staff to log equipment faults, monitor repair triage states (`Open`, `In Progress`, `Resolved`), update clinical notes, and securely manage or delete records, ensuring clinical engineering teams maintain full auditability over ward technology.

## Features & Minimum Functionality

* **Service Overview Page (`/`):** Introduces the biomedical helpdesk and displays live aggregate statistics of total logged incidents and active repairs.

* **Incident Creation Form (`/tickets/new`):** Structured form capturing staff identity/ward, hospital email, device asset subject, and detailed fault descriptions.

* **Persistent Storage (`tickets.db`):** Relational SQLite database managed via Peewee ORM using a single `Ticket` table as specified in the project guidelines.

* **Ticket Queue & Filtering (`/tickets`):** A responsive tabular view displaying all submitted incidents with color-coded status badges.

* **Detail & CRUD Operations:** Full capability to view individual ticket details, edit information/status, and securely delete records with a JavaScript confirmation dialog.

* **Interactive Client-Side Features:** Vanilla JavaScript live character counter (500-character limit) and comprehensive form validation before submission.

* **Project Report & About Page (`/about`):** Embedded short report summarizing project metadata, testing evidence, limitations, and the AI-use statement.

## Technology Stack

* **Backend:** Python 3.12, Flask Web Framework

* **Database / ORM:** SQLite, Peewee ORM

* **Frontend:** HTML5 (Jinja2 templates), CSS3 (responsive grid & mobile breakpoints)

* **Client-Side:** Vanilla JavaScript (Form validation & live character counting)

* **Development Environment:** Visual Studio Code (VS Code)

## Step-by-Step Instructions to Run in VS Code

1. **Clone or Download** the project folder (`Customer-Support-Ticket-Web-App`) and open it in **Visual Studio Code**.

2. **Open the Terminal** in VS Code (`Terminal -> New Terminal`).

3. **Install Dependencies** (Flask and Peewee):

   ```
   pip install flask peewee
   
   ```

4. **Run the Application:**

   * Open `app.py` in VS Code and click the **Run Python File (Play)** button in the top-right corner, OR type the following command in your terminal:

     ```
     python app.py
     
     ```

5. **Access the Web App:**

   * Open your web browser and navigate to:
     `http://127.0.0.1:5000`

## Project Structure

```
customer_support_app/
├── app.py                  # Main Flask application & Peewee database models
├── tickets.db              # SQLite database (auto-generated on startup)
├── README.md               # Project documentation & run instructions
├── static/
│   ├── style.css           # Responsive CSS stylesheet
│   └── script.js           # JavaScript form validation & character counter
└── templates/
    ├── base.html           # Shared layout, navigation bar, & footer
    ├── index.html          # Service overview page & live statistics
    ├── tickets.html        # Ticket queue list table
    ├── create.html         # Form to log a new incident ticket
    ├── detail.html         # Individual ticket detail view
    ├── edit.html           # Form to update ticket details & status
    └── about.html          # Embedded project short report & team info

```