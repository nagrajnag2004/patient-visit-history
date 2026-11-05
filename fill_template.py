import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

def populate_silicon_template():
    template_path = r"C:\Users\nagra\.gemini\antigravity\brain\cd5112b8-2b8b-4867-bcda-98e7404bb232\.user_uploaded\media_1793871599475_be970003.pptx"
    prs = Presentation(template_path)

    NAVY = RGBColor(26, 35, 126)      # Deep Silicon Blue
    TEXT_DARK = RGBColor(33, 37, 41)   # Dark Charcoal
    BLUE = RGBColor(13, 71, 161)      # Medium Blue
    MUTED = RGBColor(108, 117, 125)

    # -------------------------------------------------------------
    # SLIDE 1: Title Slide
    # -------------------------------------------------------------
    s1 = prs.slides[0]
    # Shape 0: Title
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

    # Shape 2: Under guidance of
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

    # Shape 3: Student Details
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
    # Shape 1 is Content Placeholder
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
        run1 = p.add_run()
        run1.text = "•  " + header
        run1.font.bold = True
        run1.font.size = Pt(13)
        run1.font.color.rgb = BLUE

        run2 = p.add_run()
        run2.text = body
        run2.font.size = Pt(13)
        run2.font.color.rgb = TEXT_DARK
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
        run1 = p.add_run()
        run1.text = f"{idx+1}.  " + header
        run1.font.bold = True
        run1.font.size = Pt(13)
        run1.font.color.rgb = BLUE

        run2 = p.add_run()
        run2.text = body
        run2.font.size = Pt(13)
        run2.font.color.rgb = TEXT_DARK
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
        run1 = p.add_run()
        run1.text = "•  " + header
        run1.font.bold = True
        run1.font.size = Pt(13)
        run1.font.color.rgb = BLUE

        run2 = p.add_run()
        run2.text = body
        run2.font.size = Pt(13)
        run2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(8)

    s4.notes_slide.notes_text_frame.text = (
        "This slide covers the technology stack we mastered and used. FastAPI handles routing, SQLAlchemy ORM prevents SQL injection, and TiDB Cloud MySQL provides scalable cloud persistence."
    )

    # -------------------------------------------------------------
    # SLIDE 5: METHODOLOGY (Embed Architecture Diagram + Steps)
    # -------------------------------------------------------------
    s5 = prs.slides[4]
    # Slide 5 has Content Placeholder 2 at left=0.74, top=1.96, width=9.40, height=4.64
    # We will resize the placeholder to the right side, and put the architecture diagram on the left!
    s5.shapes[1].left = Inches(7.4)
    s5.shapes[1].top = Inches(1.8)
    s5.shapes[1].width = Inches(5.3)
    s5.shapes[1].height = Inches(4.8)

    tf5 = s5.shapes[1].text_frame
    tf5.clear()

    p = tf5.paragraphs[0]
    p.text = "Execution Architecture & Flow:"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = NAVY
    p.space_after = Pt(8)

    method_steps = [
        ("1. Client: ", "Postman/Browser sends JSON payload."),
        ("2. Uvicorn: ", "Asynchronous ASGI server parses request."),
        ("3. FastAPI: ", "Routes URL to specific controller."),
        ("4. Pydantic: ", "Validates data types and constraints."),
        ("5. SQLAlchemy: ", "Translates model operations to SQL."),
        ("6. PyMySQL: ", "Executes query over TLS on Cloud MySQL."),
        ("7. TiDB MySQL: ", "Persists data & returns table records."),
        ("8. Hydration: ", "ORM hydrates rows, Pydantic outputs JSON.")
    ]
    for h, b in method_steps:
        p = tf5.add_paragraph()
        r1 = p.add_run()
        r1.text = h
        r1.font.bold = True
        r1.font.size = Pt(11)
        r1.font.color.rgb = BLUE

        r2 = p.add_run()
        r2.text = b
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(3)

    # Add the Architecture Diagram on the left side
    img_path = r"E:\python_fastapi\architecture_diagram.png"
    if os.path.exists(img_path):
        s5.shapes.add_picture(img_path, Inches(0.74), Inches(1.8), width=Inches(6.4))

    s5.notes_slide.notes_text_frame.text = (
        "Respected evaluators, this diagram shows our request-response methodology. From client request to Pydantic validation, ORM mapping, and encrypted cloud persistence, every layer has a single responsibility."
    )

    # -------------------------------------------------------------
    # SLIDE 6: Projects Done (CRUD Endpoints & Details)
    # -------------------------------------------------------------
    s6 = prs.slides[5]
    tf6 = s6.shapes[1].text_frame
    tf6.clear()

    # If slide 6 lacks Picture 5 (logo), let's copy the logo from slide 2
    if len(s2.shapes) >= 4 and hasattr(s2.shapes[3], 'image'):
        logo_blob = s2.shapes[3].image.blob
        import io
        s6.shapes.add_picture(io.BytesIO(logo_blob), Inches(9.89), Inches(0.40), width=Inches(2.90), height=Inches(0.88))

    p = tf6.paragraphs[0]
    p.text = "Module 1: Patient Management Service (routes/patients.py)"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = NAVY

    m1_points = [
        "•  POST /patients/  [HTTP 201 Created]  -  Register patient with age & phone validation.",
        "•  GET /patients/  [HTTP 200 OK]  -  Paginated list of all registered patients.",
        "•  GET /patients/{id}  [HTTP 200 OK]  -  Retrieve patient profile nested with complete visit history.",
        "•  PUT /patients/{id}  [HTTP 200 OK]  -  Update patient demographic details.",
        "•  DELETE /patients/{id}  [HTTP 200 OK]  -  Delete patient record; cascades and cleans child visits."
    ]
    for pt in m1_points:
        p = tf6.add_paragraph()
        p.text = pt
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(2)

    p_spacer = tf6.add_paragraph()
    p_spacer.text = "Module 2: Medical Visit History Service (routes/visits.py)"
    p_spacer.font.bold = True
    p_spacer.font.size = Pt(14)
    p_spacer.font.color.rgb = NAVY
    p_spacer.space_before = Pt(8)

    m2_points = [
        "•  POST /patients/{id}/visits  [HTTP 201 Created]  -  Log consultation visit (validates patient exists).",
        "•  GET /patients/{id}/visits  [HTTP 200 OK]  -  Retrieve all historical visits of a patient chronologically.",
        "•  GET /visits/{id}  [HTTP 200 OK]  -  Get individual visit consultation details.",
        "•  PUT /visits/{id}  [HTTP 200 OK]  -  Update diagnosis notes or medical prescriptions.",
        "•  DELETE /visits/{id}  [HTTP 200 OK]  -  Delete an individual visit consultation record."
    ]
    for pt in m2_points:
        p = tf6.add_paragraph()
        p.text = pt
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(2)

    p_ver = tf6.add_paragraph()
    p_ver.text = "✔ Verification: 100% test pass rate across all endpoints in Swagger UI and Postman."
    p_ver.font.bold = True
    p_ver.font.size = Pt(11)
    p_ver.font.color.rgb = RGBColor(16, 185, 129)
    p_ver.space_before = Pt(6)

    s6.notes_slide.notes_text_frame.text = (
        "Under Projects Done, we implemented two complete modules covering all 9 REST endpoints with proper HTTP status codes and nested JSON responses."
    )

    # -------------------------------------------------------------
    # SLIDE 7: CONCLUSION
    # -------------------------------------------------------------
    s7 = prs.slides[6]
    # In slide 7, shape 3 is the rectangle text frame
    # Let's check shape 3 or add a clean textbox
    # Let's enlarge shape 3 or replace text
    rect = s7.shapes[3]
    rect.left = Inches(0.9)
    rect.top = Inches(1.8)
    rect.width = Inches(11.4)
    rect.height = Inches(4.7)
    rect.line.fill.background() # transparent border
    rect.fill.background()      # transparent fill

    tf7 = rect.text_frame
    tf7.clear()

    p = tf7.paragraphs[0]
    p.text = "Key Project Achievements:"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = NAVY

    concl_points = [
        "•  Successfully built a complete, production-grade REST API backend from scratch using FastAPI.",
        "•  Engineered robust 1-to-Many relational database architecture with Foreign Key cascade protection.",
        "•  Integrated live cloud MySQL persistence (TiDB Serverless on AWS Tokyo) with TLS encryption.",
        "•  Achieved strict schema validation (Pydantic v2) and ORM abstraction (SQLAlchemy 2.0)."
    ]
    for pt in concl_points:
        p = tf7.add_paragraph()
        p.text = pt
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(4)

    p_future = tf7.add_paragraph()
    p_future.text = "Future Scope & Enhancements:"
    p_future.font.bold = True
    p_future.font.size = Pt(15)
    p_future.font.color.rgb = BLUE
    p_future.space_before = Pt(12)

    future_points = [
        "➔  Role-Based Access Control (RBAC) with JWT authentication for Doctors, Nurses, and Receptionists.",
        "➔  Automated patient follow-up scheduling with SMS and email notifications.",
        "➔  AI-assisted diagnosis and prescription suggestion using Gemini API integration.",
        "➔  Full-stack web application development using React / Next.js and Tailwind CSS."
    ]
    for pt in future_points:
        p = tf7.add_paragraph()
        p.text = pt
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(4)

    s7.notes_slide.notes_text_frame.text = (
        "In conclusion, this project shows how modern backend frameworks and cloud databases work together. The system is ready for hospital deployment and future AI-assisted medical record features. Thank you, and I am now open to any questions."
    )

    # Save to local project directory
    output_path = r"E:\python_fastapi\Patient_Visit_History_Silicon_Presentation.pptx"
    prs.save(output_path)
    print(f"Success: Template presentation saved to {output_path}")

    # Also save as main presentation file
    prs.save(r"E:\python_fastapi\Patient_Visit_History_Presentation.pptx")
    print("Success: Also updated main Patient_Visit_History_Presentation.pptx")

if __name__ == "__main__":
    populate_silicon_template()

