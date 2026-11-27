# Custom career-site probe

| Reader | Company | Result | Sample titles |
|---|---|---|---|
| eightfold | Microsoft | fail | eightfold: no response from apply.careers.microsoft.com |
| eightfold | Netflix | ok, 10 senior | Director, Production Management - Film; Technical Director PaFX (Houdini) - Netflix Animation Studios; Technical Director Performance  - Netflix Anima |
| eightfold | American Express | fail | eightfold: no response from aexp.eightfold.ai |
| eightfold | Qualcomm | fail | eightfold: no response from careers.qualcomm.com |
| eightfold | PayPal | fail | eightfold: no response from paypal.eightfold.ai |
| eightfold | Micron | fail | eightfold: no response from careers.micron.com |
| eightfold | Bayer | ok, 0 senior |  |
| eightfold | Starbucks | fail | eightfold: no response from starbucks.eightfold.ai |
| eightfold | Cisco | fail | eightfold: no response from cisco.eightfold.ai |
| eightfold | Vertex Pharmaceuticals | fail | eightfold: no response from vrtx.eightfold.ai |
| eightfold | Morgan Stanley | fail | eightfold: no response from morganstanley.eightfold.ai |
| eightfold | Dexcom | fail | eightfold: no response from dexcom.eightfold.ai |
| eightfold | Chevron | fail | eightfold: no response from chevron.eightfold.ai |
| eightfold | AMD | fail | eightfold: no response from careers.amd.com |
| phenom | HPE | ok, 8 senior | Vice President, Strategy for HPE Networking; VP & General Manager - GreenLake Flex Solutions; Director of Enterprise Cyber Security Architecture; Mana |
| phenom | Thermo Fisher Scientific | ok, 23 senior | Executive Director/ Vice President, General Partner (Biopharma) - US Remote; Sr. Director, IT; Sr. Director, Finance, FP&A; Quality Director |
| phenom | AbbVie | fail | phenom: no response from careers.abbvie.com |
| phenom | CVS Health | ok, 27 senior | Population Health Director, Field; National Accounts Vice President of Client Management - West Coast; Vice President, Interoperability; Lead Director |
| phenom | Mastercard | ok, 32 senior | Vice President, Business Operations; Vice President, Business Operations; Vice President, Product Operations; Vice President, European Cybersecurity E |
| phenom | Kroger | fail | phenom: no response from jobs.kroger.com |
| phenom | Boeing | fail | phenom: no response from jobs.boeing.com |
| phenom | Accenture | fail | phenom: no response from www.accenture.com |
| phenom | Johnson & Johnson | fail | phenom: no response from www.careers.jnj.com |
| phenom | Lowe's | ok, 3 senior | Director, SC Maintenance Strategy; Director, Marketplace Trust & Safety; Director, Product Management - Search and Category Experience |
| phenom | Intel | fail | phenom: no response from jobs.intel.com |
| phenom | Siemens | fail | phenom: no response from jobs.siemens.com |
| phenom | Booz Allen Hamilton | fail | phenom: no response from careers.boozallen.com |
| phenom | Bristol Myers Squibb | fail | phenom: no response from careers.bms.com |
| phenom | Caterpillar | fail | phenom: no response from careers.caterpillar.com |
| phenom | Walgreens | fail | phenom: no response from jobs.walgreens.com |
| sitemap | Apple | fail | 404 Client Error: Not Found for url: https://jobs.apple.com/sitemap.xml (1 sitemaps listed) |
| sitemap | Goldman Sachs | fail | 404 Client Error: Not Found for url: https://higher.gs.com/sitemap.xml (1 sitemaps listed) |
| sitemap | Lockheed Martin | fail | sitemap: no job URLs (1 sitemaps listed) |
| sitemap | UnitedHealth Group | ok via https://careers.unitedhealthgroup.com/sitemap.xml, 8 pages read | AI ML Engineer; Account Executive Healthcare Sales; Senior Director, Strategy & Transformation, Integrated Specialty Care - Remote |
| sitemap | ExxonMobil | fail | sitemap: no job URLs (1 sitemaps listed) |
| sitemap | IBM | fail | sitemap: no job URLs (6 sitemaps listed) |
| sitemap | Google | fail | sitemap: no job URLs (1 sitemaps listed) |
| sitemap | Oracle | fail | sitemap: no job URLs (1 sitemaps listed) |
| sitemap | Home Depot | ok via https://careers.homedepot.com/jobsitemap, 8 pages read | Cashier; MERCHANDISING; Cashier |
| sitemap | Walmart | ok via https://careers.walmart.com/sitemap.xml, 0 pages read |  |
| sitemap | Deloitte | fail | sitemap: no job URLs (17 sitemaps listed) |
| sitemap | EY | ok via https://careers.ey.com/sitemap.xml, 0 pages read |  |
| sitemap | PwC | fail | HTTPSConnectionPool(host='jobs.us.pwc.com', port=443): Max retries exceeded with (1 sitemaps listed) |
| sitemap | Citi | ok via https://jobs.citi.com/sitemap.xml, 8 pages read | Banamex - Banquero de Relación CIB; BANAMEX Recepcionista de Accesos y Seguridad; BANAMEX Especialista Senior de Partes Relacionadas en Contraloria In |
| sitemap | Bank of America | ok via https://careers.bankofamerica.com/sitemap_index.xml, 0 pages read |  |
| sitemap | AT&T | ok via https://www.att.jobs/sitemap.xml, 8 pages read | Director- Data Science; Associate Director-Chief of Staff; Senior Client Solutions Executive II Mobility (Government) |
| sitemap | Verizon | ok via https://mycareer.verizon.com/sitemap.xml, 0 pages read |  |
| sitemap | Dell Technologies | fail | 403 Client Error: Forbidden for url: https://jobs.dell.com/sitemap.xml (1 sitemaps listed) |
| sitemap | Tesla | fail | 403 Client Error: Forbidden for url: https://www.tesla.com/sitemap.xml (1 sitemaps listed) |
| sitemap | Meta | fail | 400 Client Error: Bad Request for url: https://www.metacareers.com/jobsearch/sit (2 sitemaps listed) |
| sitemap | ConocoPhillips | fail | sitemap: no job URLs (1 sitemaps listed) |
| sitemap | Halliburton | ok via https://careers.halliburton.com/sitemap.xml, 8 pages read | Accountant; Ecuador-Francisco de Orellana-Supervisor de Producción; Becario para Atraccion de Talento |
| sitemap | Kinder Morgan | fail | HTTPSConnectionPool(host='kindermorgan.jobs', port=443): Max retries exceeded wi (1 sitemaps listed) |

## Ready-to-paste entries

```yaml
- {"name": "Netflix", "ats": "eightfold", "host": "explore.jobs.netflix.net", "domain": "netflix.com", "tier": 1}
- {"name": "HPE", "ats": "phenom", "host": "careers.hpe.com", "locale": "us/en", "tier": 1}
- {"name": "Thermo Fisher Scientific", "ats": "phenom", "host": "jobs.thermofisher.com", "locale": "us/en", "tier": 1}
- {"name": "CVS Health", "ats": "phenom", "host": "jobs.cvshealth.com", "locale": "us/en", "tier": 1}
- {"name": "Mastercard", "ats": "phenom", "host": "careers.mastercard.com", "locale": "us/en", "tier": 1}
- {"name": "Lowe's", "ats": "phenom", "host": "talent.lowes.com", "locale": "us/en", "tier": 1}
- {"name": "UnitedHealth Group", "ats": "sitemap", "sitemap": "https://careers.unitedhealthgroup.com/sitemap.xml", "tier": 1}
- {"name": "Home Depot", "ats": "sitemap", "sitemap": "https://careers.homedepot.com/jobsitemap", "tier": 1}
- {"name": "Citi", "ats": "sitemap", "sitemap": "https://jobs.citi.com/sitemap.xml", "tier": 1}
- {"name": "AT&T", "ats": "sitemap", "sitemap": "https://www.att.jobs/sitemap.xml", "tier": 1}
- {"name": "Halliburton", "ats": "sitemap", "sitemap": "https://careers.halliburton.com/sitemap.xml", "tier": 1}
```
