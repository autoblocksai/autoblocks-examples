from dataclasses import dataclass

from autoblocks.testing.models import BaseTestCase
from autoblocks.testing.util import md5
from autoblocks_pinecone.data.medical_records import MedicalRecord


@dataclass
class TestCase(BaseTestCase):
    existing_treatment_plan: str
    medical_records: list[MedicalRecord]

    def hash(self) -> str:
        """
        This hash serves as a unique identifier for a test case throughout its lifetime.
        """
        return md5(self.existing_treatment_plan)


def gen_test_cases() -> list[TestCase]:
    return [
        TestCase(
            existing_treatment_plan="""
Summary of Current Health Status:

Smoking: Successfully quit smoking, smoke-free for two months with the aid of Chantix.
Diet: Continues to struggle with dietary habits.
Alcohol Consumption: Significantly reduced.
Chronic Conditions: High cholesterol, high blood pressure, diabetes, sleep apnea, joint pains, and asthma.
Medications:

Continue current medications for high cholesterol, high blood pressure, and diabetes as prescribed.
Continue using CPAP machine nightly to manage sleep apnea.
Complete the course of Chantix under supervision to ensure smoking cessation is sustained.
Goals for the Next Period:

Dietary Improvement:

Consultation with a dietitian to create a personalized meal plan focusing on managing diabetes and high cholesterol.
Implement structured meal plans with specific, achievable goals (e.g., incorporate a vegetable side dish with every meal, replace red meat with fish twice a week).
Physical Activity:

Gradual increase in physical activity, starting with daily walks, increasing duration as tolerated.
Introduction to low-impact exercises like swimming or cycling to manage joint pains and improve cardiovascular health.
Weight Management:

Set a realistic weight loss goal (e.g., 1-2 pounds per month).
Regular weigh-ins at follow-up visits to track progress and maintain motivation.
Asthma Management:

Regular use of prescribed inhalers.
Schedule a consultation with a pulmonologist to reassess asthma management and adjust medication if necessary.
Mental Health:

Discuss stressors and mental health with a counselor, especially as related to lifestyle changes and chronic disease management.
Consider joining a support group for individuals with similar health challenges.
Follow-Up Schedule:

4 Weeks: Telemedicine appointment to discuss progress with dietary changes and address any immediate concerns.
8 Weeks: In-office visit to evaluate physical health, review medication efficacy, and make adjustments to the treatment plan based on progress.
Additional Recommendations:

Engage in daily monitoring of blood pressure and blood sugar levels.
Maintain a daily journal of food intake, physical activity, and asthma symptoms to monitor trends and adjust treatment plans as needed.
Doctor's Notes:
John Doe has made commendable progress in smoking cessation and reducing alcohol consumption. It is crucial to build on this momentum by addressing dietary habits and increasing physical activity to improve overall health and manage chronic conditions effectively.
""",
            medical_records=[
                MedicalRecord(
                    id="9_2_History of Present Illness",
                    text="John Doe returns for a follow-up regarding his lifestyle changes. He has successfully quit smoking with the aid of Chantix and has been smoke-free for two months. He continues to struggle with dietary habits but has reduced alcohol consumption significantly.",
                )
            ],
        ),
        TestCase(
            existing_treatment_plan="""
1. Diagnostic Evaluation:

Full Physical Examination: To assess overall health status and identify any obesity-related complications.
Laboratory Tests: Comprehensive metabolic panel, lipid profile, thyroid function tests, fasting glucose, HbA1c to evaluate for diabetes, and liver function tests.
Sleep Study: Refer to a sleep specialist to conduct a sleep apnea evaluation due to reported symptoms of excessive fatigue.
Nutritional Assessment: Consultation with a dietician to review current dietary habits and develop a structured nutritional plan.
2. Medical Management:

Hypertension Management: Continue current antihypertensive medication and monitor blood pressure regularly. Adjustments to medication may be needed based on weight changes and overall health improvements.
Pre-operative Optimization: If surgical intervention is decided, optimize medical conditions to reduce surgical risks. This includes management of blood pressure, glucose levels, and ensuring nutritional deficiencies are addressed.
3. Lifestyle Modifications:

Dietary Changes: Implement a calorie-restricted diet tailored by the dietician to initiate gradual weight loss. Focus on nutrient-dense foods and portion control.
Physical Activity: Gradual introduction of a structured exercise program, beginning with low-impact activities such as walking, swimming, or stationary cycling, increasing in intensity as tolerated.
Behavioral Therapy: Engage with a psychologist or counselor specializing in obesity to address behavioral factors contributing to weight gain and to support dietary and lifestyle changes.
4. Surgical Consultation:

Evaluation by a Bariatric Surgeon: Discuss the types of bariatric surgery, potential benefits, risks, and long-term lifestyle implications. Ensure John Doe is a suitable candidate for surgery.
Pre-surgical Education: Attend seminars or counseling sessions to fully understand the surgical process, post-operative care, and necessary lifestyle adjustments.
5. Ongoing Monitoring and Support:

Regular Follow-ups: Schedule monthly follow-ups with the primary care team to monitor weight loss progress, adjust treatment plans, and provide continuous support.
Post-surgical Support: If surgery is performed, engage in a structured post-operative program that includes regular check-ups with the surgical team, ongoing nutritional counseling, and support group participation.
6. Reassessment:

Annual Review: Conduct an annual comprehensive evaluation to assess long-term outcomes of weight management strategies, including the effectiveness of surgical intervention if undertaken, and make adjustments as needed.
""",
            medical_records=[
                MedicalRecord(
                    id="3_1_History of Present Illness",
                    text="John Doe, a 42-year-old male, presents for a consultation regarding weight management. He reports a longstanding history of obesity, with a current weight of 344 pounds and a BMI of 51. He mentions a highest recorded weight of 358 pounds and a lowest of 260 pounds, indicating significant weight fluctuations. John Doe expresses a strong desire to pursue surgical weight loss options to improve his health and mobility. He reports physical sluggishness, rapid fatigue, and limited social outings due to his weight.",
                )
            ],
        ),
        TestCase(
            existing_treatment_plan="""
1. Diagnostic Evaluation:

Comprehensive Physical Examination: To evaluate the overall impact of obesity and associated comorbidities.
Laboratory Tests: Repeat comprehensive metabolic panel, lipid profile, HbA1c, fasting glucose, and thyroid function tests. Assess renal function and electrolytes to monitor medication effects and disease progression.
Pulmonary Function Test: To evaluate asthma control and necessity for medication adjustment.
Sleep Study Review: Re-evaluate the effectiveness of current CPAP settings and sleep apnea management strategies.
2. Medical Management:

High Cholesterol and Blood Pressure: Continue current medications and monitor lipid profiles and blood pressure monthly. Adjust medications as needed based on lab results and weight changes.
Diabetes Management: Intensify glycemic control through medication adjustment and dietary counseling. Regular monitoring of blood glucose levels at home.
Asthma Management: Review current asthma action plan and adjust medications as needed. Consider referral to a pulmonologist if symptoms persist or worsen.
Joint Pain: Referral to a physical therapist for low-impact exercises designed to strengthen muscles without putting undue stress on joints. Consider non-steroidal anti-inflammatory drugs (NSAIDs) or other pain relief measures as appropriate.
3. Lifestyle Modifications:

Dietary Changes: Consult with a dietician to refine a diabetes-friendly, heart-healthy diet that also accommodates weight loss goals. Focus on low-calorie, nutrient-rich foods to manage weight, cholesterol, and blood sugar levels.
Physical Activity: Gradual introduction of physical activity, guided by a physical therapist to ensure safety and efficacy. Emphasize activities that improve cardiovascular health without exacerbating joint pain or asthma symptoms.
Weight Management: Explore medically supervised weight loss programs, including behavioral counseling to address emotional eating and improve adherence to lifestyle changes.
4. Surgical Consultation:

Bariatric Surgery Evaluation: Consider potential candidacy for bariatric surgery based on comprehensive health assessment and failure to achieve significant weight loss through non-surgical means. Discuss risks, benefits, and long-term commitment to lifestyle changes.
5. Ongoing Monitoring and Support:

Regular Follow-ups: Schedule monthly follow-ups with the primary care team to monitor progress, make necessary adjustments to the treatment plan, and provide motivation and support.
Specialist Visits: Regular appointments with a pulmonologist, endocrinologist, and cardiologist to optimize management of asthma, diabetes, and cardiovascular health, respectively.
Psychological Support: Regular sessions with a psychologist or counselor to address psychological impacts of chronic illness and support adherence to lifestyle changes.
6. Reassessment:

Annual Comprehensive Review: Assess the effectiveness of the treatment plan and make adjustments as needed. Review all medications, lifestyle changes, and overall health improvements.
            """,
            medical_records=[
                MedicalRecord(
                    id="4_1_Past Medical History",
                    text="Includes high cholesterol, high blood pressure, diabetes, sleep apnea, joint pains, and asthma. John Doe has difficulty with physical activities like climbing stairs and walking short distances.",
                )
            ],
        ),
        TestCase(
            existing_treatment_plan="""
1. Immediate Care:

Medication Adjustment:
Diuretics: Prescribe to manage edema. Monitor for electrolyte imbalances and effects on kidney function.
Asthma Inhalers: Review and possibly adjust current asthma medication to better control wheezing.
Continued Hypertension Management: Ensure that diuretic use does not adversely affect blood pressure control.
2. Diagnostic Evaluation:

Chest X-ray: To assess the lung fields for any signs of congestion or other abnormalities and to evaluate the heart silhouette for signs of enlargement.
Echocardiogram: To evaluate heart function, looking for signs of heart failure or structural heart disease.
Blood Tests:
Kidney Function Tests: To assess baseline kidney function before initiating diuretic therapy.
BNP Test: To evaluate for heart failure.
Complete Blood Count and Comprehensive Metabolic Panel: To check for any other underlying issues.
3. Lifestyle Modifications:

Leg Elevation: Advise the patient to elevate his legs when sitting to help reduce edema.
Salt Intake Reduction: Counsel on reducing salt intake to decrease fluid retention.
Physical Activity: Encourage gentle exercises like swimming or seated exercises that do not stress the joints but help with circulation.
4. Monitoring and Follow-up:

Follow-up Appointment: Schedule a follow-up within two weeks to assess the response to the diuretic and adjustments in asthma treatment. Review the results of the diagnostic tests and adjust the treatment plan accordingly.
Regular Monitoring: Schedule regular check-ups to monitor blood pressure, kidney function, and response to the adjusted asthma treatment.
Emergency Plan: Educate on recognizing symptoms of worsening heart failure or asthma attacks, such as increasing shortness of breath, chest pain, or severe swelling, and when to seek emergency care.
5. Specialist Referrals:

Pulmonologist Consultation: Refer to a pulmonologist if asthma symptoms do not improve with current treatment adjustments.
Cardiologist Consultation: Depending on the results of the echocardiogram and other tests, a consultation with a cardiologist may be necessary to further assess and manage potential heart-related issues.
            """,
            medical_records=[
                MedicalRecord(
                    id="5_1_Physical Examination",
                    text="The patient is alert and oriented. Examination shows wheezing bilaterally in the lungs and 1+ pitting edema in the lower extremities.",
                )
            ],
        ),
        TestCase(
            existing_treatment_plan="""
1. Ongoing Monitoring and Support:

Regular Follow-up Visits: Schedule monthly follow-up appointments to monitor weight loss, nutritional intake, and overall health. Use these visits to adjust dietary plans, physical activity recommendations, and address any medical concerns.
2. Nutritional Guidance:

Dietician Consultations: Continue regular sessions with a dietician to ensure John Doe is receiving balanced nutrition suitable for his reduced stomach capacity. Focus on high-protein, low-carb meals that are rich in vitamins and minerals to prevent deficiencies.
Supplemental Support: Prescribe vitamin and mineral supplements as needed to address common post-bariatric surgery deficiencies such as vitamin B12, iron, calcium, and vitamin D.
3. Physical Activity Enhancement:

Gradual Exercise Program: Encourage a gradual increase in physical activity. Start with daily walks and progressively introduce low-impact exercises such as swimming or cycling as tolerated by John Doe’s joint health and overall endurance.
Physical Therapist Consultation: If necessary, refer to a physical therapist to design a personalized exercise program that considers John Doe's specific physical capabilities and weight loss goals.
4. Psychological Support:

Counseling Services: Refer John Doe to a psychologist or counselor specializing in weight management and bariatric surgery. Focus on developing strategies to manage emotional eating and maintain motivation for lifestyle changes.
Support Groups: Encourage participation in support groups for bariatric patients to share experiences and strategies, enhancing social support and commitment to sustained weight management.
5. Long-term Management Strategies:

Lifestyle Education: Provide ongoing education on the importance of lifestyle changes post-bariatric surgery, including the relationship between diet, exercise, and weight maintenance.
Preventive Care: Schedule routine screenings for conditions commonly associated with obesity, such as hypertension, diabetes, and cardiovascular disease, to ensure they remain well-managed or mitigated.
6. Emergency Plan:

Recognizing Complications: Educate John Doe on the signs of potential post-operative complications, such as nausea, vomiting, excessive pain, or signs of nutrient deficiencies (e.g., extreme fatigue, hair loss). Provide instructions on when to seek immediate medical attention.
            """,
            medical_records=[
                MedicalRecord(
                    id="25_5_History of Present Illness",
                    text="John Doe reports adherence to the post-operative diet. He has lost an additional 20 pounds since the surgery, bringing his weight down to 309 pounds. He expresses happiness with his progress but concerns about maintaining weight loss long-term.",
                )
            ],
        ),
    ]
