#!/usr/bin/env python3
"""Generate the complete final Nanaveda recipe book with all 10 recipes."""
import json
import os

WORKSPACE = '/Users/kethuda/Documents/ai work/Hermes/nanaveda/wrk/nvt6'
ASSETS = os.path.join(WORKSPACE, 'ASSETS')

with open(os.path.join(ASSETS, 'unsplash_images.json')) as f:
    unsplash = json.load(f)

# Helper to create clickable terms
def ct(name, text, definition):
    return f'<span class="clickable-term" data-term="{name}" title="{definition}">{text}</span>'

# All clickable term definitions
CT_DEFS = {
    'phytic_acid': 'A compound in grains and legumes that binds to minerals, reducing their absorption. Soaking deactivates it.',
    'piperine': 'The active compound in black pepper that increases curcumin absorption by 2,000%.',
    'curcumin': 'The bioactive yellow pigment in turmeric with potent anti-inflammatory and antioxidant properties.',
    'thymoquinone': 'The primary active compound in black seed with anti-inflammatory and immune-modulating effects.',
    'beta_glucans': 'Complex sugars in mushrooms that train the immune system to respond more effectively.',
    'anthocyanins': 'Antioxidant pigments that give foods their red/purple color and protect against oxidative damage.',
    'zeaxanthin': 'A carotenoid pigment that accumulates in the retina and protects against macular degeneration.',
    'nitric_oxide': 'A molecule that relaxes blood vessels, improving circulation and lowering blood pressure.',
    'ace_inhibitors': 'Compounds that block the enzyme constricting blood vessels — used by both drugs and hibiscus.',
    'agni': 'The Ayurvedic concept of digestive fire — the metabolic energy that transforms food into nourishment.',
    'spleen_qi': 'The TCM concept of digestive energy responsible for transforming food into vital energy and blood.',
    'tridoshic': 'A remedy that balances all three Ayurvedic constitutional types (Vata, Pitta, Kapha).',
    'panchakarma': 'The Ayurvedic detoxification protocol for which kitchari is the primary prescribed food.',
    'immunosenescence': 'The age-related decline in immune function that makes seniors more susceptible to illness.',
    'ibn_qayyim': '14th-century Islamic scholar whose Prophetic Medicine compiled the medical teachings of Muhammad ﷺ.',
    'ibn_sina': 'Persian polymath (Avicenna) whose Canon of Medicine was the standard textbook in Europe for 600 years.',
    'al_zahrawi': '10th-century Andalusian physician (Abulcasis) considered the father of modern surgery.',
    'scholey': 'Dr. Andrew Scholey, whose 2008 study proved sage improves memory in older adults.',
    'prophetic_medicine': 'The Islamic healing tradition derived from the medical recommendations of Prophet Muhammad ﷺ.',
    'tibb_nabawi': 'Ibn al-Qayyim\'s seminal work compiling Prophetic medical guidance.',
    'sharbat': 'An ancient Arabic beverage tradition — sweetened herbal drinks served chilled as refreshment and medicine.',
    'silk_road': 'The ancient trade network connecting China to the Mediterranean, transmitting spices, ideas, and remedies.',
    'ottoman_empire': 'A centuries-spanning empire that synthesized and advanced Islamic medical and culinary traditions.',
    'slave_trade': 'The forced migration of Africans to the Americas, which carried hibiscus and other healing traditions.',
    'dioscorides': 'Roman physician (40-90 CE) who prescribed black seed for headaches, toothache, and respiratory complaints.',
    'al_razi': '9th-century Islamic physician (Rhazes) who prescribed black seed for headaches and respiratory complaints.',
    'habba_sawda': 'The Arabic name for black seed, meaning "the blessed seed" — a cure for "every disease except death."',
    'prophetic_medicine': 'The Islamic healing tradition derived from the medical recommendations of Prophet Muhammad ﷺ.',
    'tibb_nabawi': 'Ibn al-Qayyim\'s seminal work compiling Prophetic medical guidance.',
}

# Unsplash images
def img(key):
    return unsplash.get(key, [{}])[0].get('url', '') if unsplash.get(key) else ''

# All 10 recipes with full content
RECIPES = [
    {
        'num': '1', 'page': 'page-recipe-1',
        'title': 'Kitchari', 'subtitle': 'Ayurvedic Rice & Lentil Porridge',
        'time': '30 min soak', 'diff': 'Easy', 'serves': 'Serves 4',
        'tags': ['🟢 Pantry Staple', 'Gut Healing', 'Complete Protein'],
        'img': img('kitchari'),
        'heals': f'Kitchari is the cornerstone of Ayurvedic healing — a monodiet staple used for centuries to reset the digestive system. The combination of rice and mung dal creates a complete protein profile, while the gentle spices kindle {ct("agni", CT_DEFS["agni"], "agni")} without aggravating any of the three doshas. It is {ct("tridoshic", CT_DEFS["tridoshic"], "tridoshic")}, meaning it balances Vata, Pitta, and Kapha constitutions alike.',
        'ings': [('basmati rice', '1 cup'), ('split yellow mung dal', '½ cup'), ('water', '6 cups'), ('ghee or coconut oil', '1 tbsp'), ('cumin seeds', '1 tsp'), ('turmeric powder', '1 tsp'), ('fresh ginger, grated', '1 inch'), ('mustard seeds', '½ tsp'), ('asafoetida (hing)', 'Pinch'), ('salt', 'To taste')],
        'steps': [
            ('Wash the rice and mung dal together in several changes of cold water until the water runs clear. Soak them in fresh water for at least 30 minutes — or overnight if you have the time. This soaking step is crucial: it removes phytic acid and makes the grains far gentler on the stomach.', '⏱ 30 min soak', f'Soaking activates enzymes that break down {ct("phytic_acid", CT_DEFS["phytic_acid"], "phytic acid")} — a compound in grains and legumes that binds to minerals like iron, zinc, and calcium, preventing their absorption. For seniors, whose mineral absorption naturally declines with age, this simple step can significantly increase the nutritional value of every bowl.', 'health'),
            ('Heat the ghee in a heavy-bottomed pot over medium heat. Add the cumin seeds and mustard seeds. Wait for them to pop and sizzle — about 30 seconds. Add the asafoetida and stir for just a few seconds more.', '⏱ 2 min', f'Kitchari (from Sanskrit khiccā, meaning "mixture") is one of the oldest recorded foods in human history. It appears in the Charaka Samhita, one of the foundational texts of Ayurveda dating to approximately 300 BCE. The dish was prescribed as a primary healing food during {ct("panchakarma", CT_DEFS["panchakarma"], "Panchakarma")} — Ayurvedic detoxification — and remains the go-to remedy for digestive complaints across the Indian subcontinent.', 'history'),
            ('Drain the soaked rice and dal, and add them to the pot. Stir gently for 2 minutes to coat every grain with the spiced ghee. Add the turmeric and grated ginger, stirring until fragrant.', '⏱ 3 min', 'In Indian households, kitchari holds a dual identity: it is both the food of Buddhist monks (who eat it for breakfast to sustain long meditation sessions) and the first solid food given to infants. Its reputation as "comfort food with healing powers" crosses every social and spiritual boundary in South Asia.', 'cultural'),
            ('Pour in the 6 cups of water and add salt. Bring to a rolling boil, then reduce the heat to low. Cover the pot with a lid, leaving it slightly ajar to let steam escape. Let it simmer gently for 35–40 minutes, stirring occasionally.', '⏱ 40 min simmer', f'The word "congee" (Chinese rice porridge) and "kitchari" likely share a common ancestor — the Sanskrit word kanjika, meaning "fermented rice water." As Buddhism spread from India to China along the {ct("silk_road", CT_DEFS["silk_road"], "Silk Road")}, the healing rice porridge traveled with it, evolving into the congee traditions of East Asia.', 'funfact'),
            ('Taste and adjust salt. Ladle into bowls, top with fresh cilantro, and serve with a squeeze of lemon. Eat slowly, chewing well.', '⏱ Serve', f'While kitchari itself is rooted in Ayurvedic tradition, the Islamic scholarly tradition has long recognized the healing properties of its core ingredients. {ct("ibn_qayyim", CT_DEFS["ibn_qayyim"], "Imam Ibn al-Qayyim")}, in his {ct("prophetic_medicine", CT_DEFS["prophetic_medicine"], "Prophetic Medicine")} ({ct("tibb_nabawi", CT_DEFS["tibb_nabawi"], "al-Tibb al-Nabawi")}), discusses the benefits of rice porridge (aruzz) as a gentle, nourishing food for the sick and convalescent.', 'islamic'),
        ]
    },
    {
        'num': '2', 'page': 'page-recipe-2',
        'title': 'Golden Milk — Haldi Doodh', 'subtitle': 'Turmeric, Black Pepper & Ginger Tonic',
        'time': '2 min', 'diff': 'Very Easy', 'serves': 'Serves 2',
        'tags': ['🟢 Pantry Staple', 'Anti-Inflammatory', 'Brain Health'],
        'img': img('golden_milk'),
        'heals': f'Golden milk is one of the most studied functional beverages in the world. Its active compound, {ct("curcumin", CT_DEFS["curcumin"], "curcumin")}, has been shown in over 12,000 peer-reviewed studies to reduce inflammation at the molecular level. The addition of black pepper increases curcumin absorption by up to 2,000% — a discovery that ancient Ayurvedic practitioners intuited centuries before modern science confirmed it.',
        'ings': [('whole milk (or oat milk)', '2 cups'), ('turmeric powder', '1 tsp'), ('ground cinnamon', '½ tsp'), ('ground black pepper', '¼ tsp'), ('fresh ginger, grated', '1 inch'), ('ghee or coconut oil', '1 tsp'), ('honey (optional)', '1 tsp')],
        'steps': [
            ('In a small saucepan, combine the milk, turmeric, cinnamon, black pepper, and grated ginger. Whisk together until smooth. Place over medium-low heat.', '⏱ 2 min', f'{ct("piperine", CT_DEFS["piperine"], "Piperine")}, the active compound in black pepper, inhibits an enzyme in the liver called glucuronidation — which would otherwise rapidly break down {ct("curcumin", CT_DEFS["curcumin"], "curcumin")} before it reaches the bloodstream. A landmark study published in Planta Medica (1998) found that just ¼ teaspoon of black pepper increased curcumin bioavailability by 2,000%.', 'science'),
            ('Heat gently, stirring frequently with a whisk. Do not let it boil — you want it steaming hot but not scalding. After about 5 minutes, add the ghee or coconut oil and stir until melted.', '⏱ 5 min', f'Turmeric (hurd in Arabic) has been used in the Islamic world for over a millennium. {ct("ibn_qayyim", CT_DEFS["ibn_qayyim"], "Imam Ibn al-Qayyim")} describes it in {ct("tibb_nabawi", CT_DEFS["tibb_nabawi"], "al-Tibb al-Nabawi")} as beneficial for the liver and stomach. The Prophet Muhammad ﷺ said: "Allah did not send down a disease without sending down the cure" (Sahih al-Bukhari).', 'islamic'),
            ('Remove from heat. Sweeten with honey if you like — add it after the milk has cooled slightly (below 110°F/43°C) to preserve honey\'s beneficial enzymes. Pour into your favorite mug and sip slowly, ideally in the evening.', '⏱ 2 min', f'{ct("curcumin", CT_DEFS["curcumin"], "Curcumin")} crosses the blood-brain barrier and has been shown to increase Brain-Derived Neurotrophic Factor (BDNF) — a growth hormone that functions in the brain. Decreased BDNF is linked to depression, Alzheimer\'s disease, and age-related cognitive decline. A 2018 UCLA study found that participants who took curcumin showed significant improvements in memory and attention compared to placebo.', 'health'),
        ]
    },
    {
        'num': '3', 'page': 'page-recipe-3',
        'title': 'Ginger, Goji & Jujube Bone Broth', 'subtitle': 'Traditional Chinese Medicine Tonic',
        'time': '10 min', 'diff': 'Easy', 'serves': 'Serves 6',
        'tags': ['🟡 Specialty Items', 'Blood Nourishing', '⚠️ Use Instant Pot'],
        'img': img('bone_broth'),
        'heals': f'This broth combines three powerhouse ingredients from Traditional Chinese Medicine: ginger for warming the body and aiding circulation, goji berries for nourishing the blood and supporting eye health, and jujube dates for strengthening the {ct("spleen_qi", CT_DEFS["spleen_qi"], "spleen qi")} and calming the spirit.',
        'ings': [('beef or chicken bones (pre-cut)', '2 lbs'), ('water', '6 cups'), ('fresh ginger, sliced', '1 inch'), ('goji berries', '2 tbsp'), ('dried jujube dates', '4–5'), ('apple cider vinegar', '1 tsp'), ('salt', 'To taste')],
        'steps': [
            ('Place the bones in a large pot and cover with cold water. Bring to a boil over high heat. Once boiling, reduce heat and simmer for 5 minutes. Drain the bones and rinse them under clean water. Discard the blanching water.', '⏱ 10 min', 'This initial blanching step removes blood, bone fragments, and impurities that would otherwise cloud the broth. In TCM, this step is considered essential for creating a "clean" broth that tonifies without creating internal "dampness" — a concept roughly corresponding to metabolic sluggishness and inflammation.', 'health'),
            ('Return the cleaned bones to the pot (or better yet, an Instant Pot). Add 6 cups of fresh water, the apple cider vinegar, and sliced ginger. The vinegar helps draw minerals from the bones into the broth. Bring to a boil, then reduce to the lowest possible heat. Cover and simmer gently for 4–6 hours.', '⏱ 4–6 hours', f'Goji berries and jujube dates traveled westward along the {ct("silk_road", CT_DEFS["silk_road"], "Silk Road")} for centuries, reaching the Middle East and eventually Europe. In the Islamic world, jujube (unnab or sidr) became deeply valued — mentioned in the Quran as a fruit of Paradise (al-Waqi\'ah, 56:28).', 'history'),
            ('During the last 30 minutes of simmering, add the goji berries and jujube dates. These delicate ingredients would disintegrate with prolonged cooking, so they are added at the end to preserve their flavor and nutritional value.', '⏱ 30 min', f'Goji berries contain the highest concentration of {ct("zeaxanthin", CT_DEFS["zeaxanthin"], "zeaxanthin")} of any common food — a carotenoid that accumulates in the retina and helps protect against age-related macular degeneration (AMD), the leading cause of vision loss in adults over 50. Regular consumption increases zeaxanthin levels by 26% after 90 days.', 'health'),
            ('Remove from heat. Strain the broth through a fine-mesh sieve into a clean pot or bowl. Discard the bones and spent ginger. Season with salt to taste. Serve warm, sipping slowly.', '⏱ 10 min', 'Jujube dates are sometimes called "Chinese dates" or "red dates," but they are not related to the date palm at all. They belong to the Rhamnaceae (buckthorn) family and have been cultivated in China for over 4,000 years. A mature jujube tree can live for over 1,000 years.', 'funfact'),
        ]
    },
    {
        'num': '4', 'page': 'page-recipe-4',
        'title': 'Congee with Shiitake', 'subtitle': 'Chinese/Japanese Medicinal Rice Porridge',
        'time': '4 hrs soak', 'diff': 'Easy', 'serves': 'Serves 4',
        'tags': ['🟢 Pantry Staple', 'Digestive Healing', '⚠️ Use Rice Cooker'],
        'img': img('congee'),
        'heals': f'Congee (jook/zhou) is the ultimate healing food in East Asian medicine — prescribed for the elderly, the sick, and new mothers for over 2,000 years. The addition of shiitake mushrooms brings powerful immune-modulating {ct("beta_glucans", CT_DEFS["beta_glucans"], "beta-glucans")} to an already gut-soothing base.',
        'ings': [('jasmine rice', '1 cup'), ('water or light broth', '8 cups'), ('dried shiitake mushrooms', '4'), ('fresh ginger, sliced', '1 inch'), ('soy sauce or tamari', '1 tbsp'), ('green onions, sliced', '2'), ('sesame oil', 'To finish')],
        'steps': [
            ('The night before: place the dried shiitake mushrooms in a bowl with 2 cups of warm water. Soak overnight (or at least 4 hours). This soaking liquid is liquid gold — do not discard it. In the morning, remove the mushrooms, squeeze out excess liquid, and slice them thinly.', '⏱ Overnight soak', f'Shiitake mushrooms contain {ct("beta_glucans", CT_DEFS["beta_glucans"], "beta-glucans")} — complex sugars that "train" the immune system to respond more effectively to threats. Unlike stimulants that push the immune system in one direction, beta-glucans are immunomodulators: they balance immune response, calming it when overactive and activating it when sluggish. This makes them particularly valuable for seniors, whose immune function naturally declines with age — a process called {ct("immunosenescence", CT_DEFS["immunosenescence"], "immunosenescence")}.', 'science'),
            ('Rinse the jasmine rice in cold water until the water runs clear. Place the rice in a large pot with 8 cups of water (or broth), the reserved mushroom soaking liquid, and the sliced ginger. Bring to a boil over high heat. Alternatively, use a rice cooker with a "congee" or "porridge" setting.', '⏱ 5 min', 'Congee has been a staple of Chinese cuisine since at least the Han Dynasty (206 BCE – 220 CE). Legend holds that Emperor Huangdi, the mythical founder of Chinese medicine, prescribed rice porridge as the foundation of all healing diets. In Japan, the Buddhist monk Eisai (1141–1215) introduced tea and mushroom cultivation from China.', 'history'),
            ('Once boiling, reduce heat to the lowest setting. Add the sliced shiitake. Cover with a lid slightly ajar. Simmer gently for 1.5 to 2 hours, stirring occasionally. The congee is ready when the rice has completely broken down into a creamy, porridge-like consistency.', '⏱ 1.5–2 hours', 'In Chinese Buddhist tradition, congee is considered the food of compassion — simple, humble, and nourishing without excess. During the Tang Dynasty, Buddhist monasteries would distribute congee to the poor during winter months.', 'cultural'),
            ('Stir in the soy sauce. Taste and adjust seasoning. Ladle into bowls, top with sliced green onions and a drizzle of sesame oil. Eat warm, preferably in the morning when the stomach is most receptive.', '⏱ 5 min', 'Shiitake mushrooms are the second most cultivated mushroom in the world, after the common button mushroom. Their name comes from Japanese: shii (the Castanopsis tree they grow on) + take (mushroom). In ancient China, shiitake were so valued that they were reserved for the emperor and his court.', 'funfact'),
        ]
    },
    {
        'num': '5', 'page': 'page-recipe-5',
        'title': 'Saffron & Cardamom Sleep Milk', 'subtitle': 'Adaptogenic Evening Tonic',
        'time': '5 min', 'diff': 'Very Easy', 'serves': 'Serves 2',
        'tags': ['🟡 Specialty Items', 'Sleep Quality', 'Mood Support'],
        'img': img('saffron_milk'),
        'heals': f'Saffron — the world\'s most precious spice by weight — has been clinically proven to improve sleep quality and mood in older adults. Combined with cardamom and warm milk, this drink supports the nervous system, promotes relaxation, and encourages deep, restorative sleep. Unlike many sleep aids, saffron has zero drug interactions and no morning grogginess.',
        'ings': [('whole milk (or oat milk)', '1 cup'), ('saffron threads', '8–10 threads'), ('ground cardamom', '¼ tsp'), ('ground cinnamon', '¼ tsp'), ('pinch of nutmeg', 'Pinch'), ('ghee or coconut oil', '1 tsp'), ('honey (optional)', '1 tsp')],
        'steps': [
            ('Place the saffron threads in a small dish. Add 1 tablespoon of warm water and let them steep for 5 minutes. The water will turn a deep golden-orange color, and the saffron\'s aroma will intensify. This pre-soaking step maximizes the extraction of saffron\'s active compounds — crocin and safranal.', '⏱ 5 min', 'A landmark study published in the Journal of Clinical Pharmacy and Therapeutics (PMID: 24290594) found that saffron supplementation significantly improved sleep quality in adults over 60. Another study in the Journal of Affective Disorders showed that saffron was as effective as fluoxetine (Prozac) for mild-to-moderate depression — with far fewer side effects.', 'science'),
            ('Pour the milk into a small saucepan. Add the saffron with its soaking water, cardamom, cinnamon, and nutmeg. Whisk until the spices are fully dissolved. Place over medium-low heat.', '⏱ 2 min', f'Saffron (za\'faran in Arabic) has been prized in Islamic culture for over a millennium. It was used in cooking, medicine, and as a dye for textiles and manuscripts. The great Islamic physician {ct("ibn_sina", CT_DEFS["ibn_sina"], "Ibn Sina")} (Avicenna) described saffron in his Canon of Medicine as beneficial for heart strength, digestion, and eye health. Today, Iran produces over 90% of the world\'s saffron.', 'islamic'),
            ('Heat gently, stirring frequently. Do not let it boil — you want it steaming hot but not scalding. After about 5 minutes, add the ghee or coconut oil and stir until melted. The milk will take on a beautiful golden hue from the saffron.', '⏱ 5 min', 'Sleep quality naturally declines with age — seniors produce less melatonin and spend less time in deep (slow-wave) sleep. Saffron has been shown to increase time spent in deep sleep and reduce nighttime awakenings without causing morning grogginess. Unlike pharmaceutical sleep aids, saffron does not suppress REM sleep or create dependency.', 'health'),
            ('Remove from heat. Sweeten with honey if desired (add after cooling slightly to preserve enzymes). Pour into a mug. Sip slowly, ideally 30–60 minutes before bedtime. Breathe deeply. Let the warmth and the spices do their work.', '⏱ 2 min', 'It takes approximately 150,000 saffron crocus flowers to produce just one kilogram of dried saffron — making it the most expensive spice in the world by weight. Each flower produces only three tiny stigmas, which are hand-harvested at dawn before the flowers open. Saffron has been cultivated for over 3,500 years.', 'funfact'),
        ]
    },
    {
        'num': '6', 'page': 'page-recipe-6',
        'title': 'Low-Sodium Miso Soup with Wakame', 'subtitle': 'Japanese Probiotic Tonic',
        'time': '5 min', 'diff': 'Very Easy', 'serves': 'Serves 4',
        'tags': ['🟡 Asian Market', 'Probiotic', 'Gut Health'],
        'img': img('miso_soup'),
        'heals': f'Miso is a fermented soybean paste rich in probiotics — beneficial bacteria that support gut health, immunity, and even mood. Combined with mineral-rich wakame seaweed, this soup is a daily longevity food in Japan. Okinawans, among the longest-lived people on Earth, consume miso soup almost every day.',
        'ings': [('water', '4 cups'), ('low-sodium miso paste', '3 tbsp'), ('dried wakame seaweed', '1 sheet'), ('fresh shiitake mushrooms, sliced', '4'), ('silken tofu, cubed', '1 block'), ('green onions, sliced', '2'), ('grated ginger', '1 tsp')],
        'steps': [
            ('Place the dried wakame in a small bowl of cold water. It will expand dramatically in just 5 minutes — a little goes a long way. Once rehydrated, drain and set aside. Cut into bite-sized pieces if the sheet is large.', '⏱ 5 min', 'Wakame seaweed is one of the richest natural sources of iodine, calcium, iron, and magnesium. It also contains fucoxanthin — a carotenoid pigment unique to brown seaweed that has been shown in studies to support fat metabolism and reduce inflammation. Just one gram of dried wakame provides more iodine than the daily recommended intake, supporting thyroid function.', 'science'),
            ('In a pot, bring 4 cups of water to a gentle simmer. Add the sliced shiitake mushrooms and grated ginger. Simmer for 10 minutes to extract the mushroom umami and ginger warmth into the broth.', '⏱ 10 min', 'Okinawa, Japan, is one of the world\'s five "Blue Zones" — regions where people live significantly longer than average. Okinawans consume miso soup daily, often for breakfast. The traditional Okinawan diet is rich in fermented foods, seaweed, and vegetables, with miso soup as its cornerstone.', 'history'),
            ('Remove the pot from heat. This is important: boiling destroys the beneficial probiotics in miso. Place the miso paste in a small bowl, add a few tablespoons of the warm (not boiling) broth, and whisk until smooth. Pour this mixture back into the pot and stir gently.', '⏱ 3 min', 'As we age, the diversity of our gut microbiome naturally declines — a condition linked to increased inflammation, weakened immunity, and digestive issues. Fermented foods like miso introduce beneficial bacteria (Aspergillus oryzae and lactic acid bacteria) that help restore microbial balance.', 'health'),
            ('Add the rehydrated wakame and cubed silken tofu. Let them warm through for 1–2 minutes (do not boil). Ladle into bowls, top with sliced green onions, and serve immediately.', '⏱ 3 min', f'While miso itself is Japanese, the concept of fermented foods for health has deep roots in Islamic medicine. The Prophet Muhammad ﷺ consumed and praised fermented foods including vinegar (khall), yogurt, and fermented drinks. {ct("ibn_qayyim", CT_DEFS["ibn_qayyim"], "Imam Ibn al-Qayyim")} discusses the benefits of vinegar and fermented foods in {ct("tibb_nabawi", CT_DEFS["tibb_nabawi"], "al-Tibb al-Nabawi")}.', 'islamic'),
        ]
    },
    {
        'num': '7', 'page': 'page-recipe-7',
        'title': 'Hibiscus & Cinnamon Agua de Jamaica', 'subtitle': 'Latin American Heart Tonic',
        'time': '2 min', 'diff': 'Easy', 'serves': 'Serves 6',
        'tags': ['🟡 Tea Shop', 'Heart Health', 'Blood Pressure'],
        'img': img('hibiscus'),
        'heals': f'Hibiscus (Jamaica flower) is one of the most scientifically validated herbal remedies for cardiovascular health. Multiple clinical trials have confirmed its ability to lower blood pressure and cholesterol. Combined with cinnamon — which supports healthy blood sugar levels — this refreshing drink is a delicious way to support heart health.',
        'ings': [('dried hibiscus flowers', '1 cup'), ('water', '6 cups'), ('cinnamon stick', '1'), ('sugar or honey', '½ cup'), ('vanilla extract (optional)', '1 tsp'), ('lime slices', 'For serving')],
        'steps': [
            ('Bring 6 cups of water to a boil in a large pot (or use an electric kettle with auto-shutoff for safety). Add the dried hibiscus flowers and cinnamon stick. Once the water returns to a boil, reduce heat and simmer for 15 minutes. The water will turn a deep, garnet red — the color of rubies.', '⏱ 15 min', f'Hibiscus sabdariffa contains {ct("anthocyanins", CT_DEFS["anthocyanins"], "anthocyanins")} and polyphenols that act as natural {ct("ace_inhibitors", CT_DEFS["ace_inhibitors"], "ACE inhibitors")} — the same mechanism used by prescription blood pressure medications like lisinopril. A 2010 meta-analysis in the Journal of Hypertension found that hibiscus tea significantly reduced both systolic and diastolic blood pressure.', 'science'),
            ('Remove from heat. Add the sugar or honey while the liquid is still warm, stirring until dissolved. Add vanilla extract if using. Allow the mixture to cool to room temperature.', '⏱ 10 min', f'Hibiscus sabdariffa is native to West Africa, where it has been used for centuries to make a refreshing drink called bissap or sobolo. Enslaved Africans brought hibiscus to the Americas during the {ct("slave_trade", CT_DEFS["slave_trade"], "transatlantic slave trade")}, and it became deeply embedded in Latin American culture.', 'history'),
            ('Strain through a fine-mesh sieve into a pitcher. Discard the hibiscus flowers and cinnamon stick. Refrigerate until cold. Serve over ice with lime slices. The drink should be tart, sweet, and deeply refreshing.', '⏱ Chill & serve', 'In many Latin American countries, agua de Jamaica is served at celebrations, family gatherings, and holiday meals. It is one of the three "aguas frescas" (fresh waters) that form the backbone of Mexican beverage culture — alongside horchata and tamarindo. In West Africa, bissap is served to guests as a sign of hospitality.', 'cultural'),
        ]
    },
    {
        'num': '8', 'page': 'page-recipe-8',
        'title': 'Beetroot, Ginger & Rose Sharbat', 'subtitle': 'Middle Eastern Blood Tonic',
        'time': '10 min', 'diff': 'Easy', 'serves': 'Serves 6',
        'tags': ['🟡 Easy to Find', 'Blood Tonic', 'Iron-Rich'],
        'img': img('beetroot_sharbat'),
        'heals': f'This vibrant pink sharbat combines three powerful ingredients from the Middle Eastern healing tradition: beetroot for blood-building iron and natural nitrates, ginger for circulation and warmth, and rose for its calming, anti-inflammatory properties. The {ct("sharbat", CT_DEFS["sharbat"], "sharbat")} tradition is one of the oldest beverage customs in the Islamic world.',
        'ings': [('pre-cooked beetroots, chopped', '2 medium'), ('fresh ginger, sliced', '1 inch'), ('water', '4 cups'), ('sugar or honey', '½ cup'), ('rose water', '2 tbsp'), ('lemon juice', '1 lemon'), ('dried rose petals', 'For garnish')],
        'steps': [
            ('Place the pre-cooked beetroot and ginger in a pot with 4 cups of water. Bring to a boil, then reduce heat and simmer for 20–30 minutes until the beetroot is very tender and the liquid has turned a deep, ruby red. Using pre-cooked beets eliminates the difficult peeling and chopping of raw beetroot.', '⏱ 30 min', f'Beetroot is one of the richest dietary sources of nitrates, which the body converts to {ct("nitric_oxide", CT_DEFS["nitric_oxide"], "nitric oxide")} — a molecule that relaxes and dilates blood vessels. A 2015 study in the journal Hypertension found that drinking beetroot juice daily reduced systolic blood pressure by an average of 4–5 mmHg — comparable to some blood pressure medications.', 'science'),
            ('Strain the liquid through a fine-mesh sieve into a clean pot. Press the beetroot gently to extract all the liquid. Discard the solids (or save for another use — they are delicious in salads). Return the strained liquid to the pot.', '⏱ 5 min', f'Rose water holds a special place in Islamic culture and medicine. The Prophet Muhammad ﷺ is reported to have valued roses highly, and rose water has been used in the Islamic world for centuries — in cooking, medicine, and perfumery. {ct("ibn_qayyim", CT_DEFS["ibn_qayyim"], "Imam Ibn al-Qayyim")} notes that rose water "strengthens the heart and brings joy to the soul."', 'islamic'),
            ('Add the sugar or honey to the warm beetroot liquid and stir until dissolved. Add the rose water and lemon juice. Stir well. Taste and adjust sweetness — it should be sweet-tart with a floral aroma. The lemon juice brightens the flavor and adds vitamin C, which enhances iron absorption.', '⏱ 3 min', f'{ct("sharbat", CT_DEFS["sharbat"], "Sharbat")} (from Arabic shariba, "to drink") is one of the oldest beverage traditions in the Islamic world. Medieval Arabic cookbooks describe dozens of sharbat recipes using roses, pomegranates, lemons, and herbs. The {ct("ottoman_empire", CT_DEFS["ottoman_empire"], "Ottoman Empire")} elevated sharbat-making to an art form, with dedicated sharbat-makers in the imperial palace.', 'history'),
            ('Allow to cool, then refrigerate. Serve chilled over ice, garnished with dried rose petals. This concentrate can be diluted with water or sparkling water to taste. Store in the refrigerator for up to one week.', '⏱ Chill & serve', f'The deep red color of beetroot comes from betalain pigments — the same pigments found in bougainvillea flowers. Betalains are powerful antioxidants that have been shown to protect cells from oxidative damage. Interestingly, betalains and {ct("anthocyanins", CT_DEFS["anthocyanins"], "anthocyanins")} never appear in the same plant — they are mutually exclusive in nature.', 'funfact'),
        ]
    },
    {
        'num': '9', 'page': 'page-recipe-9',
        'title': 'Black Seed (Habba Sawda) Honey Paste', 'subtitle': 'Arabic/Prophetic Immune Tonic',
        'time': '10 min', 'diff': 'Easy', 'serves': 'Serves 1 jar',
        'tags': ['🟡 Easy to Find', 'Immune Boosting', 'Prophetic Medicine'],
        'img': img('black_seed'),
        'heals': f'This recipe combines two of the most powerful healing substances in Islamic {ct("prophetic_medicine", CT_DEFS["prophetic_medicine"], "Prophetic medicine")}: black seed ({ct("habba_sawda", CT_DEFS["habba_sawda"], "habbatul barakah")}) and honey. The Prophet Muhammad ﷺ described black seed as a cure for "everything except death." Modern research has confirmed its remarkable anti-inflammatory, antioxidant, and immune-modulating properties.',
        'ings': [('black seed (nigella sativa)', '½ cup'), ('raw honey', '1 cup'), ('ground black seed (optional)', '1 tsp'), ('saffron threads (optional)', 'Pinch')],
        'steps': [
            ('Lightly toast the whole black seeds in a dry pan over low heat for 2–3 minutes, stirring constantly. You will hear them crackle and smell a warm, peppery aroma. Do not let them burn — the goal is to lightly awaken the oils, not to cook them. Remove from heat and allow to cool.', '⏱ 5 min', f'The Prophet Muhammad ﷺ said: "Hold on to the black seed — it is a cure for every disease except death" (Sahih al-Bukhari 5688, Sahih Muslim 2215). This hadith has inspired over 1,400 years of black seed use in the Islamic world. The seed is called habbatul barakah — "the blessed seed" — in Arabic.', 'islamic'),
            ('Once cooled, grind the toasted seeds coarsely in a mortar and spice grinder. You want a mix of cracked seeds and some powder — not a fine flour. The texture adds interest and ensures the oils are released slowly. A coarse grind is also gentler on the digestive system than a fine powder.', '⏱ 5 min', f'The primary active compound in black seed is {ct("thymoquinone", CT_DEFS["thymoquinone"], "thymoquinone")} — a molecule with remarkable pharmacological properties. Over 1,500 peer-reviewed studies have documented thymoquinone\'s anti-inflammatory, antioxidant, antimicrobial, and anti-cancer effects. For seniors, its immune-modulating and anti-inflammatory properties are particularly valuable.', 'science'),
            ('In a clean glass jar, layer the ground black seed with the raw honey. Stir gently to combine, ensuring the seeds are fully coated in honey. If using, add the saffron threads. Seal the jar tightly. The honey acts as both a preservative and a synergistic enhancer.', '⏱ 3 min', f'Raw honey never spoils. Archaeologists have found 3,000-year-old honey in Egyptian tombs that was still edible. Honey\'s remarkable preservative properties come from its low moisture content, high acidity, and the presence of hydrogen peroxide produced by enzymes bees add to the nectar. The Prophet Muhammad ﷺ praised honey as a healing substance: "Healing is in three things: a drink of honey, a cut of the cupping knife, or cauterization by fire" (Sahih al-Bukhari).', 'health'),
            ('Store at room temperature in a cool, dark place. Allow the flavors to meld for at least 24 hours before using. Take 1–2 teaspoons daily — straight from the spoon, or stirred into warm water, tea, or milk. Best taken in the morning on an empty stomach for maximum absorption.', '⏱ Daily use', f'Black seed was found in Tutankhamun\'s tomb — placed there, it is believed, to accompany the young king into the afterlife. The seed has been used continuously in Mediterranean and Middle Eastern cultures for over 3,000 years. The Roman physician {ct("dioscorides", CT_DEFS["dioscorides"], "Dioscorides")} (40–90 CE) prescribed black seed for headaches, toothache, and respiratory complaints.', 'history'),
        ]
    },
    {
        'num': '10', 'page': 'page-recipe-10',
        'title': 'Sage & Honey Tea', 'subtitle': 'Mediterranean Memory Tonic',
        'time': '2 min', 'diff': 'Very Easy', 'serves': 'Serves 2',
        'tags': ['🟢 Pantry Staple', 'Cognitive Health', 'Antimicrobial'],
        'img': img('sage_tea'),
        'heals': f'Sage (Salvia officinalis) has been used for cognitive enhancement since ancient times. Modern clinical research confirms what traditional healers knew: sage improves memory, attention, and mental clarity in older adults. Combined with honey — itself a revered healing substance in Islamic medicine — this simple tea is a daily ritual for brain health.',
        'ings': [('fresh sage leaves (or 1 tbsp dried)', '8–10 leaves'), ('water', '2 cups'), ('raw honey', '1–2 tsp'), ('lemon slice (optional)', '1 slice')],
        'steps': [
            ('Bring 2 cups of water to a boil. If using an electric kettle, simply boil the water and pour it into a teapot or mug. Add the sage leaves — gently bruise them between your fingers before adding to release their essential oils. If using dried sage, simply measure it into the pot or a tea infuser.', '⏱ 2 min', f'A landmark study by {ct("scholey", CT_DEFS["scholey"], "Scholey")} et al. (2008) demonstrated that sage extract significantly improved memory and attention in healthy older adults. Participants showed better word recall, improved accuracy on attention tasks, and reported feeling more alert and calm. A 2014 study in Psychopharmacology found that sage enhanced cognitive performance in adults with mild-to-moderate Alzheimer\'s disease.', 'science'),
            ('Cover and steep for 5–7 minutes. The water will turn a pale green-gold color, and the aroma will be warm, herbaceous, and slightly peppery. Do not over-steep — sage can become bitter if left too long. The ideal steeping time balances flavor with potency.', '⏱ 7 min steep', f'The genus name Salvia comes from the Latin salvare, meaning "to save" or "to heal" — a testament to sage\'s revered status in European herbal tradition. The great Islamic physician {ct("al_zahrawi", CT_DEFS["al_zahrawi"], "Al-Zahrawi")} (Abulcasis) described sage in his medical encyclopedia as beneficial for memory, digestion, and oral health.', 'history'),
            ('Strain the leaves (or remove the infuser). Add honey to taste — stir until dissolved. Add a slice of lemon if desired. Sip slowly while warm. The honey not only sweetens the tea but adds its own healing compounds, creating a synergistic effect. Best enjoyed in the morning or early afternoon.', '⏱ 2 min', f'Honey holds a uniquely honored place in Islamic medicine. The Quran dedicates an entire passage to honey and its healing properties: "There comes from their bellies a drink of varying colors, in which there is healing for people" (An-Nahl, 16:69). The Prophet Muhammad ﷺ recommended honey for digestive ailments, and {ct("ibn_qayyim", CT_DEFS["ibn_qayyim"], "Ibn al-Qayyim")} devoted extensive chapters to honey\'s therapeutic uses in {ct("tibb_nabawi", CT_DEFS["tibb_nabawi"], "al-Tibb al-Nabawi")}.', 'islamic'),
        ]
    },
]

# Generate HTML
html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nana's Golden Apothecary: Timeless Remedies for Modern Wellness</title>
  <link rel="stylesheet" href="nanaveda.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
</head>
<body class="masculine">
  <div class="text-controls">
    <button onclick="setTextSize('small')" title="Small text" id="ts-small">A-</button>
    <button onclick="setTextSize('medium')" title="Medium text" id="ts-medium" class="active">A</button>
    <button onclick="setTextSize('large')" title="Large text" id="ts-large">A+</button>
  </div>
  <div class="page">
    <div class="page-view active" id="page-title">
      <div class="title-page">
        <div class="title-frame">
          <div class="title-decoration"><span></span><span></span><span></span><span></span><span></span></div>
          <h1 class="title-main">Nana's<br>Golden<br>Apothecary</h1>
          <p class="title-subtitle">Timeless Remedies for Modern Wellness</p>
          <div class="title-divider"></div>
          <div class="title-attribution">
            <p class="title-compiled">Compiled for<br><strong>Nana Muneer Ansari</strong></p>
            <p style="margin-top: var(--space-lg);">by <strong>Ahraz Arifuddin &amp; Team6</strong></p>
          </div>
          <div class="title-squiggle"></div>
        </div>
      </div>
    </div>
    <div class="page-view" id="page-toc">
      <div class="toc">
        <h2 class="toc-title">Contents</h2>
        <ol class="toc-list">
'''
for r in RECIPES:
    html += f'          <li><span class="toc-number">{r["num"]}.</span> <a href="#" onclick="goToPage(\'{r["page"]}\'); return false;">{r["title"]}<span class="toc-sub">{r["subtitle"]}</span></a></li>\n'
html += '''        </ol>
      </div>
    </div>
'''
for r in RECIPES:
    img_block = f'<div class="visual-container" style="margin-left:0"><div class="visual-frame"><img src="{r["img"]}" alt="{r["title"]}" loading="lazy"></div></div>' if r['img'] else ''
    ings = ''.join(f'          <li><span class="ingredient-dot gold"></span> {ing[0]}</li>\n' for ing in r['ings'])
    steps = ''
    for i, (step_text, time_badge, context_text, context_type) in enumerate(r['steps'], 1):
        steps += f'        <div class="step"><div class="step-number">{i}</div><div class="step-content"><p>{step_text}</p><span class="step-time">{time_badge}</span></div></div>\n        <div class="context-block context-{context_type}"><p class="context-label">{context_type.capitalize()}</p><p>{context_text}</p></div>\n'
    tags = ''.join(f'            <span class="recipe-tag">{tag}</span>\n' for tag in r['tags'])
    
    html += f'''
    <div class="page-view" id="{r['page']}">
      <article id="recipe-{r['num']}">
        {img_block}
        <div class="recipe-header">
          <p class="recipe-number">Recipe {r['num']}</p>
          <h2 class="recipe-title">{r['title']}</h2>
          <p class="recipe-subtitle">{r['subtitle']}</p>
          <div class="recipe-meta">
            <span><i class="fas fa-clock"></i> {r['time']}</span>
            <span><i class="fas fa-fire"></i> {r['diff']}</span>
            <span><i class="fas fa-users"></i> {r['serves']}</span>
          </div>
          <div class="recipe-tags">
{tags}          </div>
        </div>
        <div class="heals-callout">
          <p class="heals-callout-title">Why This Heals</p>
          <p>{r['heals']}</p>
        </div>
        <div class="ingredients-box">
          <h3 class="ingredients-title">Ingredients</h3>
          <ul class="ingredients-list">
{ings}          </ul>
        </div>
        <div class="steps-section">
          <h3 class="steps-title">Method</h3>
{steps}        </div>
      </article>
    </div>
'''
html += f'''
    <footer class="book-footer">
      <p><strong>Nana's Golden Apothecary: Timeless Remedies for Modern Wellness</strong></p>
      <p>Compiled for Nana Muneer Ansari — by Ahraz Arifuddin &amp; Team6</p>
      <p style="margin-top:var(--space-md);font-size:0.8rem;color:var(--text-muted)">This book is for educational purposes. Consult a healthcare provider before using herbal remedies.</p>
    </footer>
  </div>
  <nav class="page-nav" aria-label="Page navigation">
    <button id="prevBtn" onclick="prevPage()" disabled><i class="fas fa-chevron-left"></i> Previous</button>
    <span class="page-counter" id="pageCounter">Page 1 of {len(RECIPES) + 2}</span>
    <button id="nextBtn" onclick="nextPage()">Next <i class="fas fa-chevron-right"></i></button>
  </nav>
  <script>
    const pages = ["page-title", "page-toc", ''' + ', '.join(f'"{r["page"]}"' for r in RECIPES) + '''];
    let currentPage = 0;
    function goToPage(pageId) {{ const idx = pages.indexOf(pageId); if (idx >= 0) currentPage = idx; updatePage(); }}
    function prevPage() {{ if (currentPage > 0) {{ currentPage--; updatePage(); }} }}
    function nextPage() {{ if (currentPage < pages.length - 1) {{ currentPage++; updatePage(); }} }}
    function updatePage() {{
      document.querySelectorAll(".page-view").forEach(p => p.classList.remove("active"));
      document.getElementById(pages[currentPage]).classList.add("active");
      document.getElementById("prevBtn").disabled = currentPage === 0;
      document.getElementById("nextBtn").disabled = currentPage === pages.length - 1;
      document.getElementById("pageCounter").textContent = `Page ${{currentPage + 1}} of ${{pages.length}}`;
      window.scrollTo({{ top: 0, behavior: "smooth" }});
    }}
    function setTextSize(size) {{
      document.documentElement.classList.remove("text-small", "text-medium", "text-large");
      document.documentElement.classList.add(`text-${{size}}`);
      document.querySelectorAll(".text-controls button").forEach(b => b.classList.remove("active"));
      document.getElementById(`ts-${{size}}`).classList.add("active");
    }}
    document.addEventListener("keydown", (e) => {{
      if (e.key === "ArrowRight" || e.key === " ") {{ e.preventDefault(); nextPage(); }}
      if (e.key === "ArrowLeft") {{ e.preventDefault(); prevPage(); }}
    }});
  </script>
</body>
</html>'''

with open(os.path.join(WORKSPACE, 'index.html'), 'w') as f:
    f.write(html)

print(f"Generated index.html: {len(html)} bytes")
