#!/usr/bin/env python3
"""Convert eval-etx2-device-report.md to HTML with GitHub-like styling"""

import markdown
from pathlib import Path

# Read the markdown file
md_file = Path('rad-mcp-server/tests/eval-etx2-device-report.md')
md_content = md_file.read_text(encoding='utf-8')

# Convert to HTML
html_content = markdown.markdown(md_content, extensions=['tables', 'extra', 'codehilite'])

# Create complete HTML document with GitHub-like styling
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ETX-2 Device Test Results</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        html {
            font-size: 16px;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #24292e;
            background-color: #ffffff;
            padding: 0;
        }
        .markdown-body {
            max-width: 960px;
            margin: 0 auto;
            padding: 45px;
        }
        @media (max-width: 768px) {
            .markdown-body {
                padding: 15px;
            }
        }
        h1, h2, h3, h4, h5, h6 {
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
            line-height: 1.25;
        }
        h1 {
            padding-bottom: 0.3em;
            font-size: 2em;
            border-bottom: 1px solid #eaecef;
        }
        h2 {
            padding-bottom: 0.3em;
            font-size: 1.5em;
            border-bottom: 1px solid #eaecef;
        }
        h3 {
            font-size: 1.25em;
        }
        h4 {
            font-size: 1em;
        }
        h5 {
            font-size: 0.875em;
        }
        h6 {
            font-size: 0.85em;
            color: #6a737d;
        }
        p {
            margin-bottom: 16px;
        }
        a {
            color: #0366d6;
            background-color: transparent;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        strong {
            font-weight: 600;
            color: #24292e;
        }
        em {
            font-style: italic;
        }
        code {
            padding: 0.2em 0.4em;
            margin: 0;
            font-size: 85%;
            background-color: rgba(27,31,35,0.05);
            border-radius: 3px;
            font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
        }
        pre {
            padding: 16px;
            overflow: auto;
            font-size: 85%;
            line-height: 1.45;
            background-color: #f6f8fa;
            border-radius: 6px;
            border: 1px solid #e1e4e8;
            margin-bottom: 16px;
        }
        pre code {
            display: inline;
            padding: 0;
            margin: 0;
            overflow: visible;
            line-height: inherit;
            background-color: transparent;
            border: 0;
        }
        blockquote {
            padding: 0 1em;
            color: #6a737d;
            border-left: 0.25em solid #dfe2e5;
            margin: 0 0 16px 0;
        }
        ul, ol {
            padding-left: 2em;
            margin-bottom: 16px;
        }
        li {
            margin-bottom: 0;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 16px;
        }
        table th {
            padding: 6px 13px;
            border: 1px solid #dfe2e5;
            background-color: #f6f8fa;
            font-weight: 600;
            text-align: left;
        }
        table td {
            padding: 6px 13px;
            border: 1px solid #dfe2e5;
        }
        table tr:nth-child(2n) {
            background-color: #f6f8fa;
        }
        table tr {
            background-color: #ffffff;
            border-top-color: #dfe2e5;
        }
        hr {
            height: 0.25em;
            padding: 0;
            margin: 24px 0;
            background-color: #e1e4e8;
            border: 0;
        }
        .badge {
            display: inline-block;
            padding: 0.4em 0.8em;
            font-size: 0.85em;
            font-weight: 600;
            line-height: 1;
            border-radius: 2em;
            margin-right: 0.5em;
        }
        .badge-success {
            background-color: #28a745;
            color: #ffffff;
        }
        .badge-warning {
            background-color: #ffc107;
            color: #24292e;
        }
        .badge-danger {
            background-color: #dc3545;
            color: #ffffff;
        }
        .badge-info {
            background-color: #17a2b8;
            color: #ffffff;
        }
        .gh-header {
            margin-bottom: 32px;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 16px;
        }
        .gh-header-meta {
            color: #6a737d;
            font-size: 0.9em;
        }
        footer {
            margin-top: 48px;
            padding-top: 24px;
            border-top: 1px solid #eaecef;
            color: #6a737d;
            font-size: 0.9em;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="markdown-body">
        {content}
        <footer>
            <p>Generated from: eval-etx2-device-report.md</p>
            <p>Test Framework: ETX-2 Device Command Validation</p>
        </footer>
    </div>
</body>
</html>
"""

# Write HTML file
html_file = Path('rad-mcp-server/tests/eval-etx2-device-report.html')
final_html = html_template.replace('{content}', html_content)
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f'✅ HTML file created: {html_file}')
print(f'📊 Size: {html_file.stat().st_size:,} bytes')
print(f'🎨 Styling: GitHub Flavored Markdown (GFM) look and feel')

