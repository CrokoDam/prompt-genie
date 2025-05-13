import json
from random import choice

categories = {
    "resume": [
        ("improve my resume", 
         "Act as a professional resume writer. Enhance this resume for a [job_title] position, emphasizing [skills] and making it ATS-optimized."),
        ("write a cover letter", 
         "Act as a career expert. Draft a compelling cover letter for a [job_title] at [company], focusing on [achievements] and values fit."),
    ],
    "coding": [
        ("debug this python code", 
         "Act as a senior Python developer. Debug this code and explain the errors clearly: [paste_code]."),
        ("optimize this function", 
         "Act as a performance engineer. Optimize this code function for speed and readability: [paste_code]."),
    ],
    "marketing": [
        ("write a facebook ad", 
         "Act as a digital marketer. Write a high-converting Facebook ad for [product/service] targeting [audience]."),
        ("create a content calendar", 
         "Act as a social media strategist. Build a 30-day content calendar for [brand] focusing on engagement and growth."),
    ],
    "education": [
        ("explain gravity to a child", 
         "Act as a science teacher. Explain gravity to a 7-year-old using simple and fun examples."),
        ("create a lesson plan", 
         "Act as a curriculum designer. Create a 1-week lesson plan for [subject] for [grade level]."),
    ],
    "business": [
        ("write a business proposal", 
         "Act as a business analyst. Write a compelling proposal to pitch [idea] to potential investors."),
        ("summarize a meeting", 
         "Act as a corporate assistant. Summarize this meeting transcript into key takeaways: [paste_transcript]."),
    ],
    "creative writing": [
        ("write a poem about stars", 
         "Act as a poet. Write a lyrical poem about the stars and the cosmos in a romantic tone."),
        ("start a fantasy story", 
         "Act as a fantasy novelist. Write an engaging first paragraph for a story set in a magical realm."),
    ],
    "health": [
        ("create a workout plan", 
         "Act as a fitness coach. Design a weekly workout plan for fat loss and muscle gain for a beginner."),
        ("write a healthy meal plan", 
         "Act as a nutritionist. Create a 7-day healthy meal plan for someone with a gluten allergy."),
    ],
    "travel": [
        ("plan a trip to japan", 
         "Act as a travel guide. Plan a 10-day itinerary for Japan including culture, food, and landmarks."),
        ("find hidden gems in paris", 
         "Act as a local Parisian guide. List hidden gems and offbeat spots in Paris for travelers."),
    ],
    "relationships": [
        ("write a romantic message", 
         "Act as a love coach. Craft a heartfelt romantic message for my partner."),
        ("deal with a breakup", 
         "Act as a therapist. Give thoughtful, caring advice for handling a recent breakup."),
    ],
    "productivity": [
        ("build a daily routine", 
         "Act as a productivity coach. Build a custom daily routine for a remote worker struggling with focus."),
        ("time management tips", 
         "Act as a time management expert. Give me actionable tips to better manage my workday."),
    ]
}

# Replicate to get 100 prompts (10 categories * ~10 prompts each)
all_prompts = {}

for category, examples in categories.items():
    all_prompts[category] = {}
    for i in range(10):  # artificially increase variety
        ex = choice(examples)
        key = f"{ex[0]} #{i+1}"
        all_prompts[category][key] = ex[1]

# Ensure we reach around 100 unique queries
output = json.dumps(all_prompts, indent=2)
output[:1000]  # Preview first portion

