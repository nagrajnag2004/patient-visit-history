import os
import io
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_silicon_deck():
    template_path = r"C:\Users\nagra\.gemini\antigravity\brain\cd5112b8-2b8b-4867-bcda-98e7404bb232\.user_uploaded\media_1793871599475_be970003.pptx"
    prs = Presentation(template_path)

    NAVY = RGBColor(26, 35, 126)       # Deep Silicon Blue
    BLUE = RGBColor(13, 71, 161)       # Medium Blue
    TEXT_DARK = RGBColor(33, 37, 41)    # Dark Charcoal
    GREEN = RGBColor(16, 185, 129)     # Success Green
    BORDER_COLOR = RGBColor(226, 232, 240)
    CARD_BG = RGBColor(255, 255, 255)

    # Extract logo blob from slide 2
    logo_blob = prs.slides[1].shapes[3].image.blob

    # -------------------------------------------------------------
    # SLIDE 1: Title Slide
    # -------------------------------------------------------------
    s1 = prs.slides[0]
    s1.shapes[0].text_frame.clear()
    p1 = s1.shapes[0].text_frame.paragraphs[0]
    p1.text = "Patient Visit History Management System"
    p1.font.size = Pt(28)
    p1.font.bold = True
    p1.font.color.rgb = NAVY

    p1_sub = s1.shapes[0].text_frame.add_paragraph()
    p1_sub.text = "Summer Internship & Training | Python, FastAPI & Cloud MySQL"
    p1_sub.font.size = Pt(16)
    p1_sub.font.color.rgb = BLUE
    p1_sub.font.bold = True

    s1.shapes[2].text_frame.clear()
    p2 = s1.shapes[2].text_frame.paragraphs[0]
    p2.text = "Under the guidance of:"
    p2.font.bold = True
    p2.font.size = Pt(14)
    p2.font.color.rgb = NAVY
    p2_sub = s1.shapes[2].text_frame.add_paragraph()
    p2_sub.text = "Faculty / Industry Mentor\nDepartment of CSE"
    p2_sub.font.size = Pt(12)
    p2_sub.font.color.rgb = TEXT_DARK

    s1.shapes[3].text_frame.clear()
    p3 = s1.shapes[3].text_frame.paragraphs[0]
    p3.text = "Submitted by:"
    p3.font.bold = True
    p3.font.size = Pt(14)
    p3.font.color.rgb = NAVY
    student_info = [
        "Name: [Your Name]",
        "Branch: Computer Science & Engineering",
        "SIC. No. : [Your SIC No.]",
        "SEMESTER: 5th / 6th / 7th Semester"
    ]
    for line in student_info:
        p = s1.shapes[3].text_frame.add_paragraph()
        p.text = line
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK

    s1.notes_slide.notes_text_frame.text = (
        "Good morning respected professors and evaluators. Today, I am presenting my summer internship project: "
        "Patient Visit History Management System, built with Python, FastAPI, SQLAlchemy ORM, and Cloud MySQL."
    )

    # -------------------------------------------------------------
    # SLIDE 2: INTRODUCTION
    # -------------------------------------------------------------
    s2 = prs.slides[1]
    tf2 = s2.shapes[1].text_frame
    tf2.clear()

    intro_points = [
        ("Domain Context: ", "Modern healthcare facilities require secure, high-speed, and centralized access to patient medical histories."),
        ("Challenges in Legacy Systems: ", "Manual paper records and monolithic hospital systems suffer from slow search times, physical file loss, human transcription errors, and lack of APIs for modern web/mobile apps."),
        ("Proposed Solution: ", "A high-performance, asynchronous RESTful API backend that decouples data management from client devices."),
        ("Core Functionality: ", "Enables healthcare staff to register patients and log detailed, multi-visit consultation timelines (attending doctor, diagnosis notes, and prescriptions)."),
        ("Cloud Infrastructure: ", "Directly connected to a live serverless Cloud MySQL database cluster (TiDB on AWS) using TLS encrypted connections.")
    ]

    for idx, (header, body) in enumerate(intro_points):
        p = tf2.paragraphs[0] if idx == 0 else tf2.add_paragraph()
        r1 = p.add_run()
        r1.text = "•  " + header
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = BLUE

        r2 = p.add_run()
        r2.text = body
        r2.font.size = Pt(13)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(10)

    s2.notes_slide.notes_text_frame.text = (
        "In our introduction, we address the challenge in traditional healthcare data management. Our system delivers a centralized REST API backend that handles patient records and historical medical consultations with high speed and reliability."
    )

    # -------------------------------------------------------------
    # SLIDE 3: OBJECTIVES
    # -------------------------------------------------------------
    s3 = prs.slides[2]
    tf3 = s3.shapes[1].text_frame
    tf3.clear()

    objectives = [
        ("Centralized Patient Management: ", "Fast registration, updating, and instant retrieval of patient demographic profiles."),
        ("Consultation Visit Tracking: ", "Maintain chronological consultation timelines with doctor names, clinical diagnoses, and prescriptions."),
        ("Referential Integrity Enforcement: ", "Implement Foreign Key constraints with ON DELETE CASCADE to eliminate orphaned visit records when a patient is removed."),
        ("Strict Data Validation: ", "Utilize Pydantic v2 schemas to validate data types, range bounds (e.g. age 0-130), and mandatory fields prior to database operations."),
        ("Database Abstraction Layer: ", "Use SQLAlchemy 2.0 ORM to decouple application logic from the database engine (zero-config SQLite locally, Cloud MySQL in production)."),
        ("Automated API Documentation: ", "Provide interactive OpenAPI/Swagger UI at /docs for immediate testing without requiring frontend development.")
    ]

    for idx, (header, body) in enumerate(objectives):
        p = tf3.paragraphs[0] if idx == 0 else tf3.add_paragraph()
        r1 = p.add_run()
        r1.text = f"{idx+1}.  " + header
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = BLUE

        r2 = p.add_run()
        r2.text = body
        r2.font.size = Pt(13)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(8)

    s3.notes_slide.notes_text_frame.text = (
        "Our primary objective was building a robust system following industry best practices: referential integrity, automatic schema validation, and database abstraction."
    )

    # -------------------------------------------------------------
    # SLIDE 4: CONTENTS OF THE PROGRAM
    # -------------------------------------------------------------
    s4 = prs.slides[3]
    tf4 = s4.shapes[1].text_frame
    tf4.clear()

    contents = [
        ("Python 3.13 Runtime: ", "Core programming language utilizing modern typing and high execution performance."),
        ("FastAPI Web Framework: ", "High-performance asynchronous framework based on Starlette and OpenAPI standards."),
        ("Uvicorn ASGI Server: ", "Production-grade, lightning-fast ASGI server for handling concurrent HTTP requests."),
        ("SQLAlchemy 2.0 ORM: ", "Object-Relational Mapping, connection pooling, and automatic SQL injection prevention."),
        ("TiDB Cloud Serverless (MySQL 8.0): ", "Fully managed cloud relational database hosted on AWS Tokyo with TLS 1.2 secure encryption."),
        ("Pydantic v2 Serialization: ", "High-speed Rust-core request validation and response schema serialization."),
        ("Postman & Swagger UI: ", "Comprehensive end-to-end API verification and documentation tooling.")
    ]

    for idx, (header, body) in enumerate(contents):
        p = tf4.paragraphs[0] if idx == 0 else tf4.add_paragraph()
        r1 = p.add_run()
        r1.text = "•  " + header
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = BLUE

        r2 = p.add_run()
        r2.text = body
        r2.font.size = Pt(13)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(8)

    s4.notes_slide.notes_text_frame.text = (
        "This slide covers the technology stack we mastered and used. FastAPI handles routing, SQLAlchemy ORM prevents SQL injection, and TiDB Cloud MySQL provides scalable cloud persistence."
    )

    # -------------------------------------------------------------
    # SLIDE 5: METHODOLOGY — Architecture & Complete Project Flow
    # -------------------------------------------------------------
    s5 = prs.slides[4]
    s5.shapes[0].text_frame.text = "METHODOLOGY: System Architecture & Execution Flow"
    s5.shapes[0].text_frame.paragraphs[0].font.size = Pt(22)
    s5.shapes[0].text_frame.paragraphs[0].font.bold = True
    s5.shapes[0].text_frame.paragraphs[0].font.color.rgb = NAVY

    # Reposition shape 1 (text frame) to the right side
    s5.shapes[1].left = Inches(7.1)
    s5.shapes[1].top = Inches(1.6)
    s5.shapes[1].width = Inches(5.6)
    s5.shapes[1].height = Inches(5.2)

    tf5 = s5.shapes[1].text_frame
    tf5.clear()

    p = tf5.paragraphs[0]
    p.text = "Project Execution Flow (Kaise Kaam Karta Hai):"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = NAVY
    p.space_after = Pt(4)

    flow_steps = [
        ("1. Client Request: ", "Postman/Browser sends HTTP JSON payload (e.g. POST /patients/1/visits)."),
        ("2. ASGI Server (Uvicorn): ", "Asynchronously handles concurrent traffic and forwards to FastAPI."),
        ("3. Routing Dispatcher: ", "FastAPI matches URL endpoint to the designated route controller."),
        ("4. Pydantic Validation: ", "Validates field types & age boundaries BEFORE touching database. If invalid, auto-returns HTTP 422."),
        ("5. Session Injection: ", "Depends(get_db) provisions isolated DB transaction session."),
        ("6. SQLAlchemy ORM: ", "Translates entity models into safe, parameterized SQL statements."),
        ("7. PyMySQL Driver: ", "Transmits queries over encrypted TLS to TiDB Cloud MySQL."),
        ("8. Cloud MySQL Engine: ", "Executes query, generates auto-increment PK, & commits."),
        ("9. Hydration & Response: ", "ORM hydrates rows into Python objects; Pydantic serializes to JSON with HTTP 201/200 status code.")
    ]

    for h, b in flow_steps:
        p = tf5.add_paragraph()
        r1 = p.add_run()
        r1.text = h
        r1.font.bold = True
        r1.font.size = Pt(10)
        r1.font.color.rgb = BLUE

        r2 = p.add_run()
        r2.text = b
        r2.font.size = Pt(10)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(2)

    # Insert Architecture Diagram on Left
    arch_img = r"E:\python_fastapi\architecture_diagram.png"
    if os.path.exists(arch_img):
        s5.shapes.add_picture(arch_img, Inches(0.6), Inches(1.6), width=Inches(6.3))

    s5.notes_slide.notes_text_frame.text = (
        "Sir, is slide mein hamare project ka complete architecture aur execution flow hai. "
        "Client jab request bhejta hai, toh Uvicorn use asynchronously receive karta hai. "
        "FastAPI router use route karta hai aur Pydantic data validate karta hai taaki database tak koi corrupt ya invalid data na pahuche. "
        "Uske baad SQLAlchemy ORM Python object ko SQL query mein convert karta hai aur PyMySQL driver TLS encryption ke sath use TiDB Cloud MySQL mein execute karta hai. "
        "Wahan se data save hone ke baad response serialize hokar client ko 201 Created ya 200 OK milta hai."
    )

    # -------------------------------------------------------------
    # SLIDE 6: METHODOLOGY — Relational Database Design (ER Model)
    # (Insert as a new dedicated slide right after Slide 5!)
    # -------------------------------------------------------------
    layout_title_content = prs.slide_layouts[1]
    s_er = prs.slides.add_slide(layout_title_content)

    # Add Silicon Logo to top right
    s_er.shapes.add_picture(io.BytesIO(logo_blob), Inches(9.89), Inches(0.40), width=Inches(2.90), height=Inches(0.88))

    # Slide Title
    s_er.shapes[0].text_frame.text = "METHODOLOGY: Database Design (Entity-Relationship Model)"
    s_er.shapes[0].text_frame.paragraphs[0].font.size = Pt(22)
    s_er.shapes[0].text_frame.paragraphs[0].font.bold = True
    s_er.shapes[0].text_frame.paragraphs[0].font.color.rgb = NAVY

    # Insert ER Diagram Image on Left
    er_img = r"E:\python_fastapi\er_diagram.png"
    if os.path.exists(er_img):
        s_er.shapes.add_picture(er_img, Inches(0.6), Inches(1.7), width=Inches(6.4))

    # Add detailed explanation text on Right
    s_er.shapes[1].left = Inches(7.2)
    s_er.shapes[1].top = Inches(1.7)
    s_er.shapes[1].width = Inches(5.5)
    s_er.shapes[1].height = Inches(5.0)

    tfer = s_er.shapes[1].text_frame
    tfer.clear()

    p = tfer.paragraphs[0]
    p.text = "1-to-Many (1:N) Relational Architecture:"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = NAVY
    p.space_after = Pt(4)

    er_points = [
        ("Relationship: ", "One Patient has many Visits (1 : N). Each visit strictly belongs to one patient."),
        ("PATIENTS Table: ", "Stores core demographic details (id PK, name, age, gender, contact_number, address, created_at)."),
        ("VISITS Table: ", "Stores consultation data (id PK, patient_id FK, visit_date, doctor_name, diagnosis, prescription, created_at)."),
        ("Foreign Key: ", "visits.patient_id references patients.id to maintain referential integrity."),
        ("ON DELETE CASCADE: ", "If a patient record is deleted, all their historical medical visit records are automatically deleted from the database. Prevents orphaned records!"),
        ("ORM Implementation: ", "SQLAlchemy handles cascade='all, delete-orphan' at the Python object layer as well as MySQL DDL constraint.")
    ]

    for h, b in er_points:
        p = tfer.add_paragraph()
        r1 = p.add_run()
        r1.text = "•  " + h
        r1.font.bold = True
        r1.font.size = Pt(10)
        r1.font.color.rgb = BLUE

        r2 = p.add_run()
        r2.text = b
        r2.font.size = Pt(10)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(3)

    s_er.notes_slide.notes_text_frame.text = (
        "Sir, ye hamare database ka Entity-Relationship (ER) model hai. Yahan Patients aur Visits ke beech 1-to-Many relationship hai. "
        "Ek patient ke kai consultation visits ho sakte hain. Humne Foreign Key 'patient_id' par ON DELETE CASCADE lagaya hai, "
        "jisse referential integrity maintain rehti hai—agar koi patient delete hota hai, toh uske related saare visit records database se automatically remove ho jaate hain."
    )

    # -------------------------------------------------------------
    # SLIDE 7: Projects Done (CRUD Endpoints & Details)
    # (Previously Slide 6)
    # -------------------------------------------------------------
    s_pd = prs.slides[5]
    tf_pd = s_pd.shapes[1].text_frame
    tf_pd.clear()

    # Add Silicon Logo if missing
    if len(s_pd.shapes) < 4:
        s_pd.shapes.add_picture(io.BytesIO(logo_blob), Inches(9.89), Inches(0.40), width=Inches(2.90), height=Inches(0.88))

    p = tf_pd.paragraphs[0]
    p.text = "Module 1: Patient Management Service (routes/patients.py)"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = NAVY

    m1_points = [
        "•  POST /patients/  [HTTP 201 Created]  -  Register patient with age & phone validation.",
        "•  GET /patients/  [HTTP 200 OK]  -  Paginated list of all registered patients.",
        "•  GET /patients/{id}  [HTTP 200 OK]  -  Retrieve patient profile nested with complete visit history.",
        "•  PUT /patients/{id}  [HTTP 200 OK]  -  Update patient demographic details.",
        "•  DELETE /patients/{id}  [HTTP 200 OK]  -  Delete patient record; cascades and cleans child visits."
    ]
    for pt in m1_points:
        p = tf_pd.add_paragraph()
        p.text = pt
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(2)

    p_spacer = tf_pd.add_paragraph()
    p_spacer.text = "Module 2: Medical Visit History Service (routes/visits.py)"
    p_spacer.font.bold = True
    p_spacer.font.size = Pt(13)
    p_spacer.font.color.rgb = NAVY
    p_spacer.space_before = Pt(6)

    m2_points = [
        "•  POST /patients/{id}/visits  [HTTP 201 Created]  -  Log consultation visit (validates patient exists).",
        "•  GET /patients/{id}/visits  [HTTP 200 OK]  -  Retrieve all historical visits of a patient chronologically.",
        "•  GET /visits/{id}  [HTTP 200 OK]  -  Get individual visit consultation details.",
        "•  PUT /visits/{id}  [HTTP 200 OK]  -  Update diagnosis notes or medical prescriptions.",
        "•  DELETE /visits/{id}  [HTTP 200 OK]  -  Delete an individual visit consultation record."
    ]
    for pt in m2_points:
        p = tf_pd.add_paragraph()
        p.text = pt
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(2)

    p_ver = tf_pd.add_paragraph()
    p_ver.text = "✔ Verification: 100% test pass rate across all endpoints in Swagger UI and Postman."
    p_ver.font.bold = True
    p_ver.font.size = Pt(11)
    p_ver.font.color.rgb = GREEN
    p_ver.space_before = Pt(4)

    s_pd.notes_slide.notes_text_frame.text = (
        "Under Projects Done, we implemented two complete modules covering all 9 REST endpoints with proper HTTP status codes and nested JSON responses."
    )

    # -------------------------------------------------------------
    # SLIDE 8: CONCLUSION
    # (Previously Slide 7)
    # -------------------------------------------------------------
    s_concl = prs.slides[6]
    rect = s_concl.shapes[3]
    rect.left = Inches(0.9)
    rect.top = Inches(1.8)
    rect.width = Inches(11.4)
    rect.height = Inches(4.8)
    rect.line.fill.background()
    rect.fill.background()

    tf_c = rect.text_frame
    tf_c.clear()

    p = tf_c.paragraphs[0]
    p.text = "Key Project Achievements:"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = NAVY

    concl_points = [
        "•  Successfully built a complete, production-grade REST API backend from scratch using FastAPI.",
        "•  Engineered robust 1-to-Many relational database architecture with Foreign Key cascade protection.",
        "•  Integrated live cloud MySQL persistence (TiDB Serverless on AWS Tokyo) with TLS encryption.",
        "•  Achieved strict schema validation (Pydantic v2) and ORM abstraction (SQLAlchemy 2.0)."
    ]
    for pt in concl_points:
        p = tf_c.add_paragraph()
        p.text = pt
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(3)

    p_future = tf_c.add_paragraph()
    p_future.text = "Future Scope & Enhancements:"
    p_future.font.bold = True
    p_future.font.size = Pt(14)
    p_future.font.color.rgb = BLUE
    p_future.space_before = Pt(8)

    future_points = [
        "➔  Role-Based Access Control (RBAC) with JWT authentication for Doctors, Nurses, and Receptionists.",
        "➔  Automated patient follow-up scheduling with SMS and email notifications.",
        "➔  AI-assisted diagnosis and prescription suggestion using Gemini API integration.",
        "➔  Full-stack web application development using React / Next.js and Tailwind CSS."
    ]
    for pt in future_points:
        p = tf_c.add_paragraph()
        p.text = pt
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(3)

    s_concl.notes_slide.notes_text_frame.text = (
        "In conclusion, this project shows how modern backend frameworks and cloud databases work together. The system is ready for hospital deployment and future AI-assisted medical record features. Thank you, and I am now open to any questions."
    )

    # Move the ER diagram slide (appended at index 7) to index 5 (Slide 6, right after Slide 5 Architecture)
    sldIdLst = prs.slides._sldIdLst
    er_slide_id = sldIdLst[7]
    sldIdLst.insert(5, er_slide_id)

    # Save presentation to Final file name
    output_path = r"E:\python_fastapi\Patient_Visit_History_Final_Presentation.pptx"
    prs.save(output_path)
    print(f"Success: Final presentation saved to {output_path}")

    # Also attempt to update Silicon presentation if user closes it
    try:
        prs.save(r"E:\python_fastapi\Patient_Visit_History_Silicon_Presentation.pptx")
        print("Success: Also updated Patient_Visit_History_Silicon_Presentation.pptx")
    except Exception as e:
        print("Note: Patient_Visit_History_Silicon_Presentation.pptx is open in PowerPoint. Saved to Patient_Visit_History_Final_Presentation.pptx instead.")

if __name__ == "__main__":
    build_silicon_deck()
