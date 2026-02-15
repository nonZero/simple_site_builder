# Simple Site Builder

A minimal static site builder that converts Markdown files to HTML.

## Run

No setup required. Build your site with:

```bash
uv run simple_site_builder.py <src_dir> <target_dir>
```

Example:

```bash
uv run simple_site_builder.py examples/hikes out/
```

To serve the generated site locally run:

```bash
python -m http.server 8181 -d out
```

Then open http://localhost:8181 in your browser.
