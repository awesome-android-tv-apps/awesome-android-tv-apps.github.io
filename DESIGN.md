---
name: Reblucky Android TV Apps
description: Dark navy showcase for three Android TV apps, set in Outfit, with one accent colour per app.
colors:
  bg: "#050c2c"
  surface: "#0b1647"
  surface-2: "#101f5a"
  text: "#f1f4ff"
  muted: "#b4bee6"
  accent: "#2a68ff"
  accent-soft: "#6aa3ff"
  line: "rgba(255, 255, 255, 0.12)"
  app-streamova: "#37d3e7"
  app-trimo: "#f4b63f"
  app-airplay: "#3da9ff"
typography:
  display:
    fontFamily: "Outfit, system-ui, sans-serif"
    fontSize: "clamp(2.1rem, 1.2rem + 3.4vw, 3.9rem)"
    fontWeight: 650
    lineHeight: 1.07
    letterSpacing: "-0.025em"
  headline:
    fontFamily: "Outfit, system-ui, sans-serif"
    fontSize: "clamp(1.5rem, 1.15rem + 1.1vw, 2.05rem)"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.015em"
  title:
    fontFamily: "Outfit, system-ui, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 600
    lineHeight: 1.35
  body:
    fontFamily: "Outfit, system-ui, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.65
rounded:
  sm: "6px"
  md: "10px"
  img: "12px"
  lg: "14px"
spacing:
  gutter: "clamp(18px, 4vw, 36px)"
  section: "2.25rem"
components:
  button-primary:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.bg}"
    rounded: "{rounded.md}"
    padding: "0.55rem 1rem"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
    padding: "0.55rem 1rem"
  more-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: "0.9rem"
---

# Design system

## Overview

The site is a showcase for the Reblucky Software apps, so it borrows the Reblucky world: deep navy, white type, one blue accent, Outfit throughout. The home page opens as a launcher row of three TV banners, the way an Android TV home screen presents apps. App pages are documents: an answer-first lead, a facts table, steps, FAQ.

The page itself stays quiet so the app art carries the colour. Each app page sets `--app` to its own accent. Only buttons, the job line on a tile, step numerals, the active nav item and focus rings use it.

## Colors

Dark only. The page is `bg`, cards and chips sit on `surface`, hover states on `surface-2`, hairlines use `line`. Body text is `text`, secondary text `muted`. Links use `accent-soft` and `accent` marks text selection. The three app accents come from each app's own artwork: Streamova cyan, Trimo amber, AirPlay Receiver sky blue. A faint blue radial glow sits at the top of the page.

## Typography

One family, Outfit variable (latin subset, `/fonts/outfit-latin-wght.woff2`, `font-display: swap`). Weights: 400 body, 600 headings, 650 for the h1. Headings use `text-wrap: balance` and paragraphs `text-wrap: pretty`. Reading width is 68ch for prose and 60ch for the lead. Numbers in the facts and comparison tables use tabular figures.

## Layout

A single 1180px column with a fluid gutter. Pages are a stack of sections separated by one hairline. The comparison table on the home page turns into stacked, labelled blocks below 860px. The facts list is two columns from 760px. Screenshot galleries run up to three columns, two when there are four images, one on a phone. There is no horizontal scroll at 390px.

## Elevation & Depth

No shadows on resting elements, only a 1px `line` ring on images. The home tile art lifts 4px and gains a 2px ring in the app accent on hover or focus. Reduced motion removes the lift.

## Shapes

Radii: 14px for cards and the app hero art, 12px for tile and gallery images, 10px for buttons, 5 to 6px for inline code and focus rings. Corners are not mixed within one component.

## Components

- **Launcher tile**: banner art (16:9), app name, one-line job in the app accent, a one-sentence blurb, a primary Google Play button and a text link to the details page. The button row is pinned to the bottom so the three tiles line up.
- **Primary button**: filled with the app accent, navy text, 10px radius. The ghost variant has a 1px `line` border.
- **Facts list**: a definition list with fixed keys (What it is, Platform, Price, Privacy, Languages, Not included, plus app-specific rows). Keys are identical across the app pages.
- **Steps**: ordered list with large numerals in the app accent.
- **FAQ**: questions as `h3`, answers as plain paragraphs. No accordions, so every answer is visible text.
- **More cards**: the other two apps, icon plus name and job.

## Do's and Don'ts

- Do keep one accent per page and take it from the app being described.
- Do put the answer before the detail, and keep the facts keys identical on all app pages.
- Do give every image `width`, `height` and real alt text.
- Don't add scripts, cookies, third-party fonts or tracking pixels.
- Don't present the site as independent. The publisher disclosure stays in the footer, the home page note, the home FAQ and on the About page.
- Don't put an em dash, bold run-in labels or marketing adjectives in copy.
