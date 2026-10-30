#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

def lint_snap_ad(manifest_path):
    with open(manifest_path, "r", encoding="utf-8") as f:
        ad = json.load(f)

    issues = []
    width = ad.get("width", 0)
    height = ad.get("height", 0)
    duration = ad.get("duration_seconds", 0)
    cta_padding_bottom = ad.get("cta_padding_bottom_px", 0)
    top_padding = ad.get("top_padding_px", 0)
    has_saudi_mawthooq = ad.get("has_saudi_mawthooq_license", False)

    if (width, height) != (1080, 1920):
        issues.append(f"Invalid dimensions: {width}x{height}. Mandatory 1080x1920 (9:16).")
    if duration < 3 or duration > 180:
        issues.append(f"Invalid duration: {duration}s. Must be between 3s and 180s.")
    if cta_padding_bottom < 340:
        issues.append(f"Critical Safe Zone breach: Bottom padding {cta_padding_bottom}px is less than 340px bottom CTA buffer.")
    if top_padding < 175:
        issues.append(f"Critical Safe Zone breach: Top padding {top_padding}px is less than 175px profile header buffer.")
    if not has_saudi_mawthooq:
        issues.append("Saudi Regulatory Warning: Missing documented Mawthooq / commercial license disclosure.")

    return {
        "status": "FAIL" if any("Invalid" in i or "Critical" in i for i in issues) else "PASS",
        "total_issues": len(issues),
        "issues": issues
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--manifest", required=True)
    args = p.parse_args()

    res = lint_snap_ad(args.manifest)
    print(json.dumps(res, indent=2, ensure_ascii=False))
    sys.exit(0 if res["status"] == "PASS" else 1)

if __name__ == "__main__":
    main()
