import sys

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace variables with Aurora Mesh dark/vibrant theme
new_vars = """:root {
    --primary-color: #ffffff;
    --primary-hover: #f0f0f0;
    --secondary-color: #34c759;
    --text-color: #ffffff;
    --text-secondary: rgba(255, 255, 255, 0.7);
    --card-bg: rgba(255, 255, 255, 0.1);
    --card-border: rgba(255, 255, 255, 0.2);
    --shadow: 0 16px 40px rgba(0, 0, 0, 0.2);
    --shadow-hover: 0 25px 50px rgba(0, 0, 0, 0.3);
    --glass-blur: blur(30px);
}"""

if ":root {" in css:
    import re
    css = re.sub(r':root\s*\{[^}]*\}', new_vars, css)

# Replace body background
new_body = """body {
    font-family: 'Heebo', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: #0d0a21;
    background-image: 
        radial-gradient(circle at 15% 50%, rgba(105, 59, 219, 0.5), transparent 30%),
        radial-gradient(circle at 85% 30%, rgba(77, 212, 235, 0.5), transparent 30%),
        radial-gradient(circle at 50% 80%, rgba(214, 53, 140, 0.5), transparent 40%),
        radial-gradient(circle at 50% 0%, rgba(77, 63, 201, 0.4), transparent 40%);
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: var(--text-color);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    overflow-x: hidden;
}"""

css = re.sub(r'body\s*\{[^}]*\}', new_body, css)

# Fix blobs for Aurora
new_blobs = """.blob-1 {
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(131,58,180,0.6) 0%, rgba(253,29,29,0.4) 100%);
    top: -150px;
    left: -200px;
    animation-duration: 25s;
}

.blob-2 {
    width: 700px;
    height: 700px;
    background: radial-gradient(circle, rgba(46,196,182,0.5) 0%, rgba(36,25,178,0.4) 100%);
    bottom: -200px;
    right: -250px;
    animation-delay: -3s;
    animation-duration: 30s;
}"""

css = re.sub(r'\.blob-1\s*\{[^}]*\}', "", css)
css = re.sub(r'\.blob-2\s*\{[^}]*\}', "", css)
css = css + "\n" + new_blobs

# Adjust app-container background slightly and primary-btn
css = css.replace("background: rgba(255, 255, 255, 0.3);", "background: rgba(0, 0, 0, 0.15);")
css = css.replace("background-color: var(--primary-color);", "background-color: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); color: #fff;")
css = css.replace("color: white;", "")

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)
