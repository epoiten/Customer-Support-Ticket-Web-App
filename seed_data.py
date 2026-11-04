from app import db, Ticket

sample_tickets = [
    {
        "name": "RN Lukas Weber - Surgical Ward 4B",
        "email": "l.weber@medclinic.org",
        "subject": "B. Braun Infusomat Space #204 - Air-in-Line Sensor False Alarm",
        "description": "Pump triggers continuous air-in-line alarm despite priming new tubing set. Device removed from Room 412 and placed in clean utility room for biomedical inspection.",
        "status": "Open"
    },
    {
        "name": "Dr. Elena Rostova - Post-Op Recovery (PACU)",
        "email": "e.rostova@medclinic.org",
        "subject": "Philips IntelliVue MX450 Monitor #11 - SpO2 Module Not Detecting",
        "description": "Pulse oximetry cable port does not register sensor connection even after swapping with a known working reusable probe. Needs connector pin repair.",
        "status": "In Progress"
    },
    {
        "name": "Charge Nurse Maria Santos - Spine Center Ward",
        "email": "m.santos@medclinic.org",
        "subject": "Mobile Clinical Workstation Cart #08 - Barcode Scanner Disconnected",
        "description": "Handheld medication barcode scanner fails to pair with the workstation dock. Update: IT replaced USB base cable and verified scanning in EHR.",
        "status": "Resolved"
    }
]

with db:
    db.create_tables([Ticket])
    if Ticket.select().count() == 0:
        for item in sample_tickets:
            Ticket.create(**item)
        print("Seeded 3 clinical support tickets into tickets.db!")
    else:
        print("Database already contains tickets. Skipping seed.")