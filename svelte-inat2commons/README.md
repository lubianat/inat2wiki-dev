# iNat2Wiki (Svelte)

Static Svelte app that mirrors both Flask apps in this repo:

- **inat2wiki-dev**: Home, Parse observation, language switcher, and Commons upload links
- **inat2wiki (legacy)**: User list, Project list, Wikistub, About

The data flow matches the legacy Python module behavior by using iNaturalist
and Wikidata endpoints directly in the browser.

## Development

From the repo root:

```bash
cd svelte-inat2commons
npm install
npm run dev
```

Build static assets:

```bash
npm run build
```

## Routes

- `/` – new home page
- `/parse` and `/parse/:observationId` – parse observation
- `/userlist` and `/userlist/:username` – legacy user list
- `/projectlist` and `/projectlist/:projectSlug` – legacy project list
- `/wikistub/:lang` and `/wikistub/:lang/:qidOrName` – legacy Wikipedia stub
- `/about` – legacy about page
