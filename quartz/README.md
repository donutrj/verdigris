# Project notes — how to update and deploy

Use these from PowerShell at the repo root.

Update content and deploy (branch `v4` powers GitHub Pages):

```powershell
cd D:\tabletop\creative\Verdigris\Verdigris_Quartz
git status
git add quartz/content -A
git commit -m "Update site content"
git push origin master
git push -f origin HEAD:v4
```

Preview locally (optional):

```powershell
cd D:\tabletop\creative\Verdigris\Verdigris_Quartz
npm ci
npx quartz build --serve
```

---

# Quartz v4

> “[One] who works with the door open gets all kinds of interruptions, but [they] also occasionally gets clues as to what the world is and what might be important.” — Richard Hamming

Quartz is a set of tools that helps you publish your [digital garden](https://jzhao.xyz/posts/networked-thought) and notes as a website for free.
Quartz v4 features a from-the-ground rewrite focusing on end-user extensibility and ease-of-use.

🔗 Read the documentation and get started: https://quartz.jzhao.xyz/

[Join the Discord Community](https://discord.gg/cRFFHYye7t)

## Sponsors

<p align="center">
  <a href="https://github.com/sponsors/jackyzha0">
    <img src="https://cdn.jsdelivr.net/gh/jackyzha0/jackyzha0/sponsorkit/sponsors.svg" />
  </a>
</p>
