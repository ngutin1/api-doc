# Setting Up Read the Docs

## Step 1: Create GitHub Repository

1. Go to GitHub and create a new repository named `ny-assembly-api-docs`
2. Clone this directory and push to GitHub:

```bash
cd ny-assembly-api-docs
git init
git add .
git commit -m "Initial documentation"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ny-assembly-api-docs.git
git push -u origin main
```

## Step 2: Set Up Read the Docs

1. Go to https://readthedocs.org/
2. Click "Sign Up" (or "Log In" if you have an account)
3. Sign up with your GitHub account
4. Click "Import a Project"
5. Find `ny-assembly-api-docs` in the list and click the "+" button
6. Configure:
   - **Name**: ny-assembly-api-docs
   - **Repository URL**: https://github.com/YOUR_USERNAME/ny-assembly-api-docs
   - **Default branch**: main
7. Click "Next"
8. Click "Build version"

## Step 3: Wait for Build

The documentation will build automatically. This takes 2-5 minutes.

You can watch the build process under "Builds" in the project dashboard.

## Step 4: View Your Documentation

Once built, your documentation will be available at:

```
https://ny-assembly-api-docs.readthedocs.io
```

## Step 5: Enable Automatic Builds

Read the Docs is already configured to automatically rebuild when you push to GitHub!

Every time you:
1. Push changes to the `main` branch
2. The documentation automatically rebuilds
3. Changes go live in 2-5 minutes

## Customization

### Change the URL

By default, your docs are at `ny-assembly-api-docs.readthedocs.io`

To use a custom domain:
1. Go to project settings in Read the Docs
2. Click "Domains"
3. Add your custom domain
4. Update your DNS records

### Add a Version Badge

Add this to your main API repository README:

```markdown
[![Documentation Status](https://readthedocs.org/projects/ny-assembly-api-docs/badge/?version=latest)](https://ny-assembly-api-docs.readthedocs.io/en/latest/?badge=latest)
```

## Troubleshooting

### Build Failed

Check the build log in Read the Docs dashboard.

Common issues:
- Missing dependencies in `requirements.txt`
- Syntax errors in `.rst` files
- Incorrect paths in `conf.py`

### Documentation Not Updating

- Check the "Builds" tab - did it rebuild?
- Try manually triggering a build
- Clear your browser cache

### Can't Find Repository

Make sure:
- Repository is public (or you've granted Read the Docs access to private repos)
- You're logged into Read the Docs with the same GitHub account

## Local Testing

Always test locally before pushing:

```bash
cd docs
make clean
make html
open _build/html/index.html
```

## Updating Documentation

1. Edit `.rst` files in `docs/`
2. Test locally: `make html`
3. Commit and push:

```bash
git add .
git commit -m "Update documentation"
git push
```

4. Read the Docs rebuilds automatically!

## Support

- Read the Docs Docs: https://docs.readthedocs.io/
- Sphinx Docs: https://www.sphinx-doc.org/
- RST Primer: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
