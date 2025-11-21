"""

TASK 1:
-------

if the last line of a `.md` file is:
```
<!-- COPY TO: "bin/<target_filename>.md" -->
```

then replace the section beginning with "---\npermalink:" and ending with
"<!-- END PREAMBLE -->" in the target file with same selection from the source file.

TASK 2:
-------

Also replace the section beginning with "<!-- BEGIN WEB CONTENT -->" and ending with
"<!-- END WEB CONTENT -->" in the target file with same selection from the source file.

If the source file also contains a "<!-- BEGIN SESSION <session_number> OVERVIEW -->" 
section, then replace the section beginning with "<!-- BEGIN SESSION <session_number> OVERVIEW -->" 
and ending with "<!-- END SESSION <session_number> OVERVIEW -->" in the `AAS_WORKSHOP_SUMMARY` 
file with same selection from the source file.

TASK 3:
-------

Append {:target="_blank"} to external links in the target file/AAS_WORKSHOP_SUMMARY file.

This might be dumb. The `{:target="_blank"}` doesn't do anything bad to the rendered
markdown, so it might be better to just ensure it's included in the source documents 
and save a processing step. 

TASK 4:
-------

Replace all rges-pit.org links with {{ site.url }}{{ site.baseurl }}<permalink> links.
"""

AAS_WORKSHOP_SUMMARY = "bin/data_challenge_aas_workshop.md"