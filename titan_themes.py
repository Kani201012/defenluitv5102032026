# titan_themes.py
# Refactored by the 50-Year Tech Architect
# Optimization: Premium UI Physics, Sub-pixel Rendering, Layered Glassmorphism

THEME_REGISTRY = {
    # --- SAAS & TECH ---
    "1. Stripe Cloud (Modern SaaS)": {"bg": "#f8fafc", "txt": "#0f172a", "card": "#ffffff", "p": "#6366f1", "s": "#10b981", "nav": "rgba(255,255,255,0.7)", "shadow": "0 4px 6px -1px rgba(0,0,0,0.05), 0 20px 40px -10px rgba(99,102,241,0.1)", "radius": "20px", "border": "1px solid rgba(226, 232, 240, 0.8)"},
    "2. Vercel Dark (Developer Core)": {"bg": "#000000", "txt": "#ededed", "card": "#0a0a0a", "p": "#ffffff", "s": "#0070f3", "nav": "rgba(0,0,0,0.6)", "shadow": "0 0 0 1px rgba(255,255,255,0.1), 0 20px 40px rgba(0,0,0,0.5)", "radius": "12px", "border": "1px solid rgba(255,255,255,0.05)"},
    "3. Apple Minimalist (Pure Clean)": {"bg": "#fbfbfd", "txt": "#1d1d1f", "card": "#ffffff", "p": "#000000", "s": "#0066cc", "nav": "rgba(251,251,253,0.7)", "shadow": "0 2px 10px rgba(0,0,0,0.02), 0 20px 40px rgba(0,0,0,0.04)", "radius": "28px", "border": "1px solid rgba(0,0,0,0.02)"},
    "4. Neo-Brutalist (Gumroad Style)": {"bg": "#f4f4f0", "txt": "#000000", "card": "#ffffff", "p": "#000000", "s": "#ff90e8", "nav": "rgba(244,244,240,0.9)", "shadow": "6px 6px 0px #000000", "radius": "0px", "border": "3px solid #000000"},
    "5. Glassmorphism (Translucent)": {"bg": "linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%)", "txt": "#1e1e24", "card": "rgba(255, 255, 255, 0.15)", "p": "#3a0ca3", "s": "#ff006e", "nav": "rgba(255,255,255,0.1)", "shadow": "0 8px 32px 0 rgba(31, 38, 135, 0.2)", "radius": "24px", "border": "1px solid rgba(255, 255, 255, 0.3)"},

    # --- RETAIL & E-COMMERCE ---
    "6. Luxury Boutique (High-End)": {"bg": "#faf9f6", "txt": "#2c2a29", "card": "#ffffff", "p": "#d4af37", "s": "#1a1a1a", "nav": "rgba(250,249,246,0.8)", "shadow": "0 10px 30px rgba(0,0,0,0.04)", "radius": "4px", "border": "1px solid rgba(0,0,0,0.05)"},
    "7. Streetwear Edge (Hypebeast)": {"bg": "#121212", "txt": "#f4f4f4", "card": "#1a1a1a", "p": "#ff4500", "s": "#ffffff", "nav": "rgba(18,18,18,0.8)", "shadow": "0 20px 40px rgba(255,69,0,0.1)", "radius": "8px", "border": "1px solid rgba(255,255,255,0.05)"},
    "8. Organic Eco (Sustainable)": {"bg": "#f0f4f0", "txt": "#2c3e2e", "card": "#ffffff", "p": "#4a7c59", "s": "#f39c12", "nav": "rgba(240,244,240,0.8)", "shadow": "0 10px 30px rgba(74,124,89,0.05)", "radius": "30px", "border": "1px solid rgba(74,124,89,0.1)"},
    "9. Cosmetic Pastel (Beauty)": {"bg": "#fff5f5", "txt": "#5c4a4a", "card": "#ffffff", "p": "#e8b4b8", "s": "#a36b7e", "nav": "rgba(255,245,245,0.8)", "shadow": "0 12px 30px rgba(232,180,184,0.1)", "radius": "24px", "border": "1px solid rgba(232,180,184,0.2)"},
    "10. Tech Hardware (Neon Dark)": {"bg": "#0d1117", "txt": "#c9d1d9", "card": "#161b22", "p": "#58a6ff", "s": "#238636", "nav": "rgba(13,17,23,0.8)", "shadow": "0 0 20px rgba(88,166,255,0.05), inset 0 1px 0 rgba(255,255,255,0.1)", "radius": "16px", "border": "1px solid rgba(255,255,255,0.05)"},

    # --- HEALTH & CLINICS ---
    "11. Medical Platinum (Trust)": {"bg": "#ffffff", "txt": "#1e293b", "card": "#f8fafc", "p": "#0284c7", "s": "#059669", "nav": "rgba(255,255,255,0.8)", "shadow": "0 4px 15px rgba(0,0,0,0.03)", "radius": "16px", "border": "1px solid rgba(226,232,240,0.8)"},
    "12. Dental Aqua (Clean)": {"bg": "#f0fdfa", "txt": "#0f172a", "card": "#ffffff", "p": "#0d9488", "s": "#0284c7", "nav": "rgba(240,253,250,0.8)", "shadow": "0 10px 25px rgba(13,148,136,0.05)", "radius": "20px", "border": "1px solid rgba(204,251,241,0.8)"},
    "13. Fitness Aggressive (Gym)": {"bg": "#0a0a0a", "txt": "#ffffff", "card": "#171717", "p": "#e11d48", "s": "#facc15", "nav": "rgba(10,10,10,0.8)", "shadow": "0 10px 40px rgba(225,29,72,0.15)", "radius": "12px", "border": "1px solid rgba(255,255,255,0.05)"},
    "14. Spa Therapy (Calm)": {"bg": "#faf5f0", "txt": "#4a443c", "card": "#ffffff", "p": "#bfa58a", "s": "#8c735a", "nav": "rgba(250,245,240,0.8)", "shadow": "0 8px 30px rgba(191,165,138,0.08)", "radius": "28px", "border": "1px solid rgba(191,165,138,0.2)"},
    "15. Yoga Mindfulness": {"bg": "#fdf8f5", "txt": "#333333", "card": "#ffffff", "p": "#d4a373", "s": "#a1c181", "nav": "rgba(253,248,245,0.8)", "shadow": "0 10px 40px rgba(0,0,0,0.03)", "radius": "40px", "border": "1px solid rgba(0,0,0,0.02)"},

    # --- CORPORATE & REAL ESTATE ---
    "16. Law Firm Heritage": {"bg": "#ffffff", "txt": "#1f2937", "card": "#f9fafb", "p": "#1e3a8a", "s": "#b45309", "nav": "rgba(255,255,255,0.9)", "shadow": "0 10px 25px rgba(0,0,0,0.04)", "radius": "8px", "border": "1px solid rgba(229,231,235,0.8)"},
    "17. Real Estate Prime": {"bg": "#111827", "txt": "#f3f4f6", "card": "#1f2937", "p": "#fbbf24", "s": "#f9fafb", "nav": "rgba(17,24,39,0.8)", "shadow": "0 20px 40px rgba(0,0,0,0.2)", "radius": "16px", "border": "1px solid rgba(255,255,255,0.05)"},
    "18. Construction Industrial": {"bg": "#f5f5f5", "txt": "#1a1a1a", "card": "#ffffff", "p": "#f59e0b", "s": "#000000", "nav": "rgba(245,245,245,0.9)", "shadow": "8px 8px 0px rgba(0,0,0,0.1)", "radius": "0px", "border": "2px solid #000000"},
    "19. Architecture Grid": {"bg": "#ffffff", "txt": "#000000", "card": "#f4f4f5", "p": "#000000", "s": "#3b82f6", "nav": "rgba(255,255,255,0.9)", "shadow": "none", "radius": "0px", "border": "1px solid rgba(0,0,0,0.1)"},
    "20. Agency Bold (Creative)": {"bg": "#4f46e5", "txt": "#ffffff", "card": "#4338ca", "p": "#f9a8d4", "s": "#fde047", "nav": "rgba(79,70,229,0.8)", "shadow": "0 20px 50px rgba(0,0,0,0.2)", "radius": "24px", "border": "1px solid rgba(255,255,255,0.1)"},

    # --- CREATOR & EXOTIC ---
    "21. Cyberpunk 2077": {"bg": "#fcee0a", "txt": "#000000", "card": "#000000", "p": "#00ffff", "s": "#ff003c", "nav": "rgba(252,238,10,0.9)", "shadow": "8px 8px 0px #00ffff", "radius": "0px", "border": "2px solid #000000"},
    "22. Monochromatic Black/White": {"bg": "#ffffff", "txt": "#000000", "card": "#ffffff", "p": "#000000", "s": "#000000", "nav": "rgba(255,255,255,0.9)", "shadow": "6px 6px 0px #000000", "radius": "0px", "border": "2px solid #000000"},
    "23. Retro Synthwave": {"bg": "#2b213a", "txt": "#e0d6eb", "card": "#181425", "p": "#ff007f", "s": "#00f0ff", "nav": "rgba(43,33,58,0.8)", "shadow": "0 0 20px rgba(255,0,127,0.3)", "radius": "12px", "border": "1px solid rgba(255,0,127,0.5)"},
    "24. Gradient Mesh": {"bg": "linear-gradient(45deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%)", "txt": "#333", "card": "rgba(255,255,255,0.4)", "p": "#f77062", "s": "#3f51b5", "nav": "rgba(255,255,255,0.3)", "shadow": "0 8px 32px rgba(0,0,0,0.1)", "radius": "32px", "border": "1px solid rgba(255,255,255,0.5)"},
    "25. Midnight Ocean": {"bg": "#0f2027", "txt": "#d1d5db", "card": "#203a43", "p": "#2c5364", "s": "#38ef7d", "nav": "rgba(15,32,39,0.8)", "shadow": "0 20px 40px rgba(0,0,0,0.4)", "radius": "20px", "border": "1px solid rgba(44,83,100,0.5)"}
}

def generate_modern_css(theme_name, h_font, b_font, hero_align, h_color, b_color, h1_size, p_size, cta_bg, cta_txt):
    t = THEME_REGISTRY.get(theme_name, THEME_REGISTRY["1. Stripe Cloud (Modern SaaS)"])
    
    # Advanced Text Rendering & Gradients
    gradient_text = ""
    if any(x in theme_name for x in ["SaaS", "Dark", "Creative", "Glassmorphism", "Gradient"]):
        gradient_text = f"background: linear-gradient(135deg, {t['p']}, {t['s']}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-size: 200% 200%; animation: gradientShift 5s ease infinite;"

    # Physics-Based Hover States
    btn_hover = "transform: translateY(-4px) scale(1.02); filter: brightness(1.1); box-shadow: 0 15px 30px -5px var(--p), 0 0 15px rgba(255,255,255,0.2) inset;"
    if any(x in theme_name for x in ["Brutalist", "Cyberpunk", "Monochromatic"]):
        btn_hover = "transform: translate(-4px, -4px); box-shadow: 8px 8px 0px #000;"

    # Supreme Glassmorphism handling
    backdrop = "backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);" 

    # Hero Alignment
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
        --easing: cubic-bezier(0.16, 1, 0.3, 1); /* Apple-esque spring physics */
    }}
    
    /* RESET & SUB-PIXEL RENDERING */
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ 
        scroll-behavior: smooth; 
        font-size: 16px; 
        width: 100%; 
        overflow-x: hidden; 
        text-rendering: optimizeLegibility;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }}
    
    /* CUSTOM PREMIUM SCROLLBAR */
    ::-webkit-scrollbar {{ width: 10px; }}
    ::-webkit-scrollbar-track {{ background: var(--bg); }}
    ::-webkit-scrollbar-thumb {{ background: var(--p); border-radius: 10px; border: 2px solid var(--bg); }}
    ::-webkit-scrollbar-thumb:hover {{ background: var(--s); }}

    /* TEXT SELECTION GLOW */
    ::selection {{ background: var(--p); color: #fff; text-shadow: none; }}
    
    body {{ 
        background: var(--bg); color: var(--txt-b); font-family: var(--b-font); 
        font-size: var(--p-size); line-height: 1.7; overflow-x: hidden; width: 100%;
    }}
    
    h1, h2, h3, h4 {{ font-family: var(--h-font); color: var(--txt-h); line-height: 1.1; font-weight: 800; letter-spacing: -0.03em; }}
    h1 {{ font-size: var(--h1-size); {gradient_text} }}
    h2 {{ font-size: clamp(2rem, 5vw, 3rem); }}
    
    /* ANIMATIONS */
    @keyframes gradientShift {{ 0% {{ background-position: 0% 50%; }} 50% {{ background-position: 100% 50%; }} 100% {{ background-position: 0% 50%; }} }}
    @keyframes float {{ 0% {{ transform: translateY(0px); }} 50% {{ transform: translateY(-15px); }} 100% {{ transform: translateY(0px); }} }}
    @keyframes pulseGlow {{ 0% {{ box-shadow: 0 0 0 0 rgba(var(--p), 0.4); }} 70% {{ box-shadow: 0 0 0 20px rgba(var(--p), 0); }} 100% {{ box-shadow: 0 0 0 0 rgba(var(--p), 0); }} }}

    /* 2026 FLUID LAYOUT SYSTEM */
    .container {{ width: min(1300px, 92%); margin: 0 auto; }}
    main section {{ padding: clamp(4rem, 10vw, 8rem) 0; width: 100%; position: relative; }}
    
    /* ULTRA-PREMIUM NAVIGATION */
    nav#main-navbar {{ 
        position: fixed; top: 0; width: 100%; z-index: 1000; 
        background: var(--nav); {backdrop}
        border-bottom: var(--border); padding: 1rem 0; 
        transition: all 0.4s var(--easing);
    }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    .nav-links {{ display: flex; align-items: center; gap: 2.5rem; }}
    .nav-links a {{ 
        text-decoration: none; font-weight: 600; color: var(--txt-b); 
        font-size: 0.95rem; transition: color 0.3s ease; position: relative; 
    }}
    .nav-links a::after {{ 
        content: ''; position: absolute; width: 0; height: 2px; 
        bottom: -4px; left: 0; background-color: var(--p); 
        transition: width 0.3s var(--easing); border-radius: 2px;
    }}
    .nav-links a:hover::after {{ width: 100%; }}
    .nav-links a:hover {{ color: var(--p); }}
    
    @media (max-width: 992px) {{
        .nav-links {{ 
            position: fixed; top: 0; right: -100%; width: 85%; height: 100vh; 
            background: var(--card); flex-direction: column; padding: 6rem 2rem; 
            transition: 0.5s var(--easing); box-shadow: -20px 0 50px rgba(0,0,0,0.1); 
            z-index: 1001; align-items: flex-start; {backdrop}
        }}
        .nav-links.active {{ right: 0; }}
        .mobile-menu {{ display: block !important; font-size: 2rem; cursor: pointer; color: var(--txt-h); z-index: 1002; transition: transform 0.3s ease; }}
        .mobile-menu:active {{ transform: scale(0.9); }}
        .nav-links a {{ font-size: 1.5rem; }}
        .modern-hero-grid {{ grid-template-columns: 1fr !important; text-align: center; gap: 3rem; }}
        .modern-hero-visual {{ height: 450px !important; }}
        .stats-ribbon {{ flex-direction: column; gap: 2.5rem; }}
        .stat-divider {{ width: 60px !important; height: 2px !important; }}
        .about-grid, .detail-view, .contact-grid {{ grid-template-columns: 1fr !important; gap: 3rem; }}
        .detail-view {{ padding: 2rem !important; }}
        .product-media-column {{ position: relative !important; top: 0 !important; }}
    }}

    /* CINEMATIC HERO COMPONENT */
    .modern-hero {{ min-height: 100vh; display: flex; align-items: center; padding-top: 100px; position: relative; }}
    .modern-hero::before {{
        content: ''; position: absolute; top: -10%; left: -10%; width: 120%; height: 120%;
        background: radial-gradient(circle at 50% 50%, rgba(128,128,128,0.03) 0%, transparent 60%);
        z-index: -1; animation: float 10s ease-in-out infinite alternate; pointer-events: none;
    }}
    .modern-hero-grid {{ display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 4rem; align-items: center; }}
    
    .visual-frame {{ 
        border-radius: 32px; overflow: hidden; height: 100%; 
        box-shadow: 0 30px 60px rgba(0,0,0,0.15), inset 0 0 0 1px rgba(255,255,255,0.2); 
        border: var(--border); background: var(--card);
        transform: perspective(1000px) rotateY(-5deg); transition: transform 0.6s var(--easing);
    }}
    .visual-frame:hover {{ transform: perspective(1000px) rotateY(0deg) translateY(-10px); }}
    
    .hero-badge {{ 
        display: inline-flex; align-items: center; gap: 8px; padding: 0.6rem 1.2rem; 
        background: rgba(128,128,128,0.08); border: var(--border); border-radius: 50px; 
        font-size: 0.85rem; font-weight: 700; margin-bottom: 2rem; color: var(--txt-b); 
        text-transform: uppercase; letter-spacing: 1.5px; {backdrop}
    }}
    
    /* FLOATING GLASS STATS RIBBON */
    .stats-ribbon-container {{ margin-top: -80px; position: relative; z-index: 10; }}
    .stats-ribbon {{ 
        background: var(--card); border-radius: 32px; padding: clamp(2rem, 5vw, 4rem); 
        display: flex; justify-content: space-around; align-items: center; 
        box-shadow: 0 20px 40px rgba(0,0,0,0.08), inset 0 0 0 1px rgba(255,255,255,0.1); 
        border: var(--border); {backdrop} 
        transform: translateY(0); transition: transform 0.4s var(--easing);
    }}
    .stats-ribbon:hover {{ transform: translateY(-5px); }}
    .stat-block h3 {{ font-size: clamp(2.5rem, 6vw, 4rem); color: var(--p); text-shadow: 0 10px 20px rgba(0,0,0,0.1); }}
    .stat-divider {{ width: 2px; height: 60px; background: linear-gradient(to bottom, transparent, rgba(128,128,128,0.2), transparent); }}

    /* PHYSICS-BASED CARDS (BENTO GRID) */
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 340px), 1fr)); gap: 2.5rem; }}
    .card {{ 
        background: var(--card); border-radius: var(--radius); border: var(--border); 
        box-shadow: var(--shadow); transition: all 0.5s var(--easing); 
        overflow: hidden; height: 100%; display: flex; flex-direction: column;
        position: relative; z-index: 1; {backdrop}
    }}
    /* Inner Glow for Premium Depth */
    .card::after {{
        content: ''; position: absolute; inset: 0; border-radius: inherit;
        box-shadow: inset 0 0 0 1px rgba(255,255,255,0.1); pointer-events: none; z-index: 2;
    }}
    .card:hover {{ 
        transform: translateY(-12px) scale(1.01); 
        box-shadow: 0 30px 60px -10px rgba(0,0,0,0.15), var(--shadow); 
    }}
    .prod-img {{ width: 100%; aspect-ratio: 4/3; object-fit: cover; transition: transform 0.8s var(--easing); }}
    .card:hover .prod-img {{ transform: scale(1.05); }}
    .card-body {{ padding: 2.5rem; flex-grow: 1; display: flex; flex-direction: column; position: relative; z-index: 3; }}

    /* PRODUCT DETAIL VIEW (Premium Refactor) */
    .detail-view {{ 
        display: grid; grid-template-columns: 0.9fr 1.1fr; gap: clamp(3rem, 8vw, 6rem); 
        background: var(--card); padding: clamp(3rem, 5vw, 5rem); border-radius: 40px; 
        box-shadow: 0 40px 80px rgba(0,0,0,0.1), inset 0 0 0 1px rgba(255,255,255,0.1); 
        border: var(--border); {backdrop}
    }}
    .product-media-column {{ position: sticky; top: 140px; }}
    .product-price-tag {{ 
        display: inline-block; padding: 0.8rem 2rem; background: rgba(5, 150, 105, 0.1); 
        color: #059669; font-size: 2.2rem; font-weight: 900; border-radius: 50px; 
        margin: 1.5rem 0; border: 1px solid rgba(5,150,105,0.2);
    }}

    /* TACTILE MAGNETIC BUTTONS */
    .btn {{ 
        padding: 1.2rem 2.5rem; border-radius: var(--radius); font-weight: 800; 
        text-decoration: none; transition: all 0.4s var(--easing); 
        display: inline-flex; align-items: center; justify-content: center;
        border: none; cursor: pointer; text-transform: uppercase; letter-spacing: 1.5px;
        position: relative; overflow: hidden; z-index: 1;
    }}
    .btn::before {{
        content: ''; position: absolute; inset: 0; background: rgba(255,255,255,0.1);
        opacity: 0; transition: opacity 0.4s ease; z-index: -1;
    }}
    .btn:hover::before {{ opacity: 1; }}
    .btn-primary {{ background: var(--p); color: #fff !important; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }}
    .btn-accent {{ background: var(--s); color: #fff !important; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }}
    .btn:hover {{ {btn_hover} }}

    /* FLOATING WIDGETS (Sleek Glassmorphism) */
    #wa-widget, #theme-toggle, #cart-float, #voice-btn {{ 
        position: fixed; z-index: 900; {backdrop}
        box-shadow: 0 10px 30px rgba(0,0,0,0.15), inset 0 0 0 1px rgba(255,255,255,0.2);
        transition: transform 0.4s var(--easing), box-shadow 0.4s ease;
    }}
    #wa-widget:hover, #theme-toggle:hover, #cart-float:hover, #voice-btn:hover {{
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 20px 40px rgba(0,0,0,0.2), inset 0 0 0 1px rgba(255,255,255,0.3);
    }}
    #wa-widget {{ bottom: 30px; right: 30px; }}
    #theme-toggle {{ bottom: 30px; left: 30px; }}
    #cart-float {{ bottom: 110px; right: 30px; }}
    #voice-btn {{ bottom: 190px; right: 30px; }}

    @media (max-width: 600px) {{
        #cart-float, #voice-btn {{ right: 15px; transform: scale(0.85); transform-origin: bottom right; }}
        #wa-widget {{ right: 15px; bottom: 20px; }}
        #theme-toggle {{ left: 15px; bottom: 20px; transform: scale(0.85); transform-origin: bottom left; }}
        .nav-flex {{ padding: 0 10px; }}
    }}

    /* STAGGERED REVEAL PHYSICS */
    .reveal {{ 
        opacity: 0; transform: translateY(40px) scale(0.98); 
        transition: all 1s var(--easing); filter: blur(5px);
    }}
    .reveal.active {{ opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }}
    
    /* MODERN FOOTER */
    footer {{ 
        background: #0f172a; color: #fff; padding: 6rem 0 2rem 0; 
        position: relative; overflow: hidden;
    }}
    footer::before {{
        content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 2px;
        background: linear-gradient(90deg, transparent, var(--p), var(--s), transparent);
    }}
    .footer-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 4rem; }}
    footer a {{ color: #94a3b8 !important; text-decoration: none; margin-bottom: 0.8rem; display: block; transition: all 0.3s var(--easing); }}
    footer a:hover {{ color: #fff !important; transform: translateX(8px); }}
    """
