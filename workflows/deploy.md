---
description: Deploy to Vercel with automated quality and security checks
---

# /deploy - Production Deployment

Use this workflow to deploy the current project to production.

## Automated Execution Steps

1. **Quality Assurance Check**
   - TypeScript: 0 errors required
   - ESLint: 0 errors required
   - Build: Must complete successfully

2. **Security Verification**
   - No exposed secrets in code or staging
   - Environment variables validated

3. **Deployment Execution**

   ```bash
   // turbo
   vercel --prod
   ```

4. **Result Reporting**
   - ✅ Deployment successful + Production URL
   - ❌ Deployment failed + Actionable fix recommendations

## Usage Context

- Completing a feature and deploying to production.
- Releasing a hotfix or bug fix.
- Deploying a stable version for stakeholder review.

## Usage Example

USER: `/deploy`

AGENT:

```text
🚀 Initiating Vercel deployment...

✅ TypeScript: 0 errors
✅ ESLint: 0 errors
✅ Build: Successful
✅ Deploy: Completed

🔗 URL: https://your-project.vercel.app
```
