$path = "c:\Users\danie\OneDrive\Documentos\landing page escoteiro\esct_presentation.html"
$content = [System.IO.File]::ReadAllText($path)
$css = @"
/* ── RESPONSIVIDADE DESKTOP ── */
@media (min-width: 1024px) {
  #nav {
    max-width: 1200px;
    padding: 24px 40px;
  }
  .nav-logo {
    font-size: 18px;
    letter-spacing: 4px;
  }
  .nav-badge {
    font-size: 13px;
    padding: 6px 16px;
  }
  .section {
    max-width: 1100px;
    padding: 100px 40px;
  }
  #hero h1 {
    font-size: 4rem;
  }
  .hero-sub {
    font-size: 1.2rem;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
  }
  .stats-grid {
    max-width: 900px;
    gap: 40px;
  }
  .stat-num {
    font-size: 36px;
  }
  .opp-cards {
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
  }
  .opp-card {
    width: calc(50% - 14px);
  }
  .utility-grid {
    grid-template-columns: repeat(4, 1fr);
    max-width: 1000px;
    margin-left: auto;
    margin-right: auto;
  }
  .profile-cols {
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
  }
  #disclaimer {
    max-width: 1100px;
  }
}
"@

if ($content.Contains('</style>')) {
    $newContent = $content.Replace('</style>', $css + "`n</style>")
    [System.IO.File]::WriteAllText($path, $newContent)
    Write-Host "File updated successfully."
} else {
    Write-Error "Could not find closing style tag."
}
