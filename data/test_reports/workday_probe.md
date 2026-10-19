# Workday probe experiment

## 1. Root URL behaviour

| Host | GET / status | final URL |
|---|---|---|
| capitalone.wd12.myworkdayjobs.com | 406 | https://capitalone.wd12.myworkdayjobs.com/ |
| nvidia.wd5.myworkdayjobs.com | 406 | https://nvidia.wd5.myworkdayjobs.com/ |
| pfizer.wd1.myworkdayjobs.com | 406 | https://pfizer.wd1.myworkdayjobs.com/ |
| walmart.wd1.myworkdayjobs.com | 406 | https://walmart.wd1.myworkdayjobs.com/ |
| walmart.wd3.myworkdayjobs.com | 406 | https://walmart.wd3.myworkdayjobs.com/ |
| walmart.wd5.myworkdayjobs.com | 406 | https://walmart.wd5.myworkdayjobs.com/ |
| walmart.wd12.myworkdayjobs.com | 406 | https://walmart.wd12.myworkdayjobs.com/ |
| walmart.wd103.myworkdayjobs.com | 406 | https://walmart.wd103.myworkdayjobs.com/ |
| walmart.wd501.myworkdayjobs.com | 406 | https://walmart.wd501.myworkdayjobs.com/ |
| dell.wd1.myworkdayjobs.com | 406 | https://dell.wd1.myworkdayjobs.com/ |
| dell.wd3.myworkdayjobs.com | 406 | https://dell.wd3.myworkdayjobs.com/ |
| dell.wd5.myworkdayjobs.com | 406 | https://dell.wd5.myworkdayjobs.com/ |
| dell.wd12.myworkdayjobs.com | 406 | https://dell.wd12.myworkdayjobs.com/ |
| dell.wd103.myworkdayjobs.com | 406 | https://dell.wd103.myworkdayjobs.com/ |
| dell.wd501.myworkdayjobs.com | 406 | https://dell.wd501.myworkdayjobs.com/ |
| qualcomm.wd1.myworkdayjobs.com | 406 | https://qualcomm.wd1.myworkdayjobs.com/ |
| qualcomm.wd3.myworkdayjobs.com | 406 | https://qualcomm.wd3.myworkdayjobs.com/ |
| qualcomm.wd5.myworkdayjobs.com | 406 | https://qualcomm.wd5.myworkdayjobs.com/ |
| qualcomm.wd12.myworkdayjobs.com | 406 | https://qualcomm.wd12.myworkdayjobs.com/ |
| qualcomm.wd103.myworkdayjobs.com | 406 | https://qualcomm.wd103.myworkdayjobs.com/ |
| qualcomm.wd501.myworkdayjobs.com | 406 | https://qualcomm.wd501.myworkdayjobs.com/ |
| redhat.wd1.myworkdayjobs.com | 406 | https://redhat.wd1.myworkdayjobs.com/ |
| redhat.wd3.myworkdayjobs.com | 406 | https://redhat.wd3.myworkdayjobs.com/ |
| redhat.wd5.myworkdayjobs.com | 406 | https://redhat.wd5.myworkdayjobs.com/ |
| redhat.wd12.myworkdayjobs.com | 406 | https://redhat.wd12.myworkdayjobs.com/ |
| redhat.wd103.myworkdayjobs.com | 406 | https://redhat.wd103.myworkdayjobs.com/ |
| redhat.wd501.myworkdayjobs.com | 406 | https://redhat.wd501.myworkdayjobs.com/ |
| thermofisher.wd1.myworkdayjobs.com | 406 | https://thermofisher.wd1.myworkdayjobs.com/ |
| thermofisher.wd3.myworkdayjobs.com | 406 | https://thermofisher.wd3.myworkdayjobs.com/ |
| thermofisher.wd5.myworkdayjobs.com | 406 | https://thermofisher.wd5.myworkdayjobs.com/ |
| thermofisher.wd12.myworkdayjobs.com | 406 | https://thermofisher.wd12.myworkdayjobs.com/ |
| thermofisher.wd103.myworkdayjobs.com | 406 | https://thermofisher.wd103.myworkdayjobs.com/ |
| thermofisher.wd501.myworkdayjobs.com | 406 | https://thermofisher.wd501.myworkdayjobs.com/ |
| zzqqxxfake.wd1.myworkdayjobs.com | 406 | https://zzqqxxfake.wd1.myworkdayjobs.com/ |
| zzqqxxfake.wd3.myworkdayjobs.com | 406 | https://zzqqxxfake.wd3.myworkdayjobs.com/ |
| zzqqxxfake.wd5.myworkdayjobs.com | 406 | https://zzqqxxfake.wd5.myworkdayjobs.com/ |
| zzqqxxfake.wd12.myworkdayjobs.com | 406 | https://zzqqxxfake.wd12.myworkdayjobs.com/ |
| zzqqxxfake.wd103.myworkdayjobs.com | 406 | https://zzqqxxfake.wd103.myworkdayjobs.com/ |
| zzqqxxfake.wd501.myworkdayjobs.com | 406 | https://zzqqxxfake.wd501.myworkdayjobs.com/ |

## 2. Jobs API with right and wrong site names

| Host | Site | POST status | total |
|---|---|---|---|
| capitalone.wd12.myworkdayjobs.com | Capital_One | 200 | 1970 |
| nvidia.wd5.myworkdayjobs.com | NVIDIAExternalCareerSite | 200 | 2000 |
| pfizer.wd1.myworkdayjobs.com | PfizerCareers | 200 | 550 |
| capitalone.wd12.myworkdayjobs.com | WrongSiteName | 404 |  |
| nvidia.wd5.myworkdayjobs.com | WrongSiteName | 404 |  |
| pfizer.wd1.myworkdayjobs.com | WrongSiteName | 404 |  |
| walmart.wd1.myworkdayjobs.com | External | 422 |  |
| walmart.wd1.myworkdayjobs.com | Careers | 422 |  |
| walmart.wd1.myworkdayjobs.com | careers | 422 |  |
| walmart.wd1.myworkdayjobs.com | jobs | 422 |  |
| walmart.wd1.myworkdayjobs.com | External_Careers | 422 |  |
| walmart.wd5.myworkdayjobs.com | External | 422 |  |
| walmart.wd5.myworkdayjobs.com | Careers | 422 |  |
| walmart.wd5.myworkdayjobs.com | careers | 422 |  |
| walmart.wd5.myworkdayjobs.com | jobs | 422 |  |
| walmart.wd5.myworkdayjobs.com | External_Careers | 422 |  |
| dell.wd1.myworkdayjobs.com | External | 422 |  |
| dell.wd1.myworkdayjobs.com | Careers | 422 |  |
| dell.wd1.myworkdayjobs.com | careers | 422 |  |
| dell.wd1.myworkdayjobs.com | jobs | 422 |  |
| dell.wd1.myworkdayjobs.com | External_Careers | 422 |  |
| dell.wd5.myworkdayjobs.com | External | 422 |  |
| dell.wd5.myworkdayjobs.com | Careers | 422 |  |
| dell.wd5.myworkdayjobs.com | careers | 422 |  |
| dell.wd5.myworkdayjobs.com | jobs | 422 |  |
| dell.wd5.myworkdayjobs.com | External_Careers | 422 |  |
| qualcomm.wd1.myworkdayjobs.com | External | 422 |  |
| qualcomm.wd1.myworkdayjobs.com | Careers | 422 |  |
| qualcomm.wd1.myworkdayjobs.com | careers | 422 |  |
| qualcomm.wd1.myworkdayjobs.com | jobs | 422 |  |
| qualcomm.wd1.myworkdayjobs.com | External_Careers | 422 |  |
| qualcomm.wd5.myworkdayjobs.com | External | 422 |  |
| qualcomm.wd5.myworkdayjobs.com | Careers | 422 |  |
| qualcomm.wd5.myworkdayjobs.com | careers | 422 |  |
| qualcomm.wd5.myworkdayjobs.com | jobs | 422 |  |
| qualcomm.wd5.myworkdayjobs.com | External_Careers | 422 |  |
| redhat.wd1.myworkdayjobs.com | External | 422 |  |
| redhat.wd1.myworkdayjobs.com | Careers | 422 |  |
| redhat.wd1.myworkdayjobs.com | careers | 422 |  |
| redhat.wd1.myworkdayjobs.com | jobs | 422 |  |
| redhat.wd1.myworkdayjobs.com | External_Careers | 422 |  |
| redhat.wd5.myworkdayjobs.com | External | 404 |  |
| redhat.wd5.myworkdayjobs.com | Careers | 404 |  |
| redhat.wd5.myworkdayjobs.com | careers | 404 |  |
| redhat.wd5.myworkdayjobs.com | jobs | 200 | 172 |
| redhat.wd5.myworkdayjobs.com | External_Careers | 404 |  |
| thermofisher.wd1.myworkdayjobs.com | External | 422 |  |
| thermofisher.wd1.myworkdayjobs.com | Careers | 422 |  |
| thermofisher.wd1.myworkdayjobs.com | careers | 422 |  |
| thermofisher.wd1.myworkdayjobs.com | jobs | 422 |  |
| thermofisher.wd1.myworkdayjobs.com | External_Careers | 422 |  |
| thermofisher.wd5.myworkdayjobs.com | External | 404 |  |
| thermofisher.wd5.myworkdayjobs.com | Careers | 404 |  |
| thermofisher.wd5.myworkdayjobs.com | careers | 404 |  |
| thermofisher.wd5.myworkdayjobs.com | jobs | 404 |  |
| thermofisher.wd5.myworkdayjobs.com | External_Careers | 404 |  |
