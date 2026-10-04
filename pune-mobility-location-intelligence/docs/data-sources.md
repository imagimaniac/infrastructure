# Data Sources — Exhaustive Inventory

> Purpose: Every third-party data source used/referenced. For each: URL, Publisher, Retrieved (YYYY-MM-DD), Type, Scope, License/Terms, Relevance, Usage (Cited|Derived|Assumed), Preprocessing, Notes. Prevents blind reliance.

## 1. Market Data (Real Estate Prices/Rents/Trends)
| Source | URL | Publisher | Retrieved | Type | Scope | License/Terms | Relevance | Usage | Preprocessing | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| MagicBricks | https://www.magicbricks.com/ | MagicBricks (Times Internet) | 2026-10-04 | Market listings/trends | Pune (Wakad/Hinjewadi focus) | Site ToS (reference only) | Price/rent ranges, supply, micro-market context | Cited | Manual review of excerpts; not bulk-scraped | Inform area rates; avoid reproducing full DB |
| Square Yards | https://www.squareyards.com/property-rates-in-pune | Square Yards | 2026-10-04 | Market data/analysis | Pune city + localities | Site ToS (reference only) | Property rate trends, locality insights | Cited | Reviewed tables/trends | Used for directional ranges |
| Economic Times (Real Estate) | https://economictimes.indiatimes.com/wealth/real-estate/buying-property-in-pune-8-hotspots-with-new-projects-prices-and-growth-potential/slideshow/133582274.cms | The Economic Times | 2026-10-04 | News/analysis | Pune hotspots H1 2026 | Copyrighted (fair use citation) | Hotspots, pipeline, price ranges | Cited | Cited excerpts only | Supports micro-market selection |
| FirstPremises | https://firstpremises.com/%F0%9F%8F%99%EF%B8%8F-pune-property-prices-2026-bubble-or-boom-complete-buyer-guide | FirstPremises | 2026-10-04 | Market analysis | Pune 2026 | Site ToS (citation) | Price bands, demand drivers (IT) | Cited | Referenced for context | Directional only |
| Tracxn | https://platform.tracxn.com/a/d/company/58511a26e4b05332c1af9e88/vastu%20real%20estate | Tracxn | 2026-10-04 | Company profile | Pune developers (context) | Tracxn ToS | Developer ecosystem context | Cited | Reference only | Not used as pricing source |
| Namrata Group (Blog) | https://www.namratagroup.com/blog/pune-metro-road-projects-boosting-tathawade-real-estate | Namrata Group | 2026-10-04 | Developer blog | Tathawade, metro+roads | Copyrighted (citation) | Infrastructure impact on values | Cited | Referenced rationale | Supports accessibility→value link |

## 2. Infrastructure, Traffic & Governance
| Source | URL | Publisher | Retrieved | Type | Scope | License/Terms | Relevance | Usage | Preprocessing | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Hindustan Times | https://www.hindustantimes.com/cities/pune-news/nhai-identifies-15-key-traffic-bottlenecks-in-pune-for-priority-fix-101788711968113.html | HT Media | 2026-10-04 | News | NHAI bottlenecks Pune | Copyrighted (citation) | Bottleneck locations (priority) | Cited | Excerpts cited | Informs junction clusters |
| Indian Express | https://indianexpress.com/article/cities/pune/pune-traffic-relief-fadnavis-four-tier-roads-purandar-airport-10793311/lite | The Indian Express | 2026-10-04 | News | Infra announcements (Ring Road/HCMTR) | Copyrighted (citation) | Planned relief claims (context) | Cited | Cited for context | Not assumed as fact for sim |
| Pune Pulse | https://www.mypunepulse.com/pune-ganesh-visarjan-traffic-2026-17-roads-to-close-major-diversions-and-48-hour-heavy-vehicle-ban | Pune Pulse | 2026-10-04 | Local news | Event traffic (peak stress) | Copyrighted (citation) | Real peak stress patterns | Cited | Contextual | Illustrative only |
| PMRDA (Press Releases) | https://www.pmrda.gov.in/en/press-release | PMRDA, Govt. of Maharashtra | 2026-10-04 | Govt authority | PMR region | Public domain/citation | Ring Road, Metro, housing plans | Cited | Reviewed index | Reference for scope |
| NHAI (Pune Division) | Referenced via HT/IE (general: nhai.gov.in) | NHAI | 2026-10-04 | Authority | NH corridors Pune | Public info (citation) | Corridor priorities | Cited | Referenced contextually | Cite specific releases when used |

## 3. Technical (Simulation, APIs, GIS)
| Source | URL | Publisher | Retrieved | Type | Scope | License/Terms | Relevance | Usage | Preprocessing | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Eclipse SUMO | https://eclipse.dev/sumo/ | Eclipse Foundation | 2026-10-04 | OSS | Microsimulation | EPL-2.0 | Core engine | Cited | Installed per docs | SUMO_HOME required |
| SUMO Documentation (TraCI) | https://sumo.dlr.de/docs/TraCI.html | DLR/SUMO | 2026-10-04 | Docs/API | TraCI Python API | CC-BY/Docs | Control API, KPIs (waiting, halting, emissions) | Cited | API reference | Ships with SUMO |
| SUMO Emissions/HBEFA | https://sumo.dlr.de/docs/Models/Emissions.html | SUMO | 2026-10-04 | Docs/Models | Fuel/emissions | As per SUMO | Proxy for fuel/CO2e | Cited | Config-dependent | Model availability varies |
| Gymnasium | https://gymnasium.farama.org/ | Farama Foundation | 2026-10-04 | OSS | RL env (optional) | MIT | Future RL wrapper | Cited (optional) | Not required for v1 | Rule-based first |
| OpenStreetMap (OSM) | https://www.openstreetmap.org/ | OSM Contributors | 2026-10-04 | GIS | Real network (optional) | ODbL | netconvert real slice later | Cited (optional) | Future use | Synthetic first for reproducibility |
| TraCI Python API Reference | https://sumo.dlr.de/pydoc/traci.html | SUMO/DLR | 2026-10-04 | API Docs | Function refs | As per SUMO | getWaitingTime, getLastStepHaltingNumber, etc. | Cited | Reference | Used in implementation |

## 4. Python Ecosystem & Tooling
| Source | URL | Publisher | Retrieved | Type | Scope | License/Terms | Relevance | Usage | Preprocessing | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Python | https://www.python.org/ | Python Software Foundation | 2026-10-04 | Language | Core | PSF | Implementation | Cited | System/venv | 3.x |
| pandas | https://pandas.pydata.org/ | PyData | 2026-10-04 | OSS | Data frames/CSV | BSD-3 | Metrics logging/agg | Cited | pip install | v1.x |
| numpy | https://numpy.org/ | NumPy devs | 2026-10-04 | OSS | Numerics | BSD-3 | Calculations | Cited | pip install | v1.x |
| matplotlib | https://matplotlib.org/ | Matplotlib devs | 2026-10-04 | OSS | Static plots | PSF | Figures | Cited | pip install | v3.x |
| plotly | https://plotly.com/python/ | Plotly | 2026-10-04 | OSS | Interactive plots | MIT | Dashboard visuals | Cited | pip install | v5.x |
| Streamlit | https://streamlit.io/ | Streamlit | 2026-10-04 | OSS | Local dashboard | Apache 2.0 | ROI UI | Cited | pip install | v1.x |
| pip | https://pip.pypa.io/ | PyPA | 2026-10-04 | Tool | Packaging | MIT | Deps | Cited | std | venv |
| venv | https://docs.python.org/3/library/venv.html | PSF | 2026-10-04 | Tool | Env isolation | PSF | Isolation | Cited | std | stdlib |

## 5. Workflow, VCS & Docs
| Source | URL | Publisher | Retrieved | Type | Scope | License/Terms | Relevance | Usage | Preprocessing | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Git | https://git-scm.com/ | Git Project | 2026-10-04 | VCS | Versioning | GPL v2 | Traceability | Cited | System install | repo history |
| GitHub Flavored Markdown (GFM) | https://github.github.com/gfm/ | GitHub | 2026-10-04 | Spec | README formatting | CommonMark-based | Docs | Cited | N/A | Pyramid READMEs |
| CommonMark | https://commonmark.org/ | CommonMark | 2026-10-04 | Spec | Markdown | BSD-3 | Docs | Cited | N/A | Rendered in CLI/UI |

**Classification Legend:** Cited = referenced from literature/news/docs; Derived = computed from data; Assumed = parameterized by us with rationale (see assumptions-log.md). All retrieval dates reflect session time of documentation.
