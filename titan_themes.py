<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Titan Furniture | Modern Minimalist Living</title>
    <meta name="description" content="Discover modern, minimalist luxury furniture for your home. Elevate your living space with Titan Furniture.">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">
    
    <!-- Boxicons for elegant icons -->
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>

    <style>
        /* CSS Reset & Variables */
        :root {
            --primary-color: #2c3e50; /* Deep navy/charcoal */
            --accent-color: #d4a373;  /* Warm wood/camel tone */
            --bg-color: #fcfcfc;      /* Off-white */
            --surface-color: #ffffff; /* Pure white */
            --text-primary: #1a1a1a;
            --text-secondary: #666666;
            --border-color: #eaeaea;
            --whatsapp-green: #25D366;
            
            --font-sans: 'Inter', sans-serif;
            --font-serif: 'Playfair Display', serif;
            
            --spacing-xs: 0.5rem;
            --spacing-sm: 1rem;
            --spacing-md: 2rem;
            --spacing-lg: 4rem;
            --spacing-xl: 6rem;
            
            --radius-md: 8px;
            --radius-lg: 16px;
            
            --shadow-sm: 0 2px 8px rgba(0,0,0,0.05);
            --shadow-md: 0 8px 24px rgba(0,0,0,0.08);
            
            --transition: all 0.3s ease;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: var(--font-sans);
            color: var(--text-primary);
            background-color: var(--bg-color);
            line-height: 1.6;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        /* Typography */
        h1, h2, h3, h4 {
            font-family: var(--font-serif);
            color: var(--primary-color);
            line-height: 1.2;
            margin-bottom: var(--spacing-sm);
        }

        h1 { font-size: clamp(2.5rem, 5vw, 4rem); }
        h2 { font-size: clamp(2rem, 4vw, 3rem); }
        h3 { font-size: clamp(1.5rem, 2vw, 2rem); font-family: var(--font-sans); font-weight: 600; }
        
        p { margin-bottom: var(--spacing-sm); color: var(--text-secondary); }
        
        a { text-decoration: none; color: inherit; transition: var(--transition); }

        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 var(--spacing-md);
        }

        .section {
            padding: var(--spacing-xl) 0;
        }

        .text-center { text-align: center; }
        
        /* Buttons */
        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 0.8rem 1.8rem;
            font-size: 1rem;
            font-weight: 500;
            border-radius: var(--radius-md);
            cursor: pointer;
            transition: var(--transition);
            border: none;
            font-family: var(--font-sans);
        }

        .btn-primary {
            background-color: var(--primary-color);
            color: white;
        }

        .btn-primary:hover {
            background-color: #1a252f;
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }

        .btn-accent {
            background-color: var(--accent-color);
            color: white;
        }
        
        .btn-accent:hover {
            background-color: #bc8f5f;
            transform: translateY(-2px);
        }

        .btn-outline {
            background-color: transparent;
            border: 1px solid var(--primary-color);
            color: var(--primary-color);
        }

        .btn-outline:hover {
            background-color: var(--primary-color);
            color: white;
        }

        /* Promo Banner */
        .promo-banner {
            background-color: var(--accent-color);
            color: white;
            text-align: center;
            padding: 0.5rem;
            font-size: 0.85rem;
            font-weight: 500;
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }
        
        .promo-banner i { font-size: 1.2rem; }

        /* Header & Navigation */
        .header {
            background-color: var(--surface-color);
            position: sticky;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid var(--border-color);
            transition: var(--transition);
        }

        .header.scrolled {
            box-shadow: var(--shadow-sm);
        }

        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 70px;
        }

        .logo {
            font-family: var(--font-serif);
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--primary-color);
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .logo i { color: var(--accent-color); }

        .nav-links {
            display: flex;
            gap: var(--spacing-md);
            align-items: center;
        }

        .nav-link {
            font-weight: 500;
            font-size: 0.95rem;
            position: relative;
        }

        .nav-link::after {
            content: '';
            position: absolute;
            width: 0;
            height: 2px;
            bottom: -4px;
            left: 0;
            background-color: var(--accent-color);
            transition: var(--transition);
        }

        .nav-link:hover::after { width: 100%; }

        .mobile-menu-btn {
            display: none;
            background: none;
            border: none;
            font-size: 1.8rem;
            color: var(--primary-color);
            cursor: pointer;
        }

        /* Hero Section */
        .hero {
            position: relative;
            padding: 0;
            height: calc(100vh - 100px); /* Adjust based on header+banner */
            min-height: 500px;
            display: flex;
            align-items: center;
            background-color: #f0ede6; /* fallback */
            overflow: hidden;
        }

        .hero-bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: 1;
        }

        .hero-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(to right, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.7) 50%, transparent 100%);
            z-index: 2;
        }

        .hero-content {
            position: relative;
            z-index: 3;
            max-width: 600px;
        }

        .hero p {
            font-size: 1.1rem;
            margin-bottom: var(--spacing-md);
            color: #4a4a4a;
        }

        .hero-btns {
            display: flex;
            gap: var(--spacing-sm);
        }

        /* Featured Categories / Services */
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: var(--spacing-md);
            margin-top: var(--spacing-md);
        }

        .feature-card {
            background: var(--surface-color);
            padding: var(--spacing-md);
            border-radius: var(--radius-lg);
            text-align: center;
            border: 1px solid var(--border-color);
            transition: var(--transition);
        }

        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-md);
            border-color: var(--accent-color);
        }

        .feature-icon {
            width: 60px;
            height: 60px;
            background-color: rgba(212, 163, 115, 0.1);
            color: var(--accent-color);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.8rem;
            margin: 0 auto var(--spacing-sm);
        }

        /* Products Section */
        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: var(--spacing-md);
            margin-top: var(--spacing-md);
        }

        .product-card {
            background: var(--surface-color);
            border-radius: var(--radius-md);
            overflow: hidden;
            box-shadow: var(--shadow-sm);
            transition: var(--transition);
            display: flex;
            flex-direction: column;
        }

        .product-card:hover {
            box-shadow: var(--shadow-md);
            transform: translateY(-5px);
        }

        .product-img-wrapper {
            position: relative;
            padding-top: 100%; /* 1:1 Aspect Ratio */
            overflow: hidden;
            background-color: #f8f8f8;
        }

        .product-img {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }

        .product-card:hover .product-img {
            transform: scale(1.05);
        }

        .product-info {
            padding: var(--spacing-sm);
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }

        .product-title {
            font-size: 1.2rem;
            margin-bottom: 0.2rem;
        }

        .product-price {
            font-weight: 600;
            color: var(--accent-color);
            font-size: 1.1rem;
            margin-bottom: var(--spacing-sm);
        }

        .product-info p {
            font-size: 0.9rem;
            margin-bottom: var(--spacing-sm);
            flex-grow: 1;
        }

        /* About Section (Split layout) */
        .about-split {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: var(--spacing-lg);
            align-items: center;
        }

        .about-img {
            width: 100%;
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-md);
            object-fit: cover;
        }

        /* Testimonials */
        .bg-light { background-color: #f9f9f9; }
        
        .testimonial-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: var(--spacing-md);
            margin-top: var(--spacing-md);
        }

        .testimonial-card {
            background: var(--surface-color);
            padding: var(--spacing-md);
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-sm);
            position: relative;
        }

        .testimonial-card::before {
            content: '"';
            font-family: var(--font-serif);
            font-size: 4rem;
            color: rgba(212, 163, 115, 0.2);
            position: absolute;
            top: 10px;
            left: 20px;
            line-height: 1;
        }

        .testimonial-text {
            font-style: italic;
            margin-bottom: var(--spacing-sm);
            position: relative;
            z-index: 1;
        }

        .testimonial-author {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-top: auto;
        }

        .author-avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background-color: var(--accent-color);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
        }

        .author-info h4 {
            margin: 0;
            font-size: 1rem;
            font-family: var(--font-sans);
        }
        .author-info span { font-size: 0.8rem; color: var(--text-secondary); }

        /* Contact Section */
        .contact-grid {
            display: grid;
            grid-template-columns: 1fr 1.5fr;
            gap: var(--spacing-lg);
            background: var(--surface-color);
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-sm);
            overflow: hidden;
        }

        .contact-info {
            background-color: var(--primary-color);
            color: white;
            padding: var(--spacing-md);
        }

        .contact-info h2, .contact-info h3 { color: white; }
        .contact-info p { color: rgba(255,255,255,0.8); }
        
        .contact-item {
            display: flex;
            align-items: flex-start;
            gap: 15px;
            margin-bottom: var(--spacing-sm);
        }
        .contact-item i { font-size: 1.5rem; color: var(--accent-color); }

        .contact-form {
            padding: var(--spacing-md);
        }

        .form-group { margin-bottom: 1rem; }
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
            font-size: 0.9rem;
        }
        .form-control {
            width: 100%;
            padding: 0.8rem;
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            font-family: var(--font-sans);
            transition: var(--transition);
        }
        .form-control:focus {
            outline: none;
            border-color: var(--accent-color);
            box-shadow: 0 0 0 3px rgba(212, 163, 115, 0.1);
        }
        textarea.form-control { resize: vertical; min-height: 120px; }

        /* Footer */
        .footer {
            background-color: #1a1a1a;
            color: white;
            padding: var(--spacing-lg) 0 var(--spacing-sm);
        }

        .footer-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: var(--spacing-md);
            margin-bottom: var(--spacing-md);
        }

        .footer-col h3 {
            color: white;
            font-family: var(--font-sans);
            font-size: 1.2rem;
        }
        .footer-col p { color: #aaaaaa; }
        
        .footer-links { list-style: none; }
        .footer-links li { margin-bottom: 0.5rem; }
        .footer-links a { color: #aaaaaa; }
        .footer-links a:hover { color: var(--accent-color); }
        
        .social-links {
            display: flex;
            gap: 15px;
            margin-top: 1rem;
        }
        .social-links a {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background-color: rgba(255,255,255,0.1);
            transition: var(--transition);
        }
        .social-links a:hover {
            background-color: var(--accent-color);
            transform: translateY(-3px);
        }

        .footer-bottom {
            text-align: center;
            padding-top: var(--spacing-md);
            border-top: 1px solid rgba(255,255,255,0.1);
            color: #777;
            font-size: 0.9rem;
        }

        /* Floating WhatsApp Button */
        .whatsapp-float {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background-color: var(--whatsapp-green);
            color: white;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            box-shadow: var(--shadow-md);
            z-index: 999;
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .whatsapp-float:hover {
            transform: scale(1.1);
            color: white;
        }

        /* Mobile Optimization */
        @media (max-width: 768px) {
            .mobile-menu-btn { display: block; }
            
            .nav-links {
                position: fixed;
                top: 70px;
                left: -100%;
                width: 100%;
                height: calc(100vh - 70px);
                background-color: var(--surface-color);
                flex-direction: column;
                justify-content: flex-start;
                padding-top: var(--spacing-lg);
                gap: var(--spacing-md);
                transition: var(--transition);
                box-shadow: inset 0 5px 10px -10px rgba(0,0,0,0.1);
            }
            
            .nav-links.active { left: 0; }
            
            .nav-links a { font-size: 1.2rem; }
            .nav-links .btn { margin-top: var(--spacing-sm); }
            
            .hero-overlay {
                background: linear-gradient(to top, rgba(255,255,255,1) 0%, rgba(255,255,255,0.85) 60%, rgba(255,255,255,0.4) 100%);
                display: flex;
                align-items: flex-end;
                padding-bottom: var(--spacing-lg);
            }
            
            .hero-content {
                padding: var(--spacing-sm);
                text-align: center;
            }
            
            .hero-btns {
                flex-direction: column;
                width: 100%;
            }
            
            .about-split { grid-template-columns: 1fr; }
            .about-split .about-img { order: -1; } /* Image on top for mobile */
            
            .contact-grid { grid-template-columns: 1fr; }
            
            .whatsapp-float {
                bottom: 20px;
                right: 20px;
                width: 50px;
                height: 50px;
                font-size: 1.8rem;
            }
        }
    </style>
</head>
<body>

    <!-- Subtle Promo Banner -->
    <div class="promo-banner">
        <i class='bx bx-check-shield'></i> Free shipping on all domestic orders over $500 | New Spring Collection
    </div>

    <!-- Header Navigation -->
    <header class="header" id="header">
        <div class="container nav-container">
            <a href="#" class="logo">
                <i class='bx bxs-chair'></i> Titan Furniture
            </a>
            
            <nav class="nav-links" id="nav-links">
                <a href="#about" class="nav-link">Our Story</a>
                <a href="#collections" class="nav-link">Collections</a>
                <a href="#testimonials" class="nav-link">Reviews</a>
                <a href="#contact" class="btn btn-primary">Contact Us</a>
            </nav>

            <button class="mobile-menu-btn" id="menu-btn" aria-label="Toggle menu">
                <i class='bx bx-menu'></i>
            </button>
        </div>
    </header>

    <main>
        <!-- Hero Section -->
        <section class="hero">
            <img src="https://images.unsplash.com/photo-1586023492125-27b2c045efd7?q=80&w=1600&auto=format&fit=crop" alt="Modern minimalist living room" class="hero-bg" loading="eager">
            <div class="hero-overlay">
                <div class="container">
                    <div class="hero-content">
                        <h1>Design Your Sanctuary.</h1>
                        <p>Discover minimalist, expertly crafted furniture that transforms houses into homes. Elevate your everyday living with pieces built to last.</p>
                        <div class="hero-btns">
                            <a href="#collections" class="btn btn-primary">Shop Collections</a>
                            <a href="#about" class="btn btn-outline">Explore Craftsmanship</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Features / Value Prop -->
        <section class="section" id="features">
            <div class="container">
                <div class="text-center" style="margin-bottom: var(--spacing-md);">
                    <h2>The Titan Standard</h2>
                    <p>Why modern homes choose our craftsmanship.</p>
                </div>
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="feature-icon"><i class='bx bx-leaf'></i></div>
                        <h3>Sustainable Sourcing</h3>
                        <p>We use ethically harvested woods and eco-friendly materials to build pieces that respect the environment.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon"><i class='bx bx-pencil'></i></div>
                        <h3>Minimalist Design</h3>
                        <p>Clean lines and uncluttered aesthetics that create a sense of calm and space in any room.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon"><i class='bx bx-shield-quarter'></i></div>
                        <h3>Lifetime Guarantee</h3>
                        <p>True quality speaks for itself. We stand behind the structural integrity of our furniture for life.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- About Split Section -->
        <section class="section bg-light" id="about">
            <div class="container">
                <div class="about-split">
                    <div class="about-text">
                        <h2>Form Meets Function.</h2>
                        <p>Founded on the belief that luxury doesn't mean clutter, Titan Furniture brings European-inspired minimalist design to modern living spaces.</p>
                        <p>Every sofa, table, and chair is rigorously tested for ergonomics and durability. We don't just sell furniture; we provide the foundational elements for your home's daily rituals.</p>
                        <br>
                        <a href="#contact" class="btn btn-outline">Book a Consultation <i class='bx bx-right-arrow-alt' style="margin-left: 5px;"></i></a>
                    </div>
                    <img src="https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?q=80&w=800&auto=format&fit=crop" alt="Craftsman working on wood furniture" class="about-img" loading="lazy">
                </div>
            </div>
        </section>

        <!-- Products / Collections -->
        <section class="section" id="collections">
            <div class="container">
                <div class="text-center" style="margin-bottom: var(--spacing-md);">
                    <h2>Signature Pieces</h2>
                    <p>Curated selections for the contemporary home.</p>
                </div>
                
                <div class="product-grid">
                    <!-- Product 1 -->
                    <div class="product-card">
                        <div class="product-img-wrapper">
                            <img src="https://images.unsplash.com/photo-1555041469-a586c61ea9bc?q=80&w=600&auto=format&fit=crop" alt="The Oslo Accent Chair" class="product-img" loading="lazy">
                        </div>
                        <div class="product-info">
                            <h3 class="product-title">The Oslo Chair</h3>
                            <span class="product-price">$499</span>
                            <p>Linen blend upholstery with solid ash wood frame. Perfect for reading corners.</p>
                            <a href="#contact" class="btn btn-outline" style="width: 100%;">Inquire Availability</a>
                        </div>
                    </div>
                    
                    <!-- Product 2 -->
                    <div class="product-card">
                        <div class="product-img-wrapper">
                            <img src="https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?q=80&w=600&auto=format&fit=crop" alt="Minimalist platform bed" class="product-img" loading="lazy">
                        </div>
                        <div class="product-info">
                            <h3 class="product-title">Luna Platform Bed</h3>
                            <span class="product-price">$1,299</span>
                            <p>Low-profile walnut frame featuring an integrated headboard and slat support system.</p>
                            <a href="#contact" class="btn btn-outline" style="width: 100%;">Inquire Availability</a>
                        </div>
                    </div>

                    <!-- Product 3 -->
                    <div class="product-card">
                        <div class="product-img-wrapper">
                            <img src="https://images.unsplash.com/photo-1533090481720-856c6e3c1fdc?q=80&w=600&auto=format&fit=crop" alt="Marble coffee table" class="product-img" loading="lazy">
                        </div>
                        <div class="product-info">
                            <h3 class="product-title">Aura Coffee Table</h3>
                            <span class="product-price">$649</span>
                            <p>Carrara marble top resting on a powder-coated steel geometric base.</p>
                            <a href="#contact" class="btn btn-outline" style="width: 100%;">Inquire Availability</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Testimonials -->
        <section class="section bg-light" id="testimonials">
            <div class="container">
                <div class="text-center" style="margin-bottom: var(--spacing-md);">
                    <h2>Living with Titan</h2>
                    <p>Hear from clients who have transformed their spaces.</p>
                </div>
                
                <div class="testimonial-grid">
                    <div class="testimonial-card">
                        <p class="testimonial-text">"The quality is exceptional. The Oslo chair entirely changed the feel of our living room. Clean lines, incredibly comfortable, and clearly built to last."</p>
                        <div class="testimonial-author">
                            <div class="author-avatar">S</div>
                            <div class="author-info">
                                <h4>Sarah Jenkins</h4>
                                <span>Interior Designer</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="testimonial-card">
                        <p class="testimonial-text">"I ordered the Luna bed frame. The delivery was seamless, assembly was straightforward, and the minimalist design is exactly what I needed for my studio."</p>
                        <div class="testimonial-author">
                            <div class="author-avatar">M</div>
                            <div class="author-info">
                                <h4>Marcus T.</h4>
                                <span>Architect</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Contact Section -->
        <section class="section" id="contact">
            <div class="container">
                <div class="contact-grid">
                    <div class="contact-info">
                        <h2>Visit Our Showroom</h2>
                        <p style="margin-bottom: 2rem;">Experience the quality and comfort of our pieces in person. Our design consultants are ready to assist you.</p>
                        
                        <div class="contact-item">
                            <i class='bx bx-map'></i>
                            <div>
                                <h4>Location</h4>
                                <p>123 Design District, Suite 400<br>Metropolis, NY 10001</p>
                            </div>
                        </div>
                        
                        <div class="contact-item">
                            <i class='bx bx-phone'></i>
                            <div>
                                <h4>Call Us</h4>
                                <p>+1 (555) 123-4567</p>
                            </div>
                        </div>
                        
                        <div class="contact-item">
                            <i class='bx bx-time-five'></i>
                            <div>
                                <h4>Hours</h4>
                                <p>Mon-Sat: 10am - 7pm<br>Sun: By Appointment</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="contact-form">
                        <h3 style="margin-bottom: 1.5rem;">Send an Inquiry</h3>
                        <form onsubmit="event.preventDefault(); alert('Message sent successfully! (Demo)');">
                            <div class="form-group">
                                <label for="name">Full Name</label>
                                <input type="text" id="name" class="form-control" required placeholder="Jane Doe">
                            </div>
                            <div class="form-group">
                                <label for="email">Email Address</label>
                                <input type="email" id="email" class="form-control" required placeholder="jane@example.com">
                            </div>
                            <div class="form-group">
                                <label for="message">How can we help you?</label>
                                <textarea id="message" class="form-control" required placeholder="I'm interested in the Luna bed..."></textarea>
                            </div>
                            <button type="submit" class="btn btn-primary" style="width: 100%;">Send Message</button>
                        </form>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <div class="logo" style="color: white; margin-bottom: 1rem;">
                        <i class='bx bxs-chair' style="color: var(--accent-color);"></i> Titan
                    </div>
                    <p style="max-width: 250px;">Modern, minimalist furniture designed for everyday living and built to last a lifetime.</p>
                    <div class="social-links">
                        <a href="#" aria-label="Instagram"><i class='bx bxl-instagram'></i></a>
                        <a href="#" aria-label="Pinterest"><i class='bx bxl-pinterest-alt'></i></a>
                        <a href="#" aria-label="Facebook"><i class='bx bxl-facebook'></i></a>
                    </div>
                </div>
                
                <div class="footer-col">
                    <h3>Shop</h3>
                    <ul class="footer-links">
                        <li><a href="#collections">All Furniture</a></li>
                        <li><a href="#collections">Seating</a></li>
                        <li><a href="#collections">Tables</a></li>
                        <li><a href="#collections">Bedroom</a></li>
                    </ul>
                </div>
                
                <div class="footer-col">
                    <h3>Company</h3>
                    <ul class="footer-links">
                        <li><a href="#about">Our Story</a></li>
                        <li><a href="#">Sustainability</a></li>
                        <li><a href="#">Trade Program</a></li>
                        <li><a href="#contact">Contact</a></li>
                    </ul>
                </div>
                
                <div class="footer-col">
                    <h3>Legal</h3>
                    <ul class="footer-links">
                        <li><a href="#">Shipping & Returns</a></li>
                        <li><a href="#">Privacy Policy</a></li>
                        <li><a href="#">Terms of Service</a></li>
                        <li><a href="#">Warranty</a></li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; <span id="current-year"></span> Titan Furniture. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <!-- Floating WhatsApp Button -->
    <a href="https://wa.me/15551234567" target="_blank" rel="noopener noreferrer" class="whatsapp-float" aria-label="Chat with us on WhatsApp">
        <i class='bx bxl-whatsapp'></i>
    </a>

    <script>
        // Update copyright year
        document.getElementById('current-year').textContent = new Date().getFullYear();

        // Mobile Menu Toggle
        const menuBtn = document.getElementById('menu-btn');
        const navLinks = document.getElementById('nav-links');
        
        menuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = menuBtn.querySelector('i');
            if(navLinks.classList.contains('active')) {
                icon.classList.replace('bx-menu', 'bx-x');
            } else {
                icon.classList.replace('bx-x', 'bx-menu');
            }
        });

        // Close mobile menu when clicking a link
        document.querySelectorAll('.nav-link, .nav-links .btn').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                menuBtn.querySelector('i').classList.replace('bx-x', 'bx-menu');
            });
        });

        // Sticky Header Shadow on Scroll
        const header = document.getElementById('header');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 10) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    </script>
</body>
</html>
