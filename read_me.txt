// Run down //

AI -> Flask -> Webpage 


#potentional issue: api key keeps crashing if multiable responses
# incase of more api keys : https://aistudio.google.com/apikey

python HenHack2025/main.py

#maybe create doc strings????

#completed
hook up healthcare test ai files to main
split out the zip code from user 
split out Specialist from ai response


pre promp 
"in futrue prompts you will be provided with a list of symptoms  





<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
incase: 

import google.generativeai as genai

genai.configure(api_key="")

model = genai.GenerativeModel('gemini-1.5-pro-latest')


# Initialize the chat session
# The session is used to maintain the context of the conversation
# Previous chat session cannot be recalled

chat = model.start_chat(history=[])  

def get_ai_response(prompt):
    try:
        response = chat.send_message(prompt) # Add error handling here.
        return response.text
    except Exception as e:
        print(f"Error getting response from Gemini: {e}")
        return "Sorry, I encountered an error processing your request."


def main():
    get_ai_response
    print("Welcome! Let's start a conversation. Type 'exit' to end.")
    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        ai_response = get_ai_response(user_input)
        print("AI: ", ai_response)


if __name__ == "__main__":
    main()


=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

Level II Taxonomy
Acupuncturist
Adult Companion
Advanced Practice Dental Therapist
Advanced Practice Midwife
Air Carrier
Allergy & Immunology
Alzheimer Center /Dementia Center/Dementia Special Care Unit
Ambulance
Anaplastologist
Anesthesiologist Assistant
Anesthesiology
Art Therapist
Assistant Behavior Analyst
Assistant, Podiatric
Assisted Living Facility
Audiologist
Audiologist-Hearing Aid Fitter
Behavior Analyst
Behavior Technician
Blood Bank
Bus
Case Management
Case Manager/Care Coordinator
Chiropractor
Chore Provider
Christian Science Sanitarium(hospital services)
Chronic Disease Hospital
Clinic/Center
Clinical Ethicist
Clinical Exercise Physiologist
Clinical Laboratory Director, Non-physician
Clinical Medical Laboratory
Clinical Neuropsychologist
Clinical Nurse Specialist
Clinical Pharmacology
Colon & Rectal Surgery
Community Based Residential Treatment Facility, Intellectual and/or Developmental Disabilities
Community Based Residential Treatment Facility, Mental Illness
Community Health Worker
Community/Behavioral Health
Contractor
Counselor
Custodial Care Facility
Dance Therapist
Day Training, Developmentally Disabled Services
Day Traning/Habilitation Specialist
Dental Assistant
Dental Hygienist
Dental Laboratory
Dental Laboratory Technician
Dental Therapist
Dentist
Denturist
Department of Veterans Affairs (VA) Pharmacy
Dermatology
Developmental Therapist
Dietary Manager
Dietetic Technician, Registered
Dietitian, Registered
Doula
Drama Therapist
Driver
Durable Medical Equipment & Medical Supplies
Early Intervention Provider Agency
Electrodiagnostic Medicine
Emergency Medical Technician, Basic
Emergency Medical Technician, Intermediate
Emergency Medical Technician, Paramedic
Emergency Medicine
Emergency Response System Companies
Epilepsy Unit
Exclusive Provider Organization
Eye Bank
Eyewear Supplier
Family Medicine
Foster Care Agency
Funeral Director
General Acute Care Hospital
General Practice
Genetic Counselor, MS
Health & Wellness Coach
Health Educator
Health Maintenance Organization
Hearing Aid Equipment
Hearing Instrument Specialist
Home Delivered Meals
Home Health
Home Health Aide
Home Infusion
Homemaker
Homeopath
Hospice Care, Community Based
Hospice, Inpatient
Hospitalist
In Home Supportive Care
Independent Medical Examiner
Indian Health Service/Tribal/Urban Indian Health (I/T/U) Pharmacy
Integrative Medicine
Intermediate Care Facility, Mentally Retarded
Intermediate Care, Mental Illness
Internal Medicine
Interpreter
Kinesiotherapist
Lactation Consultant, Non-RN
Legal Medicine
Legal Medicine
Licensed Practical Nurse
Licensed Psychiatric Technician
Licensed Vocational Nurse
Local Education Agency (LEA)
Lodging
Long Term Care Hospital
Marriage & Family Therapist
Massage Therapist
Mastectomy Fitter
Meals
Mechanotherapist
Medical Foods Supplier
Medical Genetics
Medicare Defined Swing Bed Unit
Midwife
Midwife, Lay
Military Clinical Medical Laboratory
Military Health Care Provider
Military Hospital
Military/U.S. Coast Guard Pharmacy
Military/U.S. Coast Guard Transport
Multi-Specialty
Music Therapist
Naprapath
Naturopath
Neurological Surgery
Neuromusculoskeletal Medicine & OMM
Neuromusculoskeletal Medicine, Sports Medicine
Non-emergency Medical Transport (VAN)
Non-Pharmacy Dispensing Site
Nuclear Medicine
Nurse Anesthetist, Certified Registered
Nurse Practitioner
Nurse's Aide
Nursing Care
Nursing Facility/Intermediate Care Facility
Nursing Home Administrator
Nutritionist
Obstetrics & Gynecology
Occupational Therapist
Occupational Therapy Assistant
Ophthalmology
Optometrist
Oral & Maxillofacial Surgery
Oral Medicinist
Organ Procurement Organization
Orthopaedic Surgery
Orthotics/Prosthetics Fitter
Orthotist
Other Service Providers
Otolaryngology
Pediatrics
Pedorthist
Perfusionist
Personal Emergency Response Attendant
Ph.D. Medical Genetics
Pharmacist
Pharmacy
Pharmacy Technician
Phlebology
Physical Medicine & Rehabilitation
Physical Therapist
Physical Therapy Assistant
Physician Assistant
Physiological Laboratory, (Independent Physiological Lab)
Plastic Surgery
Podiatrist
Poetry Therapist
Point of Service
Portable Xray Supplier
Preferred Provider Organization
Prevention Professional
Private Vehicle
Program of All-Inclusive Care for the Elderly (PACE) Provider Organization
Prosthetic/Orthotic Supplier
Prosthetist
Psychiatric Hospital
Psychiatric Residential Treatment Facility
Psychiatric Unit
Psychoanalyst
Psychologist
Public Health or Welfare
Pulmonary Function Technologist
Radiologic Technologist
Radiology Practitioner Assistant
Recreation Therapist
Recreational Therapist Assistant
Reflexologist
Registered Nurse
Rehabilitation Counselor
Rehabilitation Hospital
Rehabilitation Practitioner
Rehabilitation Unit
Rehabilitation, Substance Use Disorder Unit
Religious Nonmedical Health Care Institution
Religious Nonmedical Nursing Personnel
Religious Nonmedical Practitioner
Residential Treatment Facility, Emotionally Disturbed Children
Residential Treatment Facility, Intellectual and/or Developmental Disabilities
Residential Treatment Facility, Physical Disabilities
Respiratory Therapist, Certified
Respiratory Therapist, Registered
Respite Care
Secured Medical Transport (VAN)
Single Specialty
Skilled Nursing Facility
Sleep Specialist, PhD
Social Worker
Special Hospital
Specialist
Technologist
Cardiovascular
Health Information
Pathology
Speech-Language
Substance Abuse Disorder Rehabilitation Facility
Supports Brokerage
Surgical Technologist
Cardiology
Health Information
Thoracic Surgery
Train
Transplant Surgery
Transportation Broker
Transportation Network Company
Urology
Veterinarian
Voluntary or Charitable
