#!/usr/bin/env python3
"""Populate all 10 recipes with full content."""
import json
import os

WORKSPACE = '/Users/kethuda/Documents/ai work/Hermes/nanaveda/wrk/nvt6'

# Load terms data
with open(os.path.join(WORKSPACE, 'terms.json')) as f:
    terms = json.load(f)

with open(os.path.join(WORKSPACE, 'terms_complete.json')) as f:
    terms_complete = json.load(f)

# Complete recipe data
RECIPES = {
    'recipe-1': {
        'ingredients': [
            ('basmati rice', '1 cup'),
            ('split yellow mung dal', '½ cup'),
            ('water', '6 cups'),
            ('ghee or coconut oil', '1 tbsp'),
            ('cumin seeds', '1 tsp'),
            ('turmeric powder', '1 tsp'),
            ('fresh ginger, grated', '1 inch'),
            ('mustard seeds', '½ tsp'),
            ('asafoetida (hing)', 'Pinch'),
            ('salt', 'To taste'),
        ],
        'steps': [
            ('Wash the rice and mung dal together in several changes of cold water until the water runs clear. Soak them in fresh water for at least 30 minutes — or overnight if you have the time. This soaking step is crucial: it removes <span class="clickable-term" data-term="phytic acid">phytic acid</span> and makes the grains far gentler on the stomach.', '⏱ 30 min soak',
             'Soaking activates enzymes that break down <span class="clickable-term" data-term="phytic acid">phytic acid</span> — a compound in grains and legumes that binds to minerals like iron, zinc, and calcium, preventing their absorption. For seniors, whose mineral absorption naturally declines with age, this simple step can significantly increase the nutritional value of every bowl. Studies show soaking can reduce phytic acid content by 50-70%, making the iron in mung dal far more bioavailable.', 'health'),
            ('Heat the ghee in a heavy-bottomed pot over medium heat. Add the cumin seeds and mustard seeds. Wait for them to pop and sizzle — about 30 seconds. Add the asafoetida and stir for just a few seconds more.', '⏱ 2 min',
             'Kitchari (from Sanskrit <em>khiccā</em>, meaning "mixture") is one of the oldest recorded foods in human history. It appears in the <em>Charaka Samhita</em>, one of the foundational texts of Ayurveda dating to approximately 300 BCE. The dish was prescribed as a primary healing food during <span class="clickable-term" data-term="Panchakarma">Panchakarma</span> — Ayurvedic detoxification — and remains the go-to remedy for digestive complaints across the Indian subcontinent.', 'history'),
            ('Drain the soaked rice and dal, and add them to the pot. Stir gently for 2 minutes to coat every grain with the spiced ghee. Add the turmeric and grated ginger, stirring until fragrant.', '⏱ 3 min',
             'In Indian households, kitchari holds a dual identity: it is both the food of Buddhist monks (who eat it for breakfast to sustain long meditation sessions) and the first solid food given to infants. Its reputation as "comfort food with healing powers" crosses every social and spiritual boundary in South Asia.', 'cultural'),
            ('Pour in the 6 cups of water and add salt. Bring to a rolling boil, then reduce the heat to low. Cover the pot with a lid, leaving it slightly ajar to let steam escape. Let it simmer gently for 35–40 minutes, stirring occasionally.', '⏱ 40 min simmer',
             'The word "congee" (Chinese rice porridge) and "kitchari" likely share a common ancestor — the Sanskrit word <em>kanjika</em>, meaning "fermented rice water." As Buddhism spread from India to China along the <span class="clickable-term" data-term="Silk Road">Silk Road</span>, the healing rice porridge traveled with it, evolving into the congee traditions of East Asia.', 'funfact'),
            ('Taste and adjust salt. Ladle into bowls, top with fresh cilantro, and serve with a squeeze of lemon. Eat slowly, chewing well.', '⏱ Serve',
             'While kitchari itself is rooted in Ayurvedic tradition, the Islamic scholarly tradition has long recognized the healing properties of its core ingredients. <span class="clickable-term" data-term="Imam Ibn al-Qayyim">Imam Ibn al-Qayyim</span>, in his <em><span class="clickable-term" data-term="Prophetic Medicine">Prophetic Medicine</span></em> (<em><span class="clickable-term" data-term="Al-Tibb al-Nabawi">al-Tibb al-Nabawi</span></em>), discusses the benefits of rice porridge (<em>aruzz</em>) as a gentle, nourishing food for the sick and convalescent.', 'islamic'),
        ]
    },
    'recipe-2': {
        'ingredients': [
            ('whole milk (or oat milk)', '2 cups'),
            ('turmeric powder', '1 tsp'),
            ('ground cinnamon', '½ tsp'),
            ('ground black pepper', '¼ tsp'),
            ('fresh ginger, grated', '1 inch'),
            ('ghee or coconut oil', '1 tsp'),
            ('honey (optional)', '1 tsp'),
        ],
        'steps': [
            ('In a small saucepan, combine the milk, turmeric, cinnamon, black pepper, and grated ginger. Whisk together until smooth. Place over medium-low heat.', '⏱ 2 min',
             '<span class="clickable-term" data-term="piperine">Piperine</span>, the active compound in black pepper, inhibits an enzyme in the liver called glucuronidation — which would otherwise rapidly break down <span class="clickable-term" data-term="curcumin">curcumin</span> before it reaches the bloodstream. A landmark study published in <em>Planta Medica</em> (1998) found that just ¼ teaspoon of black pepper increased curcumin bioavailability by 2,000%. This is why traditional recipes always pair turmeric with pepper — ancient wisdom, modern validation.', 'science'),
            ('Heat gently, stirring frequently with a whisk. Do not let it boil — you want it steaming hot but not scalding. After about 5 minutes, add the ghee or coconut oil and stir until melted.', '⏱ 5 min',
             'Turmeric (<em>hurd</em> in Arabic) has been used in the Islamic world for over a millennium. <span class="clickable-term" data-term="Imam Ibn al-Qayyim">Imam Ibn al-Qayyim</span> describes it in <em><span class="clickable-term" data-term="Al-Tibb al-Nabawi">al-Tibb al-Nabawi</span></em> as beneficial for the liver and stomach, and notes its use as a natural dye and preservative. The Prophet Muhammad ﷺ said: "Allah did not send down a disease without sending down the cure" (Sahih al-Bukhari). Turmeric\'s extensive medicinal profile — confirmed by modern research — is seen by many scholars as a manifestation of this principle.', 'islamic'),
            ('Remove from heat. If desired, strain through a fine-mesh sieve for a smoother texture. Sweeten with honey if you like — add it after the milk has cooled slightly (below 110°F/43°C) to preserve honey\'s beneficial enzymes. Pour into your favorite mug and sip slowly, ideally in the evening.', '⏱ 2 min',
             '<span class="clickable-term" data-term="curcumin">Curcumin</span> crosses the blood-brain barrier and has been shown to increase Brain-Derived Neurotrophic Factor (BDNF) — a growth hormone that functions in the brain. Decreased BDNF is linked to depression, Alzheimer\'s disease, and age-related cognitive decline. A 2018 UCLA study found that participants who took curcumin showed significant improvements in memory and attention compared to placebo. For seniors, this golden milk is a delicious form of brain protection.', 'health'),
        ]
    },
    'recipe-3': {
        'ingredients': [
            ('beef or chicken bones (pre-cut by butcher)', '2 lbs'),
            ('water', '6 cups'),
            ('fresh ginger, sliced', '1 inch'),
            ('goji berries', '2 tbsp'),
            ('dried jujube dates (hong zao)', '4–5'),
            ('apple cider vinegar', '1 tsp'),
            ('salt', 'To taste'),
        ],
        'steps': [
            ('Place the bones in a large pot and cover with cold water. Bring to a boil over high heat. Once boiling, reduce heat and simmer for 5 minutes. Drain the bones and rinse them under clean water. Discard the blanching water.', '⏱ 10 min',
             'This initial blanching step removes blood, bone fragments, and impurities that would otherwise cloud the broth. In TCM, this step is considered essential for creating a "clean" broth that tonifies without creating internal "dampness" — a concept roughly corresponding to metabolic sluggishness and inflammation.', 'health'),
            ('Return the cleaned bones to the pot (or better yet, an Instant Pot). Add 6 cups of fresh water, the apple cider vinegar, and sliced ginger. The vinegar helps draw minerals from the bones into the broth. Bring to a boil, then reduce to the lowest possible heat. Cover and simmer gently for 4–6 hours.', '⏱ 4–6 hours',
             'Goji berries and jujube dates traveled westward along the <span class="clickable-term" data-term="Silk Road">Silk Road</span> for centuries, reaching the Middle East and eventually Europe. In the Islamic world, jujube (<em>unnab</em> or <em>sidr</em>) became deeply valued — mentioned in the Quran as a fruit of Paradise (<em>al-Waqi\'ah</em>, 56:28).', 'history'),
            ('During the last 30 minutes of simmering, add the goji berries and jujube dates. These delicate ingredients would disintegrate with prolonged cooking, so they are added at the end to preserve their flavor and nutritional value.', '⏱ 30 min',
             'Goji berries contain the highest concentration of <span class="clickable-term" data-term="zeaxanthin">zeaxanthin</span> of any common food — a carotenoid that accumulates in the retina and helps protect against age-related macular degeneration (AMD), the leading cause of vision loss in adults over 50. Regular consumption of goji berries has been shown in clinical studies to increase zeaxanthin levels in the blood by 26% after just 90 days of daily intake.', 'health'),
            ('Remove from heat. Strain the broth through a fine-mesh sieve into a clean pot or bowl. Discard the bones and spent ginger. Season with salt to taste. Serve warm, sipping slowly.', '⏱ 10 min',
             'Jujube dates are sometimes called "Chinese dates" or "red dates," but they are not related to the date palm at all. They belong to the <em>Rhamnaceae</em> (buckthorn) family and have been cultivated in China for over 4,000 years. A mature jujube tree can live for over 1,000 years — making it one of the longest-lived fruit trees on Earth.', 'funfact'),
        ]
    },
    'recipe-4': {
        'ingredients': [
            ('jasmine rice', '1 cup'),
            ('water or light broth', '8 cups'),
            ('dried shiitake mushrooms', '4'),
            ('fresh ginger, sliced', '1 inch'),
            ('soy sauce or tamari', '1 tbsp'),
            ('green onions, sliced', '2'),
            ('sesame oil', 'To finish'),
        ],
        'steps': [
            ('The night before: place the dried shiitake mushrooms in a bowl with 2 cups of warm water. Soak overnight (or at least 4 hours). This soaking liquid is liquid gold — do not discard it. In the morning, remove the mushrooms, squeeze out excess liquid, and slice them thinly.', '⏱ Overnight soak',
             'Shiitake mushrooms contain <span class="clickable-term" data-term="beta-glucans">beta-glucans</span> — complex sugars that "train" the immune system to respond more effectively to threats. Unlike stimulants that push the immune system in one direction, beta-glucans are <em>immunomodulators</em>: they balance immune response, calming it when overactive and activating it when sluggish. This makes them particularly valuable for seniors, whose immune function naturally declines with age — a process called <span class="clickable-term" data-term="immunosenescence">immunosenescence</span>.', 'science'),
            ('Rinse the jasmine rice in cold water until the water runs clear. Place the rice in a large pot with 8 cups of water (or broth), the reserved mushroom soaking liquid, and the sliced ginger. Bring to a boil over high heat. Alternatively, use a rice cooker with a "congee" or "porridge" setting.', '⏱ 5 min',
             'Congee has been a staple of Chinese cuisine since at least the Han Dynasty (206 BCE – 220 CE). Legend holds that Emperor Huangdi, the mythical founder of Chinese medicine, prescribed rice porridge as the foundation of all healing diets. In Japan, the Buddhist monk Eisai (1141–1215) introduced tea and mushroom cultivation from China.', 'history'),
            ('Once boiling, reduce heat to the lowest setting. Add the sliced shiitake. Cover with a lid slightly ajar. Simmer gently for 1.5 to 2 hours, stirring occasionally. The congee is ready when the rice has completely broken down into a creamy, porridge-like consistency.', '⏱ 1.5–2 hours',
             'In Chinese Buddhist tradition, congee is considered the food of compassion — simple, humble, and nourishing without excess. During the Tang Dynasty, Buddhist monasteries would distribute congee to the poor during winter months. The dish carries a spiritual dimension: eating it is an act of mindfulness, a reminder that healing does not require complexity.', 'cultural'),
            ('Stir in the soy sauce. Taste and adjust seasoning. Ladle into bowls, top with sliced green onions and a drizzle of sesame oil. Eat warm, preferably in the morning when the stomach is most receptive.', '⏱ 5 min',
             'Shiitake mushrooms are the second most cultivated mushroom in the world, after the common button mushroom. Their name comes from Japanese: <em>shii</em> (the Castanopsis tree they grow on) + <em>take</em> (mushroom). In ancient China, shiitake were so valued that they were reserved for the emperor and his court.', 'funfact'),
        ]
    },
    'recipe-5': {
        'ingredients': [
            ('whole milk (or oat milk)', '1 cup'),
            ('saffron threads', '8–10 threads'),
            ('ground cardamom', '¼ tsp'),
            ('ground cinnamon', '¼ tsp'),
            ('pinch of nutmeg', 'Pinch'),
            ('ghee or coconut oil', '1 tsp'),
            ('honey (optional)', '1 tsp'),
        ],
        'steps': [
            ('Place the saffron threads in a small dish. Add 1 tablespoon of warm water and let them steep for 5 minutes. The water will turn a deep golden-orange color, and the saffron\'s aroma will intensify. This pre-soaking step maximizes the extraction of saffron\'s active compounds — crocin and safranal.', '⏱ 5 min',
             'A landmark study published in the <em>Journal of Clinical Pharmacy and Therapeutics</em> (PMID: 24290594) found that saffron supplementation significantly improved sleep quality in adults over 60. Another study in the <em>Journal of Affective Disorders</em> showed that saffron was as effective as fluoxetine (Prozac) for mild-to-moderate depression — with far fewer side effects.', 'science'),
            ('Pour the milk into a small saucepan. Add the saffron with its soaking water, cardamom, cinnamon, and nutmeg. Whisk until the spices are fully dissolved. Place over medium-low heat.', '⏱ 2 min',
             'Saffron (<em>za\'faran</em> in Arabic) has been prized in Islamic culture for over a millennium. It was used in cooking, medicine, and as a dye for textiles and manuscripts. The great Islamic physician <span class="clickable-term" data-term="Ibn Sina">Ibn Sina</span> (Avicenna) described saffron in his <em>Canon of Medicine</em> as beneficial for heart strength, digestion, and eye health. Today, Iran produces over 90% of the world\'s saffron.', 'islamic'),
            ('Heat gently, stirring frequently. Do not let it boil — you want it steaming hot but not scalding. After about 5 minutes, add the ghee or coconut oil and stir until melted. The milk will take on a beautiful golden hue from the saffron.', '⏱ 5 min',
             'Sleep quality naturally declines with age — seniors produce less melatonin and spend less time in deep (slow-wave) sleep. Saffron has been shown to increase time spent in deep sleep and reduce nighttime awakenings without causing morning grogginess. Unlike pharmaceutical sleep aids, saffron does not suppress REM sleep or create dependency.', 'health'),
            ('Remove from heat. Sweeten with honey if desired (add after cooling slightly to preserve enzymes). Pour into a mug. Sip slowly, ideally 30–60 minutes before bedtime. Breathe deeply. Let the warmth and the spices do their work.', '⏱ 2 min',
             'It takes approximately 150,000 saffron crocus flowers to produce just one kilogram of dried saffron — making it the most expensive spice in the world by weight. Each flower produces only three tiny stigmas, which are hand-harvested at dawn before the flowers open. Saffron has been cultivated for over 3,500 years.', 'funfact'),
        ]
    },
    'recipe-6': {
        'ingredients': [
            ('water', '4 cups'),
            ('low-sodium miso paste', '3 tbsp'),
            ('dried wakame seaweed', '1 sheet'),
            ('fresh shiitake mushrooms, sliced', '4'),
            ('silken tofu, cubed', '1 block'),
            ('green onions, sliced', '2'),
            ('grated ginger', '1 tsp'),
        ],
        'steps': [
            ('Place the dried wakame in a small bowl of cold water. It will expand dramatically in just 5 minutes — a little goes a long way. Once rehydrated, drain and set aside. Cut into bite-sized pieces if the sheet is large.', '⏱ 5 min',
             'Wakame seaweed is one of the richest natural sources of iodine, calcium, iron, and magnesium. It also contains fucoxanthin — a carotenoid pigment unique to brown seaweed that has been shown in studies to support fat metabolism and reduce inflammation. Just one gram of dried wakame provides more iodine than the daily recommended intake, supporting thyroid function.', 'science'),
            ('In a pot, bring 4 cups of water to a gentle simmer. Add the sliced shiitake mushrooms and grated ginger. Simmer for 10 minutes to extract the mushroom umami and ginger warmth into the broth.', '⏱ 10 min',
             'Okinawa, Japan, is one of the world\'s five "Blue Zones" — regions where people live significantly longer than average. Okinawans consume miso soup daily, often for breakfast. The traditional Okinawan diet is rich in fermented foods, seaweed, and vegetables, with miso soup as its cornerstone.', 'history'),
            ('Remove the pot from heat. This is important: boiling destroys the beneficial probiotics in miso. Place the miso paste in a small bowl, add a few tablespoons of the warm (not boiling) broth, and whisk until smooth. Pour this mixture back into the pot and stir gently.', '⏱ 3 min',
             'As we age, the diversity of our gut microbiome naturally declines — a condition linked to increased inflammation, weakened immunity, and digestive issues. Fermented foods like miso introduce beneficial bacteria (<em>Aspergillus oryzae</em> and lactic acid bacteria) that help restore microbial balance.', 'health'),
            ('Add the rehydrated wakame and cubed silken tofu. Let them warm through for 1–2 minutes (do not boil). Ladle into bowls, top with sliced green onions, and serve immediately.', '⏱ 3 min',
             'While miso itself is Japanese, the concept of fermented foods for health has deep roots in Islamic medicine. The Prophet Muhammad ﷺ consumed and praised fermented foods including vinegar (<em>khall</em>), yogurt, and fermented drinks. <span class="clickable-term" data-term="Imam Ibn al-Qayyim">Imam Ibn al-Qayyim</span> discusses the benefits of vinegar and fermented foods in <em><span class="clickable-term" data-term="Al-Tibb al-Nabawi">al-Tibb al-Nabawi</span></em>.', 'islamic'),
        ]
    },
    'recipe-7': {
        'ingredients': [
            ('dried hibiscus flowers (flor de Jamaica)', '1 cup'),
            ('water', '6 cups'),
            ('cinnamon stick', '1'),
            ('sugar or honey', '½ cup'),
            ('vanilla extract (optional)', '1 tsp'),
            ('lime slices', 'For serving'),
        ],
        'steps': [
            ('Bring 6 cups of water to a boil in a large pot (or use an electric kettle with auto-shutoff for safety). Add the dried hibiscus flowers and cinnamon stick. Once the water returns to a boil, reduce heat and simmer for 15 minutes. The water will turn a deep, garnet red — the color of rubies.', '⏱ 15 min',
             'Hibiscus sabdariffa contains <span class="clickable-term" data-term="anthocyanins">anthocyanins</span> and polyphenols that act as natural <span class="clickable-term" data-term="ACE inhibitors">ACE inhibitors</span> — the same mechanism used by prescription blood pressure medications like lisinopril. A 2010 meta-analysis in the <em>Journal of Hypertension</em> found that hibiscus tea significantly reduced both systolic and diastolic blood pressure.', 'science'),
            ('Remove from heat. Add the sugar or honey while the liquid is still warm, stirring until dissolved. Add vanilla extract if using. Allow the mixture to cool to room temperature.', '⏱ 10 min',
             'Hibiscus sabdariffa is native to West Africa, where it has been used for centuries to make a refreshing drink called <em>bissap</em> or <em>sobolo</em>. Enslaved Africans brought hibiscus to the Americas during the <span class="clickable-term" data-term="transatlantic slave trade">transatlantic slave trade</span>, and it became deeply embedded in Latin American culture.', 'history'),
            ('Strain through a fine-mesh sieve into a pitcher. Discard the hibiscus flowers and cinnamon stick. Refrigerate until cold. Serve over ice with lime slices. The drink should be tart, sweet, and deeply refreshing.', '⏱ Chill & serve',
             'In many Latin American countries, agua de Jamaica is served at celebrations, family gatherings, and holiday meals. It is one of the three "aguas frescas" (fresh waters) that form the backbone of Mexican beverage culture — alongside horchata and tamarindo. In West Africa, bissap is served to guests as a sign of hospitality.', 'cultural'),
        ]
    },
    'recipe-8': {
        'ingredients': [
            ('pre-cooked beetroots, chopped', '2 medium'),
            ('fresh ginger, sliced', '1 inch'),
            ('water', '4 cups'),
            ('sugar or honey', '½ cup'),
            ('rose water', '2 tbsp'),
            ('lemon juice', '1 lemon'),
            ('dried rose petals', 'For garnish'),
        ],
        'steps': [
            ('Place the pre-cooked beetroot and ginger in a pot with 4 cups of water. Bring to a boil, then reduce heat and simmer for 20–30 minutes until the beetroot is very tender and the liquid has turned a deep, ruby red. Using pre-cooked beets eliminates the difficult peeling and chopping of raw beetroot.', '⏱ 30 min',
             'Beetroot is one of the richest dietary sources of nitrates, which the body converts to <span class="clickable-term" data-term="nitric oxide">nitric oxide</span> — a molecule that relaxes and dilates blood vessels. A 2015 study in the journal <em>Hypertension</em> found that drinking beetroot juice daily reduced systolic blood pressure by an average of 4–5 mmHg — comparable to some blood pressure medications.', 'science'),
            ('Strain the liquid through a fine-mesh sieve into a clean pot. Press the beetroot gently to extract all the liquid. Discard the solids (or save for another use — they are delicious in salads). Return the strained liquid to the pot.', '⏱ 5 min',
             'Rose water holds a special place in Islamic culture and medicine. The Prophet Muhammad ﷺ is reported to have valued roses highly, and rose water has been used in the Islamic world for centuries — in cooking, medicine, and perfumery. <span class="clickable-term" data-term="Imam Ibn al-Qayyim">Imam Ibn al-Qayyim</span> notes that rose water "strengthens the heart and brings joy to the soul."', 'islamic'),
            ('Add the sugar or honey to the warm beetroot liquid and stir until dissolved. Add the rose water and lemon juice. Stir well. Taste and adjust sweetness — it should be sweet-tart with a floral aroma. The lemon juice brightens the flavor and adds vitamin C, which enhances iron absorption.', '⏱ 3 min',
             '<span class="clickable-term" data-term="Sharbat">Sharbat</span> (from Arabic <em>shariba</em>, "to drink") is one of the oldest beverage traditions in the Islamic world. Medieval Arabic cookbooks describe dozens of sharbat recipes using roses, pomegranates, lemons, and herbs. The <span class="clickable-term" data-term="Ottoman Empire">Ottoman Empire</span> elevated sharbat-making to an art form, with dedicated sharbat-makers in the imperial palace.', 'history'),
            ('Allow to cool, then refrigerate. Serve chilled over ice, garnished with dried rose petals. This concentrate can be diluted with water or sparkling water to taste. Store in the refrigerator for up to one week.', '⏱ Chill & serve',
             'The deep red color of beetroot comes from betalain pigments — the same pigments found in bougainvillea flowers. Betalains are powerful antioxidants that have been shown to protect cells from oxidative damage. Interestingly, betalains and <span class="clickable-term" data-term="anthocyanins">anthocyanins</span> never appear in the same plant — they are mutually exclusive in nature.', 'funfact'),
        ]
    },
    'recipe-9': {
        'ingredients': [
            ('black seed (nigella sativa)', '½ cup'),
            ('raw honey', '1 cup'),
            ('ground black seed (optional)', '1 tsp'),
            ('saffron threads (optional)', 'Pinch'),
        ],
        'steps': [
            ('Lightly toast the whole black seeds in a dry pan over low heat for 2–3 minutes, stirring constantly. You will hear them crackle and smell a warm, peppery aroma. Do not let them burn — the goal is to lightly awaken the oils, not to cook them. Remove from heat and allow to cool.', '⏱ 5 min',
             'The Prophet Muhammad ﷺ said: "Hold on to the black seed — it is a cure for every disease except death" (Sahih al-Bukhari 5688, Sahih Muslim 2215). This hadith has inspired over 1,400 years of black seed use in the Islamic world. The seed is called <em>habbatul barakah</em> — "the blessed seed" — in Arabic.', 'islamic'),
            ('Once cooled, grind the toasted seeds coarsely in a mortar and spice grinder. You want a mix of cracked seeds and some powder — not a fine flour. The texture adds interest and ensures the oils are released slowly. A coarse grind is also gentler on the digestive system than a fine powder.', '⏱ 5 min',
             'The primary active compound in black seed is <span class="clickable-term" data-term="thymoquinone">thymoquinone</span> — a molecule with remarkable pharmacological properties. Over 1,500 peer-reviewed studies have documented thymoquinone\'s anti-inflammatory, antioxidant, antimicrobial, and anti-cancer effects. For seniors, its immune-modulating and anti-inflammatory properties are particularly valuable.', 'science'),
            ('In a clean glass jar, layer the ground black seed with the raw honey. Stir gently to combine, ensuring the seeds are fully coated in honey. If using, add the saffron threads. Seal the jar tightly. The honey acts as both a preservative and a synergistic enhancer.', '⏱ 3 min',
             'Raw honey never spoils. Archaeologists have found 3,000-year-old honey in Egyptian tombs that was still edible. Honey\'s remarkable preservative properties come from its low moisture content, high acidity, and the presence of hydrogen peroxide produced by enzymes bees add to the nectar. The Prophet Muhammad ﷺ praised honey as a healing substance: "Healing is in three things: a drink of honey, a cut of the cupping knife, or cauterization by fire" (Sahih al-Bukhari).', 'health'),
            ('Store at room temperature in a cool, dark place. Allow the flavors to meld for at least 24 hours before using. Take 1–2 teaspoons daily — straight from the spoon, or stirred into warm water, tea, or milk. Best taken in the morning on an empty stomach for maximum absorption.', '⏱ Daily use',
             'Black seed was found in Tutankhamun\'s tomb — placed there, it is believed, to accompany the young king into the afterlife. The seed has been used continuously in Mediterranean and Middle Eastern cultures for over 3,000 years. The Roman physician <span class="clickable-term" data-term="Dioscorides">Dioscorides</span> (40–90 CE) prescribed black seed for headaches, toothache, and respiratory complaints.', 'history'),
        ]
    },
    'recipe-10': {
        'ingredients': [
            ('fresh sage leaves (or 1 tbsp dried)', '8–10 leaves'),
            ('water', '2 cups'),
            ('raw honey', '1–2 tsp'),
            ('lemon slice (optional)', '1 slice'),
        ],
        'steps': [
            ('Bring 2 cups of water to a boil. If using an electric kettle, simply boil the water and pour it into a teapot or mug. Add the sage leaves — gently bruise them between your fingers before adding to release their essential oils. If using dried sage, simply measure it into the pot or a tea infuser.', '⏱ 2 min',
             'A landmark study by <span class="clickable-term" data-term="Scholey">Scholey</span> et al. (2008) demonstrated that sage extract significantly improved memory and attention in healthy older adults. Participants showed better word recall, improved accuracy on attention tasks, and reported feeling more alert and calm. A 2014 study in <em>Psychopharmacology</em> found that sage enhanced cognitive performance in adults with mild-to-moderate Alzheimer\'s disease.', 'science'),
            ('Cover and steep for 5–7 minutes. The water will turn a pale green-gold color, and the aroma will be warm, herbaceous, and slightly peppery. Do not over-steep — sage can become bitter if left too long. The ideal steeping time balances flavor with potency.', '⏱ 7 min steep',
             'The genus name <em>Salvia</em> comes from the Latin <em>salvare</em>, meaning "to save" or "to heal" — a testament to sage\'s revered status in European herbal tradition. The great Islamic physician <span class="clickable-term" data-term="Al-Zahrawi">Al-Zahrawi</span> (Abulcasis) described sage in his medical encyclopedia as beneficial for memory, digestion, and oral health.', 'history'),
            ('Strain the leaves (or remove the infuser). Add honey to taste — stir until dissolved. Add a slice of lemon if desired. Sip slowly while warm. The honey not only sweetens the tea but adds its own healing compounds, creating a synergistic effect. Best enjoyed in the morning or early afternoon.', '⏱ 2 min',
             'Honey holds a uniquely honored place in Islamic medicine. The Quran dedicates an entire passage to honey and its healing properties: "There comes from their bellies a drink of varying colors, in which there is healing for people" (An-Nahl, 16:69). The Prophet Muhammad ﷺ recommended honey for digestive ailments, and <span class="clickable-term" data-term="Ibn al-Qayyim">Ibn al-Qayyim</span> devoted extensive chapters to honey\'s therapeutic uses in <em><span class="clickable-term" data-term="Al-Tibb al-Nabawi">al-Tibb al-Nabawi</span></em>.', 'islamic'),
        ]
    },
}

# Read existing index.html
with open(os.path.join(WORKSPACE, 'index.html')) as f:
    html = f.read()

# For each recipe, replace the stub content with full content
for recipe_id, data in RECIPES.items():
    # Build ingredients HTML
    ingredients_html = ''
    for ingredient, amount in data['ingredients']:
        ingredients_html += f'          <li><span class="ingredient-dot gold"></span> {ingredient}</li>\n'
    
    # Build steps HTML
    steps_html = ''
    for i, (step_text, time_badge, context_text, context_type) in enumerate(data['steps'], 1):
        steps_html += f'''        <div class="step">
          <div class="step-number">{i}</div>
          <div class="step-content">
            <p>{step_text}</p>
            <span class="step-time">{time_badge}</span>
          </div>
        </div>
        <div class="context-block context-{context_type}">
          <p class="context-label">{context_type.capitalize()}</p>
          <p>{context_text}</p>
        </div>
'''
    
    # Replace the stub ingredients
    old_ingredients = f'<div class="ingredients-box">\n        <h3 class="ingredients-title">📋 Ingredients</h3>\n        <p style="color:var(--text-muted);font-style:italic">Full ingredient list being compiled by Sheikh Al-Jabr...</p>\n      </div>'
    new_ingredients = f'''<div class="ingredients-box">
        <h3 class="ingredients-title">📋 Ingredients</h3>
        <ul class="ingredients-list">
{ingredients_html}        </ul>
      </div>'''
    
    # Only replace if the old text exists
    if old_ingredients in html:
        html = html.replace(old_ingredients, new_ingredients)
    
    # Replace the stub steps
    old_steps = f'<div class="steps-section">\n        <h3 class="steps-title">Method</h3>\n        <div class="step">\n          <div class="step-number">1</div>\n          <div class="step-content">\n            <p style="color:var(--text-muted);font-style:italic">Detailed recipe steps with woven Islamic/historical context coming soon from Sheikh Al-Jabr...</p>\n          </div>\n        </div>\n      </div>'
    new_steps = f'''<div class="steps-section">
        <h3 class="steps-title">Method</h3>
{steps_html}      </div>'''
    
    if old_steps in html:
        html = html.replace(old_steps, new_steps)

# Write updated HTML
with open(os.path.join(WORKSPACE, 'index.html'), 'w') as f:
    f.write(html)

print(f"Updated index.html with full recipe content")
print(f"Total size: {len(html)} bytes")
