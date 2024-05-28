from dataclasses import dataclass

from autoblocks.testing.models import BaseTestCase
from autoblocks.testing.util import md5


@dataclass
class TestCase(BaseTestCase):
    transcript: str

    def hash(self) -> str:
        """
        This hash serves as a unique identifier for a test case throughout its lifetime.
        """
        return md5(self.transcript)


def gen_test_cases() -> list[TestCase]:
    return [
        TestCase(
            transcript="""
Doctor: Good morning, John Doe. How have you been feeling since our last appointment?

Patient (John Doe): Hello, Doctor. Honestly, I've been struggling a bit with my energy levels, especially when trying to do physical activities like climbing stairs or walking even short distances.

Doctor: I see. Have you noticed any changes or worsening in your joint pains or any other symptoms?

Patient: Yes, the joint pains have been a bit more bothersome. And I've been using my inhaler more often, seems like my asthma isn't as controlled as we thought.

Doctor: Okay, let's make sure we address all of these concerns today. First, let's review your current medications for your high cholesterol, high blood pressure, and diabetes. Are you still taking the prescribed doses without missing any?

Patient: I've been sticking to the schedule you gave me, but I'm not sure they're working as well as we hoped.

Doctor: It's good you're adhering to the medication schedule. Let's consider some adjustments. Also, we need to keep an eye on your blood pressure and sugar levels more closely. How about your sleep? Are you managing to use your CPAP machine for the sleep apnea?

Patient: I try to use it every night. It helps, but sometimes it's uncomfortable, and I end up removing it midway through the night.

Doctor: Consistent use is key for managing sleep apnea, which in turn could help improve your energy levels and possibly your joint pain. Let's explore some options to make it more comfortable for you. We might also need to revisit your diet and exercise routine to help manage these conditions effectively.

Patient: I understand. I'll try to be more consistent with the CPAP. And I'm open to trying new dietary suggestions.

Doctor: Excellent. I'll also refer you to a dietitian who can tailor a plan to your specific health needs. Meanwhile, let's update your prescriptions and schedule a follow-up in six weeks to monitor your progress.

Patient: That sounds good, Doctor. Thank you for your help.

Doctor: You're welcome. Remember, managing these conditions is a team effort. I'm here to support you every step of the way.
            """
        ),
        TestCase(
            transcript="""
Dr. Smith: Good morning, John Doe. How are you feeling today?

John Doe: Good morning, Doctor. I'm okay, just a bit overwhelmed with my situation.

Dr. Smith: I understand. Let’s discuss your current health concerns and what options might be available for you. You mentioned your current weight is around 344 pounds, is that correct?

John Doe: Yes, that's right. And my BMI is about 51.

Dr. Smith: I see you've experienced quite a range of weight over the years, reaching as high as 358 pounds and as low as 260 pounds. Can you tell me a bit about your previous efforts to manage your weight?

John Doe: I've tried multiple diets and exercise programs. Sometimes I lose weight, but I always seem to gain it back, sometimes even more than I lost.

Dr. Smith: That must be frustrating. Have you considered or been informed about surgical options before?

John Doe: I have thought about it, but I never pursued it seriously. I think I’m ready now to consider surgical options to help me manage my weight better.

Dr. Smith: That’s a significant step. Surgical options, like bariatric surgery, can be effective for long-term weight loss, especially when combined with lifestyle changes. We’ll need to conduct some tests to ensure you’re a suitable candidate. Have you had any other health issues like diabetes, hypertension, or sleep apnea?

John Doe: I have hypertension, and I often feel very tired, which I think might be sleep apnea, though it’s not diagnosed.

Dr. Smith: Those are important factors to consider, as they can affect both the feasibility and the urgency of surgery. We'll need to manage these conditions closely. I'll refer you to our dietician and a sleep specialist to evaluate your sleep apnea.

John Doe: That sounds good. I want to do whatever it takes to improve my health.

Dr. Smith: Excellent. We'll start with a full physical examination and some lab tests today. I’ll also set up an appointment with our bariatric surgeon to discuss your surgical options in detail.

John Doe: Thank you, Dr. Smith. I really appreciate your help.

Dr. Smith: You’re welcome, John Doe. We're here to support you every step of the way. Let’s get started with those tests.
"""
        ),
        TestCase(
            transcript="""
Dr. Smith: Good morning, John Doe. How have you been feeling since our last visit?

John Doe: Good morning, Doctor. Not great, honestly. I'm struggling with my mobility, and my joint pain has gotten worse. Climbing stairs is becoming really tough.

Dr. Smith: I'm sorry to hear that. Let's discuss each of your symptoms and see how we can adjust your treatment plan to address these issues more effectively.

John Doe: That sounds good.

Dr. Smith: You mentioned high cholesterol and high blood pressure; how have you been managing these conditions? Are you on medication?

John Doe: Yes, I'm on medication for both. I try to take them regularly.

Dr. Smith: Good, it’s important to stay consistent with those medications. Regarding your diabetes, have you been monitoring your blood sugar levels regularly?

John Doe: I do, but sometimes it's higher than it should be. I guess my diet still needs some adjustments.

Dr. Smith: We'll make sure the dietician helps you with that. It's crucial to keep your blood sugar levels well-controlled, especially as we consider weight loss surgery. How about your sleep apnea?

John Doe: It’s tough; I use a CPAP machine at night, but I still feel very tired during the day.

Dr. Smith: It's important that you're using the CPAP every night. The fatigue could be affecting your overall health and complicating other conditions like your diabetes and heart health. We might need to revisit your sleep specialist to see if there's more we can do.

John Doe: Okay, I’ll keep using it. And about my asthma, it seems worse when I'm more active, even just walking a short distance.

Dr. Smith: Managing your asthma effectively is key, especially as we increase your physical activity to aid weight loss. We might need to adjust your asthma medications or explore additional treatments to help with that.

John Doe: That would be helpful.

Dr. Smith: For your joint pain, once we start decreasing your weight, it should alleviate some of the pressure on your joints. In the meantime, I recommend seeing a physical therapist to help you with exercises that are safe and do not exacerbate the pain.

John Doe: I really hope that helps. I need to be more active but it’s so painful.

Dr. Smith: I understand. It’s a bit of a cycle, but we’re going to tackle it from all sides. Let's start with a gentle, tailored exercise plan from a physical therapist, and continue to focus on your diet and medication adherence.

John Doe: Thank you, Dr. Smith. I appreciate you helping me through this.

Dr. Smith: Absolutely, John Doe. We're in this together. Let’s get you scheduled for those specialist visits and a follow-up with me in six weeks. We’ll monitor your progress closely and adjust as necessary.

John Doe: Sounds good. I’ll see you then.

Dr. Smith: Take care, John Doe. Call the office if you have any concerns before our next appointment.
"""
        ),
        TestCase(
            transcript="""
Dr. Smith: Good morning, John Doe. How have you been feeling since our last meeting?

John Doe: Good morning, Doctor. I've been feeling okay, but I've noticed more trouble with my breathing and my ankles have been swelling a lot more.

Dr. Smith: I see, let's take a closer look today. I'm going to start with a physical examination. [Pauses for examination] I notice some wheezing in both lungs and there is noticeable pitting edema in your lower extremities. Have these symptoms been getting progressively worse?

John Doe: Yes, the breathing issues have been a bit of a problem for a while, but the swelling has become really noticeable over the past few weeks.

Dr. Smith: These symptoms can be indicative of several things, including heart issues, especially given your history of high blood pressure and obesity. The wheezing could be related to your asthma, but we need to rule out any cardiac contributions to these symptoms.

John Doe: What do we need to do?

Dr. Smith: I'm going to order some tests to better understand what's going on:

Chest X-ray to look at the condition of your lungs and heart.
Echocardiogram to assess your heart function.
Blood tests, including kidney function tests and a B-type natriuretic peptide (BNP) test, which will help us determine if this swelling is related to your heart function.
John Doe: Okay, what can we do in the meantime?

Dr. Smith: For now, I recommend elevating your legs when you're sitting to help reduce the swelling. We should also review your asthma action plan and make sure it's optimized to manage your wheezing. If your inhalers aren't giving you relief, we might need to adjust them.

John Doe: I've been using my inhalers, but sometimes they don’t seem to help much.

Dr. Smith: We will address that today. I’m also going to prescribe a diuretic to help with the edema. It should reduce the swelling by helping your body get rid of excess fluid. However, we need to monitor how it affects your blood pressure and kidney function.

John Doe: That sounds good. I just want to feel better.

Dr. Smith: I understand, and we're going to do everything we can to help. I'll schedule a follow-up visit to discuss the results of the tests and adjust our treatment plan based on those findings. In the meantime, if you notice any worsening of these symptoms, especially if you experience any chest pain or difficulty breathing, I want you to contact me immediately or go to the emergency room.

John Doe: Will do, Dr. Smith. Thanks for helping me out.

Dr. Smith: You're welcome, John Doe. Take care and I'll see you soon. We’ll get to the bottom of this.
"""
        ),
        TestCase(
            transcript="""
Dr. Smith: Hello, John Doe. It’s good to see you today. How have you been feeling since your surgery?

John Doe: Hi, Dr. Smith. I've been doing really well! I've lost 20 pounds since the surgery, so now I'm down to 309 pounds.

Dr. Smith: That’s fantastic progress, John Doe! I’m really pleased to hear that. It sounds like you've been sticking to the post-operative diet plan?

John Doe: Yes, I’ve been very careful about following the diet you laid out for me. I’m happy with the weight loss, but I’m a bit worried about keeping the weight off in the long run.

Dr. Smith: It’s great that you’re thinking ahead. Maintaining weight loss after bariatric surgery can be challenging, but with the right strategies, you can sustain your progress. Let’s talk about some of the ways we can support your long-term success.

John Doe: That would be helpful. I really don’t want to go back to where I was before.

Dr. Smith: Absolutely, and our goal is to prevent that. First, continuing with regular follow-up visits like this one is crucial. We can monitor your health, make dietary adjustments as needed, and catch any potential issues early.

John Doe: I understand. What else can I do?

Dr. Smith: Nutrition will continue to be a key focus. Working closely with the dietician will ensure you’re getting balanced meals that meet your reduced caloric needs. It’s also important to gradually increase your physical activity as you lose weight, which will help you burn calories and strengthen your body.

John Doe: I’ve started walking more. I hope that helps.

Dr. Smith: That’s excellent. Walking is a great way to increase your activity level. As you become more comfortable, you might add other activities like swimming or cycling, which are easier on the joints.

John Doe: I’ll definitely try that.

Dr. Smith: Another aspect to consider is psychological support. Sometimes, a counselor or a support group for bariatric patients can make a big difference in staying motivated and addressing any eating habits or emotional eating.

John Doe: I haven’t thought about that, but it makes sense. Sometimes it does get overwhelming.

Dr. Smith: It’s perfectly normal to feel that way. I’ll refer you to a counselor who specializes in post-bariatric surgery care. They can provide support in ways that friends and family, although well-meaning, might not fully understand.

John Doe: Thank you, Dr. Smith. That sounds like a comprehensive plan.

Dr. Smith: You’re welcome, John Doe. Remember, this journey is about gradual improvement and consistency. We’re here to support you every step of the way. Let’s schedule your next follow-up for about a month from now, and we’ll keep a close eye on your progress and adjust the plan as needed.

John Doe: Sounds good. I’ll see you then.

Dr. Smith: Take care, John Doe, and keep up the great work.
"""
        ),
    ]
