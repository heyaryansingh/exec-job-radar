# Collector test report (dry run: nothing saved)

```
{
 "run_at": "2026-10-19T20:45:50+00:00",
 "seconds": 165,
 "companies": 499,
 "company_errors": 0,
 "skipped_backoff": 0,
 "skipped_out_of_time": 0,
 "senior_titles_seen": 4182,
 "new_roles": 95,
 "merged_duplicates": 1,
 "reposted": 0,
 "closed_after_check": 1,
 "removed_by_rule_change": 0,
 "open_roles": 846,
 "roles_in_latest": 846,
 "universe_boards": 300,
 "universe_polled_ok": 280,
 "universe_errors": 20,
 "names_learned": 185,
 "employer_sites_found_on_boards": 107,
 "sources": {
  "board-indeed (raw)": 242,
  "themuse": 0,
  "adzuna": 0,
  "senior titles from boards/aggregators": 93
 },
 "companies_with_open_roles": 251
}
```

## Senior titles seen, by source

- workday: 1579
- greenhouse: 1552
- oracle: 528
- ashby: 246
- smartrecruiters: 140
- board-indeed: 80
- lever: 57

## Universe boards: 280 answered, 20 failed

- 20 × 404 Client Error: Not Found for url: https://boards-api.gree

## Names learned (sample)

- greenhouse:axon → Axon
- greenhouse:via → Via
- greenhouse:appdirect → AppDirect
- greenhouse:verkada → Verkada
- greenhouse:alpaca → Alpaca
- greenhouse:alphasense → AlphaSense
- greenhouse:trueanomalyinc → True Anomaly
- greenhouse:xai → SpaceXSI
- greenhouse:formlabs → Formlabs
- greenhouse:addepar1 → Addepar
- greenhouse:blankstreet → Blank Street
- greenhouse:archer56 → Archer
- greenhouse:awin → Awin
- greenhouse:accelschools → ACCEL Schools
- greenhouse:mineralystherapeutics → Mineralys Therapeutics
- greenhouse:astranis → Astranis
- greenhouse:blinkhealth → Blink Health
- greenhouse:antora → Antora Energy
- greenhouse:altentechnologyusa → ALTEN Technology USA
- greenhouse:capco → Capco
- greenhouse:allcareers → Cortica - Neurodevelopmental
- greenhouse:betatechnologiesinc → BETA Technologies
- greenhouse:atwellgroup → Atwell, LLC
- greenhouse:gomotive → Motive
- greenhouse:bouldercare → Boulder Care
- greenhouse:bitgo → BitGo
- greenhouse:relativity → Relativity Space
- greenhouse:feverup → FeverUp
- greenhouse:canonical → Canonical
- greenhouse:algolia → Algolia
- greenhouse:assetliving → Asset Living
- greenhouse:attentive → Attentive
- greenhouse:bevicareers → Bevi
- greenhouse:aircallioinc → Aircall.io, Inc.
- greenhouse:berkshiregroupllc → Berkshire Group, LLC
- greenhouse:redwoodmaterials → Redwood Materials
- greenhouse:apolloio → Apollo.io
- greenhouse:2k → 2K
- greenhouse:blackbirdhealth → Blackbird Health
- greenhouse:justworks → Justworks

## Roles from universe boards that pass the rules (50), sample

| Score | Company | Role | Location | Pay |
|---:|---|---|---|---|
| 77 | Judi Health | [SVP, Platform](https://job-boards.greenhouse.io/judihealth/jobs/5455909008) | Charlotte, North Carolina, United States | 358600 |
| 67 | AiDASH, Inc. | [Head of Engineering, AI Platform](https://job-boards.greenhouse.io/aidashinc/jobs/4454159009) | Palo Alto, California, United States | 330000 |
| 63 | BillionToOne | [Senior Director, Software Product Management and Product Engineering](https://job-boards.greenhouse.io/billiontoone/jobs/4741480005) | Menlo Park, CA | 304619 |
| 62 | 3Cloud | [Director - Data Platforms & Architecture](https://job-boards.greenhouse.io/3cloud/jobs/8858565002?gh_jid=8858565002) | Remote - US | 244200 |
| 62 | Care Access | [Director, Engineering (AI Patient Engagement Platform)](https://job-boards.greenhouse.io/careaccess/jobs/4444401009) | USA Remote | 230000 |
| 59 | AXS | [Sr. Director, Software Engineering - B2B](https://job-boards.greenhouse.io/axs/jobs/8859213002) | San Francisco, CA | 290000 |
| 59 | AXS | [Sr. Director, Software Engineering - B2B](https://job-boards.greenhouse.io/axs/jobs/8856787002) | Los Angeles, CA | 265000 |
| 58 | Attentive | [Director of Engineering, Cloud Platform](https://job-boards.greenhouse.io/attentive/jobs/4438176009) | United States | 305000 |
| 58 | TraceLink, Inc | [Director, Applied Artificial Intelligence](https://www.tracelink.com/about/culture-and-careers/jobs?gh_jid=5257415007) | US - MA - Wilmington | 347100 |
| 57 | Via | [Director of AI Engineering, Internal Products](https://job-boards.greenhouse.io/via/jobs/8892068002) | New York | 290000 |
| 57 | Voyager Technologies, Inc. | [Principal Technical Director, National Security](https://job-boards.greenhouse.io/voyagertechnologiesinc/jobs/4424878009) | Washington D.C.; Long Beach, CA | 300000 |
| 56 | Via | [Head of AI Research Product](https://job-boards.greenhouse.io/via/jobs/8885508002) | New York, New York | 310000 |
| 56 | Abacus Insights | [Head of Technical Product Management](https://boards.greenhouse.io/abacusinsights/jobs/8881341002?gh_jid=8881341002) | United States |  |
| 55 | Carrot | [Director, Information Security](https://job-boards.greenhouse.io/carrotfertility/jobs/6223408004) | Remote |  |
| 54 | Planet | [Director of Software Engineering, Analytics](https://job-boards.greenhouse.io/planetlabs/jobs/8249630) | Arlington, VA; Denver, CO | 225900 |
| 53 | BridgeBio Pharma | [Sr Director/Executive Director, Pharm Science Technical Lead](https://job-boards.greenhouse.io/bridgebio/jobs/5256185007) | San Francisco - 1800 Owens | 331900 |
| 52 | Attentive | [Senior Director, Product Management (AI/ML)](https://job-boards.greenhouse.io/attentive/jobs/4415182009) | New York, NY | 352000 |
| 52 | Planet | [Senior Director, Product Management - Defense and Intelligence](https://job-boards.greenhouse.io/planetlabs/jobs/8263945) | San Francisco, CA | 325600 |
| 52 | 6sense | [VP, Technology & Data Partnerships](https://boards.greenhouse.io/6sense/jobs/8273672?gh_jid=8273672) | San Francisco, California, United States |  |
| 52 | Defense Unicorns | [Mission Director - Air Force](https://job-boards.greenhouse.io/defenseunicorns/jobs/5265069007) | United States - Remote | 370000 |
| 52 | Defense Unicorns | [Mission Director - Army](https://job-boards.greenhouse.io/defenseunicorns/jobs/5265620007) | United States - Remote | 370000 |
| 52 | Defense Unicorns | [Mission Director - Army](https://job-boards.greenhouse.io/defenseunicorns/jobs/5265742007) | United States - Remote | 370000 |
| 50 | Coupang | [[CES] Director, Program Management (Head of Rider Operation)](https://www.coupang.jobs/en/jobs/?gh_jid=8300070) | Seoul, South Korea |  |
| 50 | 3Cloud | [Delivery Director - Project Delivery](https://job-boards.greenhouse.io/3cloud/jobs/8883941002?gh_jid=8883941002) | Remote - US | 212000 |
| 49 | PlayStation Global | [Senior Director, Corporate Security & Crisis Management](https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6218033004) | United States, San Diego, CA | 343000 |
| 49 | Gravitics, Inc | [Head of Engineering](https://job-boards.greenhouse.io/graviticsinc/jobs/4429975009) | Greater Denver Area | 275000 |
| 48 | Axsome Therapeutics | [Director, IT Operations](https://job-boards.greenhouse.io/axsometherapeutics/jobs/6224138004) | New York, NY | 225000 |
| 48 | Apptronik | [Senior Director of Product Security](https://boards.greenhouse.io/apptronik/jobs/6119788004?gh_jid=6119788004) | Austin, TX |  |
| 48 | Planet | [Senior Director, Product Management - Defense and Intelligence](https://job-boards.greenhouse.io/planetlabs/jobs/8287786) | Arlington, VA | 285900 |
| 48 | Coupang | [Director of Engineering, Fulfillment Optimization (Global Operations Technology)](https://www.coupang.jobs/en/jobs/?gh_jid=8207192) | Seoul, South Korea |  |
| 48 | Coupang | [[쿠팡이츠서비스] Director, Program Management (Head of Rider Operation)](https://www.coupang.jobs/en/jobs/?gh_jid=8299809) | Seoul, South Korea |  |
| 48 | Natera | [Director of Bioinformatics and Machine Learning](https://job-boards.greenhouse.io/natera/jobs/6226991004) | San Carlos, CA | 285800 |
| 48 | Defense Unicorns | [Director of Federal Operations](https://job-boards.greenhouse.io/defenseunicorns/jobs/5265272007) | Remote | 250000 |
| 47 | Formlabs | [Head of Software Product Management](https://careers.formlabs.com/job/8273112/apply/?gh_jid=8273112) | Somerville, MA | 260000 |
| 47 | AlertMedia | [Director, Solutions Engineering](https://job-boards.greenhouse.io/alertmedia/jobs/8885284002) | Austin, TX HQ |  |
| 47 | Apex Skin | [Information Technology Director](https://job-boards.greenhouse.io/apexskincareers/jobs/4436564009) | Corporate |  |
| 46 | Attentive | [Director, AI Developer Experience](https://job-boards.greenhouse.io/attentive/jobs/4443888009) | New York, NY | 385000 |
| 46 | Voyager Technologies, Inc. | [Senior Director, Launch Systems](https://job-boards.greenhouse.io/voyagertechnologiesinc/jobs/4420562009) | Mojave, CA | 270000 |
| 46 | Natera | [Data Privacy Director](https://job-boards.greenhouse.io/natera/jobs/6224695004) | US Remote |  |
| 45 | Verkada | [Director of Business Systems Product Management](https://job-boards.greenhouse.io/verkada/jobs/5238205007) | San Mateo, CA United States | 310000 |
| 45 | Cohere Health | [Director, Solutions Architecture](https://job-boards.greenhouse.io/coherehealth/jobs/8013507003) | United States | 215000 |
| 45 | CHAOS Industries | [Director, Electrical Engineering](https://job-boards.greenhouse.io/chaosindustries/jobs/5258939007) | El Segundo, California, United States | 321000 |
| 44 | Bevi | [Director, Embedded Engineering](https://job-boards.greenhouse.io/bevicareers/jobs/4452481009) | Boston | 245700 |
| 44 | ALO | [Director, DC Security & Asset Protection](https://boards.greenhouse.io/aloyoga/jobs/6222779004?gh_jid=6222779004) | Remote |  |
| 43 | GuidePoint Security | [Director, OT/IoT Security Services- Remote (Anywhere in the U.S.)](https://boards.greenhouse.io/guidepointsecurity/jobs/6214798004?gh_jid=6214798004) | Remote |  |
| 42 | Voyager Technologies, Inc. | [Director of Advanced Technology Programs](https://job-boards.greenhouse.io/voyagertechnologiesinc/jobs/4454592009) | Reno, NV | 265202 |
| 40 | Bevi | [Director, Program Management](https://job-boards.greenhouse.io/bevicareers/jobs/4453157009) | Boston | 239400 |
| 39 | Astranis | [Director, National Security Programs Development](https://job-boards.greenhouse.io/astranis/jobs/4718942006) | San Francisco, CA | 225000 |
| 39 | Careers at Tide | [Director of Engineering, KYX](https://job-boards.greenhouse.io/tide/jobs/8014191003) | Bulgaria |  |
| 38 | Coupang | [Director, Cybersecurity Audit & Continuous Assurance](https://www.coupang.jobs/en/jobs/?gh_jid=8280895) | Seoul, South Korea |  |

## Roles from job boards / aggregators that pass (29), sample

| Source | Company | Role | Location |
|---|---|---|---|
| board-indeed | Apple | [Director, Evaluation and Quality Assurance, Services Special Projects](https://jsv3.recruitics.com/redirect?rx_cid=3427&rx_jobId=200688194-0836&rx_url=https%3A%2F%2Fjobs.apple.com%2Fen-us%2Fdetails%2F200688194-0836%2Fdirector-evaluation-and-quality-assurance-services-special-projects%3Fboard_id%3DJB001%26rx_a%3D0%26rx_c%3D%26rx_ch%3Djobp4p%26rx_group%3D122365%26rx_id%3D5f6b2fcc-caac-11f1-8182-33e277e81f23%26rx_job%3D200688194-0836%26rx_medium%3Dcpc%26rx_r%3Dnone%26rx_source%3Dindeed%26rx_ts%3D20261018T220404Z%26rx_vp%3Dcpc%26team%3DSFTWR) | Cupertino, CA, USA |
| board-indeed | Avangrid | [Senior Director - Technology](https://iberdrola.wd3.myworkdayjobs.com/en-US/Iberdrola/job/United-States-Of-America-Connecticut-Orange/Senior-Director---Technology_R-34509) | Orange, CT, USA |
| board-indeed | Cisco | [Director - ASIC Engineering (Technical Planning and Engineering Execution)](https://careers.cisco.com/global/en/job/2028602) | San Jose, CA, USA |
| board-indeed | EPAM Systems | [Chief Technology Officer — Databricks Data & AI Platform](https://careers.epam.com/en/vacancy/bltbgo9kfba0zgmjjw7_en?country=USA&utm_source=indeed&utm_medium=xml-job-feed&utm_campaign=ta) | Remote, USA |
| board-indeed | Hewlett Packard Enterprise | HPE | [Director, Chief of Staff for Hybrid Cloud COO](https://careers.hpe.com/us/en/job/HPE1US1217311EXTERNALENUS/Director-Chief-of-Staff-for-Hybrid-Cloud-COO?utm_source=indeed&utm_medium=phenom-feeds) | San Jose, CA, USA |
| board-indeed | Huntsville Hospital Health System | [Vice President, Technology Services](https://careers-hhsys.icims.com/jobs/76558/job?utm_source=indeed_integration&iis=Job%20Board&iisn=Indeed&indeed-apply-token=73a2d2b2a8d6d5c0a62696875eaebd669103652d3f0c2cd5445d3e66b1592b0f) | Huntsville, AL, USA |
| board-indeed | Network Distribution | [Vice President, Business Technology Services](https://recruiting2.ultipro.com/NET1010NWRK/JobBoard/337433be-8153-4eda-8b37-455548451ef9/OpportunityDetail?opportunityId=888e0bae-0e04-4a24-a34c-24305c7d346b&postingId=a104f3d2-4548-4259-87c5-77a8c06627fa) | Schaumburg, IL, USA |
| board-indeed | Overwatch Mission Critical | [VP of Information Systems & Security](https://jobs.gem.com/overwatch/am9icG9zdDpXpvKaoJ2NrkqAtDjqtonp) | Austin, TX, USA |
| board-indeed | Select Milk Producers (SMP) | [Vice President of Technology](https://selectmilk.wd12.myworkdayjobs.com/SelectMilkProducers/job/Dallas-TX/Vice-President-of-Technology_JR102201) | Dallas, TX, USA |
| board-indeed | Siemens Healthineers | [Head of IT DX Strategy & Management Services](https://onehealthineers.wd3.myworkdayjobs.com/SHSJB/job/TAR-B/Head-of-IT-DX-Strategy---Management-Services_R-31383) | Remote, USA |
| board-indeed | Starbucks | [director, AI Transformation](https://click.appcast.io/t/Umr0W6u0BxHM5m0M3KO0lograP_bCWe4X6Up5S_md1E=) | Seattle, WA, USA |
| board-indeed | State of Wyoming | [WCCC Director of Information Technology 2026-02526](https://www.governmentjobs.com/careers/wyoming/jobs/5516302/wccc-director-of-information-technology-2026-02526) | Cheyenne, WY, USA |
| board-indeed | TransUnion | [Vice President, Artificial Intelligence Research & Development](https://transunion.wd5.myworkdayjobs.com/en-US/TransUnion/job/Chicago---555-West-Adams-St/Vice-President--Artificial-Intelligence-Research---Development_19042485) | Chicago, IL, USA |
| board-indeed | United Biosource Corporation | [Director, Software Engineering - Platform Development](https://workforcenow.adp.com/mascsr/default/mdf/recruitment/recruitment.html?cid=90ee0c52-4563-4bbb-a44d-0a6cd6964c61&ccId=19000101_000001&jobId=593232&source=IN&lang=en_US) | Remote, USA |
| board-indeed | Verustruct | [Head of Engineering](https://jobs.ashbyhq.com/verustruct/066cbb11-8a0a-4921-9596-47de948bff28?utm_source=p4jNLwy4oq) | Torrance, CA, USA |
| board-indeed | Tiverton Advisors | [Vice President, Portfolio Technology Operations](https://jobs.smartrecruiters.com/TivertonAdvisors/744000156394225-vice-president-portfolio-technology-operations) | Los Angeles, CA, USA |
| board-indeed | LPL Financial | [VP, Software Engineering Lead (.NET/AWS)](https://lplfinancial.wd1.myworkdayjobs.com/External/job/New-York/VP--Software-Engineering-Lead--NET-AWS-_R-054347-1) | New York, NY, USA |
| board-indeed | Pedestal Health | [Head of Technology](https://grnh.se/ycahr7vl8us) | Durham, NC, USA |
| board-indeed | GSK | [Director, Real World Data Strategy and External Partnerships Lead](https://jobs.gsk.com/gb/en/job/449565?utm_source=indeed&utm_medium=phenom-feeds) | Collegeville, PA, USA |
| board-indeed | BigHat Biosciences | [Director of Machine Learning](https://bighatbiosciences.pinpointhq.com/postings/0c79bfdf-a3f1-4e55-a1e4-93abb5930c45?utm_medium=job_board&utm_source=indeed) | San Mateo, CA, USA |
| board-indeed | MiniMed | [Director, Cyber Defense](https://mdtkangaroo.wd108.myworkdayjobs.com/en-US/MiniMedCareers/job/Virtual-Minnesota-United-States-of-America/Director--Cyber-Defense_R-802217) | MN, USA |
| board-indeed | Cisco | [Director, Product Management](https://careers.cisco.com/global/en/job/2028398) | San Jose, CA, USA |
| board-indeed | FNBO - First National Bank of Omaha | [Sr. Director, Advanced Data Scientist](https://firstnational.wd12.myworkdayjobs.com/en-US/fnbocareers/job/Omaha---FN-Tower/Sr-Director--Advanced-Data-Scientist_R-20261856) | Omaha, NE, USA |
| board-indeed | Merck | [Executive Director, AI Delivery Management](https://jobs.merck.com/us/en/job/R422940) | Rahway, NJ, USA |
| board-indeed | PGA TOUR Superstore | [Sr. Director, Digital & Ecommerce](https://pgatoursuperstore.wd12.myworkdayjobs.com/en-US/PGAT_SS/job/Store-Support-Center---Roswell-GA/Sr-Director--Digital---Ecommerce_JR7956) | Roswell, GA, USA |
| board-indeed | Advocate Aurora Health | [Director Data Center & Enterprise Operations](https://AdvocateAuroraHealth.contacthr.com/153953834) | Oak Brook, IL, USA |
| board-indeed | City and County of San Francisco | [0942 Manager VII – Managing Director, Finance - SFO (Eligible list ID 167697)](https://jobs.smartrecruiters.com/CityAndCountyOfSanFrancisco1/3743990016232883-0942-manager-vii-managing-director-finance-sfo-eligible-list-id-167697-) | San Francisco, CA, USA |
| board-indeed | Anduril | [Director, Production Analytics](https://grnh.se/3y1ln9ut7us) | Costa Mesa, CA, USA |
| board-indeed | Phykion | [Director of Scale-up Operations and Engineering](https://www.indeed.com/viewjob?jk=42281172359c57a7) | Calipatria, CA, USA |

## Employer career sites found in board results (107), sample

- Tiverton Advisors: `{"ats": "smartrecruiters", "slug": "TivertonAdvisors"}`
- STACK Infrastructure US: `{"ats": "workday", "host": "stackinfra.wd108.myworkdayjobs.com", "site": "STACK_AMER"}`
- Orchard Marketing New York: `{"ats": "smartrecruiters", "slug": "Enero"}`
- Filevine: `{"ats": "lever", "slug": "filevine"}`
- Mozilla Corporation: `{"ats": "greenhouse", "slug": "mozilla"}`
- Trustly: `{"ats": "ashby", "slug": "trustly"}`
- LPL Financial: `{"ats": "workday", "host": "lplfinancial.wd1.myworkdayjobs.com", "site": "External"}`
- Tutor Perini Corporation: `{"ats": "workday", "host": "tutorperini.wd12.myworkdayjobs.com", "site": "external"}`
- Rezolute: `{"ats": "lever", "slug": "rezolutebio"}`
- Raptive: `{"ats": "ashby", "slug": "raptive"}`
- Turner & Townsend Pty Limited: `{"ats": "smartrecruiters", "slug": "TurnerTownsend"}`
- MiniMed: `{"ats": "workday", "host": "mdtkangaroo.wd108.myworkdayjobs.com", "site": "MiniMedCareers"}`
- Avangrid: `{"ats": "workday", "host": "iberdrola.wd3.myworkdayjobs.com", "site": "Iberdrola"}`
- Wells Fargo: `{"ats": "workday", "host": "wd1.myworkdaysite.com", "tenant": "wf", "site": "WellsFargoJobs", "public_base": "https://wd1.myworkdaysite.com/en-US/recruiting/wf/WellsFargoJobs"}`
- Slate Auto: `{"ats": "workday", "host": "recar.wd108.myworkdayjobs.com", "site": "SLATEcareers"}`
- Shine Early Learning: `{"ats": "workday", "host": "acelero.wd1.myworkdayjobs.com", "site": "ShineEarlyLearningCareers"}`
- Salesforce: `{"ats": "workday", "host": "salesforce.wd12.myworkdayjobs.com", "site": "External_Career_Site"}`
- NVIDIA: `{"ats": "workday", "host": "nvidia.wd5.myworkdayjobs.com", "site": "NVIDIAExternalCareerSite"}`
- Visa: `{"ats": "workday", "host": "visa.wd5.myworkdayjobs.com", "site": "Visa"}`
- STACK Infrastructure US: `{"ats": "workday", "host": "stackinfra.wd108.myworkdayjobs.com", "site": "STACK_AMER"}`
- Wells Fargo: `{"ats": "workday", "host": "wd1.myworkdaysite.com", "tenant": "wf", "site": "WellsFargoJobs", "public_base": "https://wd1.myworkdaysite.com/en-US/recruiting/wf/WellsFargoJobs"}`
- Arizent: `{"ats": "ashby", "slug": "arizent"}`
- OpenLoop Health: `{"ats": "ashby", "slug": "openloophealth"}`
- National Vision, Inc.: `{"ats": "smartrecruiters", "slug": "NationalVision1"}`
- Turner & Townsend Pty Limited: `{"ats": "smartrecruiters", "slug": "TurnerTownsend"}`
- Summit Behavioral Healthcare: `{"ats": "workday", "host": "summitbhc.wd1.myworkdayjobs.com", "site": "Summit_BHC"}`
- MiniMed: `{"ats": "workday", "host": "mdtkangaroo.wd108.myworkdayjobs.com", "site": "MiniMedCareers"}`
- Shine Early Learning: `{"ats": "workday", "host": "acelero.wd1.myworkdayjobs.com", "site": "ShineEarlyLearningCareers"}`
- Moderna: `{"ats": "workday", "host": "modernatx.wd1.myworkdayjobs.com", "site": "M_tx"}`
- Avangrid: `{"ats": "workday", "host": "iberdrola.wd3.myworkdayjobs.com", "site": "Iberdrola"}`

Wall time: 166s
