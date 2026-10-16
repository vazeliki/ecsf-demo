# ECSF 2.0

A demo website for the ECSF 2.0: ECSF profiles and skill areas,
each skill area evolves across four proficiency levels, with tasks and skill
areas cross-linked in both directions.

## File structure

```
.
├── index.html          # page shell, nav, all view containers
├── assets/
│   ├── styles.css        # your styling (unchanged, +1 small mobile breakpoint)
│   ├── data.js              # your role/skill data (unchanged)
│   └── app.js                  # rendering + hash routing (rebuilt to match)
└── README.md
```

## Pages

- **Home** (`#/`) — hero, "how this works" cards, proficiency-level legend
- **ECSF Profiles** (`#/roles`) — searchable grid of all 12 profiles
- **Profile detail** (`#/role/<slug>`) — tasks + skill areas (with that role's
  level in each one), links through to each skill area
- **Skill Areas** (`#/skills`) — searchable grid of all 22 skill areas
- **Skill detail** (`#/skill/<id>`) — L1–L4 proficiency progression, plus every
  role that uses this skill and at what level
- **Skills Matrix** (`#/matrix`) — every profile against every skill area
- **Key Features** (`#/features`) — how levels, target levels and the task-to-skill-area mapping work


## Local preview

```bash
python3 -m http.server 8000
```
then open `http://localhost:8000`.
