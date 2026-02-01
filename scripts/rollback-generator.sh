#!/bin/bash
# 🛡️ Rollback Generator - Creates rollback plans for features
# Usage: ./rollback-generator.sh "Feature Name" "Flag Name"

FEATURE_NAME="${1:-Unnamed Feature}"
FLAG_NAME="${2:-FEATURE_FLAG}"
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
LAST_COMMIT=$(git log -1 --format="%H" 2>/dev/null || echo "unknown")

cat << EOF
# 🔙 Rollback Plan: ${FEATURE_NAME}

**Generated:** ${TIMESTAMP}  
**Branch:** ${BRANCH}  
**Last Commit:** ${LAST_COMMIT}

---

## ⚡ Quick Rollback (Feature Flag)

Disable the feature instantly without code changes:

\`\`\`yaml
# In feature-flags.yml
${FLAG_NAME}:
  enabled: false
  rollout_percentage: 0
\`\`\`

---

## 🔧 Code Rollback (If Flag Fails)

\`\`\`bash
# Option 1: Revert the commit
git revert ${LAST_COMMIT} --no-commit
git commit -m "🔙 Rollback: ${FEATURE_NAME}"
git push origin ${BRANCH}

# Option 2: Reset to previous state
git reset --hard HEAD~1
git push origin ${BRANCH} --force  # ⚠️ DANGEROUS
\`\`\`

---

## 📊 Verification Checklist

After rollback, confirm:

- [ ] Error rates returned to baseline
- [ ] Feature is no longer visible to users
- [ ] No data corruption occurred
- [ ] Dependent systems are stable

---

## 📝 Post-Mortem Template

| Item | Details |
|------|---------|
| **What broke** | [Description] |
| **When detected** | [Timestamp] |
| **Time to rollback** | [Duration] |
| **Root cause** | [Analysis] |
| **Prevention** | [Action items] |

EOF
