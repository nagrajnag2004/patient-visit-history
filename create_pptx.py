import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    NAVY = RGBColor(15, 23, 42)       # Slate 900
    BLUE = RGBColor(37, 99, 235)      # Blue 600
    LIGHT_BG = RGBColor(248, 250, 252)# Slate 50
    TEXT_DARK = RGBColor(30, 41, 59)  # Slate 800
    TEXT_MUTED = RGBColor(100, 116, 139) # Slate 500
    WHITE = RGBColor(255, 255, 255)
    CARD_BG = RGBColor(255, 255, 255)
    BORDER_COLOR = RGBColor(226, 232, 240)

    blank_layout = prs.slide_layouts[6]

    def set_slide_background(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, section_title, slide_title):
        # Section Category
        sec_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
        tf = sec_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = section_title.upper()
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = BLUE

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.7))
        tf2 = title_box.text_frame
        tf2.word_wrap = True
        p2 = tf2.paragraphs[0]
        p2.text = slide_title
        p2.font.size = Pt(22)
        p2.font.bold = True
        p2.font.color.rgb = NAVY

    # ==========================================
    # SLIDE 1: Title Slide
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, NAVY)

    t_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(3.0))
    tf = t_box.text_frame
    tf.word_wrap = True

    p_badge = tf.paragraphs[0]
    p_badge.text = "COLLEGE TRAINING & INTERNSHIP PRESENTATION"
    p_badge.font.size = Pt(13)
    p_badge.font.bold = True
    p_badge.font.color.rgb = RGBColor(96, 165, 250)

    p_title = tf.add_paragraph()
    p_title.text = "Patient Visit History Management System"
    p_title.font.size = Pt(36)
    p_title.font.bold = True
    p_title.font.color.rgb = WHITE

    p_sub = tf.add_paragraph()
    p_sub.text = "A High-Performance Relational REST API Backend with FastAPI, SQLAlchemy ORM & Cloud MySQL"
    p_sub.font.size = Pt(18)
    p_sub.font.color.rgb = RGBColor(203, 213, 225)

    meta_box = s1.shapes.add_textbox(Inches(1.0), Inches(5.2), Inches(11.3), Inches(1.5))
    mtf = meta_box.text_frame
    p_meta = mtf.paragraphs[0]
    p_meta.text = "Tech Stack: Python 3.13  |  FastAPI (ASGI)  |  SQLAlchemy 2.0  |  TiDB Cloud MySQL  |  Uvicorn\nAuthor: Computer Science & Engineering  |  Academic Year: 2026"
    p_meta.font.size = Pt(13)
    p_meta.font.color.rgb = RGBColor(148, 163, 184)

    s1.notes_slide.notes_text_frame.text = (
        "Good morning respected professors and evaluators. Today, I am presenting my backend project: "
        "the Patient Visit History Management System built with FastAPI, SQLAlchemy, and Cloud MySQL."
    )

    # ==========================================
    # SLIDE 2: INTRODUCTION
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, LIGHT_BG)
    add_header(s2, "1. Introduction", "Background & Healthcare Context")

    # Card 1: Problem Statement
    c1 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = BORDER_COLOR
    tf1 = c1.text_frame
    tf1.word_wrap = True
    tf1.margin_top = Inches(0.3)
    tf1.margin_left = Inches(0.3)
    tf1.margin_right = Inches(0.3)

    p = tf1.paragraphs[0]
    p.text = "Challenges in Legacy Healthcare"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = RGBColor(220, 38, 38)

    points1 = [
        "Traditional paper medical records are slow to retrieve and prone to physical loss.",
        "Monolithic hospital systems lack modern, interoperable REST APIs.",
        "High risk of human transcription errors and duplicate patient files.",
        "No centralized audit trail for multiple consultation visits over time."
    ]
    for pt in points1:
        p = tf1.add_paragraph()
        p.text = f"•  {pt}"
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(10)

    # Card 2: Proposed Solution
    c2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0))
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = BORDER_COLOR
    tf2 = c2.text_frame
    tf2.word_wrap = True
    tf2.margin_top = Inches(0.3)
    tf2.margin_left = Inches(0.3)
    tf2.margin_right = Inches(0.3)

    p = tf2.paragraphs[0]
    p.text = "Our Modern REST API Solution"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = RGBColor(16, 185, 129)

    points2 = [
        "High-performance REST API backend built on asynchronous ASGI architecture.",
        "Strict 1-to-Many Relational Data Model (One Patient to Many Medical Visits).",
        "Automated request payload validation & serialization powered by Pydantic.",
        "Live Cloud MySQL Database (TiDB Serverless) running with TLS encryption.",
        "Instant interactive OpenAPI documentation (Swagger UI) for developers."
    ]
    for pt in points2:
        p = tf2.add_paragraph()
        p.text = f"•  {pt}"
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(10)

    s2.notes_slide.notes_text_frame.text = (
        "In traditional healthcare, paper records cause delays and errors. "
        "Our solution decouples data storage from clients using a high-performance REST API."
    )

    # ==========================================
    # SLIDE 3: OBJECTIVES
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, LIGHT_BG)
    add_header(s3, "2. Objectives", "Core Project Goals & Design Principles")

    goals = [
        ("Centralized Patient Profiles", "Store demographic details (name, age, gender, contact number, address) with strict data types."),
        ("Chronological Visit Tracking", "Log medical consultations, attending doctors, clinical diagnoses, and prescriptions per patient."),
        ("Referential Integrity (Cascade)", "Implement Foreign Key constraints with ON DELETE CASCADE so deleting a patient purges child visits."),
        ("Automated Data Validation", "Prevent invalid data (e.g. negative age, malformed inputs) using Pydantic v2 schemas before SQL execution."),
        ("ORM Database Abstraction", "Decouple business logic from database engines using SQLAlchemy 2.0 (local SQLite or Cloud MySQL)."),
        ("Developer-Friendly OpenAPI", "Auto-generate interactive Swagger UI documentation at /docs for seamless testing and QA.")
    ]

    for i, (g_title, g_desc) in enumerate(goals):
        col = i % 2
        row = i // 2
        x = Inches(0.8 + col * 5.9)
        y = Inches(1.6 + row * 1.7)

        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.6), Inches(1.5))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = BORDER_COLOR

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = Inches(0.25)
        ctf.margin_top = Inches(0.2)

        p = ctf.paragraphs[0]
        p.text = f"{i+1}. {g_title}"
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = BLUE

        p2 = ctf.add_paragraph()
        p2.text = g_desc
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_DARK

    s3.notes_slide.notes_text_frame.text = (
        "Our primary objective was building a robust system following industry best practices: "
        "referential integrity, automatic schema validation, and database abstraction."
    )

    # ==========================================
    # SLIDE 4: CONTENTS OF THE PROGRAM (Tech Stack)
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, LIGHT_BG)
    add_header(s4, "3. Contents of the Program", "Technology Stack & Framework Selection")

    tech_items = [
        ("Python 3.13", "Core Language", "Modern Python runtime with strict type hinting and high execution efficiency."),
        ("FastAPI 0.115", "Web Framework", "Asynchronous ASGI framework with native OpenAPI doc generation."),
        ("Uvicorn 0.34", "ASGI Server", "Lightning-fast production ASGI web server handling concurrent requests."),
        ("SQLAlchemy 2.0", "ORM & Pool", "Translates Python objects into parameterized SQL; manages connection pooling."),
        ("TiDB Cloud MySQL", "Cloud Database", "AWS Tokyo managed MySQL 8.0 serverless cluster with TLS 1.2 encryption."),
        ("Pydantic v2", "Data Validation", "High-speed Rust-core serialization and request body validation.")
    ]

    for i, (t_name, t_role, t_desc) in enumerate(tech_items):
        col = i % 3
        row = i // 3
        x = Inches(0.8 + col * 3.9)
        y = Inches(1.6 + row * 2.5)

        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(3.7), Inches(2.2))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = BORDER_COLOR

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = Inches(0.25)
        ctf.margin_top = Inches(0.25)

        p = ctf.paragraphs[0]
        p.text = t_name
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = BLUE

        p_role = ctf.add_paragraph()
        p_role.text = t_role
        p_role.font.size = Pt(11)
        p_role.font.bold = True
        p_role.font.color.rgb = TEXT_MUTED

        p_desc = ctf.add_paragraph()
        p_desc.text = t_desc
        p_desc.font.size = Pt(12)
        p_desc.font.color.rgb = TEXT_DARK
        p_desc.space_before = Pt(8)

    s4.notes_slide.notes_text_frame.text = (
        "Here is our technology stack. We chose FastAPI for speed, SQLAlchemy for SQL injection prevention, "
        "and TiDB Cloud MySQL for scalable cloud data persistence."
    )

    # ==========================================
    # SLIDE 5: METHODOLOGY — Architecture Diagram
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, LIGHT_BG)
    add_header(s5, "4. Methodology", "Complete Request-Response Architecture & Data Lifecycle")

    img_path = r"E:\python_fastapi\architecture_diagram.png"
    if os.path.exists(img_path):
        s5.shapes.add_picture(img_path, Inches(0.8), Inches(1.5), width=Inches(7.2))

    # Side Card explaining the lifecycle
    sc = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.3), Inches(1.5), Inches(4.2), Inches(5.3))
    sc.fill.solid()
    sc.fill.fore_color.rgb = CARD_BG
    sc.line.color.rgb = BORDER_COLOR
    sctf = sc.text_frame
    sctf.word_wrap = True
    sctf.margin_left = Inches(0.3)
    sctf.margin_top = Inches(0.25)

    p = sctf.paragraphs[0]
    p.text = "Data Flow Execution Steps"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY

    steps = [
        "1. Client sends JSON request to Uvicorn ASGI server.",
        "2. FastAPI router forwards to endpoint controller.",
        "3. Pydantic validates payload against schema.",
        "4. Depends(get_db) injects isolated session.",
        "5. SQLAlchemy converts model logic into SQL.",
        "6. PyMySQL executes query over TLS to MySQL.",
        "7. Cloud MySQL returns rows to driver.",
        "8. ORM hydrates records -> Pydantic serializes to JSON."
    ]
    for st in steps:
        p = sctf.add_paragraph()
        p.text = st
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(4)

    s5.notes_slide.notes_text_frame.text = (
        "Respected evaluators, this diagram shows the end-to-end data lifecycle. "
        "Notice complete separation of concerns from routing, schema validation, to encrypted cloud MySQL persistence."
    )

    # ==========================================
    # SLIDE 6: METHODOLOGY — Relational Database Schema
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, LIGHT_BG)
    add_header(s6, "4. Methodology", "Relational Database Design (1-to-Many Model)")

    # Table 1: Patients
    t1 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(4.5))
    t1.fill.solid()
    t1.fill.fore_color.rgb = CARD_BG
    t1.line.color.rgb = BORDER_COLOR
    ttf1 = t1.text_frame
    ttf1.word_wrap = True
    ttf1.margin_left = Inches(0.3)
    ttf1.margin_top = Inches(0.2)

    p = ttf1.paragraphs[0]
    p.text = "Table: patients"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = BLUE

    p_cols1 = [
        "id: INT PRIMARY KEY (Auto-Increment)",
        "name: VARCHAR(100) NOT NULL",
        "age: INT NOT NULL (Range: 0-130)",
        "gender: VARCHAR(20) NOT NULL",
        "contact_number: VARCHAR(20) NOT NULL",
        "address: VARCHAR(255) NULLABLE",
        "created_at: DATETIME (Server Default Now)"
    ]
    for col_str in p_cols1:
        p = ttf1.add_paragraph()
        p.text = f"•  {col_str}"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(6)

    # Table 2: Visits
    t2 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(4.5))
    t2.fill.solid()
    t2.fill.fore_color.rgb = CARD_BG
    t2.line.color.rgb = BORDER_COLOR
    ttf2 = t2.text_frame
    ttf2.word_wrap = True
    ttf2.margin_left = Inches(0.3)
    ttf2.margin_top = Inches(0.2)

    p = ttf2.paragraphs[0]
    p.text = "Table: visits"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = BLUE

    p_cols2 = [
        "id: INT PRIMARY KEY (Auto-Increment)",
        "patient_id: INT FOREIGN KEY (patients.id)",
        "visit_date: DATETIME NOT NULL",
        "doctor_name: VARCHAR(100) NOT NULL",
        "diagnosis: TEXT NOT NULL",
        "prescription: TEXT NULLABLE",
        "created_at: DATETIME (Server Default Now)"
    ]
    for col_str in p_cols2:
        p = ttf2.add_paragraph()
        p.text = f"•  {col_str}"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(6)

    # Constraint banner at bottom
    bb = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.3), Inches(11.7), Inches(0.8))
    bb.fill.solid()
    bb.fill.fore_color.rgb = RGBColor(238, 242, 255)
    bb.line.color.rgb = RGBColor(199, 210, 254)
    bbtf = bb.text_frame
    p_b = bbtf.paragraphs[0]
    p_b.text = "Referential Integrity: Foreign Key configured with ON DELETE CASCADE to eliminate orphaned consultation records."
    p_b.font.size = Pt(12)
    p_b.font.bold = True
    p_b.font.color.rgb = BLUE

    s6.notes_slide.notes_text_frame.text = (
        "Each patient can have multiple visits. If a patient is deleted, their medical visits are automatically deleted "
        "thanks to ON DELETE CASCADE at both the ORM and SQL level."
    )

    # ==========================================
    # SLIDE 7: PROJECTS DONE — Core Endpoints
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, LIGHT_BG)
    add_header(s7, "5. Projects Done", "Implemented REST API Services & Endpoints")

    # Patient Endpoints
    pe = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
    pe.fill.solid()
    pe.fill.fore_color.rgb = CARD_BG
    pe.line.color.rgb = BORDER_COLOR
    petf = pe.text_frame
    petf.word_wrap = True
    petf.margin_left = Inches(0.3)
    petf.margin_top = Inches(0.2)

    p = petf.paragraphs[0]
    p.text = "Patient Management (routes/patients.py)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = BLUE

    p_apis = [
        ("POST /patients/", "201 Created", "Register new patient with validation"),
        ("GET /patients/", "200 OK", "Paginated list of all patients"),
        ("GET /patients/{id}", "200 OK", "Get patient with nested visit history"),
        ("PUT /patients/{id}", "200 OK", "Update patient demographic details"),
        ("DELETE /patients/{id}", "200 OK", "Delete patient and cascade delete visits")
    ]
    for method_ep, status, desc in p_apis:
        p = petf.add_paragraph()
        p.text = f"{method_ep}  [{status}]"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p2 = petf.add_paragraph()
        p2.text = f"  {desc}"
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_MUTED
        p2.space_after = Pt(4)

    # Visit Endpoints
    ve = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2))
    ve.fill.solid()
    ve.fill.fore_color.rgb = CARD_BG
    ve.line.color.rgb = BORDER_COLOR
    vetf = ve.text_frame
    vetf.word_wrap = True
    vetf.margin_left = Inches(0.3)
    vetf.margin_top = Inches(0.2)

    p = vetf.paragraphs[0]
    p.text = "Visit History (routes/visits.py)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = BLUE

    v_apis = [
        ("POST /patients/{id}/visits", "201 Created", "Log consultation visit for patient"),
        ("GET /patients/{id}/visits", "200 OK", "List all visits of a patient"),
        ("GET /visits/{visit_id}", "200 OK", "Retrieve individual visit consultation"),
        ("PUT /visits/{visit_id}", "200 OK", "Update diagnosis / doctor observations"),
        ("DELETE /visits/{visit_id}", "200 OK", "Remove an erroneous visit record")
    ]
    for method_ep, status, desc in v_apis:
        p = vetf.add_paragraph()
        p.text = f"{method_ep}  [{status}]"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p2 = vetf.add_paragraph()
        p2.text = f"  {desc}"
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_MUTED
        p2.space_after = Pt(4)

    s7.notes_slide.notes_text_frame.text = (
        "We implemented full CRUD for Patients and Visits. Notice our nested GET /patients/{id} endpoint: "
        "it returns the patient and embeds their entire medical visit history in one clean JSON response."
    )

    # ==========================================
    # SLIDE 8: PROJECTS DONE — Verification & Results
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8, LIGHT_BG)
    add_header(s8, "5. Projects Done", "Testing, Verification & Cloud Persistence")

    cards_data = [
        ("Swagger UI at /docs", "Interactive Web Testing", "Zero frontend required. Tested all 9 endpoints live with real JSON payloads.", RGBColor(37, 99, 235)),
        ("HTTP Status Codes", "REST Standards", "201 Created on inserts, 200 OK on queries/updates, 404 Not Found, and 422 on validation failure.", RGBColor(16, 185, 129)),
        ("TiDB Cloud MySQL", "Live Cloud Persistence", "Verified live encrypted connection to AWS Tokyo cluster. Data is permanently persisted.", RGBColor(139, 92, 246))
    ]

    for i, (title, sub, body, color) in enumerate(cards_data):
        x = Inches(0.8 + i * 3.9)
        card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.6), Inches(3.7), Inches(5.0))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = BORDER_COLOR

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = Inches(0.3)
        ctf.margin_top = Inches(0.3)

        p = ctf.paragraphs[0]
        p.text = title
        p.font.size = Pt(17)
        p.font.bold = True
        p.font.color.rgb = color

        p_sub = ctf.add_paragraph()
        p_sub.text = sub
        p_sub.font.size = Pt(11)
        p_sub.font.bold = True
        p_sub.font.color.rgb = TEXT_MUTED

        p_b = ctf.add_paragraph()
        p_b.text = body
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_DARK
        p_b.space_before = Pt(14)

    s8.notes_slide.notes_text_frame.text = (
        "Testing was performed using Swagger UI and Postman. "
        "We verified that all CRUD operations correctly store and retrieve records from our TiDB Cloud MySQL cluster."
    )

    # ==========================================
    # SLIDE 9: CONCLUSION & FUTURE SCOPE
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9, LIGHT_BG)
    add_header(s9, "6. Conclusion", "Key Takeaways & Future Enhancements")

    c_left = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0))
    c_left.fill.solid()
    c_left.fill.fore_color.rgb = CARD_BG
    c_left.line.color.rgb = BORDER_COLOR
    ltf = c_left.text_frame
    ltf.word_wrap = True
    ltf.margin_left = Inches(0.3)
    ltf.margin_top = Inches(0.3)

    p = ltf.paragraphs[0]
    p.text = "Key Project Achievements"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = RGBColor(16, 185, 129)

    achieve = [
        "Successfully developed an enterprise-grade REST API backend from scratch.",
        "Engineered robust 1-to-Many relational database architecture with cascade deletion.",
        "Decoupled SQL persistence using SQLAlchemy ORM for database engine flexibility.",
        "Deployed live encrypted connection to Serverless Cloud MySQL on TiDB AWS.",
        "Achieved 100% test pass rate across all 9 endpoints in OpenAPI documentation."
    ]
    for ac in achieve:
        p = ltf.add_paragraph()
        p.text = f"✔  {ac}"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(10)

    c_right = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.0))
    c_right.fill.solid()
    c_right.fill.fore_color.rgb = CARD_BG
    c_right.line.color.rgb = BORDER_COLOR
    rtf = c_right.text_frame
    rtf.word_wrap = True
    rtf.margin_left = Inches(0.3)
    rtf.margin_top = Inches(0.3)

    p = rtf.paragraphs[0]
    p.text = "Future Roadmap"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = BLUE

    roadmap = [
        "JWT Authentication & Role-Based Access Control (Admin, Doctor, Receptionist).",
        "SMS and Email automated reminders for upcoming scheduled follow-up visits.",
        "AI Diagnostic Assistant powered by Gemini API for prescription advisory.",
        "Full-Stack Web Dashboard using Next.js / React and Tailwind CSS."
    ]
    for rm in roadmap:
        p = rtf.add_paragraph()
        p.text = f"➔  {rm}"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(12)

    s9.notes_slide.notes_text_frame.text = (
        "In conclusion, this project shows how modern backend frameworks and cloud databases work together. "
        "The system is ready for hospital deployment and future AI-assisted medical record features."
    )

    # Save presentation
    output_path = r"E:\python_fastapi\Patient_Visit_History_Presentation.pptx"
    prs.save(output_path)
    print(f"Success: Presentation saved to {output_path}")

if __name__ == "__main__":
    create_deck()

