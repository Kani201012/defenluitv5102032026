# titan_themes.py
# Refactored by the 50-Year Tech Architect
# Optimization: Fluid Design Systems & Intrinsic Mobile Layouts

THEME_REGISTRY = {
    # --- SAAS & TECH ---
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
    t = THEME_REGISTRY.get(theme_name, THEME_REGISTRY["1. Stripe Cloud (Modern SaaS)"])
    
    gradient_text = ""
    if any(x in theme_name for x in ["SaaS", "Dark", "Creative"]):
        gradient_text = f"background: linear-gradient(90deg, {t['p']}, {t['s']}); -webkit-background-clip: text; -webkit-text-fill-color: transparent;"

    btn_hover = "transform: translateY(-3px) scale(1.02); filter: brightness(1.15); box-shadow: 0 10px 25px -5px var(--p);"
    if any(x in theme_name for x in ["Brutalist", "Cyberpunk", "Monochromatic"]):
        btn_hover = "transform: translate(-4px, -4px); box-shadow: 8px 8px 0px #000;"

    backdrop = "backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);" if any(x in theme_name for x in ["Glass", "Mesh"]) else ""

    h_align = "text-align: center; justify-content: center;"
    if hero_align == "Left":
        h_align = "text-align: left; justify-content: flex-start; align-items: flex-start;"

    return f"""
    :root {{
        --p: {t['p']}; --s: {t['s']}; --bg: {t['bg']}; 
        --nav: {t['nav']}; --card: {t['card']};
        --radius: {t['radius']}; --shadow: {t['shadow']}; --border: {t['border']};
        --h-font: '{h_font}', sans-serif; --b-font: '{b_font}', sans-serif;
        --txt-h: {h_color}; --txt-b: {b_color};
        --h1-size: clamp(2.5rem, 8vw, {h1_size});
        --p-size: clamp(1rem, 2vw, {p_size});
        --cta-bg: {cta_bg}; --cta-txt: {cta_txt};
    }}
    
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; font-size: 16px; width: 100%; overflow-x: hidden; }}
    
    body {{ 
        background: var(--bg); color: var(--txt-b); font-family: var(--b-font); 
        font-size: var(--p-size); line-height: 1.6; overflow-x: hidden; width: 100%;
    }}
    
    h1, h2, h3, h4 {{ font-family: var(--h-font); color: var(--txt-h); line-height: 1.1; font-weight: 800; }}
    h1 {{ font-size: var(--h1-size); {gradient_text} }}
    h2 {{ font-size: clamp(2rem, 5vw, 3rem); }}
    
    /* 2026 FLUID LAYOUT SYSTEM */
    .container {{ width: min(1400px, 92%); margin: 0 auto; }}
    main section {{ padding: clamp(4rem, 10vw, 8rem) 0; width: 100%; position: relative; }}
    
    /* NAV & MOBILE OVERLAYS */
    nav#main-navbar {{ 
        position: fixed; top: 0; width: 100%; z-index: 1000; 
        background: var(--nav); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(128,128,128,0.1); padding: 1rem 0; 
    }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    .nav-links {{ display: flex; align-items: center; gap: 2rem; }}
    
    @media (max-width: 992px) {{
        .nav-links {{ 
            position: fixed; top: 0; right: -100%; width: 80%; height: 100vh; 
            background: var(--card); flex-direction: column; padding: 6rem 2rem; 
            transition: 0.4s cubic-bezier(0.19, 1, 0.22, 1); box-shadow: -10px 0 30px rgba(0,0,0,0.1); 
            z-index: 1001; align-items: flex-start;
        }}
        .nav-links.active {{ right: 0; }}
        .mobile-menu {{ display: block !important; font-size: 2rem; cursor: pointer; color: var(--txt-h); z-index: 1002; }}
        .nav-links a {{ font-size: 1.5rem; }}
        .modern-hero-grid {{ grid-template-columns: 1fr !important; text-align: center; gap: 3rem; }}
        .modern-hero-visual {{ height: 400px !important; }}
        .stats-ribbon {{ flex-direction: column; gap: 2.5rem; }}
        .stat-divider {{ width: 60px !important; height: 2px !important; }}
        .about-grid, .detail-view, .contact-grid {{ grid-template-columns: 1fr !important; gap: 3rem; }}
        .detail-view {{ padding: 2rem !important; }}
        .product-media-column {{ position: relative !important; top: 0 !important; }}
    }}

    /* HERO COMPONENT */
    .modern-hero {{ min-height: 100vh; display: flex; align-items: center; padding-top: 100px; }}
    .modern-hero-grid {{ display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 4rem; align-items: center; }}
    .visual-frame {{ border-radius: 32px; overflow: hidden; height: 100%; box-shadow: var(--shadow); border: var(--border); background: var(--card); }}
    
    /* STATS RIBBON */
    .stats-ribbon-container {{ margin-top: -80px; position: relative; z-index: 10; }}
    .stats-ribbon {{ background: var(--card); border-radius: 24px; padding: clamp(2rem, 5vw, 4rem); display: flex; justify-content: space-around; align-items: center; box-shadow: var(--shadow); border: var(--border); {backdrop} }}
    .stat-block h3 {{ font-size: clamp(2.5rem, 6vw, 4rem); color: var(--p); }}
    .stat-divider {{ width: 2px; height: 50px; background: rgba(128,128,128,0.2); }}

    /* GRID & CARDS */
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 350px), 1fr)); gap: 2rem; }}
    .card {{ 
        background: var(--card); border-radius: var(--radius); border: var(--border); box-shadow: var(--shadow);
        transition: transform 0.3s ease; overflow: hidden; height: 100%; display: flex; flex-direction: column;
    }}
    .card:hover {{ transform: translateY(-10px); }}
    .prod-img {{ width: 100%; aspect-ratio: 4/3; object-fit: cover; }}
    .card-body {{ padding: 2rem; flex-grow: 1; display: flex; flex-direction: column; }}

    /* PRODUCT DETAIL VIEW (Refactored for Mobile) */
    .detail-view {{ 
        display: grid; grid-template-columns: 0.8fr 1.2fr; gap: clamp(2rem, 8vw, 6rem); 
        background: var(--card); padding: clamp(2rem, 5vw, 5rem); border-radius: 32px; 
        box-shadow: var(--shadow); border: var(--border); 
    }}
    .product-media-column {{ position: sticky; top: 120px; }}
    .product-price-tag {{ display: inline-block; padding: 0.5rem 1.5rem; background: rgba(5, 150, 105, 0.1); color: #059669; font-size: 2rem; font-weight: 900; border-radius: 50px; margin: 1rem 0; }}

    /* BUTTONS */
    .btn {{ 
        padding: 1rem 2rem; border-radius: var(--radius); font-weight: 800; text-decoration: none; 
        transition: 0.3s; display: inline-flex; align-items: center; justify-content: center;
        border: none; cursor: pointer; text-transform: uppercase; letter-spacing: 1px;
    }}
    .btn-primary {{ background: var(--p); color: #fff !important; }}
    .btn-accent {{ background: var(--s); color: #fff !important; }}
    .btn:hover {{ {btn_hover} }}

    /* FLOATING WIDGETS (Mobile Stack Prevention) */
    #wa-widget, #theme-toggle, #cart-float, #voice-btn {{ 
        position: fixed; z-index: 900; 
    }}
    #wa-widget {{ bottom: 20px; right: 20px; }}
    #theme-toggle {{ bottom: 20px; left: 20px; }}
    #cart-float {{ bottom: 90px; right: 20px; }}
    #voice-btn {{ bottom: 160px; right: 20px; }}

    @media (max-width: 600px) {{
        #cart-float, #voice-btn {{ right: 10px; scale: 0.8; }}
        #wa-widget {{ right: 10px; }}
        #theme-toggle {{ left: 10px; scale: 0.8; }}
        .nav-flex {{ padding: 0 10px; }}
    }}

    /* UTILS */
    .reveal {{ opacity: 0; transform: translateY(30px); transition: 0.8s ease-out; }}
    .reveal.active {{ opacity: 1; transform: translateY(0); }}
    
    footer {{ background: #0f172a; color: #fff; padding: 6rem 0 2rem 0; }}
    .footer-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 3rem; }}
    footer a {{ color: #94a3b8 !important; text-decoration: none; margin-bottom: 0.5rem; display: block; }}
    """
