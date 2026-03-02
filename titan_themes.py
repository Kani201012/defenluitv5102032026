# titan_themes.py
# 2050 Titan Architecture Theme Engine - 25 Premium Modern Layouts

THEME_REGISTRY = {
    # --- SAAS & TECH (High Conversion, Clean) ---
    "1. Stripe Cloud (Modern SaaS)": {"bg": "#f8fafc", "txt": "#0f172a", "card": "#ffffff", "p": "#6366f1", "s": "#10b981", "nav": "rgba(255,255,255,0.8)", "shadow": "0 10px 40px -10px rgba(99,102,241,0.15)", "radius": "16px", "border": "1px solid #e2e8f0"},
    "2. Vercel Dark (Developer Core)": {"bg": "#000000", "txt": "#ededed", "card": "#111111", "p": "#ffffff", "s": "#0070f3", "nav": "rgba(0,0,0,0.8)", "shadow": "0 0 0 1px #333", "radius": "8px", "border": "1px solid #333"},
    "3. Apple Minimalist (Pure Clean)": {"bg": "#fbfbfd", "txt": "#1d1d1f", "card": "#ffffff", "p": "#000000", "s": "#0066cc", "nav": "rgba(251,251,253,0.8)", "shadow": "0 4px 24px rgba(0,0,0,0.04)", "radius": "24px", "border": "none"},
    "4. Neo-Brutalist (Gumroad Style)": {"bg": "#f4f4f0", "txt": "#000000", "card": "#ffffff", "p": "#000000", "s": "#ff90e8", "nav": "#f4f4f0", "shadow": "6px 6px 0px #000000", "radius": "0px", "border": "3px solid #000000"},
    "5. Glassmorphism (Translucent)": {"bg": "linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%)", "txt": "#1e1e24", "card": "rgba(255, 255, 255, 0.25)", "p": "#3a0ca3", "s": "#ff006e", "nav": "rgba(255,255,255,0.1)", "shadow": "0 8px 32px 0 rgba(31, 38, 135, 0.37)", "radius": "20px", "border": "1px solid rgba(255, 255, 255, 0.4)"},

    # --- RETAIL & E-COMMERCE ---
    "6. Luxury Boutique (High-End)": {"bg": "#faf9f6", "txt": "#2c2a29", "card": "#ffffff", "p": "#d4af37", "s": "#1a1a1a", "nav": "rgba(250,249,246,0.9)", "shadow": "0 15px 35px rgba(0,0,0,0.05)", "radius": "0px", "border": "1px solid #eaeaea"},
    "7. Streetwear Edge (Hypebeast)": {"bg": "#121212", "txt": "#f4f4f4", "card": "#1e1e1e", "p": "#ff4500", "s": "#ffffff", "nav": "rgba(18,18,18,0.9)", "shadow": "0 20px 40px rgba(255,69,0,0.15)", "radius": "4px", "border": "1px solid #333"},
    "8. Organic Eco (Sustainable)": {"bg": "#f0f4f0", "txt": "#2c3e2e", "card": "#ffffff", "p": "#4a7c59", "s": "#f39c12", "nav": "rgba(240,244,240,0.9)", "shadow": "0 10px 30px rgba(74,124,89,0.08)", "radius": "30px", "border": "none"},
    "9. Cosmetic Pastel (Beauty)": {"bg": "#fff5f5", "txt": "#5c4a4a", "card": "#ffffff", "p": "#e8b4b8", "s": "#a36b7e", "nav": "rgba(255,245,245,0.9)", "shadow": "0 12px 24px rgba(232,180,184,0.15)", "radius": "20px", "border": "1px solid #ffe3e3"},
    "10. Tech Hardware (Neon Dark)": {"bg": "#0d1117", "txt": "#c9d1d9", "card": "#161b22", "p": "#58a6ff", "s": "#238636", "nav": "rgba(13,17,23,0.9)", "shadow": "0 0 20px rgba(88,166,255,0.1)", "radius": "12px", "border": "1px solid #30363d"},

    # --- HEALTH & CLINICS ---
    "11. Medical Platinum (Trust)": {"bg": "#ffffff", "txt": "#1e293b", "card": "#f8fafc", "p": "#0284c7", "s": "#059669", "nav": "rgba(255,255,255,0.95)", "shadow": "0 4px 6px -1px rgba(0,0,0,0.05)", "radius": "12px", "border": "1px solid #e2e8f0"},
    "12. Dental Aqua (Clean)": {"bg": "#f0fdfa", "txt": "#0f172a", "card": "#ffffff", "p": "#0d9488", "s": "#0284c7", "nav": "rgba(240,253,250,0.9)", "shadow": "0 10px 25px rgba(13,148,136,0.1)", "radius": "16px", "border": "1px solid #ccfbf1"},
    "13. Fitness Aggressive (Gym)": {"bg": "#0a0a0a", "txt": "#ffffff", "card": "#171717", "p": "#e11d48", "s": "#facc15", "nav": "rgba(10,10,10,0.9)", "shadow": "0 10px 30px rgba(225,29,72,0.2)", "radius": "8px", "border": "1px solid #262626"},
    "14. Spa Therapy (Calm)": {"bg": "#faf5f0", "txt": "#4a443c", "card": "#ffffff", "p": "#bfa58a", "s": "#8c735a", "nav": "rgba(250,245,240,0.9)", "shadow": "0 8px 20px rgba(191,165,138,0.1)", "radius": "24px", "border": "1px solid #f0e6da"},
    "15. Yoga Mindfulness": {"bg": "#fdf8f5", "txt": "#333333", "card": "#ffffff", "p": "#d4a373", "s": "#a1c181", "nav": "rgba(253,248,245,0.9)", "shadow": "0 5px 15px rgba(0,0,0,0.03)", "radius": "50px", "border": "none"},

    # --- CORPORATE & REAL ESTATE ---
    "16. Law Firm Heritage": {"bg": "#ffffff", "txt": "#1f2937", "card": "#f9fafb", "p": "#1e3a8a", "s": "#b45309", "nav": "rgba(255,255,255,0.95)", "shadow": "0 4px 6px rgba(0,0,0,0.05)", "radius": "4px", "border": "1px solid #e5e7eb"},
    "17. Real Estate Prime": {"bg": "#111827", "txt": "#f3f4f6", "card": "#1f2937", "p": "#fbbf24", "s": "#f9fafb", "nav": "rgba(17,24,39,0.9)", "shadow": "0 10px 30px rgba(251,191,36,0.1)", "radius": "8px", "border": "1px solid #374151"},
    "18. Construction Industrial": {"bg": "#f5f5f5", "txt": "#1a1a1a", "card": "#ffffff", "p": "#f59e0b", "s": "#000000", "nav": "rgba(245,245,245,0.95)", "shadow": "0 8px 0px #e5e5e5", "radius": "0px", "border": "2px solid #000000"},
    "19. Architecture Grid": {"bg": "#ffffff", "txt": "#000000", "card": "#f4f4f5", "p": "#000000", "s": "#3b82f6", "nav": "#ffffff", "shadow": "none", "radius": "0px", "border": "1px solid #000000"},
    "20. Agency Bold (Creative)": {"bg": "#4f46e5", "txt": "#ffffff", "card": "#4338ca", "p": "#f9a8d4", "s": "#fde047", "nav": "rgba(79,70,229,0.9)", "shadow": "0 20px 40px rgba(0,0,0,0.2)", "radius": "20px", "border": "none"},

    # --- CREATOR & EXOTIC ---
    "21. Cyberpunk 2077": {"bg": "#fcee0a", "txt": "#000000", "card": "#000000", "p": "#00ffff", "s": "#ff003c", "nav": "#fcee0a", "shadow": "8px 8px 0px #00ffff", "radius": "0px", "border": "2px solid #000000"},
    "22. Monochromatic Black/White": {"bg": "#ffffff", "txt": "#000000", "card": "#ffffff", "p": "#000000", "s": "#000000", "nav": "#ffffff", "shadow": "4px 4px 0px #000000", "radius": "0px", "border": "2px solid #000000"},
    "23. Retro Synthwave": {"bg": "#2b213a", "txt": "#e0d6eb", "card": "#181425", "p": "#ff007f", "s": "#00f0ff", "nav": "rgba(43,33,58,0.9)", "shadow": "0 0 15px rgba(255,0,127,0.5)", "radius": "10px", "border": "1px solid #ff007f"},
    "24. Gradient Mesh": {"bg": "linear-gradient(45deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%)", "txt": "#333", "card": "rgba(255,255,255,0.6)", "p": "#f77062", "s": "#3f51b5", "nav": "rgba(255,255,255,0.4)", "shadow": "0 8px 32px rgba(0,0,0,0.1)", "radius": "30px", "border": "1px solid rgba(255,255,255,0.5)"},
    "25. Midnight Ocean": {"bg": "#0f2027", "txt": "#d1d5db", "card": "#203a43", "p": "#2c5364", "s": "#38ef7d", "nav": "rgba(15,32,39,0.9)", "shadow": "0 15px 25px rgba(0,0,0,0.3)", "radius": "16px", "border": "1px solid #2c5364"}
}

def generate_modern_css(theme_name, h_font, b_font, hero_align):
    t = THEME_REGISTRY.get(theme_name, THEME_REGISTRY["1. Stripe Cloud (Modern SaaS)"])
    
    # Modern Text Gradients for Headings (Only for specific themes to look ultra-modern)
    gradient_text = ""
    if "SaaS" in theme_name or "Dark" in theme_name or "Creative" in theme_name:
        gradient_text = f"background: linear-gradient(90deg, {t['p']}, {t['s']}); -webkit-background-clip: text; -webkit-text-fill-color: transparent;"

    # Layout mapping
    h_align = "text-align: center; justify-content: center;"
    if hero_align == "Left":
        h_align = "text-align: left; justify-content: flex-start; align-items: center;"

    # Brutalist exceptions for buttons
    btn_hover = "transform: translateY(-3px) scale(1.02); filter: brightness(1.15); box-shadow: 0 10px 25px -5px var(--p);"
    if "Brutalist" in theme_name or "Cyberpunk" in theme_name or "Monochromatic" in theme_name:
        btn_hover = "transform: translate(-4px, -4px); box-shadow: 8px 8px 0px #000;"

    # Glassmorphism exceptions
    backdrop = "backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);" if "Glass" in theme_name or "Mesh" in theme_name else ""

    return f"""
    :root {{
        --p: {t['p']}; --s: {t['s']}; --bg: {t['bg']}; --txt: {t['txt']}; 
        --card: {t['card']}; --nav: {t['nav']};
        --radius: {t['radius']}; --shadow: {t['shadow']}; --border: {t['border']};
        --h-font: '{h_font}', sans-serif; --b-font: '{b_font}', sans-serif;
    }}
    
    /* GLOBAL RESETS & MODERN TYPOGRAPHY */
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; font-size: 16px; }}
    body {{ 
        background: var(--bg); color: var(--txt); 
        font-family: var(--b-font); line-height: 1.6; 
        overflow-x: hidden; transition: background 0.4s ease;
        -webkit-font-smoothing: antialiased; /* Mac crispness */
        -moz-osx-font-smoothing: grayscale;
    }}
    
    body.dark-mode {{ --bg: #0f172a; --txt: #f8fafc; --card: #1e293b; --nav: rgba(15,23,42,0.95); --border: 1px solid #334155; }}
    
    p, span, li, div {{ color: inherit; }}
    h1, h2, h3, h4 {{ font-family: var(--h-font); color: var(--txt); line-height: 1.1; margin-bottom: 1rem; font-weight: 800; letter-spacing:-0.03em; }}
    strong {{ font-weight: 800; color: var(--p); }}
    
    /* MODERN RESPONSIVE FLUID TYPOGRAPHY */
    h1 {{ font-size: clamp(3rem, 8vw, 5.5rem); {gradient_text} }}
    h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); }}
    h3 {{ font-size: clamp(1.5rem, 3vw, 2rem); }}
    p {{ margin-bottom: 1.2rem; font-size: 1.1rem; opacity: 0.9; }}
    
    /* 2026 ADVANCED HERO ENGINE */
    .hero {{ position: relative; min-height: 95vh; overflow: hidden; display: flex; {h_align} padding-top: 120px; }}
    .carousel-slide {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-size: cover; background-position: center; opacity: 0; transition: opacity 1.5s cubic-bezier(0.4, 0, 0.2, 1); z-index: 0; transform: scale(1.05); }}
    .carousel-slide.active {{ opacity: 1; transform: scale(1); }}
    .hero-overlay {{ background: linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.8) 100%); position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; }}
    .hero-content {{ z-index: 2; position: relative; width: 100%; padding: 0 5%; max-width: 1400px; }}
    .hero h1 {{ color: #ffffff !important; text-shadow: 0 10px 30px rgba(0,0,0,0.5); -webkit-text-fill-color: #fff; background: none; }}
    .hero p {{ color: rgba(255,255,255,0.9) !important; font-size: clamp(1.2rem, 2vw, 1.4rem); max-width: 800px; margin: 0 {'auto' if hero_align == 'Center' else '0'} 2.5rem {'auto' if hero_align == 'Center' else '0'}; font-weight: 400; }}
    
    /* BENTO-STYLE GRID LAYOUTS */
    .container {{ max-width: 1300px; margin: 0 auto; padding: 0 2rem; }}
    main section {{ padding: clamp(4rem, 8vw, 8rem) 0; position: relative; }}
    .section-head {{ text-align: center; margin-bottom: clamp(3rem, 5vw, 5rem); }}
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2.5rem; }}
    .about-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 5rem; align-items: center; }}
    
    /* 2026 CARD PHYSICS & MICRO-INTERACTIONS */
    .card {{ 
        background: var(--card); 
        border-radius: var(--radius); 
        border: var(--border); 
        box-shadow: var(--shadow);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); 
        display: flex; flex-direction: column; overflow: hidden; position: relative;
        {backdrop}
    }}
    .card::before {{ content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, var(--p), var(--s)); opacity: 0; transition: 0.3s; }}
    .card:hover {{ transform: translateY(-10px); box-shadow: 0 25px 50px -12px rgba(0,0,0,0.15); }}
    .card:hover::before {{ opacity: 1; }}
    
    .card h3, .card h4, .card a:not(.btn) {{ color: var(--txt) !important; text-decoration: none; }}
    .card-body {{ padding: 2.5rem; display: flex; flex-direction: column; flex-grow: 1; }}
    .card-desc {{ font-size: 1.05rem; opacity: 0.75; margin-bottom: 2rem; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }}
    .prod-img {{ width: 100%; height: 300px; object-fit: cover; transition: transform 0.5s ease; }}
    .card:hover .prod-img {{ transform: scale(1.05); }}
    
    /* ENTERPRISE BUTTON COMPONENTS */
    .btn {{ 
        display: inline-flex; align-items: center; justify-content: center;
        padding: 1.2rem 2.5rem; border-radius: var(--radius); 
        font-weight: 800; text-decoration: none; transition: all 0.3s ease; 
        text-transform: uppercase; cursor: pointer; border: none; text-align: center;
        font-size: 0.95rem; letter-spacing: 1.5px; position: relative; overflow: hidden;
    }}
    .btn-primary {{ background: var(--p); color: #fff !important; }}
    .btn-accent {{ background: var(--s); color: #fff !important; }}
    .btn:hover {{ {btn_hover} }}
    
    /* GLASSMORPHISM NAVIGATION */
    nav#main-navbar {{ 
        position: fixed; top: 0; width: 100%; z-index: 1000; 
        background: var(--nav); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(128,128,128,0.1); padding: 1.2rem 0; transition: top 0.3s, background 0.3s; 
    }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    .nav-links {{ display: flex; align-items: center; gap: 2rem; }}
    .nav-links a {{ text-decoration: none; font-weight: 600; color: var(--txt); font-size: 0.95rem; transition: 0.2s; position: relative; }}
    .nav-links a::after {{ content: ''; position: absolute; width: 0; height: 2px; bottom: -4px; left: 0; background-color: var(--p); transition: 0.3s; }}
    .nav-links a:hover::after {{ width: 100%; }}
    .nav-links a:hover {{ color: var(--p); }}
    .mobile-menu {{ display: none; font-size: 1.8rem; cursor: pointer; background:none; border:none; color:var(--txt); }}
    
    /* PREMIUM PRODUCT DETAIL PAGE */
    .detail-view {{ 
        display: grid; grid-template-columns: 1.2fr 1fr; gap: 5rem; align-items: start; 
        background: var(--card); padding: 4rem; border-radius: var(--radius); 
        box-shadow: var(--shadow); border: var(--border); {backdrop}
    }}
    .product-price-tag {{ font-size: 3rem; color: var(--s); font-weight: 900; margin-bottom: 2rem; display: block; }}
    .product-meta-box {{ background: rgba(128,128,128,0.05); padding: 2rem; border-radius: var(--radius); margin-bottom: 2.5rem; border-left: 5px solid var(--p); }}
    .gallery-thumbs {{ display: flex; gap: 15px; margin-top: 20px; overflow-x: auto; padding-bottom:10px; }}
    .thumb {{ width: 80px; height: 80px; border-radius: var(--radius); object-fit: cover; cursor: pointer; border: 2px solid transparent; opacity: 0.6; transition: 0.3s; }}
    .thumb:hover, .thumb.active {{ border-color: var(--p); opacity: 1; transform: translateY(-5px); }}
    
    /* RESPONSIVE PRICING TABLES */
    .pricing-wrapper {{ overflow-x: auto; -webkit-overflow-scrolling: touch; width: 100%; margin: 0 auto; box-shadow: var(--shadow); border-radius: var(--radius); background: var(--card); border: var(--border); }}
    .pricing-table {{ width: 100%; border-collapse: collapse; min-width: 800px; }}
    .pricing-table th {{ background: var(--p); color: white; padding: 2rem; text-align: left; font-size: 1.1rem; text-transform: uppercase; letter-spacing: 1px; }}
    .pricing-table td {{ padding: 2rem; border-bottom: 1px solid rgba(128,128,128,0.1); color: var(--txt); font-size: 1.1rem; }}
    .pricing-table tr:hover td {{ background: rgba(128,128,128,0.03); }}

    /* MODERN FOOTER */
    footer {{ background: #0f172a; color: #f8fafc; padding: 6rem 0 3rem 0; margin-top: auto; border-top: 4px solid var(--p); }}
    .footer-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 4rem; }}
    footer a {{ color: #94a3b8 !important; text-decoration: none; display: block; margin-bottom: 1rem; transition: 0.3s; font-size: 1.05rem; }}
    footer a:hover {{ color: #ffffff !important; transform: translateX(5px); }}
    .social-icon {{ width: 28px; height: 28px; fill: #94a3b8; transition: 0.3s; }}
    .social-icon:hover {{ fill: var(--p); transform: scale(1.2) translateY(-3px); }}

    /* ACCESSIBILITY & UTILS */
    .reveal {{ opacity: 0; transform: translateY(40px); transition: all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94); }}
    .reveal.active {{ opacity: 1; transform: translateY(0); }}
    details {{ background: var(--card); border: var(--border); border-radius: var(--radius); margin-bottom: 1.5rem; padding: 1.5rem; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.02); transition:0.3s; }}
    details:hover {{ box-shadow: var(--shadow); transform: translateX(5px); border-left: 4px solid var(--p); }}
    details summary {{ font-weight: 800; font-size: 1.2rem; outline: none; }}
    
    /* MOBILE OPTIMIZATION */
    @media (max-width: 992px) {{
        nav#main-navbar .nav-links {{ position: fixed; top: 70px; left: -100%; width: 100%; height: calc(100vh - 70px); background: var(--bg); flex-direction: column; padding: 3rem; transition: 0.4s ease; align-items: center; justify-content: center; gap: 2.5rem; }}
        nav#main-navbar .nav-links.active {{ left: 0; }}
        .nav-links a {{ font-size: 1.5rem; }}
        .mobile-menu {{ display: block; }}
        .about-grid, .detail-view, .grid-3 {{ grid-template-columns: 1fr !important; gap: 3rem; }}
        .hero {{ padding-top: 100px; text-align: center; }}
        .detail-view {{ padding: 2rem; }}
        .pricing-table th, .pricing-table td {{ padding: 1.2rem 1rem; font-size: 0.95rem; }}
    }}
    """
