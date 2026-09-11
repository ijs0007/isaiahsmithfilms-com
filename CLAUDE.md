# Isaiah Smith Films — Local Business page + hero film

## What this folder is
The entire website isaiahsmithfilms.com (no other copy exists anywhere). Deployed by dragging the site/ SUBFOLDER (only that folder)
onto Netlify Drop (app.netlify.com, site "coruscating-bublanina-da8374", custom domain isaiahsmithfilms.com). No GitHub, no build step.
Moved into site/ on 9/3/2026 so CLAUDE.md, hero-film/ and the backup are never published.

- site/index.html            the live editing portfolio (dark/gold). Do not restyle. Only change: one footer link to /local (already added).
- site/local.html            DRAFT of isaiahsmithfilms.com/local — video services for small businesses in Conyers, GA. Still in the dark
                             portfolio look; will be REBUILT bright/white with a full-bleed silent hero video (see hero-film/). Copy and offers are the current draft.
- site/local-thanks.html     form thank-you page (Netlify Forms, form name "local-inquiry").
- site/_redirects            makes /local and /local-thanks work without .html.
- index.ORIGINAL-backup.html exact copy of the site as it was live on 9/2/2026. Never edit. Undo button. Lives OUTSIDE site/ on purpose.
- hero-film/SHOTLIST.md      the locked shot list for the hero film "Ask Your Editor".
- hero-film/LOOK.md          the look bible (camera, framing, light, color, people, sets).
- hero-film/REFS.md          OpenArt reference ids, approved stills, and the generation rule for every shot with a person in it.
- hero-film/prompts/         one file per shot: model, references, the exact prompt.

## The business decision (settled 9/2/2026)
- Brand: Isaiah Smith Films LLC. isaiahsmithfilms.com stays the film/TV editing portfolio; /local is the small-business front door.
  Reached by QR code / business card / Google Business Profile, plus a quiet footer link. Nothing in the main site's nav.
- Two offers: "The Intro" (one-time brand video) and "Monthly Reels" (one 2-hr shoot a month, 4 reels + photos + captions).
  Website add-on (SmithWebHQ becomes a line item, not a peer brand). Founding-client rate for the first three.
  Prices in local.html ($750 / $950 / $500 founding) are Claude's suggestion, NOT confirmed by Isaiah.
- Prescription-pad motif for the pricing section ("Rx: Monthly Reels. Refills available.") ties the page to the hero film.
- Don't name Loose Leaf Salads (Cedric, next door) anywhere until he has said yes. Keep an unnamed "first client" slot.
- Main site keeps "Los Angeles, CA" for now — Isaiah's choice.

## Hero film — pipeline
Realistic look (chosen). Dr. IJ Smith = Isaiah, never generated from a text description: every shot with him is OpenArt nano-banana-pro,
image2image, 16:9, 2K, with the four likeness refs listed in hero-film/REFS.md attached every time (never GPT Image 2 for likeness).
Her consistency anchor is a faded sky-blue bandana worn as a headband; one approved character still of her is attached to every shot she is in.
hero-film/REFS.md is the registry of reference ids and approved stills.
Higgsfield has a trained "Isaiah" Soul but 0 credits; generation happens on OpenArt.
Rules: lock every still before animating; image-to-video with first frame locked and minimal motion; hands hidden/still or in oven mitts;
anything with words on it (chart, Rx pad text, phone screens, title) is a Fusion insert inside DaVinci Resolve, not generated.
Blender (grey-box rooms) for camera + continuity on the exam room and pizzeria shots. Claude writes AND runs the Python headless on its own
side, then saves .blend + script + renders into hero-film/blender/. Isaiah wants to stay hands-off; he reviews renders, not Blender.
Website copy of the film is MUTED; a music version goes to social.

## How Isaiah works with Claude
One step at a time: he teaches the step, Claude builds it, they test it together, then the next step. Don't dump the whole process.
Honest pushback wanted, on evidence. No em dashes in anything client-facing.
