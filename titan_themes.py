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

def generate_modern_css(theme_name, h_font, b_font, hero_align, h_color, b_color, h1_size, p_size, cta_bg, cta_txt):
    # 1. First, fetch the base colors from the registry
    t = THEME_REGISTRY.get(theme_name, THEME_REGISTRY["1. Stripe Cloud (Modern SaaS)"])
    
    # 2. Define the logic for special effects (Gradient, Hover, Backdrop)
    gradient_text = ""
    if any(x in theme_name for x in ["SaaS", "Dark", "Creative"]):
        gradient_text = f"background: linear-gradient(90deg, {t['p']}, {t['s']}); -webkit-background-clip: text; -webkit-text-fill-color: transparent;"

    btn_hover = "transform: translateY(-3px) scale(1.02); filter: brightness(1.15); box-shadow: 0 10px 25px -5px var(--p);"
    if any(x in theme_name for x in ["Brutalist", "Cyberpunk", "Monochromatic"]):
        btn_hover = "transform: translate(-4px, -4px); box-shadow: 8px 8px 0px #000;"

    backdrop = "backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);" if any(x in theme_name for x in ["Glass", "Mesh"]) else ""

    # SMART ALIGNMENT LOGIC
    h_align_logic = ""
    if hero_align == "Center":
        h_align_logic = """
        grid-template-columns: 1fr; 
        text-align: center; 
        max-width: 1000px; 
        margin: 0 auto;
        """
    else:
        h_align_logic = """
        grid-template-columns: 1.1fr 1fr; 
        text-align: left;
        """

    # 3. Compile Master CSS String
    return f"""
    :root {{
        --p: {t['p']}; --s: {t['s']}; --bg: {t['bg']}; 
        --nav: {t['nav']}; --card: {t['card']};
        --radius: {t['radius']}; --shadow: {t['shadow']}; --border: {t['border']};
        --h-font: '{h_font}', sans-serif; --b-font: '{b_font}', sans-serif;
        
        /* MANUAL OVERRIDES FROM SIDEBAR */
        --txt-h: {h_color};
        --txt-b: {b_color};
        --h1-size: {h1_size};
        --p-size: {p_size};
        --cta-bg: {cta_bg};
        --cta-txt: {cta_txt};
    }}
    
    /* GLOBAL RESETS */
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; font-size: 16px; }}
    body {{ background: var(--bg); color: var(--txt-b); font-family: var(--b-font); font-size: var(--p-size); line-height: 1.6; overflow-x: hidden; width: 100%; transition: background 0.4s ease; }}
    
    a {{ color: var(--s); text-decoration: none; transition: 0.3s; }}
    a:hover {{ color: var(--p); }}
    
    h1, h2, h3, h4 {{ font-family: var(--h-font); color: var(--txt-h); line-height: 1.1; font-weight: 800; letter-spacing:-0.03em; }}
    h1 {{ font-size: var(--h1-size); {gradient_text} }}
    h2 {{ font-size: calc(var(--h1-size) * 0.75); }}
    p {{ margin-bottom: 1.2rem; opacity: 0.9; }}

    /* MODERN ASYMMETRICAL HERO ENGINE */
    .modern-hero {{ position: relative; min-height: 100vh; display: flex; align-items: center; padding: 120px 0 80px 0; background: var(--bg); overflow: hidden; }}
    .modern-hero-grid {{ display: grid; gap: 4rem; align-items: center; width: 100%; {h_align_logic} }}
    .visual-frame {{ width: 100%; height: 550px; border-radius: 32px; overflow: hidden; box-shadow: var(--shadow); border: 8px solid var(--card); position: relative; z-index: 2; }}
    .carousel-slide {{ position: absolute; inset: 0; background-size: cover; background-position: center; opacity: 0; transition: 1.5s cubic-bezier(0.4, 0, 0.2, 1); }}
    .carousel-slide.active {{ opacity: 1; }}
    .hero-btn-group {{ display: flex; gap: 1rem; flex-wrap: wrap; justify-content: {'center' if hero_align == 'Center' else 'flex-start'}; }}
    
    .hero-badge {{ display: inline-block; padding: 0.5rem 1rem; background: rgba(128,128,128,0.1); border: 1px solid rgba(128,128,128,0.2); border-radius: 50px; font-size: 0.9rem; font-weight: 700; margin-bottom: 1.5rem; color: var(--txt-h); text-transform: uppercase; letter-spacing: 1px; }}

    /* FLOATING STATS RIBBON */
    .stats-ribbon-container {{ margin-top: -80px; position: relative; z-index: 10; padding: 0 20px; }}
    .stats-ribbon {{ background: var(--card); border-radius: 24px; padding: 3rem; display: flex; justify-content: space-around; align-items: center; box-shadow: var(--shadow); border: var(--border); backdrop-filter: blur(20px); }}
    .stat-block {{ text-align: center; }}
    .stat-block h3 {{ font-size: 3rem; color: var(--p); margin: 0; }}
    .stat-block p {{ font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin: 0; font-size: 0.9rem; color: var(--txt-h); }}
    .stat-divider {{ width: 2px; height: 60px; background: rgba(128,128,128,0.2); }}

    /* BENTO FEATURES GRID */
    .section-subtitle {{ font-size: 1.2rem; color: var(--txt-b); opacity: 0.7; margin-top: 1rem; text-transform: uppercase; letter-spacing: 2px; font-weight: 600; display: block; }}
    .modern-grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; }}
    .modern-feature-card {{ background: var(--card); padding: 3rem; border-radius: 24px; box-shadow: var(--shadow); border: var(--border); transition: 0.4s; display: flex; flex-direction: column; gap: 1.5rem; {backdrop} }}
    .modern-feature-card:hover {{ transform: translateY(-10px); border-color: var(--p); }}
    .feature-icon-wrapper {{ width: 60px; height: 60px; border-radius: 12px; background: rgba(128,128,128,0.1); display: flex; align-items: center; justify-content: center; color: var(--s); }}

    /* 2026 CARD PHYSICS */
    .card {{ 
        background: var(--card); border-radius: var(--radius); border: var(--border); box-shadow: var(--shadow);
        transition: 0.4s; display: flex; flex-direction: column; overflow: hidden; position: relative;
        color: var(--txt-b) !important; {backdrop}
    }}
    .card:hover {{ transform: translateY(-10px); box-shadow: 0 25px 50px -12px rgba(0,0,0,0.2); }}
    .card h3 {{ font-size: 1.35rem !important; margin-bottom: 0.5rem; color: var(--txt-h) !important; font-weight: 800; }}
    .prod-img {{ width: 100%; height: 260px; object-fit: cover; transition: 0.6s; }}
    .card:hover .prod-img {{ transform: scale(1.08); }}

    /* PREMIUM ASYMMETRICAL PRODUCT VIEW */
    .detail-view {{ display: grid; grid-template-columns: 0.8fr 1.2fr; gap: 6rem; align-items: start; background: var(--card); padding: 5rem; border-radius: 32px; box-shadow: var(--shadow); border: var(--border); position: relative; {backdrop} }}
    .product-media-column {{ position: sticky; top: 150px; }}
    .product-price-tag {{ display: inline-block; padding: 0.5rem 1.5rem; background: rgba(5,150,105,0.1); color: #059669; font-size: 2rem; font-weight: 900; border-radius: 50px; margin-bottom: 2rem; }}
    .thumb {{ width: 80px; height: 80px; border-radius: var(--radius); object-fit: cover; cursor: pointer; opacity: 0.6; transition: 0.3s; margin-right: 10px; border: 2px solid transparent; }}
    .thumb:hover, .thumb.active {{ opacity: 1; border-color: var(--p); transform: translateY(-5px); }}

    /* ENTERPRISE BUTTONS */
    .btn {{ display: inline-flex; align-items: center; justify-content: center; padding: 1.2rem 2.5rem; border-radius: var(--radius); font-weight: 800; text-transform: uppercase; border: none; cursor: pointer; transition: 0.3s; letter-spacing: 1px; }}
    .btn-primary {{ background: var(--p); color: #fff !important; }}
    .btn-accent {{ background: var(--s); color: #fff !important; }}
    .btn-outline-light {{ background: transparent; color: var(--txt-h) !important; border: 2px solid var(--txt-h); }}
    .btn-outline-light:hover {{ background: var(--txt-h); color: var(--bg) !important; }}
    .btn:hover {{ {btn_hover} }}

    /* FINAL CTA OVERRIDE (FIXES READABILITY) */
    section[style*="background:var(--s)"], section[style*="background: var(--s)"] {{
        background: var(--cta-bg) !important; color: var(--cta-txt) !important;
    }}
    section[style*="background:var(--s)"] h2, section[style*="background:var(--s)"] p {{
        color: var(--cta-txt) !important;
    }}

    /* MODAL PHYSICS */
    #cart-overlay, #lang-overlay {{ display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.7); backdrop-filter: blur(8px); z-index: 1000; }}
    #cart-modal, #lang-modal {{ display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: var(--card); width: 90%; max-width: 500px; padding: 3rem; border-radius: 24px; box-shadow: 0 30px 60px rgba(0,0,0,0.4); z-index: 1001; border: var(--border); color: var(--txt-b); {backdrop} }}
    
    /* FLOATING WIDGETS */
    #theme-toggle {{ position: fixed; bottom: 30px; left: 30px; width: 50px; height: 50px; background: var(--card); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 25px rgba(0,0,0,0.2); cursor: pointer; z-index: 999; font-size: 1.5rem; border: var(--border); transition:0.3s; }}
    #theme-toggle:hover {{ transform: scale(1.1) rotate(15deg); border-color: var(--p); }}
    #wa-widget {{ position: fixed; bottom: 30px; right: 30px; background: #25D366; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 25px rgba(0,0,0,0.2); z-index: 999; transition:0.3s; }}
    #wa-widget:hover {{ transform: scale(1.1); }}
    #voice-btn {{ position: fixed; bottom: 170px; right: 30px; background: var(--p); color: #fff; border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; z-index: 997; cursor: pointer; box-shadow: 0 10px 25px rgba(0,0,0,0.2); border: 2px solid rgba(255,255,255,0.1); transition:0.3s; }}
    #voice-btn:hover {{ transform: scale(1.1); background: var(--s); }}
    
    .listening {{ animation: voice-pulse 1.5s infinite; background: var(--s) !important; }}
    @keyframes voice-pulse {{ 0% {{ transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 0, 60, 0.4); }} 70% {{ transform: scale(1.2); box-shadow: 0 0 0 20px rgba(255, 0, 60, 0); }} 100% {{ transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 0, 60, 0); }} }}

    /* MODERN FOOTER */
    footer {{ background: #0f172a; color: #f8fafc; padding: 6rem 0 3rem 0; margin-top: auto; border-top: 4px solid var(--p); }}
    footer a {{ color: #94a3b8 !important; transition:0.3s; }}
    footer a:hover {{ color: #fff !important; transform:translateX(5px); }}

    /* UTILS & ABOUT SECTION */
    .container {{ max-width: 1300px; margin: 0 auto; padding: 0 2rem; }}
    .reveal {{ opacity: 0; transform: translateY(40px); transition: all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94); }}
    .reveal.active {{ opacity: 1; transform: translateY(0); }}
    .about-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 5rem; align-items: center; }}
    .modern-about {{ background: rgba(128,128,128,0.02); overflow: hidden; }}
    .about-visual {{ position: relative; }}
    .about-main-img {{ width: 100%; height: 600px; object-fit: cover; border-radius: 32px; box-shadow: var(--shadow); }}
    .about-experience-badge {{ position: absolute; bottom: -30px; right: -30px; background: var(--p); color: #fff; padding: 2rem; border-radius: 24px; box-shadow: 0 20px 40px rgba(0,0,0,0.2); display: flex; align-items: center; gap: 1rem; border: 4px solid var(--card); }}
    .about-experience-badge strong {{ font-size: 3rem; line-height: 1; color: #fff; }}
    .about-experience-badge span {{ font-size: 1rem; font-weight: 700; text-transform: uppercase; line-height: 1.2; }}
    .about-lead {{ font-size: 1.25rem; line-height: 1.8; opacity: 0.9; color: var(--txt-b); border-left: 4px solid var(--s); padding-left: 1.5rem; }}

    /* =========================================
       📱 MOBILE OPTIMIZATION MATRIX (THE FIX)
       ========================================= */
    @media (max-width: 992px) {{
        nav#main-navbar .nav-links {{ position: fixed; top: 70px; left: -100%; width: 100%; height: calc(100vh - 70px); background: var(--bg); flex-direction: column; padding: 3rem; transition: 0.4s ease; align-items: center; justify-content: center; gap: 2.5rem; }}
        nav#main-navbar .nav-links.active {{ left: 0; }}
        .nav-links a {{ font-size: 1.5rem; }}
        .mobile-menu {{ display: block; }}
        .detail-view {{ grid-template-columns: 1fr; padding: 2rem; gap: 3rem; }}
        .product-media-column {{ position: relative; top: 0; }}
        .about-grid {{ grid-template-columns: 1fr !important; gap: 4rem; text-align: center; }}
    }}

    @media (max-width: 768px) {{
        /* Typography Scaling */
        h1 {{ font-size: clamp(2.5rem, 8vw, 3.5rem); }}
        .container {{ padding: 0 1.5rem; }}
        
        /* Hero & Buttons Overlap Fix */
        .modern-hero {{ padding-top: 140px; min-height: auto; padding-bottom: 60px; }}
        .modern-hero-grid {{ grid-template-columns: 1fr !important; text-align: center !important; }}
        .hero-btn-group {{ flex-direction: column; width: 100%; justify-content: center; align-items: center; }}
        .hero-btn-group .btn {{ width: 100%; max-width: 350px; margin: 0 auto; }}
        .visual-frame {{ height: 300px; border-width: 4px; }}
        
        /* Stats Ribbon Fix */
        .stats-ribbon-container {{ margin-top: 2rem; padding: 0 1rem; }}
        .stats-ribbon {{ flex-direction: column; padding: 2rem 1.5rem; gap: 1.5rem; }}
        .stat-block h3 {{ font-size: 2.5rem; }}
        .stat-divider {{ width: 100%; height: 1px; }} /* Horizontal line on mobile */
        
        /* Cards & Paddings Fix */
        .modern-feature-card {{ padding: 2rem 1.5rem; }}
        .card-body {{ padding: 1.5rem; }}
        
        /* About Image Bleed Fix */
        .about-main-img {{ height: 350px; }}
        .about-experience-badge {{ right: 5%; bottom: -15px; padding: 1rem; border-width: 2px; }}
        .about-experience-badge strong {{ font-size: 2rem; }}
        .about-lead {{ border-left: none; border-top: 4px solid var(--s); padding-left: 0; padding-top: 1.5rem; }}
        
        /* Floating Widgets Resizing */
        #wa-widget {{ width: 50px; height: 50px; bottom: 20px; right: 20px; }}
        #theme-toggle {{ width: 45px; height: 45px; bottom: 20px; left: 20px; font-size: 1.2rem; }}
        #cart-float {{ bottom: 85px; right: 20px; padding: 12px 20px; font-size: 0.9rem; }}
        #voice-btn {{ bottom: 150px; right: 20px; width: 45px; height: 45px; font-size: 1rem; }}
    }}
    """
