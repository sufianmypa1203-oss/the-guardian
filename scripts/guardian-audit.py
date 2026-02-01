#!/usr/bin/env python3
"""
🛡️ Guardian Audit - Wrapper for safe-feature audit
Compares current branch against main for destructive patterns.
"""
import subprocess
import sys
import os

def main():
    base_branch = sys.argv[1] if len(sys.argv) > 1 else "main"
    
    print("🛡️ THE GUARDIAN: Audit Starting...")
    print("=" * 50)
    print(f"Comparing against: {base_branch}")
    print()
    
    # Find safe-feature.py in common locations
    script_paths = [
        "scripts/safe-feature.py",
        ".agent/skills/safe-feature-addition/scripts/safe-feature.py",
        "node_modules/.bin/safe-feature",
    ]
    
    script = None
    for path in script_paths:
        if os.path.exists(path):
            script = path
            break
    
    if not script:
        print("⚠️ Could not find safe-feature.py")
        print("Run: pip install safe-feature-addition")
        print("Or copy scripts from the skill folder.")
        sys.exit(1)
    
    # Run the audit
    result = subprocess.run(
        ["python", script, "audit", "--base", base_branch],
        capture_output=False
    )
    
    print()
    print("=" * 50)
    
    if result.returncode == 0:
        print("✅ AUDIT PASSED - Safe to proceed")
    else:
        print("❌ AUDIT FAILED - Fix issues before merge")
    
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
