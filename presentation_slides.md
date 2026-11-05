# Silicon Institute of Technology: Summer Internship Presentation

**Course Title:** Python Using Fast Api Internship  
**Project Title:** Patient Visit History Management System  
**Institution:** Silicon Institute of Technology | An Autonomous Institute  
**Guide:** Shashank Shekhar  
**Student Details:**

- Name: NAGRAJ NAG
- Branch: CSE
- SIC. No. : 23BCSC32
- Semester: 7th

---

## Slide 1: Title Slide

- **Course Name:** Python Using Fast Api Internship
- **Mini-Project:** Patient Visit History Management System
- **Under the guidance of:** Shashank Shekhar
- **Submitted by:** Animesh Soumyadarshi | Branch: CSE | SIC. No. : 23BCSC65 | SEMESTER: 7th
- **Institution:** Silicon Institute of Technology | An Autonomous Institute

> **Speaker Notes (Hinglish mein kya bolna hai):**  
> _"Good morning respected professors and evaluators. Today, I am presenting my one-month summer internship on 'Python Using FastAPI', along with the major project I developed: the 'Patient Visit History System'."_

---

## Slide 2: INTRODUCTION

- ▶ This one-month training on Python with FastAPI gave me my first real exposure to backend development and the way modern web APIs are built.
- ▶ Through it, I got hands-on with Python programming, building REST APIs, handling requests and responses, connecting to MySQL databases, and testing APIs.
- ▶ As part of the training, I designed and implemented a Patient Visit History System, which showed me how a backend talks to a database and keeps patient consultation records organized.
- ▶ The project applies industry best practices including Pydantic data validation, SQLAlchemy ORM database abstraction, and live Cloud MySQL persistence with TLS encryption.

> **Speaker Notes (Hinglish mein kya bolna hai):**  
> _"In our introduction, this one-month training gave me practical hands-on exposure to backend engineering. I learned to build REST APIs, handle requests/responses, connect to MySQL, and successfully developed the Patient Visit History System."_

---

## Slide 3: OBJECTIVES

- ▶ To build a solid grounding in Python and the basics of backend development.
- ▶ To get practical experience building REST APIs with FastAPI.
- ▶ To learn how requests are processed, responses are validated, and CRUD operations work.
- ▶ To learn how to connect to a database and write SQL queries in MySQL.
- ▶ To apply API testing, error handling, and debugging in practice.
- ▶ To build a mini-project, the Patient Visit History System, by combining FastAPI with MySQL.

> **Speaker Notes (Hinglish mein kya bolna hai):**  
> _"The objectives of my internship were to build strong Python fundamentals, master FastAPI REST APIs, understand database integration with MySQL, and apply these skills to develop the Patient Visit History System."_

---

## Slide 4: CONTENTS OF THE PROGRAM

- ▶ Over the one-month program, the training moved step by step through Python basics and backend development.
- ▶ Python basics: syntax, data types, functions, and control flow.
- ▶ Core concepts of FastAPI and building REST APIs.
- ▶ Working with HTTP requests and responses, routing, and data validation (Pydantic).
- ▶ CRUD operations and linking the application to a MySQL database (SQLAlchemy ORM & PyMySQL).
- ▶ Mini-project: a complete Patient Visit History System built with Python, FastAPI, and Cloud MySQL.

> **Speaker Notes (Hinglish mein kya bolna hai):**  
> _"The internship program was structured systematically: starting from Python fundamentals, moving to FastAPI routing and validation, database CRUD with MySQL, and culminating in our final mini-project."_

---

## Slide 5: METHODOLOGY — Training Approach & Project Architecture

- **Visual:** Architecture Diagram (`architecture_diagram.png`)
- **Key Points & Execution Flow:**
  - Theory + Practice: Blended conceptual learning with hands-on coding exercises.
  - Environment Setup: Configured Python venv, FastAPI, Uvicorn, and MySQL drivers.
  - Client Request: Postman/Browser sends JSON payload (e.g. `POST /patients/1/visits`).
  - ASGI Processing: Uvicorn asynchronously receives requests and hands to FastAPI.
  - Pydantic Validation: Validates types & age constraints BEFORE touching database.
  - ORM & Cloud MySQL: SQLAlchemy maps models -> PyMySQL executes queries over TLS on TiDB Cloud MySQL.
  - Hydration & Response: ORM hydrates rows; Pydantic serializes JSON with HTTP 201/200.

> **Speaker Notes (Hinglish mein kya bolna hai):**  
> _"In our methodology, the program blended theory with hands-on exercises. The architecture diagram on the left illustrates how client requests pass through Uvicorn, FastAPI routing, Pydantic validation, SQLAlchemy ORM, and encrypted cloud MySQL persistence."_

---

## Slide 6: METHODOLOGY — Database Design (Entity-Relationship Model)

- **Visual:** ER Diagram (`er_diagram.png`)
- **Relational Model & Cascade Rules:**
  - 1-to-Many Relationship: One Patient has many consultation Visits (1 : N). Each visit record belongs strictly to one Patient.
  - `PATIENTS` Table: Stores core demographic details (id PK, name, age, gender, contact_number, address, created_at).
  - `VISITS` Table: Stores clinical data (id PK, patient_id FK, visit_date, doctor_name, diagnosis, prescription, created_at).
  - Foreign Key Constraint: `visits.patient_id` references `patients.id` to maintain referential integrity.
  - `ON DELETE CASCADE`: When a patient record is deleted, all their associated medical visits are automatically removed, preventing orphaned records.
  - SQLAlchemy Modeling: Implemented via `cascade='all, delete-orphan'` at the ORM layer and foreign key at MySQL DDL level.

> **Speaker Notes (Hinglish mein kya bolna hai):**  
> _"Sir, this is our database ER model. There is a 1-to-Many relationship between Patients and Visits. We configured 'ON DELETE CASCADE' on the foreign key to ensure complete referential integrity."_

---

## Slide 7: Projects Done — Patient Visit History System

- **Project Overview:**
  - Built a backend application in Python with FastAPI for storing and retrieving patient visit records quickly.
  - Designed REST API endpoints that return a patient's details along with their visit history, giving organized access to visit information.
  - Used MySQL to store patient data and wrote SQL queries to look up records by patient ID.
  - Added request handling, data validation, and error handling so the API and database communicate reliably.
- **Implemented REST API Endpoints & Verification:**
  - Patient Management: `POST /patients` (Create), `GET /patients` (List), `GET /patients/{id}` (Nested Visits), `PUT`, `DELETE`.
  - Visit History: `POST /patients/{id}/visits` (Add Visit), `GET /patients/{id}/visits`, `GET /visits/{id}`, `PUT`, `DELETE`.
  - Verification: 100% pass rate in Swagger UI (`http://127.0.0.1:8000/docs`) and Postman with standard HTTP status codes (`201`, `200`, `404`, `422`).

> **Speaker Notes (Hinglish mein kya bolna hai):**  
> _"Under Projects Done, I built the Patient Visit History System combining FastAPI and MySQL. All 9 endpoints were implemented and verified with proper request validation, error handling, and status codes."_

---

## Slide 8: CONCLUSION

- This one-month training in Python and FastAPI strengthened both my technical knowledge and my coding skills. I learned to build REST APIs, work with MySQL databases, and test and debug APIs.
- It gave me a firm base in backend development and a clearer picture of how real-world applications are designed and built. I now feel ready to take on bigger software development challenges and create efficient, dependable applications.
- **Key Takeaways from the Internship:**
  - Practical mastery over modern backend API development using FastAPI and asynchronous Python.
  - Hands-on experience with Relational Database Modeling and Cloud MySQL (TiDB Serverless).
  - Professional API documentation, testing, and debugging using Swagger UI and Postman.
  - Confidence to architect scalable, full-stack enterprise solutions.

> **Speaker Notes (Hinglish mein kya bolna hai):**  
> _"In conclusion, this one-month training gave me a firm foundation in backend engineering. I am confident in building scalable REST APIs and handling database integrations. Thank you!"_

---

## Slide 9: THANK YOU

- **THANK YOU**
- Questions & Answers
