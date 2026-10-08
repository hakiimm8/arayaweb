"""Build the three static preview routes using a shared site shell."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
BASE = "https://hakiimm8.github.io/arayaweb/"
ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15M13 5l7 7-7 7"/></svg>'


def shell(title, description, content, route=""):
    prefix = "../" if route else "./"
    home = prefix + "index.html"
    def nav(label, target):
        return f'<a href="{home}{target}">{label}</a>'
    schema = {
        "@context": "https://schema.org", "@type": "Organization",
        "name": "PT Araya Internusa", "url": "https://arayainternusa.co.id/araya/",
        "logo": BASE + "assets/images/araya-logo.png",
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
  <link rel="stylesheet" href="{prefix}assets/site.css">
  <script src="{prefix}assets/site.js" defer></script>
  <script type="application/ld+json">{json.dumps(schema)}</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="utility"><div class="container utility-inner"><span>Gateway Citra Harmoni · Sidoarjo, Indonesia</span><a href="mailto:cs@arayainternusa.com">cs@arayainternusa.com</a><a href="tel:+62317877990">+62 (031) 7877990</a></div></div>
  <div class="container navigation">
    <a class="brand" href="{home}" aria-label="PT Araya Internusa home"><img src="{prefix}assets/images/araya-logo.png" alt="PT Araya Internusa" width="238" height="52"></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="main-navigation"><span>Menu</span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
    <nav class="main-nav" id="main-navigation" aria-label="Main navigation">
      {nav('Home', '')}{nav('About Us', '#about')}{nav('Our Services', '#services')}{nav('Noris & ComAp', '#brands')}{nav('Our Projects', '#projects')}
      <a class="nav-contact" href="{home}#contact">Contact Us {ARROW}</a>
    </nav>
  </div>
</header>
<main id="main">{content}</main>
<section class="contact" id="contact" aria-labelledby="contact-heading">
  <div class="container contact-intro"><div><p class="eyebrow">GET IN TOUCH</p><h2 id="contact-heading">Let’s find the right solution.</h2><p>Tell us about your equipment, application, and project location.</p></div><a class="button" href="mailto:cs@arayainternusa.com">Discuss your project {ARROW}</a></div>
  <div class="container footer-grid">
    <div class="footer-company"><img src="{prefix}assets/images/araya-logo.png" alt="PT Araya Internusa" width="238" height="52" loading="lazy"><p>Total solutions for engineering and automation.</p><a class="text-link light" href="https://arayainternusa.co.id/araya/">Visit our current website {ARROW}</a></div>
    <div><h3>Explore Araya</h3><a href="{home}#about">About Us</a><a href="{home}#services">Our Services</a><a href="{prefix}noris/">Noris Automation</a><a href="{prefix}comap/">ComAp Control</a></div>
    <div><h3>Office Address</h3><p>Gateway Citra Harmoni RKG 32–33<br>Taman, Sidoarjo<br>Jawa Timur 61257, Indonesia</p></div>
    <div><h3>Contact Us</h3><a href="mailto:cs@arayainternusa.com">cs@arayainternusa.com</a><a href="tel:+62317877990">+62 (031) 7877990</a><a href="https://wa.me/6281326396262">WhatsApp: +62 813 2639 6262</a><p class="contact-note">Share your system details with our team.</p></div>
  </div>
</section>
<footer class="copyright"><div class="container"><span>© 2026 PT Araya Internusa.</span><span>Design preview · Current website remains live</span></div></footer>
</body></html>'''


HOME = f'''
<section class="hero" aria-labelledby="hero-heading">
  <img class="hero-photo" src="./assets/images/ship.webp" alt="Passenger vessel alongside a quay, from Araya’s marine project photographs" width="1400" height="840" fetchpriority="high">
  <div class="hero-shade"></div>
  <div class="container hero-content"><p class="eyebrow">PT ARAYA INTERNUSA</p><h1 id="hero-heading">Engineering &amp;<br>automation solutions<br><span>in Indonesia.</span></h1><p class="hero-description">Marine. Industrial. Automation.<br>Noris and ComAp solutions, with a local team to discuss your requirements.</p><div class="hero-actions"><a class="button" href="#brands">Explore Noris &amp; ComAp {ARROW}</a><a class="button button-outline" href="#contact">Contact our team {ARROW}</a></div></div>
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
    <a class="service-card" href="https://arayainternusa.co.id/araya/services/marine/"><img src="./assets/images/marine.webp" alt="Technical inspection of marine engine equipment" width="600" height="690" loading="lazy"><div class="service-body"><span class="service-number">01</span><h3>Marine</h3><p>Vessel systems, engineering, monitoring, and control.</p><span class="card-link">Explore marine services {ARROW}</span></div></a>
    <a class="service-card" href="https://arayainternusa.co.id/araya/services/industrial/"><img src="./assets/images/industrial.webp" alt="Industrial electrical installation, from Araya’s existing service imagery" width="600" height="500" loading="lazy"><div class="service-body"><span class="service-number">02</span><h3>Industrial</h3><p>Electrical equipment and engineering for industrial applications.</p><span class="card-link">Explore industrial services {ARROW}</span></div></a>
    <a class="service-card" href="https://arayainternusa.co.id/araya/services/automation/"><img src="./assets/images/control-room.webp" alt="Marine control console with a Noris monitoring display" width="1400" height="840" loading="lazy"><div class="service-body"><span class="service-number">03</span><h3>Automation</h3><p>Control systems, instrumentation, and system integration.</p><span class="card-link">Explore automation services {ARROW}</span></div></a>
  </div>
</div></section>
<section class="section" id="brands"><div class="container">
  <div class="section-heading"><div><p class="eyebrow">NORIS &amp; COMAP IN INDONESIA</p><h2>Specialist solutions.<br>A local point of contact.</h2></div><p>PT Araya Internusa distributes Noris and ComAp solutions in Indonesia. Talk to us about your equipment and application.</p></div>
  <div class="brand-grid">
    <article class="brand-panel"><div class="brand-name">NORIS<span>01 / MARINE AUTOMATION</span></div><h3>Monitoring. Control. Clarity.</h3><p>Explore marine alarm, monitoring, and control applications, and discuss your Noris requirements with Araya.</p><a class="text-link" href="./noris/">Explore Noris in Indonesia {ARROW}</a></article>
    <article class="brand-panel"><div class="brand-name">ComAp<span>02 / GENERATOR CONTROL</span></div><h3>Control at the heart of power.</h3><p>Explore generator and power-control applications, and discuss the needs of your ComAp installation with Araya.</p><a class="text-link" href="./comap/">Explore ComAp in Indonesia {ARROW}</a></article>
  </div>
</div></section>
<section class="section projects" id="projects"><div class="container">
  <div class="section-heading"><div><p class="eyebrow">OUR PROJECTS</p><h2>Closer to the work.<br>Closer to the solution.</h2></div><p>A look inside the marine environments and systems featured in Araya’s project photography.</p></div>
  <div class="project-grid"><figure><img src="./assets/images/control-room.webp" alt="Noris monitoring equipment installed in a marine control console" width="1400" height="840" loading="lazy"><figcaption><span>Marine automation</span><h3>Inside the control room</h3></figcaption></figure><figure><img src="./assets/images/team.webp" alt="Araya’s technical team working around marine engine equipment" width="600" height="600" loading="lazy"><figcaption><span>Technical services</span><h3>Alongside your equipment</h3></figcaption></figure></div>
</div></section>'''

BRANDS = {
  "noris": {
    "title": "Noris Automation Distributor Indonesia | PT Araya Internusa",
    "description": "Discuss Noris marine automation, alarm, monitoring and control requirements in Indonesia with PT Araya Internusa in Sidoarjo.",
    "label": "NORIS AUTOMATION IN INDONESIA", "heading": "Noris automation.<br>For your marine systems.",
    "intro": "A local conversation about marine monitoring and control.",
    "body": "PT Araya Internusa distributes Noris solutions in Indonesia. Tell us about your vessel, existing installation, and project requirements so we can discuss the appropriate next steps.",
    "image": "control-room.webp", "alt": "Noris monitoring display in a vessel’s control room, from Araya’s project photographs",
    "summary": "Noris develops automation and sensor solutions for shipbuilding. Its marine portfolio covers alarm, monitoring, and control, as well as propulsion control and power management.",
    "applications": [("Alarm & monitoring", "Discuss the signals, alarms, and operating information your vessel needs to monitor."), ("Marine control", "Discuss the existing control architecture and the interfaces involved in your project."), ("System requirements", "Share your equipment details and documentation to help scope the conversation.")],
    "source": "https://www.noris-group.com/industries/shipbuilding", "source_name": "Explore the Noris marine portfolio",
    "other": "comap", "other_label": "Explore ComAp generator control",
  },
  "comap": {
    "title": "ComAp Distributor Indonesia | PT Araya Internusa",
    "description": "Discuss ComAp generator controllers, power control and marine applications in Indonesia with PT Araya Internusa. Share your installation requirements.",
    "label": "COMAP CONTROL IN INDONESIA", "heading": "ComAp control.<br>For your power systems.",
    "intro": "Understand your installation. Discuss the right control approach.",
    "body": "PT Araya Internusa distributes ComAp solutions in Indonesia. Tell us about your generator or power installation, operating needs, and existing controller so we can discuss your requirements.",
    "image": "team.webp", "alt": "Araya technicians working around marine machinery; illustrative engineering photograph, not a ComAp product image",
    "summary": "ComAp offers controllers for single and paralleling generator sets, engines, marine applications, and energy installations. Controller selection depends on the application and system requirements.",
    "applications": [("Generator control", "Discuss standby or continuous-power requirements and the controller used in your installation."), ("Paralleling & power", "Discuss how generators and other power sources operate together in your system."), ("Marine applications", "Discuss engine or generator-control requirements for your vessel.")],
    "source": "https://www.comap-control.com/products/controllers/", "source_name": "Explore ComAp controllers",
    "other": "noris", "other_label": "Explore Noris marine automation",
  },
}


def brand_content(key, data):
    rows = ''.join(f'<div class="application-row"><span>0{i}</span><h3>{escape(title)}</h3><p>{escape(body)}</p></div>' for i, (title, body) in enumerate(data['applications'], 1))
    return f'''<section class="brand-hero"><div class="container"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="../index.html">Home</a><span aria-hidden="true">/</span><span>{'Noris' if key == 'noris' else 'ComAp'}</span></nav><p class="eyebrow">{data['label']}</p><h1>{data['heading']}</h1><p>{data['intro']}</p><a class="button" href="#contact">Discuss your requirements {ARROW}</a></div></section>
<section class="section"><div class="container brand-overview"><div><p class="eyebrow">YOUR LOCAL POINT OF CONTACT</p><h2>{'Noris' if key == 'noris' else 'ComAp'} solutions<br>in Indonesia.</h2><p class="lead">{data['body']}</p><p>{data['summary']}</p><a class="text-link" href="{data['source']}">{data['source_name']} {ARROW}</a><p class="manufacturer-note">Manufacturer information. Contact Araya to confirm the products and services available for your project.</p></div><figure><img src="../assets/images/{data['image']}" alt="{data['alt']}" width="700" height="600" loading="lazy"><figcaption>From Araya’s marine engineering photography.</figcaption></figure></div></section>
<section class="section section-muted"><div class="container"><p class="eyebrow">START WITH YOUR APPLICATION</p><h2>What does your system need?</h2><div class="application-list">{rows}</div><div class="equipment-note"><h3>Help us understand your installation.</h3><p>Include the equipment or controller model, system description, project location, and any available drawings in your enquiry.</p></div></div></section>
<section class="related container"><a class="text-link" href="../{data['other']}/">{data['other_label']} {ARROW}</a><a href="../index.html#brands">Back to our solutions</a></section>'''


def main():
    PUBLIC.mkdir(parents=True, exist_ok=True)
    (PUBLIC / "index.html").write_text(shell("Marine & Industrial Automation Indonesia | PT Araya Internusa", "Engineering and automation solutions in Indonesia. Explore Noris and ComAp distribution, marine engineering, and industrial applications with PT Araya Internusa.", HOME), encoding="utf-8")
    for key, data in BRANDS.items():
        folder = PUBLIC / key
        folder.mkdir(exist_ok=True)
        (folder / "index.html").write_text(shell(data['title'], data['description'], brand_content(key, data), key + '/'), encoding="utf-8")
    print("Built homepage, Noris page, and ComAp page.")


if __name__ == "__main__":
    main()
