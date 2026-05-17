import os, glob

new_footer = """    <footer class="modern-footer">
        <div class="container footer-content">
            <div class="footer-brand">
                <div class="logo">nakache<span>.app</span></div>
                <p>פיתוח יישומים מדויקים לחיים דיגיטליים חכמים יותר.</p>
            </div>
            <div class="footer-links">
                <h3>צור קשר</h3>
                <a href="mailto:doronenakache@example.com"><i class="fa-solid fa-envelope"></i> doronenakache@example.com</a>
                <div class="social-links">
                    <a href="#"><i class="fa-brands fa-linkedin"></i></a>
                    <a href="#"><i class="fa-brands fa-github"></i></a>
                    <a href="#"><i class="fa-brands fa-twitter"></i></a>
                </div>
            </div>
        </div>
        <div class="footer-bottom text-center">
            <p>&copy; 2026 Nakache.app - כל הזכויות שמורות. פותח עם ❤️ על ידי דורון נקש.</p>
        </div>
    </footer>
</body>"""

for file_path in glob.glob("*.html"):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace existing footer setup
    import re
    if "<footer" in content:
        content = re.sub(r'<footer.*?</body>', new_footer, content, flags=re.DOTALL)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

