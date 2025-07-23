import streamlit as st
import pandas as pd

# Define skincare recommendations for each skin type
SKINCARE_RECOMMENDATIONS = {
    "Dry": {
        "Cleanser": ["Creamy, hydrating cleanser (e.g., CeraVe Hydrating Cleanser)", "Oil-based cleanser for makeup removal"],
        "Moisturizer": ["Rich, occlusive cream with ceramides, hyaluronic acid, shea butter (e.g., La Roche-Posay Lipikar Balm AP+, Aquaphor)"],
        "Serum": ["Hyaluronic acid serum", "Squalane oil", "Glycerin-based serums"],
        "SPF": ["Cream-based SPF 30+ (e.g., EltaMD UV Physical Broad-Spectrum SPF 41)"],
        "Treatments": ["Sleeping masks", "Facial oils"]
    },
    "Normal": {
        "Cleanser": ["Gentle foaming or gel cleanser (e.g., Fresh Soy Face Cleanser)"],
        "Moisturizer": ["Lightweight, non-comedogenic lotion or cream (e.g., Neutrogena Hydro Boost Water Gel)"],
        "Serum": ["Vitamin C serum (for glow and antioxidants)", "Hyaluronic acid serum (for hydration)"],
        "SPF": ["Broad-spectrum SPF 30+ (e.g., Supergoop! Unseen Sunscreen SPF 40)"],
        "Treatments": ["Occasional hydrating masks", "Antioxidant-rich serums"]
    },
    "Combination": {
        "Cleanser": ["Gentle foaming or gel cleanser (e.g., COSRX Low pH Good Morning Gel Cleanser)"],
        "Moisturizer": ["Lightweight, oil-free moisturizer for oily areas, slightly richer cream for dry areas (e.g., Paula's Choice Water-Infusing Electrolyte Moisturizer)"],
        "Serum": ["Niacinamide serum (for oil balance and pores)", "Hyaluronic acid serum (for hydration)"],
        "SPF": ["Non-comedogenic, lightweight SPF 30+ (e.g., Biore UV Aqua Rich Watery Essence SPF 50+)"],
        "Treatments": ["Clay masks (for T-zone), hydrating masks (for dry areas)", "BHA (salicylic acid) for congested areas"]
    },
    "Oily": {
        "Cleanser": ["Foaming or gel cleanser with salicylic acid (e.g., La Roche-Posay Effaclar Purifying Foaming Gel Cleanser)"],
        "Moisturizer": ["Lightweight, oil-free, non-comedogenic gel moisturizer (e.g., Innisfree Green Tea Seed Hyaluronic Serum)"],
        "Serum": ["Niacinamide serum", "Salicylic acid serum (BHA)"],
        "SPF": ["Matte-finish, oil-free SPF 30+ (e.g., ISDIN Eryfotona Actinica)"],
        "Treatments": ["Clay masks", "Oil-absorbing blotting papers", "Retinoids (under guidance for acne)"]
    },
    "Sensitive": {
        "Cleanser": ["Creamy, gentle, fragrance-free cleanser (e.g., Vanicream Gentle Facial Cleanser)"],
        "Moisturizer": ["Fragrance-free, hypoallergenic cream with ceramides (e.g., Aveeno Calm + Restore Oat Gel Moisturizer)"],
        "Serum": ["Centella Asiatica (Cica) serum", "Oat-based serums", "Aloe vera"],
        "SPF": ["Mineral-based (zinc oxide, titanium dioxide) SPF 30+ (e.g., Blue Lizard Sensitive Skin Mineral Sunscreen)"],
        "Treatments": ["Soothing masks", "Minimal ingredient routines"]
    }
}

# --- Custom CSS for Pink Theme ---
# You can adjust the hex code for different shades of pink!
PINK_THEME_CSS = """
<style>
/* Main app background color */
.stApp {
  background-color: #FFF0F5; /* LavenderBlush - a soft, cute pink */
}

/* Make headers and text a slightly darker pink for contrast */
h1, h2, h3, h4, h5, h6 {
    color: #FF69B4; /* HotPink */
}

/* Input boxes and buttons can also get a subtle pink border or shadow */
.stTextInput > div > div > input {
    border: 1px solid #FFC0CB; /* Pink */
    box-shadow: 2px 2px 5px rgba(255, 192, 203, 0.5);
}

.stButton > button {
    background-color: #FF69B4; /* HotPink */
    color: white; /* THIS IS THE CHANGE FOR BUTTON TEXT COLOR */
    border-radius: 12px;
    padding: 10px 20px;
    font-size: 1.1em;
    box-shadow: 2px 2px 5px rgba(255, 192, 203, 0.7);
}
.stButton > button:hover {
    background-color: #FF1493; /* DeepPink */
    box-shadow: 3px 33px 8px rgba(255, 192, 203, 0.9);
}

/* Radio buttons could have a pink accent */
.stRadio > label {
    color: #FF69B4; /* HotPink */
    font-weight: bold;
}
.stRadio > label > div > div:first-child {
    border: 2px solid #FFC0CB; /* Pink for radio circle */
}
.stRadio > label > div > div:first-child > div {
    background-color: #FF69B4; /* HotPink for selected radio dot */
}


</style>
"""

# --- Common Mistakes to Avoid ---
def display_common_mistakes():
    st.markdown("---")
    st.markdown("### 🚫 **Common Skincare Mistakes to Avoid!** 🚫")
    st.markdown("Let's make sure we're not accidentally sabotaging our skin's glow, sweetie! Here are some big no-nos:")
    st.markdown("- **🥺 Over-Exfoliating:** Using harsh scrubs or too many active ingredients can strip your skin's barrier, leading to irritation, redness, and even more breakouts! Be gentle and know your limits. ✨")
    st.markdown("- **☀️ Skipping SPF Daily:** This is a huge one! UV rays cause premature aging, dark spots, and can worsen acne. Sunscreen is your non-negotiable bestie, every single day, rain or shine! 💖")
    st.markdown("- **🖐️ Picking at Pimples/Blemishes:** I know, it's SO tempting, but squeezing or picking can push bacteria deeper, cause inflammation, scarring, and even infection. Let them heal naturally or use a spot treatment! 🙅‍♀️")
    st.markdown("- **🚿 Using Hot Water:** Super hot showers or face washes can strip your skin of its natural oils, leading to dryness and irritation. Lukewarm water is always the kindest choice! 💧")
    st.markdown("- **😬 Not Moisturizing Oily Skin:** Even oily skin needs moisturizer! Skipping it can trick your skin into producing *more* oil to compensate. Choose a lightweight, non-comedogenic formula. 🌿")
    st.markdown("- **🛌 Sleeping with Makeup On:** Oh no, sweetie! This clogs pores, leads to breakouts, and can make your skin look dull. Always cleanse your face thoroughly before bed! 🌙")
    st.markdown("- **🧴 Not Patch Testing New Products:** Especially for sensitive skin! Always try a new product on a small, inconspicuous area (like behind your ear or on your inner arm) for 24-48 hours before applying it all over. 🌱")
    st.markdown("---")
    st.markdown("Avoiding these little traps will help your skin truly flourish! You've got this! 💖")

def display_recommendations(skin_type):
    """Helper function to display recommendations for a given skin type."""
    if skin_type in SKINCARE_RECOMMENDATIONS:
        recs = SKINCARE_RECOMMENDATIONS[skin_type]
        st.markdown(f"Here are some lovely product recommendations for your **{skin_type} Skin!** 💖")
        
        st.markdown("### **✨ Cleanser Recommendations ✨**")
        for item in recs.get("Cleanser", []):
            st.markdown(f"- {item}")
        
        st.markdown("### **✨ Moisturizer Recommendations ✨**")
        for item in recs.get("Moisturizer", []):
            st.markdown(f"- {item}")
            
        st.markdown("### **✨ Serum Recommendations ✨**")
        for item in recs.get("Serum", []):
            st.markdown(f"- {item}")

        st.markdown("### **✨ SPF (Super Important!) Recommendations ✨**")
        for item in recs.get("SPF", []):
            st.markdown(f"- {item}")

        if recs.get("Treatments"):
            st.markdown("### **✨ Extra Treatments & Tips ✨**")
            for item in recs.get("Treatments", []):
                st.markdown(f"- {item}")
        
        st.markdown("---")
        st.markdown("Remember, sweetie, these are general ideas! Always patch test new products and listen to what your beautiful skin tells you! 🌸")
    else:
        st.markdown("Awww, Yeppuda AI doesn't have specific recommendations for that type yet, but keep exploring! ✨")


def skincare_bot():
    # --- Apply Custom CSS for Pink Theme ---
    st.markdown(PINK_THEME_CSS, unsafe_allow_html=True)

    # Initialize session state variables for quiz answers and quiz visibility
    if 'show_quiz' not in st.session_state:
        st.session_state.show_quiz = False
    if 'q1' not in st.session_state:
        st.session_state.q1 = None
    if 'q2' not in st.session_state:
        st.session_state.q2 = None
    if 'q3' not in st.session_state:
        st.session_state.q3 = None
    if 'q4' not in st.session_state:
        st.session_state.q4 = None
    if 'quiz_completed' not in st.session_state:
        st.session_state.quiz_completed = False
    if 'determined_skin_type' not in st.session_state:
        st.session_state.determined_skin_type = None

    st.markdown("<h1 style='text-align: center; color: #FF69B4;'>💖 Yeppuda AI's Skincare Haven! 🌸</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2em; color: #FFB6C1;'>Awww, hello sweetie! Your personal skincare guide is here to make your skin glow! ✨</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Button to start/toggle the quiz
    if st.button("🎀 Unsure of your skin type? Take our cute quiz! 🎀", key="quiz_start_button"):
        st.session_state.show_quiz = not st.session_state.show_quiz # Toggle quiz visibility
        # Reset quiz answers if starting fresh or retaking
        if st.session_state.show_quiz: # If quiz is now visible (either shown or toggled back on)
            st.session_state.q1 = None
            st.session_state.q2 = None
            st.session_state.q3 = None
            st.session_state.q4 = None
            st.session_state.quiz_completed = False
            st.session_state.determined_skin_type = None


    # --- Reset Quiz Button ---
    # Only show reset button if quiz is shown AND already started/completed
    if st.session_state.show_quiz and (st.session_state.q1 is not None or st.session_state.quiz_completed):
        if st.button("Reset Quiz! 🌸", key="reset_quiz_button"):
            st.session_state.q1 = None
            st.session_state.q2 = None
            st.session_state.q3 = None
            st.session_state.q4 = None
            st.session_state.quiz_completed = False
            st.session_state.determined_skin_type = None
            st.rerun() # Force rerun to clear radio button selections

    if st.session_state.show_quiz:
        # Quiz Section
        st.markdown("### 🌟 **Discover Your Skin Type!** 🌟")
        st.markdown("Let's find out what makes your skin uniquely beautiful! Answer these simple questions: 😊")

        st.markdown("---")
        st.markdown("**Question 1: How does your skin feel after cleansing (without applying any products)?**")
        q1_options = ("💖 Tight, dry, and sometimes flaky", 
                       "✨ Smooth and comfortable", 
                       "💧 A little oily in the T-zone, normal elsewhere", 
                       "🌟 Oily all over, shiny")
        # Find the index of the stored value, or 0 if not set yet
        current_q1_index = q1_options.index(st.session_state.q1) if st.session_state.q1 else 0
        st.session_state.q1 = st.radio("Choose one:", 
                                       q1_options, 
                                       index=current_q1_index, # Use index to set default
                                       key="q1_radio")

        st.markdown("---")
        st.markdown("**Question 2: How does your skin look midday (around lunchtime)?**")
        q2_options = ("💖 Dull, tight, and maybe flaky patches", 
                       "✨ Balanced, neither too oily nor too dry", 
                       "💧 Shiny in the T-zone (forehead, nose, chin)", 
                       "🌟 Very shiny, especially on the forehead and nose")
        current_q2_index = q2_options.index(st.session_state.q2) if st.session_state.q2 else 0
        st.session_state.q2 = st.radio("Choose one:", 
                                       q2_options,
                                       index=current_q2_index,
                                       key="q2_radio")
        
        st.markdown("---")
        st.markdown("**Question 3: How often do you experience breakouts (pimples/acne)?**")
        q3_options = ("💖 Rarely, if ever",
                       "✨ Occasionally, around specific times (e.g., hormonal)",
                       "💧 Sometimes, mainly in the T-zone",
                       "🌟 Frequently, all over my face")
        current_q3_index = q3_options.index(st.session_state.q3) if st.session_state.q3 else 0
        st.session_state.q3 = st.radio("Choose one:",
                                       q3_options,
                                       index=current_q3_index,
                                       key="q3_radio")

        st.markdown("---")
        st.markdown("**Question 4: How do your pores typically appear?**")
        q4_options = ("💖 Barely visible",
                       "✨ Small and refined",
                       "💧 Slightly enlarged in the T-zone",
                       "🌟 Noticeably large, especially on nose and forehead")
        current_q4_index = q4_options.index(st.session_state.q4) if st.session_state.q4 else 0
        st.session_state.q4 = st.radio("Choose one:",
                                       q4_options,
                                       index=current_q4_index,
                                       key="q4_radio")

        # Only show the reveal button if all questions have been answered OR if quiz was already completed
        if (st.session_state.q1 is not None and st.session_state.q2 is not None and st.session_state.q3 is not None and st.session_state.q4 is not None) or st.session_state.quiz_completed:
            if not st.session_state.quiz_completed: # Only show 'Reveal' button if quiz not yet completed
                if st.button("✨ Reveal My Skin Type! ✨", key="reveal_button_quiz"):
                    dry_score = 0
                    normal_score = 0
                    combo_score = 0
                    oily_score = 0

                    # Score based on answers
                    if st.session_state.q1 == "💖 Tight, dry, and sometimes flaky": dry_score += 2
                    elif st.session_state.q1 == "✨ Smooth and comfortable": normal_score += 2
                    elif st.session_state.q1 == "💧 A little oily in the T-zone, normal elsewhere": combo_score += 2
                    elif st.session_state.q1 == "🌟 Oily all over, shiny": oily_score += 2

                    if st.session_state.q2 == "💖 Dull, tight, and maybe flaky patches": dry_score += 2
                    elif st.session_state.q2 == "✨ Balanced, neither too oily nor too dry": normal_score += 2
                    elif st.session_state.q2 == "💧 Shiny in the T-zone (forehead, nose, chin)": combo_score += 2
                    elif st.session_state.q2 == "🌟 Very shiny, especially on the forehead and nose": oily_score += 2
                    
                    if st.session_state.q3 == "💖 Rarely, if ever": dry_score +=1
                    elif st.session_state.q3 == "✨ Occasionally, around specific times (e.g., hormonal)": normal_score +=1
                    elif st.session_state.q3 == "💧 Sometimes, mainly in the T-zone": combo_score +=1
                    elif st.session_state.q3 == "🌟 Frequently, all over my face": oily_score +=1

                    if st.session_state.q4 == "💖 Barely visible": dry_score +=1
                    elif st.session_state.q4 == "✨ Small and refined": normal_score +=1
                    elif st.session_state.q4 == "💧 Slightly enlarged in the T-zone": combo_score +=1
                    elif st.session_state.q4 == "🌟 Noticeably large, especially on nose and forehead": oily_score +=1

                    # Determine the skin type
                    scores = {
                        "Dry": dry_score,
                        "Normal": normal_score,
                        "Combination": combo_score,
                        "Oily": oily_score
                    }
                    
                    determined_type = max(scores, key=scores.get) 
                    st.session_state.determined_skin_type = determined_type # Store the result
                    st.session_state.quiz_completed = True # Mark quiz as completed
                    st.rerun() # Force rerun to show results immediately

            if st.session_state.quiz_completed:
                st.markdown("---")
                st.markdown(f"### ✨ Your Skin Type is likely: **{st.session_state.determined_skin_type} Skin!** ✨")
                
                if st.session_state.determined_skin_type == "Dry":
                    st.markdown("💖 Looks like your skin loves extra hydration! It often feels tight or flaky. 😊")
                elif st.session_state.determined_skin_type == "Normal":
                    st.markdown("✨ Wow, your skin is beautifully balanced! It feels comfortable and rarely has issues. 🥰")
                elif st.session_state.determined_skin_type == "Combination":
                    st.markdown("💧 You have lovely combination skin, which means different areas have different needs! 🌈")
                elif st.session_state.determined_skin_type == "Oily":
                    st.markdown("🌟 Hello, oily skin! Your skin might feel shiny and be prone to breakouts. Let's balance that! ✨")
                
                st.markdown("---")
                st.markdown("Now, let's look at some lovely product recommendations for you! 🛍️")
                display_recommendations(st.session_state.determined_skin_type)
                
                # Check for sensitive tendency in initial query if quiz was taken
                initial_query_input_for_sensitive_check = st.session_state.get('main_query_input_val', '').lower()
                if "sensitive" in initial_query_input_for_sensitive_check or "irritated" in initial_query_input_for_sensitive_check or "redness" in initial_query_input_for_sensitive_check:
                    st.markdown("---")
                    st.markdown("**P.S.** Since you also mentioned **irritation or redness**, remember your skin might have **sensitive tendencies**! Please prioritize fragrance-free products and always patch test new items. 🌸")
                    st.markdown("Here are some additional tips for sensitive skin: ")
                    display_recommendations("Sensitive")

                st.markdown("---")
                st.markdown("Now that you know your type, feel free to ask me more specific questions, sweetie! 🎀")


    # Main query section (after the quiz, so it's always available)
    st.markdown("---")
    st.markdown("### Or, if you already know your concern, type it below! 👇")
    user_query = st.text_input("Tell me about your skin problem here:", key="main_query_input", 
                                value=st.session_state.get('main_query_input_val', ''))
    st.session_state.main_query_input_val = user_query # Store current text input value

    # Responses based on user query (your existing logic, now with more concerns!)
    if "pimple" in user_query.lower() or "acne" in user_query.lower():
        st.markdown("---")
        st.markdown("### 💖 **Pimple Alert!** 💖")
        st.markdown("A pimple? No problem! Here are some gentle tips:")
        st.markdown("- **Don't Squeeze!** Resist the urge; it can make things worse. 🥺")
        st.markdown("- **Gentle Cleansing:** Wash the area with a mild cleanser. 🧼")
        st.markdown("- **Spot Treat:** Look for products with **salicylic acid** or **benzoyl peroxide**. ✨")
        st.markdown("- **Cool Compress:** A little ice wrapped in cloth can help with redness. 🧊")
        st.markdown("Remember to be kind to your skin! 💖")
    elif "dry skin" in user_query.lower():
        st.markdown("---")
        st.markdown("### 💧 **Dry Skin Woes?** 💧")
        st.markdown("Dry skin can be tricky, but we can make it soft again! Here's what helps:")
        st.markdown("- **Hydrating Cleanser:** Use a gentle, creamy cleanser that won't strip your skin. 🧴")
        st.markdown("- **Moisturize, Moisturize, Moisturize!** Apply a rich moisturizer while your skin is still damp. 💖")
        st.markdown("- **Hyaluronic Acid:** This ingredient is a moisture magnet! Look for it in serums. ✨")
        st.markdown("- **Avoid Hot Showers:** Very hot water can dry out your skin even more. Lukewarm is best. 🚿")
        st.markdown("Keep those skin cells happy and plump! 😊")
        display_recommendations("Dry")
    elif "oily skin" in user_query.lower() or "shiny" in user_query.lower():
        st.markdown("---")
        st.markdown("### ✨ **Oily Skin Tips!** ✨")
        st.markdown("Dealing with oily skin? We can help balance that shine! Here are some friendly tips:")
        st.markdown("- **Gel Cleanser:** Use a gentle foaming or gel cleanser twice a day to remove excess oil. 💧")
        st.markdown("- **Lightweight Moisturizer:** Don't skip moisturizer! Choose a non-comedogenic, gel-based one. 🌿")
        st.markdown("- **Niacinamide:** This ingredient can help regulate oil production and minimize pores. Look for it in serums! 💖")
        st.markdown("- **Blotting Papers:** Keep blotting papers handy for quick touch-ups throughout the day. 📝")
        st.markdown("Let's keep your skin feeling fresh and balanced! 😊")
        display_recommendations("Oily")
    elif "sensitive skin" in user_query.lower() or "irritated" in user_query.lower() or "redness" in user_query.lower():
        st.markdown("---")
        st.markdown("### 💖 **Caring for Sensitive Skin!** 💖")
        st.markdown("Sensitive skin needs extra love and gentle care! Try these tips:")
        st.markdown("- **Fragrance-Free:** Opt for products that are fragrance-free and dye-free to avoid irritation. 🧴")
        st.markdown("- **Patch Test:** Always test new products on a small area of skin before applying all over. 🌱")
        st.markdown("- **Soothing Ingredients:** Look for ingredients like **centella asiatica (Cica)**, **oatmeal**, or **aloes vera** to calm your skin. ✨")
        st.markdown("- **Minimal Routine:** Keep your routine simple to reduce potential irritants. Fewer products can be better! ✨")
        st.markdown("Be super gentle with your lovely skin! 💖")
        display_recommendations("Sensitive")
    elif "uneven skin tone" in user_query.lower() or "dark spots" in user_query.lower() or "hyperpigmentation" in user_query.lower():
        st.markdown("---")
        st.markdown("### 🌟 **Brightening Your Skin!** 🌟")
        st.markdown("Want to achieve a more even skin tone and tackle dark spots? Here are some brightening tips:")
        st.markdown("- **Sun Protection is Key!** Always use **SPF 30 or higher** daily, even on cloudy days, to prevent new spots. ☀️")
        st.markdown("- **Vitamin C:** This powerful antioxidant brightens skin and can reduce the appearance of dark spots. Look for a serum! 🍊")
        st.markdown("- **Niacinamide:** Another fantastic ingredient that helps improve skin tone and reduce redness. 💖")
        st.markdown("- **Exfoliation (Gentle!):** Gentle chemical exfoliants like **AHAs (glycolic or lactic acid)** can help shed pigmented cells. Start slowly! ✨")
        st.markdown("Let's get that radiant glow! 😊")
    elif "combination skin" in user_query.lower() or "routine for combination" in user_query.lower() or "combo skin" in user_query.lower():
        st.markdown("---")
        st.markdown("### 🌈 **Loving Your Combination Skin!** 🌈")
        st.markdown("Combination skin can be unique, sweetie, as it has both oily and dry areas! The key is to balance both.")
        st.markdown("- **Gentle Cleansing:** Use a balanced cleanser that cleans without stripping. 🧼")
        st.markdown("- **Targeted Moisturizing:** A lighter, gel-based moisturizer for your T-zone and a slightly richer one for drier cheeks. Or, use one lightweight, non-comedogenic option all over! 💧")
        st.markdown("- **Niacinamide:** Perfect for combination skin, it helps with oiliness and pore appearance. ✨")
        st.markdown("- **Clay Masks (T-zone) & Hydrating Masks (Dry Areas):** Treat different zones with different masks! 🎭")
        st.markdown("It's all about giving each part of your beautiful face what it needs! 🥰")
        display_recommendations("Combination") # Directly call recommendations for Combination skin
    
    # --- NEW SKIN CONCERNS START HERE ---
    elif "eczema" in user_query.lower() or "dermatitis" in user_query.lower():
        st.markdown("---")
        st.markdown("### 🦋 **Soothing Eczema-Prone Skin!** 🦋")
        st.markdown("Oh, sweetie, eczema can be so uncomfortable! It's all about gentle care and barrier support:")
        st.markdown("- **Ultra-Gentle Cleansing:** Use a non-foaming, fragrance-free cleanser. Keep showers lukewarm and short. 🚿")
        st.markdown("- **Thick Emollients:** Apply thick creams or ointments (like petroleum jelly or ceramides) immediately after bathing to 'lock in' moisture. 🧴")
        st.markdown("- **Avoid Triggers:** Identify and avoid things that make your eczema flare, like harsh soaps, certain fabrics, or allergens. 🤧")
        st.markdown("- **Topical Steroids (Doctor's Advice):** For active flares, a doctor might prescribe topical steroids or other medications. Always consult a professional! 👩‍⚕️")
        st.markdown("- **Cool Compresses:** Can help relieve itching during a flare. 🧊")
        st.markdown("Remember, for persistent or severe eczema, a dermatologist is your best friend! Stay gentle, beautiful! 💖")
    
    elif "rosacea" in user_query.lower():
        st.markdown("---")
        st.markdown("### 🌹 **Calming Rosacea-Prone Skin!** 🌹")
        st.markdown("Rosacea can be tricky, sweetie, with its redness and sensitivity. The key is to avoid triggers and be super gentle:")
        st.markdown("- **Identify Triggers:** Common triggers include spicy foods, hot beverages, alcohol, sun exposure, strong winds, and stress. Keep a diary to find yours! 🌶️☀️🍷")
        st.markdown("- **Gentle, Fragrance-Free Products:** Use mild cleansers and moisturizers designed for sensitive skin. 🧴")
        st.markdown("- **Mineral SPF Daily:** Sun protection is CRUCIAL. Opt for mineral sunscreens (zinc oxide, titanium dioxide) as they are less irritating. ☀️")
        st.markdown("- **Avoid Harsh Exfoliants:** Steer clear of scrubs, strong acids, and retinoids unless advised by a dermatologist. 🙅‍♀️")
        st.markdown("- **Cooling Products:** Gels or creams with ingredients like licorice root or green tea can offer some relief. 🌿")
        st.markdown("If your rosacea is bothering you, a dermatologist can offer prescription treatments! Stay calm and lovely! 💖")

    elif "psoriasis" in user_query.lower():
        st.markdown("---")
        st.markdown("### 🌸 **Managing Psoriasis-Prone Skin!** 🌸")
        st.markdown("Psoriasis can be really challenging, sweetie, but with the right care, you can manage it! Here are general tips:")
        st.markdown("- **Moisturize Religiously:** Keep skin well-hydrated with thick, emollient creams or ointments, especially after bathing. This helps reduce scaling. 🧴")
        st.markdown("- **Tar or Salicylic Acid:** Over-the-counter products with coal tar or salicylic acid can help with scaling, but use as directed. 🧪")
        st.markdown("- **Lukewarm Baths/Showers:** Avoid hot water, which can irritate. Consider oatmeal baths for soothing. 🛀")
        st.markdown("- **Avoid Triggers:** Stress, infections, certain medications, and skin injury can trigger flares. Try to manage these! 🧘‍♀️")
        st.markdown("- **Sunlight (Controlled):** Brief, controlled sun exposure can sometimes help, but *always* consult a doctor first, as sunburn can worsen it. ☀️")
        st.markdown("Psoriasis is a chronic condition, so regular consultation with a dermatologist is highly recommended for treatment plans! You're amazing for taking care of yourself! 💖")

    elif "blackheads" in user_query.lower() or "whiteheads" in user_query.lower() or "clogged pores" in user_query.lower():
        st.markdown("---")
        st.markdown("### ⚫⚪ **Tackling Blackheads & Whiteheads!** ⚪⚫")
        st.markdown("These little bumps are common, sweetie, but we can help minimize them!")
        st.markdown("- **Salicylic Acid (BHA):** This oil-soluble acid goes into pores to dissolve oil and dead skin cells. Look for it in cleansers or toners. ✨")
        st.markdown("- **Gentle Exfoliation:** Avoid harsh scrubs that can irritate. Chemical exfoliants (like BHAs or mild AHAs) are better. 🌿")
        st.markdown("- **Non-Comedogenic Products:** Make sure all your skincare and makeup are labeled 'non-comedogenic' to avoid clogging pores. 🚫")
        st.markdown("- **Retinoids:** Over-the-counter retinoids (like adapalene gel) can help prevent new clogs and promote cell turnover. Start slowly! 🌙")
        st.markdown("- **Don't Squeeze!** As tempting as it is, extractions should ideally be done by a professional to avoid scarring and worsening. 🥺")
        st.markdown("Keep your pores happy and clear! 💖")

    elif "fine lines" in user_query.lower() or "wrinkles" in user_query.lower() or "anti-aging" in user_query.lower():
        st.markdown("---")
        st.markdown("### 🌟 **Hello, Youthful Glow!** 🌟")
        st.markdown("Want to keep your skin looking plump and smooth, sweetie? It's all about prevention and boosting!")
        st.markdown("- **Daily SPF:** This is the #1 anti-aging product! Sun damage causes most premature aging. Wear broad-spectrum SPF 30+ every single day. ☀️")
        st.markdown("- **Retinoids (Vitamin A):** Gold standard for anti-aging! They boost collagen and speed up cell turnover, reducing lines. Start with a low concentration and use at night. 🌙")
        st.markdown("- **Antioxidants (e.g., Vitamin C):** Protect your skin from environmental damage and can brighten skin tone. Use in the morning! 🍊")
        st.markdown("- **Hydration:** Well-hydrated skin looks plumper and smoother. Use hyaluronic acid and good moisturizers. 💧")
        st.markdown("- **Healthy Lifestyle:** Balanced diet, good sleep, and avoiding smoking all contribute to youthful skin! 🍎😴🚭")
        st.markdown("Embrace your beautiful journey and keep that glow! 💖")
    
    elif "recommendations for" in user_query.lower():
        if "dry skin" in user_query.lower():
            st.markdown("---")
            st.markdown("💖 You got it, sweetie! Here are some wonderful recommendations for dry skin:")
            display_recommendations("Dry")
        elif "oily skin" in user_query.lower():
            st.markdown("---")
            st.markdown("✨ Of course! Here are some amazing product ideas for oily skin:")
            display_recommendations("Oily")
        elif "sensitive skin" in user_query.lower():
            st.markdown("---")
            st.markdown("💖 Absolutely! Here are some super gentle recommendations for sensitive skin:")
            display_recommendations("Sensitive")
        elif "normal skin" in user_query.lower():
            st.markdown("---")
            st.markdown("✨ For your perfectly balanced skin, here are some lovely recommendations:")
            display_recommendations("Normal")
        elif "combination skin" in user_query.lower():
            st.markdown("---")
            st.markdown("💧 Here are some fabulous product suggestions for your combination skin:")
            display_recommendations("Combination")
        else:
            st.markdown("---")
            st.markdown("Hmm, I can give recommendations for specific skin types, sweetie! Try asking for 'recommendations for dry skin' or 'oily skin recommendations'. ✨")
    
    elif "common mistakes" in user_query.lower() or "what to avoid" in user_query.lower() or "mistakes" in user_query.lower():
        display_common_mistakes()

    elif user_query: # If something is typed but not matched
        st.markdown("---")
        st.markdown("Hmm, this skin secret is still a mystery to Yeppuda AI! 🤔 Could you tell me a bit more? ✨")
    
    st.markdown("---")
    st.markdown("<p style='text-align: center; font-size: 1.2em; color: #FF69B4;'>🌸 Keep glowing, beautiful! Yeppuda AI is always here for you! 🌸</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    skincare_bot()