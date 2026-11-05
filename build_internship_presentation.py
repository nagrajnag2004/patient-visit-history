import os
import io
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_internship_deck():
    template_path = r"C:\Users\nagra\.gemini\antigravity\brain\cd5112b8-2b8b-4867-bcda-98e7404bb232\.user_uploaded\media_1793871599475_be970003.pptx"
    prs = Presentation(template_path)

    NAVY = RGBColor(26, 35, 126)       # Silicon Blue
    BLUE = RGBColor(13, 71, 161)       # Medium Blue
    TEXT_DARK = RGBColor(33, 37, 41)    # Dark Charcoal
    GREEN = RGBColor(16, 185, 129)     # Success Green

    # Extract logo from slide 2
    logo_blob = prs.slides[1].shapes[3].image.blob

    # =============================================================
    # SLIDE 1: Title Slide (Matches Sample Slide 1)
    # =============================================================
    s1 = prs.slides[0]
    s1.shapes[0].text_frame.clear()
    p1 = s1.shapes[0].text_frame.paragraphs[0]
    p1.text = "Python Using Fast Api Internship"
    p1.font.size = Pt(28)
    p1.font.bold = True
    p1.font.color.rgb = NAVY

    p1_sub = s1.shapes[0].text_frame.add_paragraph()
    p1_sub.text = "Mini-Project: Patient Visit History Management System"
    p1_sub.font.size = Pt(16)
    p1_sub.font.color.rgb = BLUE
    p1_sub.font.bold = True

    # Guide
    s1.shapes[2].text_frame.clear()
    p2 = s1.shapes[2].text_frame.paragraphs[0]
    p2.text = "Under the guidance of:"
    p2.font.bold = True
    p2.font.size = Pt(14)
    p2.font.color.rgb = NAVY
    p2_sub = s1.shapes[2].text_frame.add_paragraph()
    p2_sub.text = "Shashank Shekhar"
    p2_sub.font.size = Pt(14)
    p2_sub.font.bold = True
    p2_sub.font.color.rgb = TEXT_DARK

    # Student Details
    s1.shapes[3].text_frame.clear()
    p3 = s1.shapes[3].text_frame.paragraphs[0]
    p3.text = "Name: Animesh Soumyadarshi"
    p3.font.bold = True
    p3.font.size = Pt(13)
    p3.font.color.rgb = TEXT_DARK

    details = [
        "Branch: CSE",
        "SIC. No. : 23BCSC65",
        "SEMESTER: 7th"
    ]
    for d in details:
        p = s1.shapes[3].text_frame.add_paragraph()
        p.text = d
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK

    s1.notes_slide.notes_text_frame.text = (
        "Good morning respected evaluators. Today, I am presenting my one-month summer internship on "
        "'Python Using FastAPI', along with the major project I developed: the 'Patient Visit History System'."
    )

    # =============================================================
    # SLIDE 2: INTRODUCTION (Matches Sample Slide 2 + Technical Context)
    # =============================================================
    s2 = prs.slides[1]
    tf2 = s2.shapes[1].text_frame
    tf2.clear()

    intro_points = [
        "This one-month training on Python with FastAPI gave me my first real exposure to backend development and the way modern web APIs are built.",
        "Through it, I got hands-on with Python programming, building REST APIs, handling requests and responses, connecting to MySQL databases, and testing APIs.",
        "As part of the training, I designed and implemented a Patient Visit History System, which showed me how a backend talks to a database and keeps patient consultation records organized.",
        "The project applies industry best practices including Pydantic data validation, SQLAlchemy ORM database abstraction, and live Cloud MySQL persistence with TLS encryption."
    ]

    for idx, text in enumerate(intro_points):
        p = tf2.paragraphs[0] if idx == 0 else tf2.add_paragraph()
        r_arrow = p.add_run()
        r_arrow.text = "▶  "
        r_arrow.font.bold = True
        r_arrow.font.size = Pt(13)
        r_arrow.font.color.rgb = BLUE

        r_text = p.add_run()
        r_text.text = text
        r_text.font.size = Pt(13)
        r_text.font.color.rgb = TEXT_DARK
        p.space_after = Pt(12)

    s2.notes_slide.notes_text_frame.text = (
        "In our introduction, this one-month training gave me practical hands-on exposure to backend engineering. "
        "I learned to build REST APIs, handle requests/responses, connect to MySQL, and successfully developed the Patient Visit History System."
    )

    # =============================================================
    # SLIDE 3: OBJECTIVES (Matches Sample Slide 3)
    # =============================================================
    s3 = prs.slides[2]
    tf3 = s3.shapes[1].text_frame
    tf3.clear()

    sample_objectives = [
        "To build a solid grounding in Python and the basics of backend development.",
        "To get practical experience building REST APIs with FastAPI.",
        "To learn how requests are processed, responses are validated, and CRUD operations work.",
        "To learn how to connect to a database and write SQL queries in MySQL.",
        "To apply API testing, error handling, and debugging in practice.",
        "To build a mini-project, the Patient Visit History System, by combining FastAPI with MySQL."
    ]

    for idx, obj in enumerate(sample_objectives):
        p = tf3.paragraphs[0] if idx == 0 else tf3.add_paragraph()
        r_arrow = p.add_run()
        r_arrow.text = "▶  "
        r_arrow.font.bold = True
        r_arrow.font.size = Pt(13)
        r_arrow.font.color.rgb = BLUE

        r_text = p.add_run()
        r_text.text = obj
        r_text.font.size = Pt(13)
        r_text.font.color.rgb = TEXT_DARK
        p.space_after = Pt(9)

    s3.notes_slide.notes_text_frame.text = (
        "The objectives of my internship were to build strong Python fundamentals, master FastAPI REST APIs, "
        "understand database integration with MySQL, and apply these skills to develop the Patient Visit History System."
    )

    # =============================================================
    # SLIDE 4: CONTENTS OF THE PROGRAM (Matches Sample Slide 4)
    # =============================================================
    s4 = prs.slides[3]
    tf4 = s4.shapes[1].text_frame
    tf4.clear()

    sample_contents = [
        "Over the one-month program, the training moved step by step through Python basics and backend development.",
        "Python basics: syntax, data types, functions, and control flow.",
        "Core concepts of FastAPI and building REST APIs.",
        "Working with HTTP requests and responses, routing, and data validation (Pydantic).",
        "CRUD operations and linking the application to a MySQL database (SQLAlchemy ORM & PyMySQL).",
        "Mini-project: a complete Patient Visit History System built with Python, FastAPI, and Cloud MySQL."
    ]

    for idx, item in enumerate(sample_contents):
        p = tf4.paragraphs[0] if idx == 0 else tf4.add_paragraph()
        r_arrow = p.add_run()
        r_arrow.text = "▶  "
        r_arrow.font.bold = True
        r_arrow.font.size = Pt(13)
        r_arrow.font.color.rgb = BLUE

        r_text = p.add_run()
        r_text.text = item
        r_text.font.size = Pt(13)
        r_text.font.color.rgb = TEXT_DARK
        p.space_after = Pt(9)

    s4.notes_slide.notes_text_frame.text = (
        "The internship program was structured systematically: starting from Python fundamentals, moving to FastAPI routing and validation, "
        "database CRUD with MySQL, and culminating in our final mini-project."
    )

    # =============================================================
    # SLIDE 5: METHODOLOGY — Training Approach & Project Architecture
    # =============================================================
    s5 = prs.slides[4]
    s5.shapes[0].text_frame.text = "METHODOLOGY"
    s5.shapes[0].text_frame.paragraphs[0].font.size = Pt(22)
    s5.shapes[0].text_frame.paragraphs[0].font.bold = True
    s5.shapes[0].text_frame.paragraphs[0].font.color.rgb = NAVY

    # Architecture Image on Left
    arch_img = r"E:\python_fastapi\architecture_diagram.png"
    if os.path.exists(arch_img):
        s5.shapes.add_picture(arch_img, Inches(0.6), Inches(1.6), width=Inches(6.2))

    # Reposition shape 1 (text frame) to the right side
    s5.shapes[1].left = Inches(7.0)
    s5.shapes[1].top = Inches(1.5)
    s5.shapes[1].width = Inches(5.8)
    s5.shapes[1].height = Inches(5.4)

    tf5 = s5.shapes[1].text_frame
    tf5.clear()

    p = tf5.paragraphs[0]
    p.text = "Training Approach & Execution Flow:"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = NAVY
    p.space_after = Pt(4)

    meth_points = [
        ("Theory + Practice: ", "Blended conceptual learning with hands-on coding exercises."),
        ("Environment Setup: ", "Configured Python venv, FastAPI, Uvicorn, and MySQL drivers."),
        ("Client Request: ", "Postman/Browser sends JSON payload (e.g. POST /patients/1/visits)."),
        ("ASGI Processing: ", "Uvicorn asynchronously receives requests and hands to FastAPI."),
        ("Pydantic Validation: ", "Validates types & age constraints BEFORE touching database."),
        ("ORM & Cloud MySQL: ", "SQLAlchemy maps models -> PyMySQL executes queries over TLS on TiDB Cloud MySQL."),
        ("Hydration & Response: ", "ORM hydrates rows; Pydantic serializes JSON with HTTP 201/200.")
    ]

    for h, b in meth_points:
        p = tf5.add_paragraph()
        r1 = p.add_run()
        r1.text = "•  " + h
        r1.font.bold = True
        r1.font.size = Pt(10)
        r1.font.color.rgb = BLUE

        r2 = p.add_run()
        r2.text = b
        r2.font.size = Pt(10)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(2)

    s5.notes_slide.notes_text_frame.text = (
        "In our methodology, the program blended theory with hands-on exercises. "
        "The architecture diagram on the left illustrates how client requests pass through Uvicorn, FastAPI routing, Pydantic validation, "
        "SQLAlchemy ORM, and encrypted cloud MySQL persistence."
    )

    # =============================================================
    # SLIDE 6: METHODOLOGY — Database Design (ER Model)
    # =============================================================
    layout_title_content = prs.slide_layouts[1]
    s_er = prs.slides.add_slide(layout_title_content)

    # Logo
    s_er.shapes.add_picture(io.BytesIO(logo_blob), Inches(9.89), Inches(0.40), width=Inches(2.90), height=Inches(0.88))

    # Title
    s_er.shapes[0].text_frame.text = "METHODOLOGY: Database Design (Entity-Relationship Model)"
    s_er.shapes[0].text_frame.paragraphs[0].font.size = Pt(20)
    s_er.shapes[0].text_frame.paragraphs[0].font.bold = True
    s_er.shapes[0].text_frame.paragraphs[0].font.color.rgb = NAVY

    # ER Image on Left
    er_img = r"E:\python_fastapi\er_diagram.png"
    if os.path.exists(er_img):
        s_er.shapes.add_picture(er_img, Inches(0.6), Inches(1.7), width=Inches(6.3))

    # Text Frame on Right
    s_er.shapes[1].left = Inches(7.1)
    s_er.shapes[1].top = Inches(1.6)
    s_er.shapes[1].width = Inches(5.7)
    s_er.shapes[1].height = Inches(5.2)

    tfer = s_er.shapes[1].text_frame
    tfer.clear()

    p = tfer.paragraphs[0]
    p.text = "Relational Model & Cascade Rules:"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = NAVY
    p.space_after = Pt(4)

    er_points = [
        ("1-to-Many Relationship: ", "One Patient has many consultation Visits (1 : N). Each visit record belongs strictly to one Patient."),
        ("PATIENTS Table: ", "Stores core demographic details (id PK, name, age, gender, contact_number, address, created_at)."),
        ("VISITS Table: ", "Stores clinical data (id PK, patient_id FK, visit_date, doctor_name, diagnosis, prescription, created_at)."),
        ("Foreign Key Constraint: ", "visits.patient_id references patients.id to maintain referential integrity."),
        ("ON DELETE CASCADE: ", "When a patient record is deleted, all their associated medical visits are automatically removed, preventing orphaned records."),
        ("SQLAlchemy Modeling: ", "Implemented via cascade='all, delete-orphan' at the ORM layer and foreign key at MySQL DDL level.")
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
        "Sir, this is our database ER model. There is a 1-to-Many relationship between Patients and Visits. "
        "We configured 'ON DELETE CASCADE' on the foreign key to ensure complete referential integrity."
    )

    # =============================================================
    # SLIDE 7: Projects Done (Matches Sample Slide 6 + Technical Endpoints)
    # =============================================================
    s_pd = prs.slides[5]
    tf_pd = s_pd.shapes[1].text_frame
    tf_pd.clear()

    if len(s_pd.shapes) < 4:
        s_pd.shapes.add_picture(io.BytesIO(logo_blob), Inches(9.89), Inches(0.40), width=Inches(2.90), height=Inches(0.88))

    p = tf_pd.paragraphs[0]
    p.text = "1. Patient Visit History System with Python and FastAPI"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = NAVY

    p_desc = tf_pd.add_paragraph()
    p_desc.text = (
        "Built a backend application in Python with FastAPI for storing and retrieving patient visit records quickly. "
        "Designed REST API endpoints that return a patient's details along with their visit history, giving organized access to visit information. "
        "Used MySQL to store patient data and wrote SQL queries to look up records by patient ID. "
        "Added request handling, data validation, and error handling so the API and database communicate reliably."
    )
    p_desc.font.size = Pt(11)
    p_desc.font.color.rgb = TEXT_DARK
    p_desc.space_after = Pt(8)

    p_sub = tf_pd.add_paragraph()
    p_sub.text = "Implemented REST API Endpoints & Verification:"
    p_sub.font.bold = True
    p_sub.font.size = Pt(12)
    p_sub.font.color.rgb = BLUE

    endpoints = [
        "• Patient Management: POST /patients (Create), GET /patients (List), GET /patients/{id} (Nested Visits), PUT, DELETE.",
        "• Visit History: POST /patients/{id}/visits (Add Visit), GET /patients/{id}/visits, GET /visits/{id}, PUT, DELETE.",
        "• Verification: 100% pass rate in Swagger UI (http://127.0.0.1:8000/docs) and Postman with standard HTTP status codes (201, 200, 404, 422)."
    ]
    for ep in endpoints:
        p = tf_pd.add_paragraph()
        p.text = ep
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(2)

    s_pd.notes_slide.notes_text_frame.text = (
        "Under Projects Done, I built the Patient Visit History System combining FastAPI and MySQL. "
        "All 9 endpoints were implemented and verified with proper request validation, error handling, and status codes."
    )

    # =============================================================
    # SLIDE 8: CONCLUSION (Matches Sample Slide 7)
    # =============================================================
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
    p.text = (
        "This one-month training in Python and FastAPI strengthened both my technical knowledge and my coding skills. "
        "I learned to build REST APIs, work with MySQL databases, and test and debug APIs. "
        "It gave me a firm base in backend development and a clearer picture of how real-world applications are designed and built. "
        "I now feel ready to take on bigger software development challenges and create efficient, dependable applications."
    )
    p.font.size = Pt(14)
    p.font.color.rgb = TEXT_DARK
    p.space_after = Pt(14)

    p_achieve = tf_c.add_paragraph()
    p_achieve.text = "Key Takeaways from the Internship:"
    p_achieve.font.bold = True
    p_achieve.font.size = Pt(13)
    p_achieve.font.color.rgb = NAVY

    concl_bullets = [
        "•  Practical mastery over modern backend API development using FastAPI and asynchronous Python.",
        "•  Hands-on experience with Relational Database Modeling and Cloud MySQL (TiDB Serverless).",
        "•  Professional API documentation, testing, and debugging using Swagger UI and Postman.",
        "•  Confidence to architect scalable, full-stack enterprise solutions."
    ]
    for pt in concl_bullets:
        p = tf_c.add_paragraph()
        p.text = pt
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(2)

    s_concl.notes_slide.notes_text_frame.text = (
        "In conclusion, this one-month training gave me a firm foundation in backend engineering. "
        "I am confident in building scalable REST APIs and handling database integrations. Thank you!"
    )

    # =============================================================
    # SLIDE 9: THANK YOU (Matches Sample Slide 8)
    # =============================================================
    s_thank = prs.slides.add_slide(prs.slide_layouts[6]) # blank layout
    # Add Silicon Logo
    s_thank.shapes.add_picture(io.BytesIO(logo_blob), Inches(9.89), Inches(0.40), width=Inches(2.90), height=Inches(0.88))

    # Center Thank you box
    tbox = s_thank.shapes.add_textbox(Inches(2.0), Inches(2.6), Inches(9.3), Inches(2.2))
    ttf = tbox.text_frame
    p_ty = ttf.paragraphs[0]
    p_ty.text = "THANK YOU"
    p_ty.alignment = PP_ALIGN.CENTER
    p_ty.font.size = Pt(48)
    p_ty.font.bold = True
    p_ty.font.color.rgb = NAVY

    p_qa = ttf.add_paragraph()
    p_qa.text = "Questions & Answers"
    p_qa.alignment = PP_ALIGN.CENTER
    p_qa.font.size = Pt(20)
    p_qa.font.color.rgb = BLUE

    s_thank.notes_slide.notes_text_frame.text = (
        "Thank you respected professors and evaluators for your time and guidance. I am now open to your questions."
    )

    # Move ER slide (index 7) to index 5 (Slide 6, right after Slide 5 Architecture)
    sldIdLst = prs.slides._sldIdLst
    er_slide_id = sldIdLst[7]
    sldIdLst.insert(5, er_slide_id)

    output_path = r"E:\python_fastapi\Patient_Visit_History_Internship_Presentation.pptx"
    prs.save(output_path)
    print(f"Success: Internship presentation saved to {output_path}")

    # Also try saving to Final
    try:
        prs.save(r"E:\python_fastapi\Patient_Visit_History_Final_Presentation.pptx")
        print("Success: Also updated Patient_Visit_History_Final_Presentation.pptx")
    except Exception as e:
        print("Note: Final pptx was open in PowerPoint. Saved cleanly as Patient_Visit_History_Internship_Presentation.pptx")

if __name__ == "__main__":
    build_internship_deck()

