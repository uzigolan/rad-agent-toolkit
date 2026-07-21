#!/usr/bin/env python3
"""Convert eval-etx2-device-report.md to HTML"""

import markdown
from pathlib import Path

# Read the markdown file
md_file = Path('rad-mcp-server/tests/eval-etx2-device-report.md')
md_content = md_file.read_text(encoding='utf-8')

# Convert to HTML
html_content = markdown.markdown(md_content, extensions=['tables', 'extra'])

# Create complete HTML document with styling
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
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        h1, h2, h3, h4 {
            margin-top: 30px;
            margin-bottom: 15px;
            color: #2c3e50;
        }
        h1 {
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            font-size: 2.5em;
        }
        h2 {
            font-size: 1.8em;
            margin-top: 40px;
            border-left: 4px solid #3498db;
            padding-left: 15px;
        }
        h3 {
            font-size: 1.3em;
            color: #34495e;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        th {
            background: #3498db;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: 600;
        }
        td {
            padding: 12px;
            border-bottom: 1px solid #ecf0f1;
        }
        tr:hover {
            background: #f8f9fa;
        }
        tr:last-child td {
            border-bottom: none;
        }
        strong, b {
            color: #2c3e50;
            font-weight: 600;
        }
        code {
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }
        p {
            margin: 15px 0;
        }
        ul, ol {
            margin: 15px 0 15px 30px;
        }
        li {
            margin: 8px 0;
        }
        .status-pass {
            background: #d4edda;
            color: #155724;
            padding: 3px 8px;
            border-radius: 3px;
            font-weight: 600;
        }
        .status-skip {
            background: #fff3cd;
            color: #856404;
            padding: 3px 8px;
            border-radius: 3px;
            font-weight: 600;
        }
        .status-fail {
            background: #f8d7da;
            color: #721c24;
            padding: 3px 8px;
            border-radius: 3px;
            font-weight: 600;
        }
        footer {
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #ecf0f1;
            color: #7f8c8d;
            font-size: 0.9em;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
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
