import pytest
from requests_toolbelt.utils import formdata
import requests
import json

url = "https://www.copart.com/public/lots/search"

payload = "draw=1&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=6&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=7&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=8&columns%5B8%5D%5Bname%5D=&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=9&columns%5B9%5D%5Bname%5D=&columns%5B9%5D%5Bsearchable%5D=true&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B10%5D%5Bdata%5D=10&columns%5B10%5D%5Bname%5D=&columns%5B10%5D%5Bsearchable%5D=true&columns%5B10%5D%5Borderable%5D=true&columns%5B10%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B10%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B11%5D%5Bdata%5D=11&columns%5B11%5D%5Bname%5D=&columns%5B11%5D%5Bsearchable%5D=true&columns%5B11%5D%5Borderable%5D=true&columns%5B11%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B11%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B12%5D%5Bdata%5D=12&columns%5B12%5D%5Bname%5D=&columns%5B12%5D%5Bsearchable%5D=true&columns%5B12%5D%5Borderable%5D=true&columns%5B12%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B12%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B13%5D%5Bdata%5D=13&columns%5B13%5D%5Bname%5D=&columns%5B13%5D%5Bsearchable%5D=true&columns%5B13%5D%5Borderable%5D=true&columns%5B13%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B13%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B14%5D%5Bdata%5D=14&columns%5B14%5D%5Bname%5D=&columns%5B14%5D%5Bsearchable%5D=true&columns%5B14%5D%5Borderable%5D=false&columns%5B14%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B14%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B15%5D%5Bdata%5D=15&columns%5B15%5D%5Bname%5D=&columns%5B15%5D%5Bsearchable%5D=true&columns%5B15%5D%5Borderable%5D=false&columns%5B15%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B15%5D%5Bsearch%5D%5Bregex%5D=false&start=0&length=100&search%5Bvalue%5D=&search%5Bregex%5D=false&query=lamborghini+huracan&watchListOnly=false&freeFormSearch=true&page=0&size=100"

cookie_str = 's_fid=6A33240F35C852A7-3CEA6317CFBC486D; s_vi=[CS]v1|2F34098505159621-60000B9B408FCC80[CE]; _ga=GA1.2.1804649036.1583878923; _fbp=fb.1.1583878923261.2134575386; OAID=f0a158d26968fb97cb4b69b9fe8f6f5c; __gads=ID=773497ae053dc659:T=1583879001:S=ALNI_MaKSSEScJPxyVPd_Ig3MjaIweUoPA; _gcl_aw=GCL.1587239998.Cj0KCQjwyur0BRDcARIsAEt86IAUQo1tjvaazjBUN5hDpX8wxgWLxHK-zGqiAgWZs_BPL7C0spR6DCMaAnDmEALw_wcB; _gac_UA-90930613-1=1.1587239998.Cj0KCQjwyur0BRDcARIsAEt86IAUQo1tjvaazjBUN5hDpX8wxgWLxHK-zGqiAgWZs_BPL7C0spR6DCMaAnDmEALw_wcB; g2app.searchResultsPageLength=100; _gcl_au=1.1.458864109.1592094966; visid_incap_242093=hdqKTmeYR3SBg7OParZVjuUBaF4AAAAAQkIPAAAAAACAdG+VAUYTLnjBI05yWa0qtiPMA9a9oQnG; g2app.locationInfo=%7B%22countryCode%22%3A%22USA%22%2C%22countryName%22%3A%22United%20States%22%2C%22stateName%22%3A%22New%20York%22%2C%22stateCode%22%3A%22NY%22%2C%22cityName%22%3A%22New%20York%20City%22%2C%22latitude%22%3A40.71427%2C%22longitude%22%3A-74.00597%2C%22zipCode%22%3A%2210116%22%2C%22timeZone%22%3A%22-04%3A00%22%7D; __cfduid=d81e6f1b1df01ef18c8377b05a1f8dcb51594236872; g2usersessionid=023c5fb0412f4eeeabb81f3a16fe981a; userLang=en; copartTimezonePref=%7B%22displayStr%22%3A%22MSK%22%2C%22offset%22%3A3%2C%22dst%22%3Afalse%2C%22windowsTz%22%3A%22Europe%2FMinsk%22%7D; timezone=Europe%2FMinsk; s_cc=true; OAGEO=US%7C%7C%7C%7C%7C%7C%7C%7C%7C%7C; usersessionid=1e4a3cac16ebec272c21cc19ed4e1f1e; _gid=GA1.2.2071213884.1594759814; G2JSESSIONID=5013FCA33AA335D7845EB4965FAC1385-n2; incap_ses_481_242093=ZSqCdrq0pQVyyJ/eEdusBtgxDl8AAAAA2pF7JcF68mSgFrxexdG4Jg==; s_depth=1; s_vnum=1595126212459%26vn%3D6; s_invisit=true; s_lv_s=Less%20than%201%20day; _uetsid=97a5419e-93b9-eeb9-80dc-67bbf05abeba; _uetvid=b7496093-9eec-9947-61a2-2ec814b62c58; s_pv=no%20value; s_nr=1594765981807-Repeat; s_lv=1594765981809; s_sq=copart-g2-us-prod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fwww.copart.com%25252FlotSearchResults%25252F%25253Ffree%25253Dtrue%252526query%25253Dlamborghini%25252520huracan%2526link%253DSearch%2526region%253Dsearch-form%2526.activitymap%2526.a%2526.c; s_ppvl=member%253AsearchResults%2C80%2C30%2C1757%2C1366%2C208%2C1366%2C768%2C1%2CP; s_ppv=https%253A%2F%2Fwww.copart.com%2FlotSearchResults%2F%253Ffree%253Dtrue%2526query%253Dlamborghini%252520huracan%2C26%2C26%2C208%2C1366%2C208%2C1366%2C768%2C1%2CP; g2usersessionid=023c5fb0412f4eeeabb81f3a16fe981a'

headers = {
    'authority': 'www.copart.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.copart.com',
    'referer': 'https://www.copart.com/lotSearchResults/?free=true&query=lamborghini%20huracan',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': cookie_str
}

#response = requests.request("POST", url, headers=headers, data=formdata.urlencode(payload))
response = requests.request("POST", url, headers=headers, data=payload)
responsetxt = '{"returnCode":1,"returnCodeDesc":"Success","data":{"query":{"query":["lamborghini huracan"],"page":0,"size":100,"start":0,"watchListOnly":false,"freeFormSearch":true,"hideImages":false,"defaultSort":false,"specificRowProvided":false},"results":{"totalElements":9,"content":[{"lotYardSameAsKioskYard":false,"lotNumberStr":"32744160","ln":32744160,"mkn":"LAMBORGHINI","lm":"HURACAN","lcy":2015,"fv":"ZHWUC1ZF0FLA02967","la":181878.0,"rc":150439.0,"obc":"A","orr":19511.0,"ord":"ACTUAL","egn":"5.2L 10","cy":"10","ld":"2015 LAMBORGHINI HURACAN ","yn":"TX - CRASHEDTOYS DALLAS","cuc":"USD","tz":"CDT","ad":1595437200000,"at":"12:00:00","aan":0,"hb":90500.0,"ss":2,"bndc":"","bnp":0.0,"sbf":false,"ts":"TX","stt":"SV","td":"SALVAGE VEHICLE TITLE","tgc":"TITLEGROUP_S","dd":"FRONT END","tims":"https://cs.copart.com/v1/AUTH_svc.pdoc00001/PIX265/2f728d7c-19ab-4d3b-89b4-05d2acd9e29a.JPG","lic":["IV","SITE-CT","NLC","CERT-D"],"gr":"WC001","dtc":"FR","adt":"E","ynumb":313,"phynumb":313,"bf":true,"ymin":100,"offFlg":false,"htsmn":"Y","tmtp":"AUTOMATIC","myb":0.0,"lmc":"LAMO","lcc":"CERT-D","bstl":"COUPE","lcd":"RUNS AND DRIVES","ft":"GAS","hk":"YES","sn":"***CRASHEDTOYS BUYER FEES APPLY***","drv":"All wheel drive","ess":"Minimum Bid","showSeller":false,"sstpflg":false,"syn":"TX - CRASHEDTOYS DALLAS","ifs":true,"pbf":false,"crg":0.0,"brand":"CRASHEDTOYS","hegn":"Y"},{"lotYardSameAsKioskYard":false,"lotNumberStr":"34218510","ln":34218510,"mkn":"LAMBORGHINI","lm":"HURACAN","lcy":2019,"fv":"ZHWUR2ZF3KLA12620","la":215448.0,"rc":151958.76,"obc":"N","orr":4676.0,"ord":"NOT ACTUAL","egn":"5.2L 10","cy":"10","ld":"2019 LAMBORGHINI HURACAN ","yn":"FL - MIAMI NORTH","cuc":"USD","tz":"EDT","at":"10:00:00","aan":0,"hb":0.0,"ss":2,"bndc":"","bnp":0.0,"sbf":false,"ts":"FL","stt":"RB","td":"CERT OF TITLE SLVG REBUILDABLE","tgc":"TITLEGROUP_S","dd":"FRONT END","tims":"https://cs.copart.com/v1/AUTH_svc.pdoc00001/PIX281/bc355bae-e6de-4845-a2b5-a1afb5e19b58.JPG","lic":["IV","CERT-E"],"gr":"9K040","dtc":"FR","ynumb":33,"phynumb":33,"bf":false,"ymin":150,"offFlg":false,"htsmn":"Y","tmtp":"AUTOMATIC","myb":0.0,"lmc":"LAMO","lcc":"CERT-E","sdd":"SIDE","lcd":"ENHANCED VEHICLES","ft":"GAS","hk":"YES","drv":"Rear-wheel drive","ess":"Minimum Bid","showSeller":false,"sstpflg":false,"syn":"FL - MIAMI NORTH","ifs":false,"pbf":false,"crg":0.0,"brand":"COPART","hegn":"Y"},{"lotYardSameAsKioskYard":false,"lotNumberStr":"37767300","ln":37767300,"mkn":"LAMBORGHINI","lm":"HURACAN","lcy":2017,"fv":"ZHWUR1ZF2HLA05483","la":287150.0,"rc":0.0,"obc":"A","orr":3027.0,"ord":"ACTUAL","egn":"5.2L 10","cy":"10","ld":"2017 LAMBORGHINI HURACAN ","yn":"TX - HOUSTON","cuc":"USD","tz":"CDT","ad":1595005200000,"at":"12:00:00","aan":0,"hb":53000.0,"ss":2,"bndc":"BUY IT NOW","bnp":135000.0,"sbf":false,"ts":"GA","stt":"ST","td":"CERT OF TITLE-SALVAGE","tgc":"TITLEGROUP_S","dd":"REAR END","tims":"https://cs.copart.com/v1/AUTH_svc.pdoc00001/PIX280/3f1cda91-2442-4472-9a21-7c90ef54dff7.JPG","lic":["FEATURED","IV","NLC","CERT-D"],"gr":" INSP","dtc":"RR","adt":"F","ynumb":11,"phynumb":11,"bf":true,"ymin":25,"offFlg":false,"htsmn":"Y","tmtp":"AUTOMATIC","myb":0.0,"lmc":"LAMO","lcc":"CERT-D","sdd":"SIDE","bstl":"CONVERTI","lcd":"RUNS AND DRIVES","ft":"GAS","hk":"YES","drv":"All wheel drive","ess":"Minimum Bid","showSeller":false,"sstpflg":false,"syn":"TX - HOUSTON","ifs":false,"pbf":false,"crg":0.0,"brand":"COPART","hegn":"Y"},{"lotYardSameAsKioskYard":false,"lotNumberStr":"39754940","ln":39754940,"mkn":"LAMBORGHINI","lm":"HURACAN","lcy":2018,"fv":"ZHWUC2ZF6JLA08903","la":162310.0,"rc":115516.63,"orr":12737.0,"egn":"5.2L 10","cy":"10","ld":"2018 LAMBORGHINI HURACAN ","yn":"CA - VAN NUYS","cuc":"USD","tz":"PDT","at":"12:00:00","aan":0,"hb":0.0,"ss":5,"bndc":"","bnp":0.0,"sbf":false,"dd":"REAR END","tims":"https://cs.copart.com/v1/AUTH_svc.pdoc00001/PIX291/8e23eb2e-83e5-4c79-807d-1e2c8d758f17.JPG","lic":["IV","SITE-CT","CERT-S"],"gr":"JJJ10","dtc":"RR","ynumb":327,"phynumb":43,"bf":false,"ymin":100,"offFlg":false,"htsmn":"Y","tmtp":"AUTOMATIC","myb":0.0,"lmc":"LAMO","lcc":"CERT-S","sdd":"MECHANICAL","lcd":"ENGINE START PROGRAM","ft":"GAS","hk":"YES","sn":"2018 Lamborghini Huracan with 12,737 miles. Located in Van Nuys California. Has a key and the engine runs.\nThis is an insurance company supplied vehicle that was damaged from a side and rear end collision. There is damage to the rear bumper, tail light, quarter panel, reinforcement, wheel and rear suspension. None of the airbags were deployed. The Huracan is powered by a 5.2L V-10 producing 602HP.\nThere is a key and the engine runs.\nThis vehicle is located in Van Nuys California and will need to be picked up from that location. Buyer is subject to all California licensing and eligibility requirements. CRASHEDTOYS Buyer Fees apply. Please review the CRASHEDTOYS Terms and Conditions for Buyer Fee Schedule.\n","drv":"Rear-wheel drive","ess":"Pure Sale","showSeller":false,"sstpflg":false,"syn":"CA - CRASHEDTOYS SACRAMENTO","ifs":false,"pbf":false,"crg":0.0,"brand":"CRASHEDTOYS","hegn":"Y"},{"lotYardSameAsKioskYard":false,"lotNumberStr":"40721210","ln":40721210,"mkn":"LAMBORGHINI","lm":"HURACAN","lcy":2016,"fv":"ZHWCC1ZF6GLA03747","la":273583.0,"rc":0.0,"obc":"A","orr":5925.0,"ord":"ACTUAL","egn":"5.2L 10","cy":"10","ld":"2016 LAMBORGHINI HURACAN ","yn":"ON - TORONTO","cuc":"USD","tz":"EDT","ad":1594861200000,"at":"21:00:00","aan":0,"hb":151000.0,"ss":3,"bndc":"","bnp":0.0,"sbf":false,"ts":"ON","stt":"ST","td":"PERMIT SALVAGE (P)","tgc":"TITLEGROUP_S","dd":"FRONT END","tims":"https://cs.copart.com/v1/AUTH_svc.pdoc00001/PIX291/e2a39cb0-d94f-45c7-b683-149c470138ae.JPG","lic":["NCS","IV","SITE-CA","CERT-D"],"gr":"SA001","dtc":"FR","adt":"F","ynumb":880,"phynumb":201,"bf":false,"ymin":10,"offFlg":false,"htsmn":"Y","tmtp":"AUTOMATIC","myb":0.0,"lmc":"LAMO","lcc":"CERT-D","sdd":"REAR END","bstl":"COUPE","lcd":"RUNS AND DRIVES","ft":"GAS","hk":"YES","drv":"All wheel drive","ess":"On Approval","showSeller":false,"sstpflg":false,"syn":"*NCS - EASTERN REGION","ifs":false,"pbf":false,"crg":0.0,"brand":"UNKNOWN","hegn":"Y"},{"lotYardSameAsKioskYard":false,"lotNumberStr":"42427030","ln":42427030,"mkn":"LAMBORGHINI","lm":"HURACAN","lcy":2017,"fv":"ZHWUR2ZF0HLA06346","la":204522.35,"rc":0.0,"obc":"A","orr":21958.0,"ord":"ACTUAL","egn":"5.2L 10","cy":"10","ld":"2017 LAMBORGHINI HURACAN ","yn":"GA - CARTERSVILLE","cuc":"USD","tz":"EDT","at":"10:00:00","aan":0,"hb":0.0,"ss":5,"bndc":"","bnp":0.0,"sbf":false,"dd":"FRONT END","tims":"https://cs.copart.com/v1/AUTH_svc.pdoc00001/PIX299/bd80897f-4d3b-4359-88ae-1e9d87fb0cdf.JPG","lic":["IV","CERT-E"],"gr":"","dtc":"FR","ynumb":175,"phynumb":175,"bf":false,"ymin":125,"offFlg":false,"htsmn":"Y","tmtp":"AUTOMATIC","myb":0.0,"lmc":"LAMO","lcc":"CERT-E","sdd":"UNDERCARRIAGE","bstl":"CONVERTI","lcd":"ENHANCED VEHICLES","ft":"GAS","hk":"YES","drv":"Rear-wheel drive","ess":"Pure Sale","showSeller":false,"sstpflg":false,"syn":"GA - CARTERSVILLE","ifs":false,"pbf":false,"crg":0.0,"brand":"COPART","hegn":"Y"},{"lotYardSameAsKioskYard":false,"lotNumberStr":"42577900","ln":42577900,"mkn":"LAMBORGHINI","lm":"HURACAN","lcy":2015,"fv":"ZHWUC1ZF7FLA02612","la":129180.0,"rc":0.0,"obc":"A","orr":15171.0,"ord":"ACTUAL","egn":"5.2L 10","cy":"10","ld":"2015 LAMBORGHINI HURACAN","yn":"CA - LOS ANGELES","cuc":"USD","tz":"PDT","ad":1594861200000,"at":"18:00:00","aan":0,"hb":72000.0,"ss":2,"bndc":"","bnp":0.0,"sbf":false,"ts":"CA","stt":"CQ","td":"CERT OF TITLE OR SALVAGE ACQ (P)","tgc":"TITLEGROUP_C","dd":"FRONT END","tims":"https://cs.copart.com/v1/AUTH_svc.pdoc00001/PIX298/99f93544-4b47-4a5f-85da-4ae4be614a46.JPG","lic":["NCS","OFS","IV","SITE-CA"],"gr":"*OFF","dtc":"FR","adt":"F","ynumb":883,"phynumb":10,"bf":false,"ymin":50,"offFlg":true,"myb":0.0,"lmc":"LAMO","sdd":"ALL OVER","bstl":"COUPE","ft":"GAS","hk":"YES","drv":"All wheel drive","ess":"Minimum Bid","showSeller":false,"sstpflg":false,"syn":"*NCS - PACIFIC REGION","ifs":false,"pbf":false,"crg":0.0,"brand":"UNKNOWN"},{"lotYardSameAsKioskYard":false,"lotNumberStr":"35391200","ln":35391200,"mkn":"LAMBORGHINI","lm":"HURACAN","lcy":2015,"fv":"N0V1N35391200","la":179711.0,"rc":159.0,"obc":"N","orr":0.0,"ord":"NOT ACTUAL","ld":"2015 lamborghini huracan","yn":"DC - WASHINGTON DC","cuc":"USD","tz":"EDT","at":"10:00:00","aan":0,"hb":0.0,"ss":5,"bndc":"","bnp":0.0,"sbf":false,"dd":"BURN","tims":"https://cs.copart.com/v1/AUTH_svc.pdoc00001/PIX270/a56959ab-6a4c-4056-9429-dca191d46f01.JPG","lic":["IV","CERT-E"],"gr":"HV013","dtc":"BN","ynumb":32,"phynumb":32,"bf":false,"ymin":175,"offFlg":false,"htsmn":"Y","tmtp":"AUTOMATIC","myb":0.0,"lmc":"LAMO","lcc":"CERT-E","sdd":"BURN - ENGINE","bstl":"COUPE","lcd":"ENHANCED VEHICLES","hk":"EXEMPT","ess":"Pure Sale","showSeller":false,"sstpflg":false,"syn":"DC - WASHINGTON DC","ifs":false,"pbf":false,"crg":0.0,"brand":"COPART","hegn":"Y"},{"lotYardSameAsKioskYard":false,"lotNumberStr":"40274970","ln":40274970,"mkn":"LAMBORGHINI","lm":"HURACAN EV","lcy":2020,"fv":"ZHWUT4ZF3LLA13443","la":264555.0,"rc":0.0,"orr":772.0,"egn":"5.2L 10","cy":"10","ld":"2020 LAMBORGHINI HURACAN EVO","yn":"CA - RANCHO CUCAMONGA","cuc":"USD","tz":"PDT","at":"12:00:00","aan":0,"hb":0.0,"ss":2,"bndc":"","bnp":0.0,"sbf":false,"dd":"SIDE","tims":"https://cs.copart.com/v1/AUTH_svc.pdoc00001/PIX296/02c788f1-6130-4fc2-acf7-bd42744e0959.JPG","lic":["IV","S-F182","CERT-S"],"gr":" INSP","dtc":"SD","ynumb":97,"phynumb":97,"bf":false,"ymin":80,"offFlg":false,"htsmn":"Y","tmtp":"AUTOMATIC","myb":0.0,"lmc":"LAMO","lcc":"CERT-S","lcd":"ENGINE START PROGRAM","ft":"GAS","hk":"YES","drv":"All wheel drive","ess":"Minimum Bid","showSeller":false,"sstpflg":false,"syn":"CA - RANCHO CUCAMONGA","ifs":false,"pbf":false,"crg":0.0,"brand":"COPART","hegn":"Y"}],"facetFields":[{"quickPickCode":"NLTS","facetCounts":[],"sequenceNumber":1,"includeTag":"","displayName":"Newly Added Lots"},{"quickPickCode":"FETI","facetCounts":[{"count":1,"query":"buy_it_now_code:B1","sortKey":"","sequenceNumber":1,"uri":"buyitnow","synonyms":[""],"displayName":"Buy It Now"},{"count":3,"query":"lot_condition_code:CERT-D","sortKey":"","sequenceNumber":2,"uri":"runanddrive","synonyms":[""],"displayName":"Run and Drive"},{"count":2,"query":"lot_features_code:LOTFEATURE_0","sortKey":"","sequenceNumber":3,"uri":"nolicenserequired","synonyms":[""],"displayName":"No License Required"},{"count":3,"query":"-on_approval:Y AND minimum_bid_amount:0","sortKey":"","sequenceNumber":4,"uri":"puresaleitems","synonyms":[""],"displayName":"Pure Sale Items"},{"count":2,"query":"lot_condition_code:CERT-S","sortKey":"","sequenceNumber":55,"uri":"enginestartprogram","synonyms":[""],"displayName":"Engine Start Program"},{"count":3,"query":"lot_condition_code:CERT-E","sortKey":"","sequenceNumber":65,"uri":"enhancedvehicles","synonyms":[""],"displayName":"Enhanced Vehicles"},{"count":9,"query":"lot_features_code:EXOTIC","sortKey":"","sequenceNumber":80,"uri":"exotics","synonyms":[""],"displayName":"Exotics"},{"count":2,"query":"expected_sale_assigned_ts_utc:[NOW-2DAY TO NOW]","sortKey":"expected_sale_assigned_ts_utc desc,lot_assignment_date_utc desc","sequenceNumber":105,"uri":"newitems","synonyms":[""],"displayName":"New Items"},{"count":1,"query":"lot_features_code:LOTFEATURE_V","sortKey":"","sequenceNumber":110,"uri":"featuredvehicles","synonyms":[""],"displayName":"Featured Vehicles"},{"count":1,"query":"lot_features_code:LOTFEATURE_I","sortKey":"","sequenceNumber":120,"uri":"offsitesales","synonyms":[""],"displayName":"Offsite Sales"},{"count":1,"query":"go_app_user:*","sortKey":"","sequenceNumber":150,"uri":"copartgo","synonyms":[""],"displayName":"Copart GO"}],"sequenceNumber":5,"includeTag":"","displayName":"Featured Items"},{"quickPickCode":"MAKE","facetCounts":[{"count":9,"query":"lot_make_desc:\"LAMBORGHINI\"","sequenceNumber":0,"displayName":"Lamborghini","columnName":"lot_make_desc"}],"sequenceNumber":10,"includeTag":"{!tag=MAKE}","displayName":"Make"},{"quickPickCode":"MODL","facetCounts":[{"count":8,"query":"lot_model_desc:\"HURACAN\"","sequenceNumber":0,"displayName":"Huracan","columnName":"lot_model_desc"},{"count":1,"query":"lot_model_desc:\"HURACAN EV\"","sequenceNumber":0,"displayName":"Huracan Ev","columnName":"lot_model_desc"}],"sequenceNumber":20,"includeTag":"{!tag=MODL}","displayName":"Model"},{"quickPickCode":"YEAR","facetCounts":[{"count":1,"query":"lot_year:\"2020\"","sequenceNumber":0,"displayName":"2020","columnName":"lot_year"},{"count":1,"query":"lot_year:\"2019\"","sequenceNumber":0,"displayName":"2019","columnName":"lot_year"},{"count":1,"query":"lot_year:\"2018\"","sequenceNumber":0,"displayName":"2018","columnName":"lot_year"},{"count":2,"query":"lot_year:\"2017\"","sequenceNumber":0,"displayName":"2017","columnName":"lot_year"},{"count":1,"query":"lot_year:\"2016\"","sequenceNumber":0,"displayName":"2016","columnName":"lot_year"},{"count":3,"query":"lot_year:\"2015\"","sequenceNumber":0,"displayName":"2015","columnName":"lot_year"}],"sequenceNumber":30,"includeTag":"{!tag=YEAR}","displayName":"Year"},{"quickPickCode":"ODM","facetCounts":[{"count":9,"query":"odometer_reading_received:[* TO 25000]","sortKey":"","sequenceNumber":10,"uri":"lessthan25000","synonyms":[""],"displayName":"Less than 25,000"}],"sequenceNumber":40,"includeTag":"{!tag=ODM} ","displayName":"Mileage"},{"quickPickCode":"LOC","facetCounts":[{"count":1,"query":"yard_name:\"CA - LOS ANGELES\"","sequenceNumber":0,"displayName":"Ca - Los Angeles","columnName":"yard_name"},{"count":1,"query":"yard_name:\"CA - RANCHO CUCAMONGA\"","sequenceNumber":0,"displayName":"Ca - Rancho Cucamonga","columnName":"yard_name"},{"count":1,"query":"yard_name:\"CA - VAN NUYS\"","sequenceNumber":0,"displayName":"Ca - Van Nuys","columnName":"yard_name"},{"count":1,"query":"yard_name:\"DC - WASHINGTON DC\"","sequenceNumber":0,"displayName":"Dc - Washington Dc","columnName":"yard_name"},{"count":1,"query":"yard_name:\"FL - MIAMI NORTH\"","sequenceNumber":0,"displayName":"Fl - Miami North","columnName":"yard_name"},{"count":1,"query":"yard_name:\"GA - CARTERSVILLE\"","sequenceNumber":0,"displayName":"Ga - Cartersville","columnName":"yard_name"},{"count":1,"query":"yard_name:\"ON - TORONTO\"","sequenceNumber":0,"displayName":"On - Toronto","columnName":"yard_name"},{"count":1,"query":"yard_name:\"TX - CRASHEDTOYS DALLAS\"","sequenceNumber":0,"displayName":"Tx - Crashedtoys Dallas","columnName":"yard_name"},{"count":1,"query":"yard_name:\"TX - HOUSTON\"","sequenceNumber":0,"displayName":"Tx - Houston","columnName":"yard_name"}],"sequenceNumber":50,"includeTag":"{!tag=LOC} ","displayName":"Location"},{"quickPickCode":"SLOC","facetCounts":[{"count":1,"query":"auction_host_name:\"CA - CRASHEDTOYS SACRAMENTO\"","sequenceNumber":0,"displayName":"Ca - Crashedtoys Sacramento","columnName":"auction_host_name"},{"count":1,"query":"auction_host_name:\"CA - RANCHO CUCAMONGA\"","sequenceNumber":0,"displayName":"Ca - Rancho Cucamonga","columnName":"auction_host_name"},{"count":1,"query":"auction_host_name:\"DC - WASHINGTON DC\"","sequenceNumber":0,"displayName":"Dc - Washington Dc","columnName":"auction_host_name"},{"count":1,"query":"auction_host_name:\"FL - MIAMI NORTH\"","sequenceNumber":0,"displayName":"Fl - Miami North","columnName":"auction_host_name"},{"count":1,"query":"auction_host_name:\"GA - CARTERSVILLE\"","sequenceNumber":0,"displayName":"Ga - Cartersville","columnName":"auction_host_name"},{"count":1,"query":"auction_host_name:\"TX - CRASHEDTOYS DALLAS\"","sequenceNumber":0,"displayName":"Tx - Crashedtoys Dallas","columnName":"auction_host_name"},{"count":1,"query":"auction_host_name:\"TX - HOUSTON\"","sequenceNumber":0,"displayName":"Tx - Houston","columnName":"auction_host_name"}],"sequenceNumber":52,"includeTag":"{!tag=SLOC}","displayName":"Sale Name"},{"quickPickCode":"SDAT","facetCounts":[{"count":2,"query":"auction_date_utc:\"2020-07-16T01:00:00Z\"","sequenceNumber":0,"displayName":"2020-07-16t01:00:00z","columnName":"auction_date_utc"},{"count":1,"query":"auction_date_utc:\"2020-07-17T17:00:00Z\"","sequenceNumber":0,"displayName":"2020-07-17t17:00:00z","columnName":"auction_date_utc"},{"count":1,"query":"auction_date_utc:\"2020-07-22T17:00:00Z\"","sequenceNumber":0,"displayName":"2020-07-22t17:00:00z","columnName":"auction_date_utc"}],"sequenceNumber":55,"includeTag":"{!tag=SDAT}","displayName":"Sale Date"},{"quickPickCode":"TITL","facetCounts":[{"count":1,"query":"title_group_code:TITLEGROUP_C","sortKey":"","sequenceNumber":5,"uri":"cleantitle","synonyms":[""],"displayName":"Clean Title"},{"count":4,"query":"title_group_code:TITLEGROUP_S","sortKey":"","sequenceNumber":15,"uri":"salvagetitle","synonyms":[""],"displayName":"Salvage Title"}],"sequenceNumber":60,"includeTag":"{!tag=TITL}","displayName":"Ownership Doc Type"},{"quickPickCode":"SRCE","facetCounts":[],"sequenceNumber":75,"includeTag":"{!tag=SRCE}","displayName":"Source"},{"quickPickCode":"VEHT","facetCounts":[{"count":9,"query":"vehicle_type_code:VEHTYPE_V","sortKey":"","sequenceNumber":10,"uri":"automobiles","synonyms":[""],"displayName":"Automobiles"}],"sequenceNumber":80,"includeTag":"{!tag=VEHT}","displayName":"Vehicle Type"},{"quickPickCode":"PRID","facetCounts":[{"count":1,"query":"damage_type_code:DAMAGECODE_BN","sortKey":"","sequenceNumber":15,"uri":"burn","synonyms":[""],"displayName":"Burn"},{"count":5,"query":"damage_type_code:DAMAGECODE_FR","sortKey":"","sequenceNumber":45,"uri":"frontend","synonyms":[""],"displayName":"Front End"},{"count":2,"query":"damage_type_code:DAMAGECODE_RR","sortKey":"","sequenceNumber":95,"uri":"rearend","synonyms":[""],"displayName":"Rear End"},{"count":1,"query":"damage_type_code:DAMAGECODE_SD","sortKey":"","sequenceNumber":100,"uri":"side","synonyms":[""],"displayName":"Side"}],"sequenceNumber":110,"includeTag":"{!tag=PRID}","displayName":"Damage"},{"quickPickCode":"BODY","facetCounts":[{"count":2,"query":"body_style:\"CONVERTI\"","sequenceNumber":0,"displayName":"Converti","columnName":"body_style"},{"count":4,"query":"body_style:\"COUPE\"","sequenceNumber":0,"displayName":"Coupe","columnName":"body_style"}],"sequenceNumber":120,"includeTag":"{!tag=BODY}","displayName":"Body Style"},{"quickPickCode":"FUEL","facetCounts":[{"count":8,"query":"fuel_type_desc:\"GAS\"","sequenceNumber":0,"displayName":"Gas","columnName":"fuel_type_desc"}],"sequenceNumber":130,"includeTag":"{!tag=FUEL}","displayName":"Fuel Type"},{"quickPickCode":"ENGN","facetCounts":[{"count":8,"query":"engine:\"5.2L 10\"","sequenceNumber":0,"displayName":"5.2l 10","columnName":"engine"}],"sequenceNumber":140,"includeTag":"{!tag=ENGN}","displayName":"Engine Type"},{"quickPickCode":"TMTP","facetCounts":[{"count":8,"query":"transmission_type:\"AUTOMATIC\"","sequenceNumber":0,"displayName":"Automatic","columnName":"transmission_type"}],"sequenceNumber":145,"includeTag":"{!tag=TMTP}","displayName":"Transmission"},{"quickPickCode":"DRIV","facetCounts":[{"count":5,"query":"drive:\"All wheel drive\"","sequenceNumber":0,"displayName":"All Wheel Drive","columnName":"drive"},{"count":3,"query":"drive:\"Rear-wheel drive\"","sequenceNumber":0,"displayName":"Rear-wheel Drive","columnName":"drive"}],"sequenceNumber":150,"includeTag":"{!tag=DRIV}","displayName":"Drive Train"},{"quickPickCode":"CYLN","facetCounts":[{"count":8,"query":"cylinders:\"10\"","sequenceNumber":0,"displayName":"10","columnName":"cylinders"}],"sequenceNumber":160,"includeTag":"{!tag=CYLN}","displayName":"Cylinder"}],"spellCheckList":null,"suggestions":null,"realTime":false}}}'

assert response.status_code == 200
print("Assertion is complete")
jo = json.loads(response.text)

print(jo['data']['results']['content'][1])

data_1 = (jo['data']['results']['content'][0])
data_2 = (jo['data']['results']['content'][1])
data_3 = (jo['data']['results']['content'][3])
data_4 = (jo['data']['results']['content'][4])
data_5 = (jo['data']['results']['content'][5])
data_6 = (jo['data']['results']['content'][6])
data_7 = (jo['data']['results']['content'][7])
data_8 = (jo['data']['results']['content'][8])

page_1 = (jo['data']['results']['content'][0])
page_2 = (jo['data']['results']['content'][1])
page_3 = (jo['data']['results']['content'][3])
page_4 = (jo['data']['results']['content'][4])
page_5 = (jo['data']['results']['content'][5])
page_6 = (jo['data']['results']['content'][6])
page_7 = (jo['data']['results']['content'][7])
page_8 = (jo['data']['results']['content'][8])


print(page_1)
@pytest.mark.parametrize("test_input, expected_result",
                         [(data_1, page_1), (data_2, page_2), (data_3, page_4), (data_4, page_4)])
def test_multiplication(test_input, expected_result):
    if test_input == expected_result:
        assert test_input == expected_result
    elif test_input != expected_result:
        print(" ----- This assertion is failed----")
