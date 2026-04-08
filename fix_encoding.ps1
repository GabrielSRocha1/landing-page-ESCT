$path = "c:\Users\danie\OneDrive\Documentos\landing page escoteiro\index.html"
$utf8NoBOM = New-Object System.Text.UTF8Encoding $False
$content = [IO.File]::ReadAllText($path, $utf8NoBOM)

# Replace broken characters with HTML entities or correct UTF8
# The '?' might have been inserted by previous failed attempts, so we replace those too if they appear in the eyebrow
$content = $content -replace '<p class="hero-eyebrow">\? Verum Crypto Ecosystem \?</p>', '<p class="hero-eyebrow">&#10022; Verum Crypto Ecosystem &#10022;</p>'
$content = $content.Replace('âœ¦', '&#10022;')
$content = $content.Replace('â—†', '&#9670;')
$content = $content.Replace('â”€', '&#9472;')

[IO.File]::WriteAllText($path, $content, $utf8NoBOM)
