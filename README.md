# Snapchat Saudi Ad Spec & Regulatory Compliance Linter

> Prevent Snapchat ad rejections in Saudi Arabia. Automatically verify video safe-zones, technical specs, and Mawthooq compliance.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: CLI_SCRIPT](https://img.shields.io/badge/Format-CLI--SCRIPT-green.svg)](#)
[![Tier: 2](https://img.shields.io/badge/Tier-2-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Build an open-source pre-flight validation toolkit for Snapchat Saudi advertising: 1) Python inspection script (`snap_spec_linter.py`) that checks video dimensions (1080x1920), duration, file size, audio presence, and text bounding-box safe-zone clearance, 2) SVG safe-zone overlays for Figma and Premiere Pro, 3) 20-point Saudi advertising legal compliance checklist (Mawthooq, pricing clarity, VAT transparency).

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `assets/safe_zone_overlay_1080x1920.svg`
- `checklists/saudi-advertising-compliance.md`
- `examples/sample_manifest.json`
- `LICENSE`
- `README.md`
- `src/snap_spec_linter.py`
- `tests/test_linter.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/snap_spec_linter.py --help
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "media-buying",
  "repository": "snapchat-saudi-ad-spec-linter",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Saudi Mawthooq Verification:** Commercial creator ads in KSA must display valid Mawthooq license numbers to avoid punitive ad account suspensions.
- **Snap Safe Zone Inset:** Vertical 9:16 videos must maintain top (150px) and bottom (250px) clear zones to prevent CTA button overlap.
- **Bitrate & File Size Compression:** Max file size of 32MB and H.264/AAC encoding constraints strictly enforced for fast loading on cellular networks.

---

## 📚 Primary Documentation & Verifiable References

- [Snap Ads Specifications & Video Guidelines](https://forbusiness.snapchat.com/ad-specs) - Official creative specifications, aspect ratios, and safe zone overlays.
- [Saudi General Authority for Media Regulation (GAMR)](https://gcam.gov.sa/) - Statutory advertising compliance rules and Mawthooq licensing requirements.
- [Snap Marketing API: Creative Validation](https://businessapi-docs.snapchat.com/) - Technical validation for automated asset uploads and dimensions.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
