"""Build the homepage, brand pages and service pages using a shared shell."""
from pathlib import Path
from html import escape
import json
import hashlib
from brand_profiles import BRANDS
from brand_pages import brand_content

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
BASE = "https://hakiimm8.github.io/arayaweb/"
ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15M13 5l7 7-7 7"/></svg>'
CSS_VERSION = hashlib.sha256((PUBLIC / 'assets/site.css').read_bytes()).hexdigest()[:10]


def shell(title, description, content, route=""):
    prefix = "../" if route else "./"
    home = prefix + "index.html"
    def nav(label, target):
        return f'<a href="{home}{target}">{label}</a>'
    schema = {
        "@context": "https://schema.org", "@type": "Organization",
        "name": "PT Araya Internusa", "url": "https://arayainternusa.co.id/araya/",
        "logo": BASE + "assets/images/araya-logo-original.png",
        "email": "cs@arayainternusa.com", "telephone": "+62-31-7877990",
    }
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description, quote=True)}">
  <meta name="robots" content="noindex, nofollow">
  <meta name="theme-color" content="#1e2023">
  <link rel="canonical" href="{BASE}{route}">
  <meta property="og:title" content="{escape(title, quote=True)}">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <meta property="og:type" content="website"><meta property="og:url" content="{BASE}{route}">
  <meta property="og:image" content="{BASE}assets/images/ship.webp">
  <link rel="icon" href="{prefix}assets/images/favicon.png">
  <link rel="preload" href="{prefix}assets/fonts/space-grotesk.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{prefix}assets/site.css?v={CSS_VERSION}">
  <script src="{prefix}assets/site.js" defer></script>
  <script type="application/ld+json">{json.dumps(schema)}</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="utility"><div class="container utility-inner"><span>Gateway Citra Harmoni · Sidoarjo, Indonesia</span><a href="mailto:cs@arayainternusa.com">cs@arayainternusa.com</a><a href="tel:+62317877990">+62 (031) 7877990</a></div></div>
  <div class="container navigation">
    <a class="brand" href="{home}" aria-label="PT Araya Internusa home"><img src="{prefix}assets/images/araya-logo-original.png" alt="PT Araya Internusa" width="291" height="52"></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="main-navigation"><span>Menu</span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
    <nav class="main-nav" id="main-navigation" aria-label="Main navigation">
      {nav('Home', '')}{nav('About Us', '#about')}{nav('Our Services', '#services')}<a href="{prefix}noris/">Noris</a><a href="{prefix}comap/">ComAp</a>{nav('Our Projects', '#projects')}
      <a class="nav-contact" href="{home}#contact">Contact Us {ARROW}</a>
    </nav>
  </div>
</header>
<main id="main">{content}</main>
<section class="contact" id="contact" aria-labelledby="contact-heading">
  <div class="container contact-intro"><div><p class="eyebrow">GET IN TOUCH</p><h2 id="contact-heading">Let’s find the right solution.</h2><p>Tell us about your equipment, application, and project location.</p></div><a class="button" href="mailto:cs@arayainternusa.com">Discuss your project {ARROW}</a></div>
  <div class="container footer-grid">
    <div class="footer-company"><img src="{prefix}assets/images/araya-logo-original.png" alt="PT Araya Internusa" width="291" height="52" loading="lazy"><p>Total solutions for engineering and automation.</p><a class="text-link light" href="https://arayainternusa.co.id/araya/">Visit our current website {ARROW}</a></div>
    <div><h3>Explore Araya</h3><a href="{home}#about">About Us</a><a href="{prefix}marine/">Marine projects</a><a href="{prefix}industrial/">Industrial projects</a><a href="{prefix}noris/">Noris Group GmbH</a><a href="{prefix}comap/">ComAp Control</a></div>
    <div><h3>Office Address</h3><p>Gateway Citra Harmoni RKG 32–33<br>Taman, Sidoarjo<br>Jawa Timur 61257, Indonesia</p></div>
    <div><h3>Contact Us</h3><a href="mailto:cs@arayainternusa.com">cs@arayainternusa.com</a><a href="tel:+62317877990">+62 (031) 7877990</a><a href="https://wa.me/6281326396262">WhatsApp: +62 813 2639 6262</a><p class="contact-note">Share your system details with our team.</p></div>
  </div>
</section>
<footer class="copyright"><div class="container"><span>© 2026 PT Araya Internusa.</span><span>Design preview · Current website remains live</span></div></footer>
</body></html>'''


SECTORS = {
    'marine': {
        'name': 'Marine', 'title': 'Marine Electrical & Mechanical Services Indonesia | Araya Internusa',
        'description': 'Marine fire alarms, AMS, engine overhaul and control, generator synchronisation, tank monitoring, navigation, steering and system retrofits with Araya Internusa.',
        'heading': 'Marine engineering.<br>From machinery to control.',
        'intro': 'Electrical, mechanical, and automation projects for onboard systems.',
        'image': 'team.webp', 'alt': 'Araya technicians working around machinery in a vessel engine room',
        'overview': 'A vessel project can involve machinery, electrical equipment, instruments, and the controls that connect them. Araya brings these requirements into one project conversation—from a faulty sensor to an engine overhaul or system retrofit.',
        'groups': [
            ('alarms', 'Fire alarms & AMS', 'Fire alarm systems, general alarms, and alarm monitoring systems (AMS). Discuss fault finding, signal monitoring, alarm displays, and replacement or retrofit requirements.'),
            ('engines', 'Engine overhaul & control', 'Mechanical overhaul requirements alongside engine monitoring, protection, and control. Share the engine model, condition, symptoms, and existing control arrangement.'),
            ('generators', 'Generator synchronisation & auto start/stop', 'Synchronising generators, automatic start/stop, load sharing, and power management. Define the generator ratings, operating sequence, and switchboard interfaces.'),
            ('automation', 'Electrical panels, PLC & SCADA', 'Control and electrical panels, PLC logic, HMI operator interfaces, and SCADA monitoring. Bring together equipment status, alarms, and operating commands.'),
            ('monitoring', 'Water level & cargo monitoring', 'Water level sensors, tank-level monitoring, and cargo monitoring systems. Discuss measuring points, sensor signals, alarm thresholds, and display requirements.'),
            ('navigation', 'Navigation, steering & manoeuvring', 'Navigation equipment and steering or manoeuvring controls, including controllable-pitch propeller and bow-thruster systems where applicable to the vessel.'),
            ('cranes', 'Cranes & deck equipment', 'Deck-crane mechanical and electrical requirements, including control panels, operating interfaces, and fault investigation. Start with the crane model and the work required.'),
            ('retrofit', 'System retrofit & integration', 'Updating ageing systems, replacing obsolete control equipment, and integrating new instruments or interfaces with retained machinery. Discuss the existing drawings and shutdown window.'),
        ],
        'enquiry': 'Vessel name/type, location, engine or equipment models, fault symptoms, photographs, wiring drawings, and the intended maintenance or retrofit window.',
    },
    'industrial': {
        'name': 'Industrial', 'title': 'Industrial Machinery & Automation Services Indonesia | Araya Internusa',
        'description': 'Industrial machinery and crane supply and repair, electrical panels, motor controls, PLC/SCADA, instrumentation and generator control projects with Araya Internusa.',
        'heading': 'Industrial equipment.<br>Connected by engineering.',
        'intro': 'Machinery, electrical systems, and automation for industrial operations.',
        'image': 'industrial.webp', 'alt': 'Industrial electrical equipment from Araya’s original service photography',
        'overview': 'Industrial work starts with the machine and the process it serves. Araya’s project scopes bring together machinery supply and repair, cranes, electrical equipment, and the automation used to operate and monitor them.',
        'groups': [
            ('machinery', 'Industrial machinery supply & repair', 'CNC lathes and milling machines, wire-cut and EDM machines, cutting equipment, and other industrial machinery. Discuss the machine condition and repair or replacement scope.'),
            ('cranes', 'Crane supply & repair', 'Overhead, portal, slewing, and luffing cranes. Discuss the mechanical condition, electrical equipment, control system, and operating requirements of the installation.'),
            ('electrical', 'Electrical panels & motor controls', 'Electrical panels, MV/LV switchboards, motor-control centres, soft starters, and variable-frequency drives. Define the loads, motor ratings, and operating sequence.'),
            ('automation', 'PLC, HMI, SCADA & instrumentation', 'Machine and process control, operator interfaces, supervisory monitoring, and instrument signals. Discuss the PLC platform, I/O list, process requirements, and existing software.'),
            ('power', 'Generator control & system retrofit', 'Generator control, automatic start/stop, synchronisation, and load-sharing requirements, alongside upgrades to existing electrical and automation systems.'),
        ],
        'enquiry': 'Site location, machine or generator model, equipment ratings, process description, fault symptoms, electrical drawings, and available PLC/HMI project files.',
    },
}


HOME = f'''
<section class="hero" aria-labelledby="hero-heading">
  <img class="hero-photo" src="./assets/images/ship.webp" alt="Passenger vessel alongside a quay, from Araya’s marine project photographs" width="1400" height="840" fetchpriority="high">
  <div class="hero-shade"></div>
  <div class="container hero-content"><p class="eyebrow">PT ARAYA INTERNUSA</p><h1 id="hero-heading">Engineering &amp;<br>automation solutions<br><span>in Indonesia.</span></h1><p class="hero-description">Marine. Industrial. Automation.<br>Noris and ComAp solutions, with a local team to discuss your requirements.</p><div class="hero-actions"><a class="button" href="./noris/">Explore Noris {ARROW}</a><a class="button button-outline" href="./comap/">Explore ComAp {ARROW}</a><a class="button button-outline" href="#contact">Contact our team {ARROW}</a></div></div>
  <div class="hero-index" aria-hidden="true"><span>01</span> / MARINE &amp; AUTOMATION</div>
</section>
<section class="feature-strip" aria-label="Our approach"><div class="container feature-grid">
  <div><span class="feature-number">01</span><div><h2>Engineering solutions</h2><p>Start with your system and application requirements.</p></div></div>
  <div><span class="feature-number">02</span><div><h2>Specialist brands</h2><p>Explore Noris automation and ComAp control solutions.</p></div></div>
  <div><span class="feature-number">03</span><div><h2>Local conversation</h2><p>Connect with our team in Sidoarjo, Indonesia.</p></div></div>
</div></section>
<section class="section about" id="about"><div class="container about-grid">
  <div class="about-media"><img src="./assets/images/team.webp" alt="Araya technicians working together in a vessel’s engine room" width="600" height="600" loading="lazy"><div class="since"><strong>2009</strong><span>Where our story began</span></div></div>
  <div><p class="eyebrow">WELCOME TO PT ARAYA INTERNUSA</p><h2>Total solutions for<br>engineering &amp; automation.</h2><p class="lead">Built on a passion for automation. Focused on the needs of your operation.</p><p>Araya began in 2009 as CV Araya Internusa, founded by Arif Fatkur Rohman. Our work brings together marine, industrial, and automation engineering.</p><p>From understanding an existing system to discussing a new installation, the conversation starts with the problem you need to solve.</p><div class="scope-list"><span>Marine</span><span>Industrial</span><span>Automation</span></div><a class="text-link" href="#contact">Get in touch {ARROW}</a></div>
</div></section>
<section class="section section-muted" id="services"><div class="container">
  <div class="section-heading"><div><p class="eyebrow">OUR SERVICES</p><h2>Engineering for<br>the systems you rely on.</h2></div><p>Discuss your requirements across marine systems, industrial equipment, and automation.</p></div>
  <div class="service-grid">
    <a class="service-card" href="./marine/"><img src="./assets/images/marine.webp" alt="Technical inspection of marine engine equipment" width="600" height="690" loading="lazy"><div class="service-body"><span class="service-number">01</span><h3>Marine</h3><p>Electrical, mechanical, and automation work for vessel systems.</p><span class="card-link">Explore marine services {ARROW}</span></div></a>
    <a class="service-card" href="./industrial/"><img src="./assets/images/industrial.webp" alt="Industrial electrical installation, from Araya’s existing service imagery" width="600" height="500" loading="lazy"><div class="service-body"><span class="service-number">02</span><h3>Industrial</h3><p>Machinery, cranes, electrical panels, and motor controls.</p><span class="card-link">Explore industrial services {ARROW}</span></div></a>
    <a class="service-card" href="./industrial/#automation"><img src="./assets/images/control-room.webp" alt="Marine control console with a Noris monitoring display" width="1400" height="840" loading="lazy"><div class="service-body"><span class="service-number">03</span><h3>Automation</h3><p>PLC, HMI, SCADA, instrumentation, and system retrofit.</p><span class="card-link">Explore automation services {ARROW}</span></div></a>
  </div>
</div></section>
<section class="section" id="brands"><div class="container">
  <div class="section-heading"><div><p class="eyebrow">OUR BRAND PORTFOLIOS</p><h2>Specialist solutions.<br>A local point of contact.</h2></div><p>PT Araya Internusa distributes Noris and ComAp solutions in Indonesia. Talk to us about your equipment and application.</p></div>
  <div class="brand-grid">
    <article class="brand-panel"><div class="brand-name">NORIS<span>NORIS GROUP GmbH</span></div><h3>Instruments &amp; sensors.<br>Marine automation.</h3><p>Speed, temperature, and pressure measurement. Indicators and signal processing. Explore Noris instrumentation, sensors, and marine monitoring solutions with Araya.</p><a class="text-link" href="./noris/">Explore Noris in Indonesia {ARROW}</a></article>
    <article class="brand-panel"><div class="brand-name">ComAp<span>ENGINE &amp; POWER CONTROL</span></div><h3>Engine control.<br>Power management.<br>Load sharing.</h3><p>Engine monitoring and protection, coordination of generating sources, and load sharing between parallel generators. Discuss your ComAp application with Araya.</p><a class="text-link" href="./comap/">Explore ComAp in Indonesia {ARROW}</a></article>
  </div>
</div></section>
<section class="section projects" id="projects"><div class="container">
  <div class="section-heading"><div><p class="eyebrow">OUR PROJECTS</p><h2>Project experience<br>across Indonesia.</h2></div><p>From marine environments to industrial systems, our work reaches Sumatra, Jawa, Kalimantan, Sulawesi, and Papua.</p></div>
  <div class="project-reach"><div class="project-total"><strong>1,500+</strong><span>projects across Indonesia</span></div><div class="project-coverage"><h3>Across the archipelago</h3><ul><li>Sumatra</li><li>Jawa</li><li>Kalimantan</li><li>Sulawesi</li><li>Papua</li></ul></div></div>
  <div class="project-grid project-scopes">
    <figure><img src="./assets/images/control-room.webp" alt="Noris monitoring equipment installed in a marine control console" width="1400" height="840" loading="lazy"><figcaption><span>MARINE PROJECTS</span><h3>From engine room to bridge.</h3><p>Electrical, mechanical, and automation scopes for vessel operation.</p><ul><li>Fire alarms, AMS, and water-level or cargo monitoring</li><li>Engine overhaul, engine control, and generator synchronisation</li><li>Auto start/stop, electrical panels, and PLC/SCADA</li><li>Navigation, steering, manoeuvring, cranes, and system retrofit</li></ul><a class="text-link light" href="./marine/">Explore marine project scopes {ARROW}</a></figcaption></figure>
    <figure><img src="./assets/images/industrial.webp" alt="Industrial electrical installation from Araya’s existing service photography" width="600" height="500" loading="lazy"><figcaption><span>INDUSTRIAL PROJECTS</span><h3>Machinery, power &amp; control.</h3><p>Equipment supply and repair, with electrical and automation systems.</p><ul><li>Industrial machinery, CNC, wire-cut, and EDM equipment</li><li>Crane supply and repair</li><li>Electrical panels, switchboards, motor controls, and drives</li><li>PLC/HMI/SCADA, instrumentation, and generator control</li></ul><a class="text-link light" href="./industrial/">Explore industrial project scopes {ARROW}</a></figcaption></figure>
  </div>
</div></section>'''

def sector_content(key, data):
    rows = ''.join(f'<article class="scope-detail" id="{anchor}"><span class="portfolio-number">0{i}</span><h3>{escape(title)}</h3><p>{escape(body)}</p></article>' for i, (anchor, title, body) in enumerate(data['groups'], 1))
    other = 'industrial' if key == 'marine' else 'marine'
    return f'''<section class="brand-hero"><div class="container"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="../index.html">Home</a><span aria-hidden="true">/</span><span>{data['name']}</span></nav><p class="eyebrow">{data['name'].upper()} PROJECT SCOPES</p><h1>{data['heading']}</h1><p>{data['intro']}</p><a class="button" href="#project-scopes">Explore our work {ARROW}</a></div></section>
<section class="section"><div class="container brand-overview"><div><p class="eyebrow">PT ARAYA INTERNUSA</p><h2>Engineering around<br>your equipment.</h2><p class="lead">{data['overview']}</p><p>Tell us what needs to be repaired, replaced, controlled, or monitored. We can discuss the equipment, interfaces, and work required for your installation.</p></div><figure><img src="../assets/images/{data['image']}" alt="{data['alt']}" width="600" height="600" loading="lazy"><figcaption>From Araya’s original engineering and service photography.</figcaption></figure></div></section>
<section class="section section-muted" id="project-scopes"><div class="container"><p class="eyebrow">THE WORK WE HANDLE</p><h2>Typical {data['name'].lower()} project scopes.</h2><p class="portfolio-intro">A starting point for your enquiry. The scope of work is agreed around your equipment, operating requirements, and site or vessel conditions.</p><div class="scope-details">{rows}</div></div></section>
<section class="section"><div class="container"><p class="eyebrow">RELEVANT BRAND PORTFOLIOS</p><h2>Connect the project<br>to the right technology.</h2><div class="connection-grid"><a href="../noris/#portfolio"><h3>Noris Group GmbH</h3><p>Instruments, sensors, signal processing, and marine alarm/monitoring systems.</p><span class="text-link">Explore Noris details {ARROW}</span></a><a href="../comap/#portfolio"><h3>ComAp Control</h3><p>Engine control, generator synchronisation, power management, and load sharing.</p><span class="text-link">Explore ComAp details {ARROW}</span></a></div><div class="equipment-note"><h3>Help us understand your project.</h3><p>{data['enquiry']}</p><a class="text-link" href="https://wa.me/6281326396262">Discuss your project on WhatsApp {ARROW}</a></div></div></section>
<section class="related container"><a class="text-link" href="../{other}/">Explore {other} projects {ARROW}</a><a href="../index.html#projects">Back to our projects</a></section>'''


def main():
    PUBLIC.mkdir(parents=True, exist_ok=True)
    (PUBLIC / "index.html").write_text(shell("Marine & Industrial Automation Indonesia | PT Araya Internusa", "Engineering and automation solutions in Indonesia. Explore Noris and ComAp distribution, marine engineering, and industrial applications with PT Araya Internusa.", HOME), encoding="utf-8")
    for key, data in BRANDS.items():
        folder = PUBLIC / key
        folder.mkdir(exist_ok=True)
        (folder / "index.html").write_text(shell(data['title'], data['description'], brand_content(key, data, ARROW), key + '/'), encoding="utf-8")
    for key, data in SECTORS.items():
        folder = PUBLIC / key
        folder.mkdir(exist_ok=True)
        (folder / 'index.html').write_text(shell(data['title'], data['description'], sector_content(key, data), key + '/'), encoding='utf-8')
    print("Built homepage, Noris, ComAp, marine and industrial pages.")


if __name__ == "__main__":
    main()
