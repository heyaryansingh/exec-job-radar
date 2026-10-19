# Collector test report (dry run: nothing saved)

```
{
 "run_at": "2026-10-19T20:52:31+00:00",
 "seconds": 295,
 "companies": 499,
 "company_errors": 0,
 "skipped_backoff": 0,
 "skipped_out_of_time": 0,
 "senior_titles_seen": 4753,
 "new_roles": 126,
 "merged_duplicates": 2,
 "reposted": 0,
 "closed_after_check": 0,
 "removed_by_rule_change": 14,
 "open_roles": 902,
 "roles_in_latest": 902,
 "universe_boards": 600,
 "universe_polled_ok": 570,
 "universe_errors": 30,
 "names_learned": 347,
 "employer_sites_found_on_boards": 130,
 "sources": {
  "board-indeed (raw)": 255,
  "themuse": 0,
  "adzuna": 0,
  "senior titles from boards/aggregators": 99
 },
 "companies_with_open_roles": 295
}
```

## Senior titles seen, by source

- workday: 2040
- greenhouse: 1305
- ashby: 577
- oracle: 533
- smartrecruiters: 162
- board-indeed: 77
- lever: 59

## Universe boards: 570 answered, 30 failed

- 14 × 404 Client Error: Not Found for url: https://boards-api.gree
- 2 × 404 Client Error: Not Found for url: https://api.ashbyhq.com
- 2 × 422 Client Error: Unprocessable Entity for url: https://fran
- 1 × 404 Client Error: Not Found for url: https://highmarkhealth.
- 1 × 404 Client Error: Not Found for url: https://3m.wd1.myworkda
- 1 × 404 Client Error: Not Found for url: https://fhi.wd1.myworkd
- 1 × 404 Client Error: Not Found for url: https://okgov.wd1.mywor
- 1 × 403 Client Error: Forbidden for url: https://csl.wd1.myworkd

## Names learned (sample)

- ashby:bjakcareer → Bjak
- ashby:deepgram → Deepgram
- greenhouse:axon → Axon
- ashby:applied → Applied Intuition
- greenhouse:via → Via
- greenhouse:verkada → Verkada
- greenhouse:appdirect → AppDirect
- greenhouse:alphasense → AlphaSense
- ashby:rula → Rula
- greenhouse:alpaca → Alpaca
- workday:cox.wd1.myworkdayjobs.com:cox:cox_external_career_site_1 → CAI Cox Automotive Corp Svcs., LLC
- greenhouse:trueanomalyinc → True Anomaly
- ashby:rain → Rain
- greenhouse:formlabs → Formlabs
- ashby:volta → Volta
- greenhouse:xai → SpaceXSI
- ashby:clera → Clera
- greenhouse:addepar1 → Addepar
- greenhouse:blankstreet → Blank Street
- workday:wd1.myworkdaysite.com:snapchat:snap → Snap Inc.
- workday:cardinalhealth.wd1.myworkdayjobs.com:cardinalhealth:ext → 112 Cardinal Health 5, LLC
- ashby:zip → Zip
- greenhouse:archer56 → Archer
- ashby:chainalysis-careers → Chainalysis
- greenhouse:awin → Awin
- workday:osu.wd1.myworkdayjobs.com:osu:osucareers → The Ohio State University
- ashby:sardine → Sardine
- greenhouse:accelschools → ACCEL Schools
- workday:boydgroup.wd1.myworkdayjobs.com:boydgroup:boydcareers → Gerber Payroll Services, Inc.
- ashby:1x → 1X
- workday:altera.wd1.myworkdayjobs.com:altera:altera → 191 Altera Corporation
- workday:bah.wd1.myworkdayjobs.com:bah:bah_jobs → 631 Booz Allen Hamilton_United States
- greenhouse:mineralystherapeutics → Mineralys Therapeutics
- ashby:xona-space → Xona Space Systems
- greenhouse:astranis → Astranis
- workday:3m.wd1.myworkdayjobs.com:3m:search → USA 3M Company
- workday:bilh.wd1.myworkdayjobs.com:bilh:external → Beth Israel Lahey Health, Inc.
- workday:asmglobal.wd1.myworkdayjobs.com:asmglobal:careers → Legends Hospitality, LLC
- ashby:skydio → Skydio
- greenhouse:blinkhealth → Blink Health

## Roles from universe boards that pass the rules (125), sample

| Score | Company | Role | Location | Pay |
|---:|---|---|---|---|
| 77 | Judi Health | [SVP, Platform](https://job-boards.greenhouse.io/judihealth/jobs/5455909008) | Charlotte, North Carolina, United States | 358600 |
| 73 | Second Front Systems | [Head of Security Compliance & Authorization](https://jobs.ashbyhq.com/Second-Front-Systems/03680ea0-ba43-4914-9955-241c2768e50f) | Remote | 215000 |
| 69 | 191 Altera Corporation | [Senior Director, Silicon Architecture and Design Engineering (Ethernet/PCIe Center of Excellence))](https://altera.wd1.myworkdayjobs.com/Altera/job/San-Jose-California-United-States/Senior-Director--Silicon-Architecture-and-Design-Engineering--Ethernet-_R03226) | San Jose, California, United States | 341075 |
| 68 | 001 Brown & Brown, Inc | [Head of AI and Data Platform Engineering - Specialty Distribution](https://bbinsurance.wd1.myworkdayjobs.com/Careers/job/Plano-TX-USA/Head-of-AI-and-Data-Platform-Engineering---Specialty-Distribution_R26_0000002462-1) | Plano, TX, USA; Daytona Beach, FL, USA |  |
| 65 | Openly | [VP, Insurance Data Science](https://jobs.ashbyhq.com/openly/4647f9c5-0eb4-4770-8b43-e21d45215f95) | Remote - United States | 350000 |
| 64 | 001 Brown & Brown, Inc | [VP, IT Strategy and Architecture](https://bbinsurance.wd1.myworkdayjobs.com/Careers/job/Plano-TX-USA/VP--IT-Strategy-and-Architecture_R26_0000002301) | Plano, TX, USA |  |
| 64 | 001 Brown & Brown, Inc | [Head of Software Engineering](https://bbinsurance.wd1.myworkdayjobs.com/Careers/job/Plano-TX-USA/Head-of-Software-Engineering_R26_0000003460) | Plano, TX, USA |  |
| 63 | 1000 Becton, Dickinson and Company | [Director ISC Data and AI](https://bdx.wd1.myworkdayjobs.com/EXTERNAL_CAREER_SITE_USA/job/USA-UT---Sandy/Director-ISC-Data-and-AI_R-556906) | USA UT - Sandy |  |
| 63 | BillionToOne | [Senior Director, Software Product Management and Product Engineering](https://job-boards.greenhouse.io/billiontoone/jobs/4741480005) | Menlo Park, CA | 304619 |
| 63 | 001 Brown & Brown, Inc | [Director, AI & Security Development](https://bbinsurance.wd1.myworkdayjobs.com/Careers/job/Remote---USA/Director--AI---Security-Development_R26_0000002016) | Remote - USA | 214000 |
| 62 | Orchard Marketing New York | [Orchard - VP, Client Services & Digital Transformation](https://jobs.smartrecruiters.com/Enero/6000000001500101-orchard-vp-client-services-digital-transformation) | New York, New York, us |  |
| 62 | Skydio | [Director of Product Management, Platform & Infrastructure](https://jobs.ashbyhq.com/Skydio/073e72a7-b7e1-4d7a-b64d-fade3c209fc9) | San Mateo, California, United States | 290000 |
| 62 | 3Cloud | [Director - Data Platforms & Architecture](https://job-boards.greenhouse.io/3cloud/jobs/8858565002?gh_jid=8858565002) | Remote - US | 244200 |
| 62 | Care Access | [Director, Engineering (AI Patient Engagement Platform)](https://job-boards.greenhouse.io/careaccess/jobs/4444401009) | USA Remote | 230000 |
| 61 | Bjak | [Chief Technology Officer](https://jobs.ashbyhq.com/bjakcareer/1262bcda-3197-43db-a540-520d44452004) | United States |  |
| 61 | 100 The Gap, Inc. | [Sr. Director - AI & Agentic Platform Engineering](https://gapinc.wd1.myworkdayjobs.com/GAPINC/job/SF---2-Folsom/Sr-Director---AI---Agentic-Platform-Engineering_R219376) | SF - 2 Folsom; Dallas-Coppell/Vari |  |
| 60 | 1240 Invesco Distributors Inc. | [Head of Digital Asset Distribution](https://invesco.wd1.myworkdayjobs.com/IVZ/job/New-York-New-York/Head-of-Digital-Asset-Distribution_R-14010-1) | New York, New York; Atlanta, Georgia | 300000 |
| 59 | AXS | [Sr. Director, Software Engineering - B2B](https://job-boards.greenhouse.io/axs/jobs/8856787002) | Los Angeles, CA | 265000 |
| 59 | AXS | [Sr. Director, Software Engineering - B2B](https://job-boards.greenhouse.io/axs/jobs/8859213002) | San Francisco, CA | 290000 |
| 58 | 7Z4 Pfizer, Inc. | [Vice President, Digital Finance](https://pfizer.wd1.myworkdayjobs.com/PfizerCareers/job/United-States---New-York---New-York-City/Vice-President--Digital-Finance_4966112-1) | United States - New York - New York City |  |
| 58 | Attentive | [Director of Engineering, Cloud Platform](https://job-boards.greenhouse.io/attentive/jobs/4438176009) | United States | 305000 |
| 58 | CADENCE US | [Director of Software Security](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/SAN-JOSE/Director-of-Software-Security_R54237) | SAN JOSE | 305500 |
| 57 | Via | [Director of AI Engineering, Internal Products](https://job-boards.greenhouse.io/via/jobs/8892068002) | New York | 290000 |
| 57 | HAR Labcorp Early Development Laboratories Limited | [VP, Data and AI Readiness Platforms](https://labcorp.wd1.myworkdayjobs.com/en-US/External/job/Durham-NC/VP--Data-and-AI-Readiness-Platforms_2632570) | Durham NC |  |
| 57 | Voyager Technologies, Inc. | [Principal Technical Director, National Security](https://job-boards.greenhouse.io/voyagertechnologiesinc/jobs/4424878009) | Washington D.C.; Long Beach, CA | 300000 |
| 57 | Pluralsight, LLC | [Senior Director of Information Security (CISO)](https://pluralsight.wd1.myworkdayjobs.com/Careers/job/Remote---USA/Senior-Director-of-Information-Security--CISO-_R0014439) | Remote - USA | 265000 |
| 57 | EverCommerce Solutions Inc. | [Director Software Engineering - Bold Group - Security and Alarm (Remote, US)](https://evercommerce.wd1.myworkdayjobs.com/EverCommerce_Careers/job/Remote--US/Director-Software-Engineering---Bold-Group---Security-and-Alarm--Remote--US-_R-106575) | Remote- US |  |
| 56 | Via | [Head of AI Research Product](https://job-boards.greenhouse.io/via/jobs/8885508002) | New York, New York | 310000 |
| 56 | City and County of San Francisco | [0942 Manager VII – Managing Director, Finance - SFO (Eligible list ID 167697)](https://jobs.smartrecruiters.com/CityAndCountyOfSanFrancisco1/3743990016233476-0942-manager-vii-managing-director-finance-sfo-eligible-list-id-167697-) | San Francisco, CA, us | 274196 |
| 56 | Snap Inc. | [Director, Software Engineering, Product Eng](https://wd1.myworkdaysite.com/recruiting/snapchat/snap/job/Los-Angeles-California/Director--Software-Engineering--Product-Eng_R0047059-1) | Los Angeles, California; San Francisco,  | 500000 |
| 55 | 112 Cardinal Health 5, LLC | [Director, Security Architecture](https://cardinalhealth.wd1.myworkdayjobs.com/EXT/job/US-Nationwide-FIELD/Director--Security-Architecture_20187025) | US-Nationwide-FIELD | 261250 |
| 55 | Carrot | [Director, Information Security](https://job-boards.greenhouse.io/carrotfertility/jobs/6223408004) | Remote |  |
| 55 | CADENCE US | [SerDes IP Systems Engineering Director](https://cadence.wd1.myworkdayjobs.com/External_Careers/job/SAN-JOSE/Design-Engineering-Architect_R52908-1) | SAN JOSE | 331500 |
| 55 | ResolveAI | [Head of Technical Support](https://jobs.ashbyhq.com/ResolveAI/992e652e-cc88-4d66-9071-a318b41ae920) | San Francisco |  |
| 54 | Acquisition.com | [Director of Data](https://jobs.ashbyhq.com/acquisition/3b5fb996-c60a-479b-846a-bf3182a84027) | Remote, USA  | 275000 |
| 54 | Planet | [Director of Software Engineering, Analytics](https://job-boards.greenhouse.io/planetlabs/jobs/8249630) | Arlington, VA; Denver, CO | 225900 |
| 54 | PAE | [Senior Director, Business System Strategy & Transformation](https://pae.wd1.myworkdayjobs.com/Amentum_Careers/job/US-Remote/Senior-Director--Business-System-Strategy---Transformation_R0171879) | US-Remote |  |
| 53 | 1550 India PDC | [Director of Systems Engineering](https://analogdevices.wd1.myworkdayjobs.com/External/job/US-CA-Milpitas-Tasman/Systems-Engineering-Manager_R266735) | US, CA, Milpitas, Tasman | 307740 |
| 52 | Attentive | [Senior Director, Product Management (AI/ML)](https://job-boards.greenhouse.io/attentive/jobs/4415182009) | New York, NY | 352000 |
| 52 | HAR Labcorp Early Development Laboratories Limited | [Director, Lab Systems Software Development Engineering](https://labcorp.wd1.myworkdayjobs.com/en-US/External/job/USA---NC---Durham---10-Moore-Drive/Director--Lab-Systems-Software-Development-Engineering_2635318) | 2 Locations |  |
| 52 | 2012 CSL Behring L.L.C. | [Director, I&T Plasma Engineering](https://csl.wd1.myworkdayjobs.com/CSL_External/job/Americas-US-PA-King-of-Prussia-CSL-Behring/Director--I-T-Plasma-Engineering_R-293016) | Americas, US-PA, King of Prussia, CSL Be |  |
| 52 | News Corporate Services Inc. | [Director, Technical Vulnerability Management & Remediation Orchestration](https://dowjones.wd1.myworkdayjobs.com/News_Corp_Careers/job/NYC---1211-Ave-of-the-Americas/Director--Technical-Vulnerability-Management---Remediation-Orchestration_Job_Req_55981) | NYC - 1211 Ave of the Americas | 250000 |
| 52 | Planet | [Senior Director, Product Management - Defense and Intelligence](https://job-boards.greenhouse.io/planetlabs/jobs/8263945) | San Francisco, CA | 325600 |
| 52 | Slash Financial | [Chief Information Security Officer](https://jobs.ashbyhq.com/slash-financial/aa0be8a3-00ea-4a9e-9484-58942c41c7f8) | San Francisco Office |  |
| 52 | 6sense | [VP, Technology & Data Partnerships](https://boards.greenhouse.io/6sense/jobs/8273672?gh_jid=8273672) | San Francisco, California, United States |  |
| 52 | LXA Lexia Voyager Sopris Inc. | [Director, Data Strategy & Analytics](https://cambiumlearning.wd1.myworkdayjobs.com/camb/job/Remote/Director--Data-Strategy---Analytics_REQ-4643) | Remote |  |
| 51 | Rula | [Director of Finance Systems (Remote)](https://jobs.ashbyhq.com/rula/8f49abb1-6c5c-4fed-b2d3-a171dece403b) | Remote - United States | 244965 |
| 51 | AT&T Services, Inc. | [Director Cybersecurity - Enterprise Network Security](https://att.wd1.myworkdayjobs.com/ATTGeneral/job/USANJMiddletown--S-Laurel-Ave---Bldg-A200-S-Laurel-Ave-Bldg-A/Director-Cybersecurity---Enterprise-Network-Security_R-125427-1) | USA:NJ:Middletown / S Laurel Ave - Bldg  |  |
| 50 | 300 FLEXTRONICS MANUFACTURING MEX, SA DE CV. | [Sr. Director, Validation Test Engineering](https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-TX-Austin/Sr-Director--Validation-Test-Engineering_WD228339-1) | USA, TX, Austin |  |
| 50 | 3Cloud | [Delivery Director - Project Delivery](https://job-boards.greenhouse.io/3cloud/jobs/8883941002?gh_jid=8883941002) | Remote - US | 212000 |
| 50 | Trustees of University of Pennsylvania | [Executive Director – Penn Center for Language and Vision - Penn Engineering](https://wd1.myworkdaysite.com/recruiting/upenn/careers-at-penn/job/Comp-Info-Science-Moore/Executive-Director---Penn-Center-for-Language-and-Vision---Penn-Engineering_JR00129105) | Comp Info Science-Moore |  |
| 50 | 001 Brown & Brown, Inc | [Senior Director, Technology Solutions](https://bbinsurance.wd1.myworkdayjobs.com/Careers/job/Daytona-Beach-FL-USA/Senior-Director--Technology-Solutions_R26_0000001639-1) | Daytona Beach, FL, USA; Plano, TX, USA |  |
| 49 | TENEX.AI | [Director of Forward Deployed Engineering](https://jobs.ashbyhq.com/tenex/b2501a2a-4a55-40ff-b08c-430d76fbaa53) | Kansas City Metro; Sarasota, FL HQ; Scot |  |
| 49 | 0001 Applied Materials, Inc | [Director, Product AI Platform Architect](https://amat.wd1.myworkdayjobs.com/External/job/Santa-ClaraCA/Director--Product-AI-Platform-Architect_R2629698) | Santa Clara,CA |  |
| 49 | USA7 DXC Technology Services LLC | [Director Business Transformation](https://dxctechnology.wd1.myworkdayjobs.com/DXCJobs/job/USA---TX---ANY-CITY/Director-Business-Leadership_51587952) | USA - TX - ANY CITY | 289000 |
| 48 | Highmark Inc | [Director, Enterprise Data Platform Strategy & Engineering](https://highmarkhealth.wd1.myworkdayjobs.com/highmark/job/Pittsburgh-PA-15222-PAP-Penn-Avenue-Place/Direct-of-Data-Platform_J276952) | Pittsburgh PA, 15222, PAP, Penn Avenue P |  |
| 48 | Mayor and City Council of Baltimore | [Director of IT Infrastructure (NCS) - BCIT](https://baltimorecity.wd1.myworkdayjobs.com/External/job/401-E-Fayette-St/Director-of-IT-Infrastructure--NCS----BCIT_R0019853) | 401 E Fayette St |  |
| 48 | Axsome Therapeutics | [Director, IT Operations](https://job-boards.greenhouse.io/axsometherapeutics/jobs/6224138004) | New York, NY | 225000 |
| 48 | Apptronik | [Senior Director of Product Security](https://boards.greenhouse.io/apptronik/jobs/6119788004?gh_jid=6119788004) | Austin, TX |  |
| 48 | 1000 Becton, Dickinson and Company | [Director of Platform Engineering & Cloud Operations](https://bdx.wd1.myworkdayjobs.com/EXTERNAL_CAREER_SITE_USA/job/USA-CA---Irvine-Laguna-Canyon/Director-of-Platform-Engineering---Cloud-Operations_R-556493-1) | USA CA - Irvine Laguna Canyon |  |

## Roles from job boards / aggregators that pass (30), sample

| Source | Company | Role | Location |
|---|---|---|---|
| board-indeed | Advocate Aurora Health | [Director Data Center & Enterprise Operations](https://AdvocateAuroraHealth.contacthr.com/153953834) | Oak Brook, IL, USA |
| board-indeed | Anduril | [Director, Production Analytics](https://grnh.se/3y1ln9ut7us) | Costa Mesa, CA, USA |
| board-indeed | Apple | [Director, Evaluation and Quality Assurance, Services Special Projects](https://jsv3.recruitics.com/redirect?rx_cid=3427&rx_jobId=200688194-0836&rx_url=https%3A%2F%2Fjobs.apple.com%2Fen-us%2Fdetails%2F200688194-0836%2Fdirector-evaluation-and-quality-assurance-services-special-projects%3Fboard_id%3DJB001%26rx_a%3D0%26rx_c%3D%26rx_ch%3Djobp4p%26rx_group%3D122365%26rx_id%3D5f6b2fcc-caac-11f1-8182-33e277e81f23%26rx_job%3D200688194-0836%26rx_medium%3Dcpc%26rx_r%3Dnone%26rx_source%3Dindeed%26rx_ts%3D20261018T220404Z%26rx_vp%3Dcpc%26team%3DSFTWR) | Cupertino, CA, USA |
| board-indeed | Avangrid | [Senior Director - Technology](https://iberdrola.wd3.myworkdayjobs.com/en-US/Iberdrola/job/United-States-Of-America-Connecticut-Orange/Senior-Director---Technology_R-34509) | Orange, CT, USA |
| board-indeed | BigHat Biosciences | [Director of Machine Learning](https://bighatbiosciences.pinpointhq.com/postings/0c79bfdf-a3f1-4e55-a1e4-93abb5930c45?utm_medium=job_board&utm_source=indeed) | San Mateo, CA, USA |
| board-indeed | Cisco | [Director, Product Management](https://careers.cisco.com/global/en/job/2028398) | San Jose, CA, USA |
| board-indeed | Cisco | [Director - ASIC Engineering (Technical Planning and Engineering Execution)](https://careers.cisco.com/global/en/job/2028602) | San Jose, CA, USA |
| board-indeed | EPAM Systems | [Chief Technology Officer — Databricks Data & AI Platform](https://careers.epam.com/en/vacancy/bltbgo9kfba0zgmjjw7_en?country=USA&utm_source=indeed&utm_medium=xml-job-feed&utm_campaign=ta) | Remote, USA |
| board-indeed | FNBO - First National Bank of Omaha | [Sr. Director, Advanced Data Scientist](https://firstnational.wd12.myworkdayjobs.com/en-US/fnbocareers/job/Omaha---FN-Tower/Sr-Director--Advanced-Data-Scientist_R-20261856) | Omaha, NE, USA |
| board-indeed | GSK | [Director, Real World Data Strategy and External Partnerships Lead](https://jobs.gsk.com/gb/en/job/449565?utm_source=indeed&utm_medium=phenom-feeds) | Collegeville, PA, USA |
| board-indeed | Hewlett Packard Enterprise | HPE | [Director, Chief of Staff for Hybrid Cloud COO](https://careers.hpe.com/us/en/job/HPE1US1217311EXTERNALENUS/Director-Chief-of-Staff-for-Hybrid-Cloud-COO?utm_source=indeed&utm_medium=phenom-feeds) | San Jose, CA, USA |
| board-indeed | Huntsville Hospital Health System | [Vice President, Technology Services](https://careers-hhsys.icims.com/jobs/76558/job?utm_source=indeed_integration&iis=Job%20Board&iisn=Indeed&indeed-apply-token=73a2d2b2a8d6d5c0a62696875eaebd669103652d3f0c2cd5445d3e66b1592b0f) | Huntsville, AL, USA |
| board-indeed | LPL Financial | [VP, Software Engineering Lead (.NET/AWS)](https://lplfinancial.wd1.myworkdayjobs.com/External/job/New-York/VP--Software-Engineering-Lead--NET-AWS-_R-054347-1) | New York, NY, USA |
| board-indeed | Merck | [Executive Director, AI Delivery Management](https://jobs.merck.com/us/en/job/R422940) | Rahway, NJ, USA |
| board-indeed | MiniMed | [Director, Cyber Defense](https://mdtkangaroo.wd108.myworkdayjobs.com/en-US/MiniMedCareers/job/Virtual-Minnesota-United-States-of-America/Director--Cyber-Defense_R-802217) | MN, USA |
| board-indeed | Network Distribution | [Vice President, Business Technology Services](https://recruiting2.ultipro.com/NET1010NWRK/JobBoard/337433be-8153-4eda-8b37-455548451ef9/OpportunityDetail?opportunityId=888e0bae-0e04-4a24-a34c-24305c7d346b&postingId=a104f3d2-4548-4259-87c5-77a8c06627fa) | Schaumburg, IL, USA |
| board-indeed | Overwatch Mission Critical | [VP of Information Systems & Security](https://jobs.gem.com/overwatch/am9icG9zdDpXpvKaoJ2NrkqAtDjqtonp) | Austin, TX, USA |
| board-indeed | Pedestal Health | [Head of Technology](https://grnh.se/ycahr7vl8us) | Durham, NC, USA |
| board-indeed | PGA TOUR Superstore | [Sr. Director, Digital & Ecommerce](https://pgatoursuperstore.wd12.myworkdayjobs.com/en-US/PGAT_SS/job/Store-Support-Center---Roswell-GA/Sr-Director--Digital---Ecommerce_JR7956) | Roswell, GA, USA |
| board-indeed | Phykion | [Director of Scale-up Operations and Engineering](https://www.indeed.com/viewjob?jk=42281172359c57a7) | Calipatria, CA, USA |
| board-indeed | Select Milk Producers (SMP) | [Vice President of Technology](https://selectmilk.wd12.myworkdayjobs.com/SelectMilkProducers/job/Dallas-TX/Vice-President-of-Technology_JR102201) | Dallas, TX, USA |
| board-indeed | Siemens Healthineers | [Head of IT DX Strategy & Management Services](https://onehealthineers.wd3.myworkdayjobs.com/SHSJB/job/TAR-B/Head-of-IT-DX-Strategy---Management-Services_R-31383) | Remote, USA |
| board-indeed | Starbucks | [director, AI Transformation](https://click.appcast.io/t/Umr0W6u0BxHM5m0M3KO0lograP_bCWe4X6Up5S_md1E=) | Seattle, WA, USA |
| board-indeed | State of Wyoming | [WCCC Director of Information Technology 2026-02526](https://www.governmentjobs.com/careers/wyoming/jobs/5516302/wccc-director-of-information-technology-2026-02526) | Cheyenne, WY, USA |
| board-indeed | Tiverton Advisors | [Vice President, Portfolio Technology Operations](https://jobs.smartrecruiters.com/TivertonAdvisors/744000156394225-vice-president-portfolio-technology-operations) | Los Angeles, CA, USA |
| board-indeed | TransUnion | [Vice President, Artificial Intelligence Research & Development](https://transunion.wd5.myworkdayjobs.com/en-US/TransUnion/job/Chicago---555-West-Adams-St/Vice-President--Artificial-Intelligence-Research---Development_19042485) | Chicago, IL, USA |
| board-indeed | United Biosource Corporation | [Director, Software Engineering - Platform Development](https://workforcenow.adp.com/mascsr/default/mdf/recruitment/recruitment.html?cid=90ee0c52-4563-4bbb-a44d-0a6cd6964c61&ccId=19000101_000001&jobId=593232&source=IN&lang=en_US) | Remote, USA |
| board-indeed | Verustruct | [Head of Engineering](https://jobs.ashbyhq.com/verustruct/066cbb11-8a0a-4921-9596-47de948bff28?utm_source=p4jNLwy4oq) | Torrance, CA, USA |
| board-indeed | Gallatin | [Senior Director, Solutions Architecture](https://jobs.ashbyhq.com/gallatin/a4c4fdf3-4247-4c65-a220-7738447429ec?utm_source=qZyxO8XDee) | Austin, TX, USA |
| board-indeed | Katalyst Space Technologies | [Director of National Security Partnerships](https://grnh.se/5tyssck64us) | Broomfield, CO, USA |

## Source log lines

```
boards: 'Vice President Cloud Infrastructure' -> 5 results {'indeed': np.int64(5)}
boards: 'VP Platform Engineering' -> 29 results {'indeed': np.int64(29)}
boards: 'Head of Site Reliability Engineering' -> 5 results {'indeed': np.int64(5)}
boards: 'Director Cloud Engineering' -> 27 results {'indeed': np.int64(27)}
boards: 'Senior Director Infrastructure' -> 40 results {'indeed': np.int64(40)}
boards: 'VP Technology Infrastructure' -> 21 results {'indeed': np.int64(21)}
boards: 'Head of Enterprise Architecture' -> 0 results
boards: 'Chief Technology Officer' -> 2 results {'indeed': np.int64(2)}
boards: 'VP AI Platform' -> 37 results {'indeed': np.int64(37)}
boards: 'Executive Director Technology' -> 9 results {'indeed': np.int64(9)}
boards: 'Managing Director Technology Infrastructure' -> 40 results {'indeed': np.int64(40)}
boards: 'Director Production Engineering' -> 40 results {'indeed': np.int64(40)}
themuse: page 0 returned 0 items of 149587 total
boards/aggregators: {"board-indeed (raw)": 255, "themuse": 0, "adzuna": 0, "senior titles from boards/aggregators": 99}; employer sites found: 130
```

## Universe sample by career-site type (answered / polled)

- greenhouse: 182 / 196
- workday: 182 / 196
- ashby: 194 / 196
- smartrecruiters: 8 / 8
- lever: 3 / 3
- oracle: 1 / 1

Passing roles by type: ashby 12, greenhouse 27, smartrecruiters 2, workday 84

## Employer career sites found in board results (130), sample

- Tiverton Advisors: `{"ats": "smartrecruiters", "slug": "TivertonAdvisors"}`
- STACK Infrastructure US: `{"ats": "workday", "host": "stackinfra.wd108.myworkdayjobs.com", "site": "STACK_AMER"}`
- Orchard Marketing New York: `{"ats": "smartrecruiters", "slug": "Enero"}`
- Filevine: `{"ats": "lever", "slug": "filevine"}`
- Mozilla Corporation: `{"ats": "greenhouse", "slug": "mozilla"}`
- Trustly: `{"ats": "ashby", "slug": "trustly"}`
- APRIL: `{"ats": "ashby", "slug": "april"}`
- LPL Financial: `{"ats": "workday", "host": "lplfinancial.wd1.myworkdayjobs.com", "site": "External"}`
- Tutor Perini Corporation: `{"ats": "workday", "host": "tutorperini.wd12.myworkdayjobs.com", "site": "external"}`
- NerdWallet: `{"ats": "ashby", "slug": "nerdwallet"}`
- Rezolute: `{"ats": "lever", "slug": "rezolutebio"}`
- CRUSOE: `{"ats": "ashby", "slug": "Crusoe"}`
- Raptive: `{"ats": "ashby", "slug": "raptive"}`
- Jellyfish: `{"ats": "ashby", "slug": "jellyfishcareers"}`
- MiniMed: `{"ats": "workday", "host": "mdtkangaroo.wd108.myworkdayjobs.com", "site": "MiniMedCareers"}`
- Turner & Townsend Pty Limited: `{"ats": "smartrecruiters", "slug": "TurnerTownsend"}`
- Avangrid: `{"ats": "workday", "host": "iberdrola.wd3.myworkdayjobs.com", "site": "Iberdrola"}`
- Shine Early Learning: `{"ats": "workday", "host": "acelero.wd1.myworkdayjobs.com", "site": "ShineEarlyLearningCareers"}`
- Wells Fargo: `{"ats": "workday", "host": "wd1.myworkdaysite.com", "tenant": "wf", "site": "WellsFargoJobs", "public_base": "https://wd1.myworkdaysite.com/en-US/recruiting/wf/WellsFargoJobs"}`
- Slate Auto: `{"ats": "workday", "host": "recar.wd108.myworkdayjobs.com", "site": "SLATEcareers"}`
- Salesforce: `{"ats": "workday", "host": "salesforce.wd12.myworkdayjobs.com", "site": "External_Career_Site"}`
- NVIDIA: `{"ats": "workday", "host": "nvidia.wd5.myworkdayjobs.com", "site": "NVIDIAExternalCareerSite"}`
- Gallatin: `{"ats": "ashby", "slug": "gallatin"}`
- Visa: `{"ats": "workday", "host": "visa.wd5.myworkdayjobs.com", "site": "Visa"}`
- Wells Fargo: `{"ats": "workday", "host": "wd1.myworkdaysite.com", "tenant": "wf", "site": "WellsFargoJobs", "public_base": "https://wd1.myworkdaysite.com/en-US/recruiting/wf/WellsFargoJobs"}`
- STACK Infrastructure US: `{"ats": "workday", "host": "stackinfra.wd108.myworkdayjobs.com", "site": "STACK_AMER"}`
- OpenLoop Health: `{"ats": "ashby", "slug": "openloophealth"}`
- Arizent: `{"ats": "ashby", "slug": "arizent"}`
- CRUSOE: `{"ats": "ashby", "slug": "Crusoe"}`
- National Vision, Inc.: `{"ats": "smartrecruiters", "slug": "NationalVision1"}`

Wall time: 295s
