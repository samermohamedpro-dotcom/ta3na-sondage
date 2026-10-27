#!/usr/bin/env python3
"""Fabrique index.html depuis modele.html : l'icône de l'app y entre en SVG,
pour que la page n'ait aucun fichier à côté. Ne jamais modifier index.html à la main."""
from pathlib import Path
from urllib.parse import quote
ICI = Path(__file__).resolve().parent
svg = (ICI / "../../../5-APP/assets/logo/ta3na-icone.svg").resolve().read_text(encoding="utf-8").strip()
page = (ICI / "modele.html").read_text(encoding="utf-8")
page = page.replace("%%ICONE_SVG%%", svg).replace("%%ICONE_URI%%", quote(svg))
(ICI / "index.html").write_text(page, encoding="utf-8")
print("index.html :", len(page), "octets")
