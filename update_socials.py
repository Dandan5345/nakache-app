import glob, re

new_socials = """                <div class="social-links">
                    <a href="https://www.linkedin.com/in/dorone-nakache-7566443bb?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app" target="_blank" title="LinkedIn"><i class="fa-brands fa-linkedin"></i></a>
                    <a href="https://www.instagram.com/nakache_app?igsh=NjYzMWd6a21tbWdm&utm_source=qr" target="_blank" title="Instagram"><i class="fa-brands fa-instagram"></i></a>
                    <a href="https://www.tiktok.com/@nakache_app?_r=1&_t=ZS-96RQYcjZCUe" target="_blank" title="TikTok"><i class="fa-brands fa-tiktok"></i></a>
                    <a href="https://wa.me/972500000000" target="_blank" title="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
                </div>"""

for html_file in glob.glob("*.html"):
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the existing social links block
    content = re.sub(
        r'<div class="social-links">.*?</div>',
        new_socials,
        content,
        flags=re.DOTALL
    )
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)

print("Social links updated!")
