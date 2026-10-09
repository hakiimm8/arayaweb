"""Shared layout for Araya's dedicated manufacturer guides."""
from html import escape


def portfolio_image(product, brand):
    """Optional local manufacturer image; never imply an Araya installation."""
    if 'image' not in product:
        return ''
    picture = product['image']
    return f'''<figure class="portfolio-picture"><img src="../assets/images/{escape(picture['file'], quote=True)}" alt="{escape(picture['alt'], quote=True)}" width="{picture['width']}" height="{picture['height']}" loading="lazy" decoding="async"><figcaption><a href="{escape(product['source'], quote=True)}">{escape(picture['caption'])} · Image: {escape(brand)}</a></figcaption></figure>'''


def brand_content(key, data, arrow):
    name = escape(data['name'])
    sections = [('about-brand', 'About the brand'), ('portfolio', 'Products & systems'),
                ('applications', 'Applications'), ('araya-support', 'Enquire with Araya'), ('brand-faq', 'FAQs')]
    contents = ''.join(f'<a href="#{anchor}">{label}</a>' for anchor, label in sections)
    facts = ''.join(f'<div><dt>{escape(label)}</dt><dd>{escape(value)}</dd></div>' for label, value in data['facts'])
    finder = ''.join(f'<a href="#{product["id"]}"><span>{i:02}</span>{escape(product["short"])}{arrow}</a>' for i, product in enumerate(data['products'], 1))
    portfolio = ''.join(f'''<article class="portfolio-row" id="{product['id']}">
      <div><span class="portfolio-number">{i:02}</span><h3>{escape(product['title'])}</h3><p class="family-name">{escape(product['family'])}</p>{portfolio_image(product, data['name'])}</div>
      <div><p>{escape(product['body'])}</p><dl><div><dt>Applications</dt><dd>{escape(product['application'])}</dd></div><div><dt>Selection details</dt><dd>{escape(product['selection'])}</dd></div></dl><a class="text-link" href="{escape(product['source'], quote=True)}">Manufacturer details &amp; documents {arrow}</a></div>
    </article>''' for i, product in enumerate(data['products'], 1))
    applications = ''.join(f'''<article class="application-row"><span>{i:02}</span><h3>{escape(title)}</h3><div><p>{escape(body)}</p><a class="text-link" href="#{anchor}">{escape(label)} {arrow}</a></div></article>''' for i, (title, body, anchor, label) in enumerate(data['applications'], 1))
    enquiry = ''.join(f'<li><h3>{escape(title)}</h3><p>{escape(body)}</p></li>' for title, body in data['enquiry'])
    faqs = ''.join(f'<details><summary>{escape(question)}</summary><p>{escape(answer)}</p></details>' for question, answer in data['faqs'])
    return f'''<section class="brand-hero brand-landing"><div class="container">
      <nav class="breadcrumb" aria-label="Breadcrumb"><a href="../index.html">Home</a><span aria-hidden="true">/</span><span>{name}</span></nav>
      <div class="brand-landing-grid"><div><p class="eyebrow">{escape(data['label'])}</p><h1>{data['heading']}</h1><p class="brand-intro">{escape(data['intro'])}</p><div class="brand-actions"><a class="button" href="#portfolio">Explore {name} products {arrow}</a><a class="text-link light" href="#araya-support">Talk to Araya {arrow}</a></div></div>
      <figure class="product-figure hero-product"><img src="../assets/images/{data['image']}" alt="{escape(data['alt'], quote=True)}" width="{data['image_width']}" height="{data['image_height']}" fetchpriority="high"><figcaption><a href="{escape(data['image_source'], quote=True)}">{escape(data['image_caption'])}</a></figcaption></figure></div>
    </div></section>
    <nav class="brand-contents" aria-label="{name} page sections"><div class="container">{contents}</div></nav>
    <section class="section" id="about-brand"><div class="container"><div class="brand-profile"><div><p class="eyebrow">ABOUT {name.upper()}</p><h2>{data['profile_heading']}</h2><a class="text-link" href="{escape(data['profile_source'], quote=True)}">Manufacturer background {arrow}</a></div><div><p class="lead">{escape(data['profile'])}</p><p>{escape(data['local'])}</p></div></div><dl class="brand-facts">{facts}</dl></div></section>
    <section class="section section-muted" id="portfolio"><div class="container"><p class="eyebrow">{name.upper()} PRODUCTS &amp; SYSTEMS</p><h2>{data['portfolio_heading']}</h2><p class="portfolio-intro">Find the product family for your application. These manufacturer examples are a starting point; confirm the model, availability, configuration, and required features with Araya.</p><nav class="product-finder" aria-label="{name} product families">{finder}</nav><div class="portfolio-list">{portfolio}</div></div></section>
    <section class="section" id="applications"><div class="container"><p class="eyebrow">START WITH YOUR APPLICATION</p><h2>What does your system need?</h2><div class="application-list">{applications}</div></div></section>
    <section class="section brand-enquiry" id="araya-support"><div class="container"><div class="section-heading"><div><p class="eyebrow">{name.upper()} IN INDONESIA</p><h2>Bring your equipment.<br>Let’s define the scope.</h2></div><p>Discuss {name} supply, replacement, and integration requirements with PT Araya Internusa. A clear equipment brief helps us review the work around your installation.</p></div><ol class="enquiry-list">{enquiry}</ol><div class="brand-actions"><a class="button" href="https://wa.me/6281326396262">Discuss {name} on WhatsApp {arrow}</a><a class="text-link" href="mailto:cs@arayainternusa.com">Email your project details {arrow}</a></div></div></section>
    <section class="section" id="brand-faq"><div class="container brand-faq"><div><p class="eyebrow">COMMON QUESTIONS</p><h2>Before you<br>choose {name}.</h2></div><div class="faq-list">{faqs}</div></div></section>
    <section class="section section-muted project-connections"><div class="container"><p class="eyebrow">FROM PRODUCT TO PROJECT</p><h2>Connect the technology<br>to the work you need.</h2><div class="connection-grid"><a href="../marine/"><h3>Marine project scopes</h3><p>{escape(data['marine_connection'])}</p><span class="text-link">Explore marine work {arrow}</span></a><a href="../industrial/"><h3>Industrial project scopes</h3><p>{escape(data['industrial_connection'])}</p><span class="text-link">Explore industrial work {arrow}</span></a></div></div></section>
    <section class="related container"><a class="text-link" href="../{data['other']}/">{escape(data['other_label'])} {arrow}</a><a href="../index.html#brands">Back to our solutions</a></section>'''
