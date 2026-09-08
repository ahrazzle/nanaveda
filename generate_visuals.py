#!/usr/bin/env python3
"""Generate custom SVG visuals for Nanaveda recipe book."""
import os

WORKSPACE = '/Users/kethuda/Documents/ai work/Hermes/nanaveda/wrk/nvt6'
ASSETS = os.path.join(WORKSPACE, 'ASSETS')

def generate_silk_road_map():
    """Generate a simplified Silk Road trade route map."""
    svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="auto">
  <defs>
    <style>
      .map-bg { fill: #faf6ee; }
      .land { fill: #e8dfc8; stroke: #b8a88a; stroke-width: 1; }
      .route { fill: none; stroke: #c85a4a; stroke-width: 3; stroke-dasharray: 8,4; }
      .route-node { fill: #b88a3a; }
      .city-label { font-family: Georgia, serif; font-size: 14px; fill: #2a2018; font-weight: bold; }
      .region-label { font-family: Georgia, serif; font-size: 11px; fill: #6b5a48; font-style: italic; }
      .title { font-family: Georgia, serif; font-size: 18px; fill: #2a2018; font-weight: bold; }
      .legend-text { font-family: Georgia, serif; font-size: 11px; fill: #4a3828; }
    </style>
  </defs>
  
  <!-- Background -->
  <rect class="map-bg" width="800" height="400"/>
  
  <!-- Simplified land masses -->
  <path class="land" d="M50,180 Q200,120 350,160 T650,140 L750,180 L750,320 Q600,340 450,320 T150,340 L50,320 Z"/>
  
  <!-- Europe -->
  <ellipse class="land" cx="120" cy="200" rx="60" ry="40"/>
  
  <!-- Middle East -->
  <ellipse class="land" cx="320" cy="220" rx="80" ry="50"/>
  
  <!-- India -->
  <path class="land" d="M480,200 Q520,160 560,200 Q580,260 540,290 Q480,280 460,240 Z"/>
  
  <!-- China/East Asia -->
  <path class="land" d="M620,140 Q700,120 750,160 Q760,220 720,260 Q650,270 600,240 Q580,200 620,140 Z"/>
  
  <!-- Main Silk Road Route -->
  <path class="route" d="M150,200 Q250,210 320,220 Q400,230 460,220 Q520,210 580,200 Q640,190 700,170"/>
  
  <!-- Alternative sea route -->
  <path class="route" d="M320,280 Q400,300 480,290 Q540,280 580,260" stroke="#4a9fa8" stroke-width="2" stroke-dasharray="4,4"/>
  
  <!-- City nodes -->
  <circle class="route-node" cx="150" cy="200" r="6"/>
  <circle class="route-node" cx="320" cy="220" r="6"/>
  <circle class="route-node" cx="460" cy="220" r="6"/>
  <circle class="route-node" cx="580" cy="200" r="6"/>
  <circle class="route-node" cx="700" cy="170" r="6"/>
  
  <!-- City labels -->
  <text class="city-label" x="150" y="180" text-anchor="middle">Constantinople</text>
  <text class="city-label" x="320" y="200" text-anchor="middle">Baghdad</text>
  <text class="city-label" x="460" y="200" text-anchor="middle">Delhi</text>
  <text class="city-label" x="580" y="180" text-anchor="middle">Kashgar</text>
  <text class="city-label" x="700" y="150" text-anchor="middle">Xi'an</text>
  
  <!-- Region labels -->
  <text class="region-label" x="100" y="240" text-anchor="middle">Europe</text>
  <text class="region-label" x="320" y="260" text-anchor="middle">Middle East</text>
  <text class="region-label" x="510" y="250" text-anchor="middle">India</text>
  <text class="region-label" x="670" y="220" text-anchor="middle">China</text>
  
  <!-- Title -->
  <text class="title" x="400" y="80" text-anchor="middle">The Silk Road — Highway of Healing</text>
  <text class="region-label" x="400" y="100" text-anchor="middle">Ingredients, ideas, and remedies traveled these routes for over 1,500 years</text>
  
  <!-- Legend -->
  <line x1="100" y1="350" x2="130" y2="350" stroke="#c85a4a" stroke-width="3" stroke-dasharray="8,4"/>
  <text class="legend-text" x="140" y="355">Overland Route</text>
  <line x1="250" y1="350" x2="280" y2="350" stroke="#4a9fa8" stroke-width="2" stroke-dasharray="4,4"/>
  <text class="legend-text" x="290" y="355">Maritime Route</text>
  
  <!-- Ingredient movement arrows -->
  <g transform="translate(200, 120)">
    <path d="M0,20 L30,0 L30,10 L50,10 L50,30 L30,30 L30,40 Z" fill="#d4a853" opacity="0.7"/>
    <text x="60" y="25" fill="#2a2018" font-size="12" font-family="Georgia, serif">Ginger, Turmeric → West</text>
  </g>
  
  <g transform="translate(450, 120)">
    <path d="M0,10 L20,10 L20,0 L50,20 L20,40 L20,30 L0,30 Z" fill="#4a9fa8" opacity="0.7"/>
    <text x="60" y="25" fill="#2a2018" font-size="12" font-family="Georgia, serif">← Saffron, Rose, Dates</text>
  </g>
</svg>'''
    
    with open(os.path.join(ASSETS, 'silk_road_map.svg'), 'w') as f:
        f.write(svg)
    print("Generated: silk_road_map.svg")

def generate_nitric_oxide_pathway():
    """Generate diagram showing how dietary nitrates become nitric oxide."""
    svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 300" width="100%" height="auto">
  <defs>
    <style>
      .bg { fill: #faf6ee; }
      .box { fill: #e8dfc8; stroke: #b8a88a; stroke-width: 2; rx: 8; }
      .highlight { fill: #4a9fa8; }
      .arrow { stroke: #c85a4a; stroke-width: 3; fill: none; marker-end: url(#arrowhead); }
      .label { font-family: Georgia, serif; font-size: 14px; fill: #2a2018; font-weight: bold; }
      .sublabel { font-family: Georgia, serif; font-size: 11px; fill: #6b5a48; font-style: italic; }
      .title { font-family: Georgia, serif; font-size: 16px; fill: #2a2018; font-weight: bold; }
      .molecule { font-family: Georgia, serif; font-size: 12px; fill: #2a2018; }
    </style>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#c85a4a"/>
    </marker>
  </defs>
  
  <rect class="bg" width="800" height="300"/>
  
  <!-- Title -->
  <text class="title" x="400" y="40" text-anchor="middle">How Beetroot Lowers Blood Pressure</text>
  <text class="sublabel" x="400" y="58" text-anchor="middle">The Nitric Oxide Pathway</text>
  
  <!-- Step 1: Ingestion -->
  <rect class="box" x="30" y="100" width="120" height="80" rx="8"/>
  <text class="label" x="90" y="130" text-anchor="middle">Step 1</text>
  <text class="label" x="90" y="150" text-anchor="middle">Consume</text>
  <text class="sublabel" x="90" y="168" text-anchor="middle">Beetroot nitrates</text>
  
  <!-- Arrow 1 -->
  <line class="arrow" x1="150" y1="140" x2="190" y2="140"/>
  
  <!-- Step 2: Conversion in mouth -->
  <rect class="box" x="190" y="100" width="120" height="80" rx="8"/>
  <text class="label" x="250" y="130" text-anchor="middle">Step 2</text>
  <text class="label" x="250" y="150" text-anchor="middle">Oral Bacteria</text>
  <text class="sublabel" x="250" y="168" text-anchor="middle">Nitrate → Nitrite</text>
  
  <!-- Arrow 2 -->
  <line class="arrow" x1="310" y1="140" x2="350" y2="140"/>
  
  <!-- Step 3: Stomach conversion -->
  <rect class="box" x="350" y="100" width="120" height="80" rx="8"/>
  <text class="label" x="410" y="130" text-anchor="middle">Step 3</text>
  <text class="label" x="410" y="150" text-anchor="middle">Stomach Acid</text>
  <text class="sublabel" x="410" y="168" text-anchor="middle">Nitrite → NO₂</text>
  
  <!-- Arrow 3 -->
  <line class="arrow" x1="470" y1="140" x2="510" y2="140"/>
  
  <!-- Step 4: Nitric Oxide -->
  <rect class="highlight" x="510" y="100" width="120" height="80" rx="8" fill="#4a9fa8"/>
  <text class="label" x="570" y="130" text-anchor="middle" fill="white">Step 4</text>
  <text class="label" x="570" y="150" text-anchor="middle" fill="white">Nitric Oxide</text>
  <text class="sublabel" x="570" y="168" text-anchor="middle" fill="white">NO molecule</text>
  
  <!-- Arrow down -->
  <line class="arrow" x1="570" y1="180" x2="570" y2="220"/>
  
  <!-- Result -->
  <rect class="box" x="410" y="220" width="160" height="60" rx="8"/>
  <text class="label" x="490" y="245" text-anchor="middle">Vasodilation</text>
  <text class="sublabel" x="490" y="265" text-anchor="middle">Blood vessels relax and widen</text>
  
  <!-- Arrow to result -->
  <line class="arrow" x1="570" y1="280" x2="570" y2="310" stroke-dasharray="4,4"/>
  
  <!-- Final result -->
  <rect class="highlight" x="410" y="310" width="160" height="40" rx="8" fill="#b88a3a"/>
  <text class="label" x="490" y="335" text-anchor="middle" fill="white">Blood Pressure Drops</text>
  
  <!-- Time indicator -->
  <text class="sublabel" x="60" y="230" text-anchor="middle">Effect peaks</text>
  <text class="sublabel" x="60" y="248" text-anchor="middle">2-3 hours</text>
  <text class="sublabel" x="60" y="266" text-anchor="middle">after consumption</text>
  
  <!-- Molecule diagrams -->
  <text class="molecule" x="90" y="200" text-anchor="middle">NO₃⁻</text>
  <text class="molecule" x="250" y="200" text-anchor="middle">NO₂⁻</text>
  <text class="molecule" x="410" y="200" text-anchor="middle">NO₂</text>
  <text class="molecule" x="570" y="200" text-anchor="middle">NO</text>
</svg>'''
    
    with open(os.path.join(ASSETS, 'nitric_oxide_pathway.svg'), 'w') as f:
        f.write(svg)
    print("Generated: nitric_oxide_pathway.svg")

def generate_curcumin_absorption():
    """Generate diagram showing curcumin absorption with piperine."""
    svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 280" width="100%" height="auto">
  <defs>
    <style>
      .bg { fill: #faf6ee; }
      .liver-box { fill: #e8dfc8; stroke: #b8a88a; stroke-width: 2; rx: 8; }
      .curcumin { fill: #d4a853; }
      .piperine { fill: #4a9fa8; }
      .blocked { fill: #c85a4a; opacity: 0.3; }
      .label { font-family: Georgia, serif; font-size: 13px; fill: #2a2018; font-weight: bold; }
      .sublabel { font-family: Georgia, serif; font-size: 10px; fill: #6b5a48; font-style: italic; }
      .title { font-family: Georgia, serif; font-size: 16px; fill: #2a2018; font-weight: bold; }
    </style>
  </defs>
  
  <rect class="bg" width="800" height="280"/>
  
  <!-- Title -->
  <text class="title" x="400" y="35" text-anchor="middle">The Pepper Secret: Piperine Blocks Curcumin Breakdown</text>
  
  <!-- WITHOUT pepper scenario -->
  <g transform="translate(50, 60)">
    <text class="label" x="150" y="0" text-anchor="middle">Without Black Pepper</text>
    
    <!-- Curcumin molecules entering liver -->
    <circle class="curcumin" cx="50" cy="50" r="8"/>
    <circle class="curcumin" cx="80" cy="50" r="8"/>
    <circle class="curcumin" cx="110" cy="50" r="8"/>
    <circle class="curcumin" cx="140" cy="50" r="8"/>
    <circle class="curcumin" cx="170" cy="50" r="8"/>
    
    <!-- Liver -->
    <rect class="liver-box" x="30" y="80" width="160" height="60" rx="8"/>
    <text class="label" x="110" y="105" text-anchor="middle">Liver Enzymes</text>
    <text class="sublabel" x="110" y="125" text-anchor="middle">Glucuronidation</text>
    
    <!-- Blocked/eliminated -->
    <rect class="blocked" x="200" y="30" width="80" height="80" rx="8"/>
    <text class="label" x="240" y="60" text-anchor="middle" fill="#c85a4a">Destroyed</text>
    <text class="sublabel" x="240" y="80" text-anchor="middle">90% lost</text>
    
    <!-- Arrow -->
    <path d="M190,110 L220,80" stroke="#c85a4a" stroke-width="2" fill="none"/>
    
    <!-- Result -->
    <text class="label" x="110" y="180" text-anchor="middle">Only 10% survives</text>
    <text class="sublabel" x="110" y="198" text-anchor="middle">to reach bloodstream</text>
  </g>
  
  <!-- WITH pepper scenario -->
  <g transform="translate(400, 60)">
    <text class="label" x="150" y="0" text-anchor="middle">With Black Pepper</text>
    
    <!-- Curcumin molecules -->
    <circle class="curcumin" cx="50" cy="50" r="8"/>
    <circle class="curcumin" cx="80" cy="50" r="8"/>
    <circle class="curcumin" cx="110" cy="50" r="8"/>
    <circle class="curcumin" cx="140" cy="50" r="8"/>
    <circle class="curcumin" cx="170" cy="50" r="8"/>
    
    <!-- Piperine blocking -->
    <rect class="piperine" x="30" y="80" width="160" height="60" rx="8"/>
    <text class="label" x="110" y="105" text-anchor="middle" fill="white">Piperine Blocks</text>
    <text class="sublabel" x="110" y="125" text-anchor="middle" fill="white">Enzyme activity</text>
    
    <!-- Protected -->
    <rect x="200" y="30" width="80" height="80" rx="8" fill="#7ab89a"/>
    <text class="label" x="240" y="60" text-anchor="middle" fill="white">Protected</text>
    <text class="sublabel" x="240" y="80" text-anchor="middle" fill="white">90% survives</text>
    
    <!-- Arrow -->
    <path d="M190,110 L220,80" stroke="#7ab89a" stroke-width="2" fill="none"/>
    
    <!-- Result -->
    <text class="label" x="110" y="180" text-anchor="middle">20x more reaches</text>
    <text class="sublabel" x="110" y="198" text-anchor="middle">your bloodstream</text>
  </g>
  
  <!-- Bottom note -->
  <text class="sublabel" x="400" y="260" text-anchor="middle">Source: Planta Medica (1998) — Shoba et al.</text>
</svg>'''
    
    with open(os.path.join(ASSETS, 'curcumin_absorption.svg'), 'w') as f:
        f.write(svg)
    print("Generated: curcumin_absorption.svg")

def generate_spice_route_map():
    """Generate map showing global spread of spices."""
    svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="auto">
  <defs>
    <style>
      .map-bg { fill: #faf6ee; }
      .ocean { fill: #d4e8f0; }
      .land { fill: #e8dfc8; stroke: #b8a88a; stroke-width: 1; }
      .origin { fill: #d4a853; stroke: #b88a3a; stroke-width: 2; }
      .spread { fill: #4a9fa8; }
      .route { stroke: #c85a4a; stroke-width: 2; fill: none; stroke-dasharray: 6,3; opacity: 0.7; }
      .label { font-family: Georgia, serif; font-size: 11px; fill: #2a2018; }
      .title { font-family: Georgia, serif; font-size: 16px; fill: #2a2018; font-weight: bold; }
      .legend-text { font-family: Georgia, serif; font-size: 10px; fill: #4a3828; }
    </style>
  </defs>
  
  <!-- Background -->
  <rect class="map-bg" width="800" height="500"/>
  <rect class="ocean" width="800" height="500"/>
  
  <!-- Simplified continents -->
  <path class="land" d="M80,150 Q200,100 350,140 L380,200 Q350,280 250,300 L150,280 Q80,220 80,150 Z"/>
  <path class="land" d="M380,120 Q500,100 600,150 L620,220 Q580,300 480,320 L400,280 Q380,200 380,120 Z"/>
  <path class="land" d="M600,180 Q720,150 780,220 L760,320 Q680,380 600,350 L580,280 Q580,220 600,180 Z"/>
  <path class="land" d="M280,350 Q380,330 450,380 L420,450 Q350,470 280,440 Z"/>
  
  <!-- Origin points -->
  <circle class="origin" cx="480" cy="200" r="10"/>
  <text class="label" x="500" y="195">INDIA</text>
  <text class="label" x="500" y="212" fill="#b88a3a">Turmeric, Black Pepper</text>
  
  <circle class="origin" cx="680" cy="220" r="10"/>
  <text class="label" x="700" y="215">CHINA</text>
  <text class="label" x="700" y="232" fill="#b88a3a">Ginger, Jujube</text>
  
  <circle class="origin" cx="420" cy="170" r="10"/>
  <text class="label" x="370" y="165">IRAN</text>
  <text class="label" x="355" y="182" fill="#b88a3a">Saffron</text>
  
  <!-- Spread to Middle East -->
  <circle class="spread" cx="350" cy="220" r="6"/>
  <text class="label" x="320" y="240">Middle East</text>
  
  <!-- Spread to Europe -->
  <circle class="spread" cx="200" cy="200" r="6"/>
  <text class="label" x="160" y="220">Europe</text>
  
  <!-- Spread to Americas -->
  <circle class="spread" cx="180" cy="280" r="6"/>
  <text class="label" x="140" y="300">Americas</text>
  
  <!-- Routes -->
  <path class="route" d="M480,200 Q420,220 350,220"/>
  <path class="route" d="M480,200 Q550,220 680,220"/>
  <path class="route" d="M350,220 Q280,210 200,200"/>
  <path class="route" d="M200,200 Q180,240 180,280"/>
  <path class="route" d="M420,170 Q380,200 350,220"/>
  <path class="route" d="M680,220 Q600,250 500,280"/>
  
  <!-- Title -->
  <text class="title" x="400" y="50" text-anchor="middle">The Global Journey of Healing Spices</text>
  <text class="legend-text" x="400" y="70" text-anchor="middle">How the ingredients in this book traveled the world</text>
  
  <!-- Legend -->
  <circle cx="100" cy="470" r="6" fill="#d4a853" stroke="#b88a3a" stroke-width="2"/>
  <text class="legend-text" x="115" y="475">Origin</text>
  <circle cx="180" cy="470" r="6" fill="#4a9fa8"/>
  <text class="legend-text" x="195" y="475">Adopted Region</text>
  <line x1="280" y1="470" x2="310" y2="470" stroke="#c85a4a" stroke-width="2" stroke-dasharray="6,3"/>
  <text class="legend-text" x="320" y="475">Trade Route</text>
</svg>'''
    
    with open(os.path.join(ASSETS, 'spice_route_map.svg'), 'w') as f:
        f.write(svg)
    print("Generated: spice_route_map.svg")

def generate_timeline():
    """Generate a historical timeline of key events."""
    svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 250" width="100%" height="auto">
  <defs>
    <style>
      .bg { fill: #faf6ee; }
      .timeline { stroke: #b8a88a; stroke-width: 3; }
      .event-dot { fill: #d4a853; stroke: #b88a3a; stroke-width: 2; }
      .islamic-dot { fill: #8a3a4a; }
      .label { font-family: Georgia, serif; font-size: 11px; fill: #2a2018; }
      .date { font-family: Georgia, serif; font-size: 12px; fill: #b88a3a; font-weight: bold; }
      .title { font-family: Georgia, serif; font-size: 14px; fill: #2a2018; font-weight: bold; }
    </style>
  </defs>
  
  <rect class="bg" width="800" height="250"/>
  
  <!-- Title -->
  <text class="title" x="400" y="35" text-anchor="middle">Timeline: 3,500 Years of Kitchen Medicine</text>
  
  <!-- Timeline line -->
  <line class="timeline" x1="50" y1="120" x2="750" y2="120"/>
  
  <!-- Events -->
  <!-- 1500 BCE -->
  <circle class="event-dot" cx="80" cy="120" r="8"/>
  <text class="date" x="80" y="90" text-anchor="middle">1500 BCE</text>
  <text class="label" x="80" y="150" text-anchor="middle">Ayurveda</text>
  <text class="label" x="80" y="165" text-anchor="middle">formalized</text>
  
  <!-- 200 BCE -->
  <circle class="event-dot" cx="180" cy="120" r="8"/>
  <text class="date" x="180" y="90" text-anchor="middle">200 BCE</text>
  <text class="label" x="180" y="150" text-anchor="middle">Charaka</text>
  <text class="label" x="180" y="165" text-anchor="middle">Samhita</text>
  
  <!-- 600 CE -->
  <circle class="islamic-dot event-dot" cx="300" cy="120" r="8"/>
  <text class="date" x="300" y="90" text-anchor="middle" fill="#8a3a4a">622 CE</text>
  <text class="label" x="300" y="150" text-anchor="middle">Prophetic</text>
  <text class="label" x="300" y="165" text-anchor="middle">Medicine</text>
  
  <!-- 1025 CE -->
  <circle class="islamic-dot event-dot" cx="420" cy="120" r="8"/>
  <text class="date" x="420" y="90" text-anchor="middle" fill="#8a3a4a">1025 CE</text>
  <text class="label" x="420" y="150" text-anchor="middle">Canon of</text>
  <text class="label" x="420" y="165" text-anchor="middle">Medicine</text>
  
  <!-- 1200 CE -->
  <circle class="event-dot" cx="540" cy="120" r="8"/>
  <text class="date" x="540" y="90" text-anchor="middle">1200 CE</text>
  <text class="label" x="540" y="150" text-anchor="middle">Silk Road</text>
  <text class="label" x="540" y="165" text-anchor="middle">peak</text>
  
  <!-- 1400 CE -->
  <circle class="event-dot" cx="650" cy="120" r="8"/>
  <text class="date" x="650" y="90" text-anchor="middle">1400 CE</text>
  <text class="label" x="650" y="150" text-anchor="middle">Ottoman</text>
  <text class="label" x="650" y="165" text-anchor="middle">sharbat</text>
  
  <!-- 1998 CE -->
  <circle class="event-dot" cx="730" cy="120" r="8"/>
  <text class="date" x="730" y="90" text-anchor="middle">1998 CE</text>
  <text class="label" x="730" y="150" text-anchor="middle">Piperine</text>
  <text class="label" x="730" y="165" text-anchor="middle">discovery</text>
  
  <!-- Legend -->
  <circle cx="250" cy="220" r="5" fill="#d4a853" stroke="#b88a3a" stroke-width="2"/>
  <text class="label" x="265" y="225">Historical Event</text>
  <circle cx="400" cy="220" r="5" fill="#8a3a4a"/>
  <text class="label" x="415" y="225">Islamic Golden Age</text>
</svg>'''
    
    with open(os.path.join(ASSETS, 'timeline.svg'), 'w') as f:
        f.write(svg)
    print("Generated: timeline.svg")

def generate_body_diagram():
    """Generate anatomical diagram showing where remedies work."""
    svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 500" width="100%" height="auto">
  <defs>
    <style>
      .bg { fill: #faf6ee; }
      .body { fill: none; stroke: #b8a88a; stroke-width: 2; }
      .organ { fill: #e8dfc8; stroke: #b8a88a; stroke-width: 1; }
      .target { fill: none; stroke: #c85a4a; stroke-width: 2; }
      .label { font-family: Georgia, serif; font-size: 10px; fill: #2a2018; }
      .title { font-family: Georgia, serif; font-size: 12px; fill: #2a2018; font-weight: bold; }
    </style>
  </defs>
  
  <rect class="bg" width="400" height="500"/>
  
  <!-- Title -->
  <text class="title" x="200" y="30" text-anchor="middle">How Golden Milk Works</text>
  
  <!-- Head outline -->
  <ellipse class="body" cx="200" cy="80" rx="30" ry="35"/>
  
  <!-- Brain target -->
  <circle class="target" cx="200" cy="75" r="12" stroke-dasharray="4,2"/>
  <text class="label" x="200" y="78" text-anchor="middle" font-size="8">Brain</text>
  
  <!-- Throat -->
  <rect class="body" x="190" y="115" width="20" height="20" rx="3"/>
  
  <!-- Torso -->
  <path class="body" d="M170,135 Q150,200 160,300 L240,300 Q250,200 230,135 Z"/>
  
  <!-- Stomach -->
  <ellipse class="organ" cx="200" cy="200" rx="25" ry="20"/>
  <circle class="target" cx="200" cy="200" r="15" stroke-dasharray="4,2"/>
  <text class="label" x="200" y="203" text-anchor="middle" font-size="8">Stomach</text>
  
  <!-- Liver -->
  <ellipse class="organ" cx="230" cy="180" rx="20" ry="15"/>
  <circle class="target" cx="235" cy="180" r="12" stroke-dasharray="4,2"/>
  <text class="label" x="255" y="183" font-size="8">Liver</text>
  
  <!-- Intestines -->
  <path class="organ" d="M180,240 Q160,260 180,280 Q200,300 220,280 Q240,260 220,240" fill="#e8dfc8" stroke="#b8a88a"/>
  <circle class="target" cx="200" cy="260" r="12" stroke-dasharray="4,2"/>
  <text class="label" x="200" y="263" text-anchor="middle" font-size="7">Gut</text>
  
  <!-- Arms -->
  <path class="body" d="M170,150 L140,200 L135,250"/>
  <path class="body" d="M230,150 L260,200 L265,250"/>
  
  <!-- Legs -->
  <path class="body" d="M180,300 L170,400 L165,470"/>
  <path class="body" d="M220,300 L230,400 L235,470"/>
  
  <!-- Labels explaining effects -->
  <g transform="translate(280, 100)">
    <rect x="0" y="0" width="110" height="140" fill="#faf6ee" stroke="#e8dfc8" rx="5"/>
    <text class="label" x="55" y="20" text-anchor="middle" font-weight="bold">Curcumin:</text>
    <text class="label" x="10" y="40">• Reduces brain</text>
    <text class="label" x="10" y="55">  inflammation</text>
    <text class="label" x="10" y="75">• Supports liver</text>
    <text class="label" x="10" y="90">  detoxification</text>
    <text class="label" x="10" y="110">• Soothes joint</text>
    <text class="label" x="10" y="125">  discomfort</text>
  </g>
  
  <!-- Key -->
  <g transform="translate(280, 260)">
    <circle cx="10" cy="10" r="6" fill="none" stroke="#c85a4a" stroke-width="2" stroke-dasharray="4,2"/>
    <text class="label" x="25" y="15">Target organs</text>
    <ellipse cx="10" cy="35" rx="10" ry="8" fill="#e8dfc8" stroke="#b8a88a"/>
    <text class="label" x="25" y="38">Active organs</text>
  </g>
</svg>'''
    
    with open(os.path.join(ASSETS, 'body_diagram.svg'), 'w') as f:
        f.write(svg)
    print("Generated: body_diagram.svg")

if __name__ == '__main__':
    generate_silk_road_map()
    generate_nitric_oxide_pathway()
    generate_curcumin_absorption()
    generate_spice_route_map()
    generate_timeline()
    generate_body_diagram()
    print("\nAll SVG visuals generated successfully.")
