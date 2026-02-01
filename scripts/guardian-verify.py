#!/usr/bin/env python3
"""
🛡️ Guardian Verify - Wrapper for safe-feature verify
Ensures all feature flags in code are defined in config.
"""
import subprocess
import sys
import os

def main():
    src_path = sys.argv[1] if len(sys.argv) > 1 else "./src"
    config_path = sys.argv[2] if len(sys.argv) > 2 else "./feature-flags.yml"
    
    print("🛡️ THE GUARDIAN: Feature Flag Verification")
    print("=" * 50)
    print(f"Scanning: {src_path}")
    print(f"Config: {config_path}")
    print()
    
    # Find safe-feature.py
    script_paths = [
        "scripts/safe-feature.py",
        ".agent/skills/safe-feature-addition/scripts/safe-feature.py",
    ]
    
    script = None
    for path in script_paths:
        if os.path.exists(path):
            script = path
            break
    
    if not script:
        print("⚠️ Could not find safe-feature.py")
        sys.exit(1)
    
    # Run verification
    result = subprocess.run(
        ["python", script, "verify", "--path", src_path, "--config", config_path],
        capture_output=False
    )
    
    print()
    print("=" * 50)
    
    if result.returncode == 0:
        print("✅ All feature flags are properly configured")
    else:
        print("❌ Feature flag mismatch detected - Fix before deploy")
    
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
