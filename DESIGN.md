---
name: Awesome Android TV Apps
description: The rating plate on the back of a TV box, as a website: cool gray case, label-stock plates with ink keylines, condensed type, one signal orange.
colors:
  ground: "#e2e5e9"
  plate: "#fbfbfa"
  ink: "#14171c"
  ink-raised: "#2b3038"
  ink-muted: "#c3c9d2"
  print-gray: "#3d4550"
  rule: "rgba(20, 23, 28, 0.22)"
  white: "#ffffff"
  mark-bar: "#f3f5f7"
  rule-on-ink: "rgba(255, 255, 255, 0.18)"
  signal: "#ff5a1f"
  signal-line: "#d9400a"
  app-streamova: "#37d3e7"
  app-trimo: "#f4b63f"
  app-airplay: "#3da9ff"
typography:
  display:
    fontFamily: "Barlow Semi Condensed, Arial Narrow, Barlow, system-ui, sans-serif"
    fontSize: "clamp(2.5rem, 1.2rem + 5vw, 4.6rem)"
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "Barlow Semi Condensed, Arial Narrow, Barlow, system-ui, sans-serif"
    fontSize: "clamp(1.65rem, 1.25rem + 1.2vw, 2.15rem)"
    fontWeight: 700
    lineHeight: 1.1
  title:
    fontFamily: "Barlow Semi Condensed, Arial Narrow, Barlow, system-ui, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 600
    lineHeight: 1.25
  body:
    fontFamily: "Barlow, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Barlow Semi Condensed, Arial Narrow, Barlow, system-ui, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 600
    lineHeight: 1.7
    letterSpacing: "0.07em"
rounded:
  swatch: "2px"
  chip: "4px"
  plate: "6px"
  screen: "8px"
  icon: "12px"
spacing:
  gutter: "clamp(18px, 4vw, 36px)"
  section: "2.25rem"
  section-wide: "2.75rem"
  rail-gap: "2.5rem"
components:
  button-primary:
    backgroundColor: "{colors.app-streamova}"
    textColor: "{colors.ink}"
    rounded: "{rounded.plate}"
    padding: "0.65rem 1.1rem"
  button-primary-trimo:
    backgroundColor: "{colors.app-trimo}"
    textColor: "{colors.ink}"
    rounded: "{rounded.plate}"
    padding: "0.65rem 1.1rem"
  button-primary-airplay:
    backgroundColor: "{colors.app-airplay}"
    textColor: "{colors.ink}"
    rounded: "{rounded.plate}"
    padding: "0.65rem 1.1rem"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.plate}"
    padding: "0.65rem 1.1rem"
  plate:
    backgroundColor: "{colors.plate}"
    textColor: "{colors.ink}"
    rounded: "{rounded.plate}"
    padding: "0.8rem 1.1rem"
  chip:
    backgroundColor: "{colors.plate}"
    textColor: "{colors.ink}"
    rounded: "{rounded.chip}"
    padding: "0.15rem 0.6rem"
  header:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
    padding: "0.7rem 0"
  step-key:
    backgroundColor: "{colors.app-streamova}"
    textColor: "{colors.ink}"
    rounded: "{rounded.plate}"
    size: "2.5rem"
---

# Design System: Awesome Android TV Apps

## Overview

**Creative North Star: "The Rating Plate"**

The site reads like the label on the back of a TV box. Every fact sits in a row with a label on the left and a value on the right, under a ruled line. The page is the cool gray device case, the content is near-white label stock held by an ink keyline, and the header and footer are the ink front and base of the unit. The only warmth is a signal orange, used the way a device uses a status lamp: rarely, and always meaning "this is the thing to look at".

The scene that forces light: a person on a phone or laptop in room light, checking what an app does before pressing install, with the remote in the other hand. Printed labels are light stock with black print, so the site is too. The apps' own TV screenshots are the only dark surfaces on the page besides the ink bookends, which makes them read as screens.

It refuses the dark navy page with a glowing triplet of cards, and it refuses the warm-cream editorial look. Type is condensed and engineered rather than friendly: Barlow Semi Condensed for names and labels, Barlow for reading.

**Key Characteristics:**
- One sheet of rows: section titles live in a left rail, content in the right column, 2px ink rules between rows.
- Label-stock plates with a 1.5px ink keyline and a 6px corner; no shadows anywhere.
- Uppercase condensed labels for row names; tabular figures for every number.
- App banners and screenshots sit in a 3px ink bezel, like a TV screen.
- One accent per app (cyan, amber, blue), spent only on the Play button, the step keys and a small swatch.

## Colors

A cool gray case, near-white label stock, one ink, one signal orange, and three borrowed accents that belong to the apps.

### Primary
- **Panel Ink** (#14171c): header, footer, body text, plate keylines, focus rings, and the bezels around screens. It is the only dark ground; Raised Ink exists solely as the mark's square on the header.

### Secondary
- **Signal Orange** (#ff5a1f): the status lamp in the mark, the active navigation underline on the ink header, text selection and the skip link. Never text, never a fill on light ground.
- **Underline Orange** (#d9400a): the 2px underline under every link. Deeper than the signal so it clears 3:1 on gray (3.54), label stock (4.33) and ink (4.01).

### Tertiary
- **Streamova Cyan** (#37d3e7), **Trimo Amber** (#f4b63f), **AirPlay Blue** (#3da9ff): taken from each app's own artwork. They fill that app's Play button, its numbered step keys and the swatch beside its job line. Text on them is always Panel Ink (9.95, 9.93 and 7.11).

### Neutral
- **Device Case Gray** (#e2e5e9): the page.
- **Label Stock** (#fbfbfa): plates, chips, cards.
- **Print Gray** (#3d4550): secondary text, row labels, captions (7.67 on the page, 9.37 on a plate).
- **Hairline Rule** (rgba(20, 23, 28, 0.22)): lines between rows inside a plate.
- **Raised Ink** (#2b3038) and **Muted Ink** (#c3c9d2): the mark's square on the header, and secondary text on ink (10.78). **Mark Bar** (#f3f5f7) is the white of the three rows in the mark, and **Rule On Ink** (rgba(255, 255, 255, 0.18)) is the one line in the footer.

### Named Rules
**The Rationed Signal Rule.** Signal orange is a lamp, not a theme. If it appears as a fill on the page or as text on gray, it is wrong.

**The App Owns Its Accent Rule.** A per-app accent colors only that app's Play button, step keys and job swatch. It never tints a heading, a border or a background.

## Typography

**Display Font:** Barlow Semi Condensed (with Arial Narrow, Barlow)
**Body Font:** Barlow (with system-ui)
**Label/Mono Font:** none. Labels are Barlow Semi Condensed 600, uppercase.

**Character:** A signage face built from highway and license-plate lettering, set tight for names and wide-open for reading. Condensed for anything that is stamped, regular width for anything that is read.

### Hierarchy
- **Display** (700, clamp(2.5rem, 1.2rem + 5vw, 4.6rem), 1.02, -0.01em): the home h1. App pages use clamp(2.3rem, 1.2rem + 4vw, 3.9rem).
- **Headline** (700, clamp(1.65rem, 1.25rem + 1.2vw, 2.15rem), 1.1): section titles in the left rail.
- **Title** (600, 1.25rem, 1.25): FAQ questions, step names. Tile names go to 1.95rem at 700.
- **Body** (400, 1.0625rem, 1.6): prose capped at 66ch; the lead is 1.2 to 1.45rem capped at 54ch.
- **Label** (600, 0.9rem, 0.07em, uppercase): row names in plates and table row heads, chips (0.875rem, 0.05em).

### Named Rules
**The Stamped And Read Rule.** Condensed type is for names, numbers and labels. Sentences are always Barlow regular.

## Layout

A single 1180px column with a fluid gutter. Pages are one sheet cut into rows by 2px ink rules. From 900px each section is a two-column row: the title in a 3fr rail (sticky), the content in a 9fr column, 2.5rem apart. Below 900px the title sits above the content. The comparison table is the exception and spans the full width, then turns into labeled blocks below 860px. The home hero is a two-column grid from 960px: headline and lead on the left, a three-row publisher plate (Made by, This site, Updated) on the right, tops aligned. Below 760px the plate's label and value share a row, so the first app unit appears in the first phone screen. Section padding is 2.25rem (2.75rem from 900px), and the home tile row keeps the same space above the next rule so plates never sit on it. Facts plates use a 9.5rem label column from 760px.

## Elevation & Depth

Flat. Depth is a keyline, not a shadow: a 1.5px ink border on plates, a 3px ink border on screens. Hover lifts a tile or card 2 to 3px by transform with an exponential ease-out, and reduced-motion removes it. The only layering is the ink header and footer against the gray case. The one authored moment is the status lamp in the mark: on every page load it comes on over 900ms (opacity from 0.12 to 1, exponential ease-out); under reduced motion it is simply on.

### Named Rules
**The Keyline Rule.** Elevation is declared once. A plate has a border or a shadow, never both; here it is always the border.

## Shapes

Small, engineered corners: 6px on plates, buttons, step keys and screens' bezels, 8px on the app hero art, 12px on app icons, 4px on chips and inline code, 2px on the job swatch. Larger radii read as app cards rather than as labels, so they are not used. Borders are ink at 1.5px for plates, 2px for buttons, 3px for screens. The mark is a rounded square with three label rows and a lamp.

## Components

### Buttons
- **Shape:** 6px corner, 2px ink border.
- **Primary:** the app accent as fill, Panel Ink text at weight 600, padding 0.65rem 1.1rem (0.5rem 0.95rem inside a tile). The default accent is Signal Orange when no app owns the page.
- **Hover / Focus:** brightness 1.07; pressed moves 1px down. Focus is a 3px ink ring, 3px offset (white on the ink header and footer).
- **Ghost:** transparent with the same ink border; hover fills with Label Stock.

### Chips
- **Style:** Label Stock with a 1.5px ink border, 4px corner, uppercase condensed 0.875rem. They state limits (Android 7.0 or newer, No ads) and are not interactive.

### Plates (facts, hero plate, tiles, more cards)
- **Corner Style:** 6px.
- **Background:** Label Stock.
- **Border:** 1.5px Panel Ink; rows inside separated by Hairline Rule.
- **Internal Padding:** 0.8rem by 1.1rem per row; tiles 0.9rem.
- **Facts plate:** a definition list with fixed keys (What it is, Made by, Platform, Price, Privacy, Languages, Not included, plus app rows), ending in an Updated date code.

### Navigation
- **Style:** the ink header holds the mark, a stacked AWESOME / ANDROID TV APPS lockup and the page links in condensed 600. Hover underlines in white; the current page underlines 3px in Signal Orange. Links wrap below the lockup on narrow screens. Breadcrumbs are plain Barlow at 0.95rem in Print Gray with a slash between steps: navigation, not a label above the heading.

### Screens (banners and screenshots)
- A 3px ink border at 6px (8px for the app hero), `object-fit: cover`, ink behind the image while it loads. Captions are 0.95rem Print Gray below.

### Numbered steps
- A 2.5rem square key in the app accent with a 2px ink border and a condensed numeral, then the step title and text, with a Hairline Rule between steps.

### Comparison plate
- The only table: an ink header row with the app names in white condensed 700, label-style row heads, 1.5px ink keyline. Below 860px each row becomes a block with the app name above each value.

## Do's and Don'ts

### Do:
- **Do** put every fact in a label-and-value row, and keep the row keys identical on all three app pages.
- **Do** end a plate with the Updated date code so freshness is always visible.
- **Do** keep the publisher in text: a Made by row on each plate, the home hero plate, the footer and the About page.
- **Do** give every number tabular figures and every image `width`, `height` and real alt text.
- **Do** put app art in a 3px ink bezel so it reads as a screen.

### Don't:
- **Don't** use Signal Orange as a fill or as text on the gray page.
- **Don't** add shadows, glows, gradients or blur; the keyline is the depth.
- **Don't** put a per-app accent on headings, borders or backgrounds.
- **Don't** use corner radii above 8px on content, or pill shapes outside chips.
- **Don't** reuse another brand's logo, palette or typeface here; this site has its own mark and its own world.
- **Don't** add scripts beyond the one Google Analytics tag, or load fonts and images from other hosts.
- **Don't** write an eyebrow above a heading, an em dash, or bold run-in labels in copy.
