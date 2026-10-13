#!/usr/bin/env python3
"""Generate comprehensive HTML with clickable terms, images, and SVG visuals."""
import json
import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(WORKSPACE, 'ASSETS')

# Load asset data
with open(os.path.join(ASSETS, 'unsplash_images.json')) as f:
    unsplash = json.load(f)

with open(os.path.join(ASSETS, 'grokipedia_terms.json')) as f:
    grokipedia = json.load(f)

# Custom term content for terms Grokipedia got wrong or missed
CUSTOM_TERMS = {
    'piperine': 'Piperine is the bioactive alkaloid in black pepper (Piper nigrum) responsible for its pungency. In the liver, it inhibits the enzyme UDP-glucuronosyltransferase, which would otherwise rapidly break down curcumin. A 1998 study in Planta Medica found that just 20 mg of piperine increased curcumin bioavailability by 2,000%. Traditional Ayurvedic recipes pairing turmeric with black pepper anticipated this discovery by centuries.',
    'thymoquinone': 'Thymoquinone is the primary active compound in Nigella sativa (black seed), comprising 30–48% of the seed\'s essential oil. It exhibits potent anti-inflammatory, antioxidant, and immune-modulating properties through multiple molecular pathways, including inhibition of NF-κB and COX-2 enzymes. Over 1,500 peer-reviewed studies have documented its pharmacological effects.',
    'anthocyanins': 'Anthocyanins are water-soluble pigments belonging to the flavonoid family that give fruits and vegetables their red, purple, or blue coloration. In the body, they function as powerful antioxidants, scavenging free radicals and reducing oxidative stress. Studies show they improve cardiovascular health, cognitive function, and insulin sensitivity. Hibiscus sabdariffa contains some of the highest concentrations of any common food.',
    'zeaxanthin': 'Zeaxanthin is a carotenoid pigment that accumulates in the macula of the human retina, where it filters harmful blue light and protects against oxidative damage. Goji berries (Lycium barbarum) contain the highest concentration of zeaxanthin of any common food—approximately 100 mg per 100 g of dried berries. Regular consumption increases serum zeaxanthin levels by 26% after 90 days, reducing risk of age-related macular degeneration.',
    'tridoshic': 'In Ayurveda, the three doshas—Vata (air/space), Pitta (fire/water), and Kapha (earth/water)—govern physiological and psychological functions. A food or remedy described as "tridoshic" balances all three doshas rather than aggravating any single one. This is rare and highly valued, meaning the remedy is suitable for virtually any constitution and can be consumed long-term without adverse effects.',
    'spleen qi': 'In Traditional Chinese Medicine (TCM), the Spleen is responsible for transforming food into qi (vital energy) and blood. "Spleen qi deficiency" manifests as fatigue, poor appetite, loose stools, and weak muscles. Jujube dates and ginger are classified as "spleen qi tonics"—they strengthen digestive function and energy production. The concept parallels modern understanding of gut health as central to systemic vitality.',
    'immunosenescence': 'Immunosenescence refers to the gradual deterioration of the immune system associated with aging. It involves reduced production of naive T-cells, decreased vaccine responsiveness, and chronic low-grade inflammation (inflammaging). Beta-glucans from mushrooms like shiitake are immunomodulators—they enhance immune function in the elderly without overstimulating it, helping restore balance to an aging immune system.',
    'ACE inhibitors': 'ACE (angiotensin-converting enzyme) inhibitors are a class of drugs used to treat hypertension and heart failure. They work by blocking the enzyme that converts angiotensin I to angiotensin II, a potent vasoconstrictor. Hibiscus sabdariffa contains natural ACE-inhibitory compounds—anthocyanins and polyphenols that function through the same mechanism as prescription drugs like lisinopril, but with fewer side effects.',
    'Al-Zahrawi': 'Abu al-Qasim Khalaf ibn al-Abbas al-Zahrawi (936–1013 CE), known in the West as Abulcasis, was an Andalusian physician, surgeon, and chemist. He is considered the father of modern surgery and authored the 30-volume medical encyclopedia "Al-Tasrif," which included descriptions of over 200 surgical instruments and detailed herbal remedies. His work on sage (Salvia officinalis) described its benefits for memory, digestion, and oral health.',
    'Ibn al-Qayyim': 'Imam Ibn Qayyim al-Jawziyya (1292–1350 CE) was a prominent Islamic scholar and physician whose work "Al-Tibb al-Nabawi" (Prophetic Medicine) systematically compiled the medical teachings of Prophet Muhammad ﷺ. His approach integrated spiritual, dietary, and herbal therapies, emphasizing moderation, natural foods, and the healing properties of honey, black seed, and other substances. His work remains influential in Islamic medical tradition today.',
    'Ibn Sina': 'Ibn Sina (980–1037 CE), known in the West as Avicenna, was a Persian polymath whose "Canon of Medicine" became the standard medical textbook in European universities for over 600 years. He described saffron\'s benefits for heart strength, digestion, and eye health, and his systematic approach to pharmacology influenced both Islamic and European medicine.',
    'Habba Sawda': 'Habba Sawda (حبة البركة, "the blessed seed") is the Arabic name for Nigella sativa, also known as black seed or black cumin. It is called "habbatul barakah" in Islamic tradition because the Prophet Muhammad ﷺ described it as a cure for "every disease except death" (Sahih al-Bukhari 5688). The seed has been used continuously in Mediterranean and Middle Eastern medicine for over 3,000 years.',
    'Scholey': 'Dr. Andrew Scholey is a professor of psychopharmacology at Swinburne University of Technology in Melbourne, Australia. His 2008 study published in "Psychopharmacology" demonstrated that sage extract significantly improved memory and attention in healthy older adults. A subsequent 2014 study found that sage enhanced cognitive performance in adults with mild-to-moderate Alzheimer\'s disease through acetylcholinesterase inhibition.',
    'Panchakarma': 'Panchakarma (पञ्चकर्म, "five actions") is a traditional Ayurvedic detoxification and rejuvenation protocol consisting of five therapeutic procedures: Vamana (emesis), Virechana (purgation), Basti (enema), Nasya (nasal administration), and Raktamokshana (bloodletting). Kitchari is the primary food prescribed during Panchakarma because it provides complete nutrition while gently cleansing the digestive tract of accumulated toxins (ama).',
    'Sharbat': 'Sharbat (from Arabic "shariba," to drink) is one of the oldest beverage traditions in the Islamic world, dating back over 1,000 years. Medieval Arabic cookbooks describe dozens of sharbat recipes using roses, pomegranates, lemons, and herbs. The Ottoman Empire elevated sharbat-making to an art form, with dedicated sharbat-makers in the imperial palace. Sharbats were served chilled in special glasses and considered both refreshing and medicinal.',
    'Memphis Design': 'Memphis Design was a postmodern design movement founded in Milan in 1981 by Ettore Sottsass. Characterized by bold geometric shapes, clashing colors, and playful patterns—including squiggles, dots, and terrazzo textures—it dominated 1980s visual culture from architecture to furniture. The aesthetic represented rebellion against minimalism and embraced ornamentation, irony, and pop culture references.',
    'Ottoman Empire': 'The Ottoman Empire (1299–1922 CE) was one of the longest-lasting empires in history, stretching from North Africa through the Middle East to Southeast Europe. Ottoman culinary and medical traditions synthesized Persian, Arab, Turkish, and Byzantine influences. Sharbat-making became a refined art form in the imperial palace, and Ottoman physicians developed sophisticated herbal remedies using ingredients from across the empire.'
}

# Clickable terms with their definitions (short version for inline display)
CLICKABLE_TERMS = {
    'phytic acid': 'A compound in grains and legumes that binds to minerals, reducing their absorption. Soaking deactivates it.',
    'piperine': 'The active compound in black pepper that increases curcumin absorption by 2,000%.',
    'curcumin': 'The bioactive yellow pigment in turmeric with potent anti-inflammatory and antioxidant properties.',
    'thymoquinone': 'The primary active compound in black seed with anti-inflammatory and immune-modulating effects.',
    'beta-glucans': 'Complex sugars in mushrooms that "train" the immune system to respond more effectively.',
    'anthocyanins': 'Antioxidant pigments that give foods their red/purple color and protect against oxidative damage.',
    'zeaxanthin': 'A carotenoid pigment that accumulates in the retina and protects against macular degeneration.',
    'nitric oxide': 'A molecule that relaxes blood vessels, improving circulation and lowering blood pressure.',
    'ACE inhibitors': 'Compounds that block the enzyme constricting blood vessels—used by both drugs and hibiscus.',
    'agni': 'The Ayurvedic concept of digestive fire—the metabolic energy that transforms food into nourishment.',
    'spleen qi': 'The TCM concept of digestive energy responsible for transforming food into vital energy and blood.',
    'tridoshic': 'A remedy that balances all three Ayurvedic constitutional types (Vata, Pitta, Kapha).',
    'Panchakarma': 'The Ayurvedic detoxification protocol for which kitchari is the primary prescribed food.',
    'immunosenescence': 'The age-related decline in immune function that makes seniors more susceptible to illness.',
    'Imam Ibn al-Qayyim': '14th-century Islamic scholar whose "Prophetic Medicine" compiled the medical teachings of Muhammad ﷺ.',
    'Ibn Sina (Avicenna)': 'Persian polymath whose "Canon of Medicine" was the standard textbook in Europe for 600 years.',
    'Al-Zahrawi (Abulcasis)': '10th-century Andalusian physician considered the father of modern surgery.',
    'Scholey': 'Dr. Andrew Scholey, whose 2008 study proved sage improves memory in older adults.',
    'Habba Sawda': 'The Arabic name for black seed, meaning "the blessed seed"—a cure for "every disease except death."',
    'Prophetic Medicine': 'The Islamic healing tradition derived from the medical recommendations of Prophet Muhammad ﷺ.',
    'Al-Tibb al-Nabawi': 'Ibn al-Qayyim\'s seminal work compiling Prophetic medical guidance.',
    'Sharbat': 'An ancient Arabic beverage tradition—sweetened herbal drinks served chilled as both refreshment and medicine.',
    'Memphis Design': 'A bold 1980s design movement characterized by geometric shapes, clashing colors, and playful patterns.',
    'Silk Road': 'The ancient trade network connecting China to the Mediterranean, transmitting spices, ideas, and remedies.',
    'Ottoman Empire': 'A centuries-spanning empire that synthesized and advanced Islamic medical and culinary traditions.'
}

print("Loaded clickable terms:", len(CLICKABLE_TERMS))
print("Loaded custom term details:", len(CUSTOM_TERMS))
print("Loaded Unplash images for:", len(unsplash), "recipes")
print("Loaded Grokipedia data for:", len(grokipedia), "terms")
