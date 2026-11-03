# Data sources and rights

## Comparative Agendas Project

The UK parliamentary-question data and topic-code material originate in the Comparative Agendas Project. Upstream project-generated variables and codebooks are offered under CC BY-NC-SA 4.0; primary-source text retains applicable upstream rights. This artifact does not relicense those materials as software.

- Dataset: https://www.comparativeagendas.net/project/uk/datasets
- Terms: https://www.comparativeagendas.net/pages/Copyright-and-Legal
- Citation guidance: https://www.comparativeagendas.net/pages/How-to-cite
- UK citation: John, Peter, Anthony Bertelli, Will Jennings, and Shaun Bevan (2013), *Policy Agendas in British Politics*, Palgrave Macmillan.

The full-corpus CSV retains only date, question and major topic for the weighting calculation; the sampled records, codebook text and prompts retain their scientific content. Deduplication and stratification are described in the code. The raw repeat prompts contain public parliamentary text and category descriptions. Public names in source material are third-party subjects or credited data creators, not artifact-author attribution.

## Documentary study

`documentary/source_catalogue.csv` records the analysed text hashes and source pointers. Original UK/EU policy PDFs and the full source bank are not redistributed. The coding files contain selected quoted passages and analytical annotations for review; third-party copyright and source attribution remain with the original issuers. The legal and guidance versions named in the catalogue and paper govern interpretation; a current web page can differ from the analysed copy.

## Experimental and analytical records

Stored labels, probability fields, repeat responses, coded placements and outputs are supplied for research reproduction. They must be used with the evidence boundaries in `docs/PROVENANCE.md`. The software licence applies only to original artifact code, not to third-party texts, datasets or model-provider materials.
