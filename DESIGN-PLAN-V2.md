# index.html v2 — Stage 2 design plan
Written 9/14/2026. Follows the anti-template ruleset. No code until Isaiah picks a type pairing.

## What is NOT changing
Every credit, every role, every network, every section, every heading. "Built in the Cutting Room"
stays; that grid is work Isaiah was in the room for but did not edit, and the heading does that job.
Every movie poster stays. The poster swap in the hero stays. Copy gets made more real, not shorter.

## The decision that drove this
Sampled six frames from "editng frames", all from films Isaiah produced:

  violinist / blue violin      77% of frame at luma 0.05
  empty theatre from stage     69% of frame under luma 0.10
  the man in the hat           39% of frame at luma 0.05
  sodium tunnel                23% at 0.07, 25% at 0.16
  magenta window               39% under luma 0.06
  fog + stage lights           the only bright one, and it is bright because it is fog

His own work is deliberately dark. The site stays dark. What goes is the gold: nothing in the
#c8a84b range exists in any frame sampled. The warmest real values are browns near #684E3C / #7B6254.

## Palette — 5 values, each sourced

  --black    #000000   the page ground. NOT sampled, chosen: a poster hung in a dark room.
                       True black, not the #060606 tinted near-black the ruleset bans.
  --slate    #0C1523   violinist frame, the cool shadow behind her (7% of frame).
                       Elevated surfaces: card grounds, section separation, form fields.
  --ember    #3D2724   "the man in the hat" (13% of frame). Rules, borders, hover states.
  --sodium   #7B6254   sodium tunnel, the practical light (10% of frame, luma 0.40).
                       The accent. Replaces gold entirely.
  --bone     #ADB7BC   "the man in the hat" (17%, luma 0.71). Body text. Not white.
                       Film highlights are never pure white.

CUT before presenting (Stage 5 discipline): --window #917296 from the magenta window silhouette.
Two accents is one accent too many, and it only exists in a single frame.

### Contrast, measured on #000000
  bone    10.28:1  body text, passes
  sodium   3.72:1  LARGE TEXT AND UI ONLY. Never small type.
  window   5.05:1  (cut)
  slate / ember       structure only, never text
Bug in the live site, unrelated: --muted #666 on #060606 is 3.53:1 and fails. It is currently used
for nav links, all small labels, meta lines and the footer. Fixed in v2 by using bone at low opacity.

## Type — Isaiah picks one

A. ONE FAMILY. Archivo, 900 at display sizes / 400 for text, wide optical range.
   Argument: a main title card is set in one family at different sizes, never in two competing
   faces. Most restrained option. The posters become the only visual variety on the page.

B. Bricolage Grotesque (display) + Public Sans (text).
   Argument: Bricolage's forms are slightly irregular and non-neutral, so they read as chosen
   rather than defaulted. Public Sans is already on /local, so the two pages feel like one person
   made them without looking like each other.

C. Instrument Serif (display only, large only, never italic, never one accented word) + Archivo.
   Argument: the film-festival poster and book-jacket move. HONEST FLAG: this is the closest of
   the three to the display-serif-plus-sans pairing the ruleset warns about, and it only survives
   if the serif is disciplined to large sizes and never used to accent a single word.

Current site is Cormorant Garamond + Montserrat, which is exactly the banned default.

## Layout, one sentence
A black page where the only bright things are the posters, the credits organised as two clearly
different walls, and three of Isaiah's own frames run full bleed as the only breaks between them.

## Wireframe
  NAV            name left, sections right, Local 700 right. No arrow glyphs on links.
  HERO           poster + swap row kept. Name, role, location, bio. Two buttons.
  FACTS          same four facts as the stat bar, set as one quiet line of type.
                 No bordered boxes, no big gold numerals. (15+ years is stale, should read 16.)
  NETWORKS       same six names, full opacity, one line. Not a 35% greyscale logo strip.
  [FRAME 1]      full bleed, empty theatre from the stage
  EDITING        the editor grid. Posters at 100%. No filter.
  [FRAME 2]      full bleed, sodium tunnel
  CUTTING ROOM   the AE grid, heading intact. Posters at 100%. Visibly a different wall from
                 the editor grid, so the distinction reads without needing to be explained.
  ABOUT          photo, copy, the four pills, rewritten to be real
  [FRAME 3]      full bleed, fog and stage lights
  WATCH          YouTube / Vimeo
  CONTACT        unchanged in content
  FOOTER         incl. the quiet /local link, Isaiah Smith Films LLC

## Principles
1. Black is black. No tinted near-black standing in for it.
2. Nothing is dimmed to protect the design. Posters run at 100%, never brightness(.58).
3. One accent, sampled, used rarely, never on small text.
4. Bone, not white.
5. Every heading says something. No eyebrow labels above headings.
6. One motion moment (the poster swap, which the visitor triggers). Not thirty card hovers and
   not a fade-and-slide-up on every section.
7. No middle dots, no arrows appended to links, no italic accent word, no em dashes.

## Stage 3, reviewed against itself
Would a generic "dark film editor portfolio" prompt have produced black plus a poster grid? Yes.
Those two are not distinctive and should not be claimed as design. What a generic prompt would NOT
have produced: the accent being sodium #7B6254 off Isaiah's own tunnel shot instead of gold,
refusing to dim the posters, bone instead of white, and the two grids being visibly different walls
rather than the same card repeated at two sizes.

## Build plan
site/v2.html, live at isaiahsmithfilms.com/v2. index.html untouched. Judge it on the phone.
One push, not five: Netlify credits were at 50% on 9/12 with roughly ten deploys left before 10/10.
