import asyncio
import random

from Legendbot.core.managers import eor
from Legendbot.helpers.functions import age_verification
from Legendbot.helpers.utils import reply_id
from Legendbot.plugins import legend, swtmemes, useless
from Legendbot.sql_helper.globals import addgvar, gvarstatus

menu_category = "extra"


RAID = [
    "MADARCHOD TERI MAA KI CHUT ME GHUTKA KHAAKE THOOK DUNGA ð¤£ð¤£",
    "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA",
    "TERI MAA K BHOSDE ME AEROPLANEPARK KARKE UDAAN BHAR DUGA âï¸ð«",
    "TERI MAA KI CHUT ME SUTLI BOMB FOD DUNGA TERI MAA KI JHAATE JAL KE KHAAK HO JAYEGIð£",
    "TERI MAAKI CHUT ME SCOOTER DAAL DUGAð",
    "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA",
    "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA",
    "TERI MAA KI CHUT KAKTE ð¤± GALI KE KUTTO ð¦® ME BAAT DUNGA PHIR ð BREAD KI TARH KHAYENGE WO TERI MAA KI CHUT",
    "DUDH HILAAUNGA TERI VAHEEN KE UPR NICHE ððð",
    "TERI MAA KI CHUT ME â HATTH DALKE ð¶ BACCHE NIKAL DUNGA ð",
    "TERI BEHN KI CHUT ME KELE KE CHILKE ððð",
    "TERI BHEN KI CHUT ME USERBOT LAGAAUNGA SASTE SPAM KE CHODE",
    "TERI VAHEEN DHANDHE VAALI ðð",
    "TERI MAA KE BHOSDE ME AC LAGA DUNGA SAARI GARMI NIKAL JAAYEGI",
    "TERI VAHEEN KO HORLICKS PEELAUNGA MADARCHODð",
    "TERI MAA KI GAAND ME SARIYA DAAL DUNGA MADARCHOD USI SARIYE PR TANG KE BACHE PAIDA HONGE ð±ð±",
    "TERI MAA KO KOLKATA VAALE JITU BHAIYA KA LUND MUBARAK ð¤©ð¤©",
    "TERI MUMMY KI FANTASY HU LAWDE, TU APNI BHEN KO SMBHAAL ðð",
    "TERA PEHLA BAAP HU MADARCHOD ",
    "TERI VAHEEN KE BHOSDE ME XVIDEOS.COM CHALA KE MUTH MAARUNGA ð¤¡ð¹",
    "TERI MAA KA GROUP VAALON SAATH MILKE GANG BANG KRUNGAðð»â ï¸ ",
    "TERI ITEM KI GAAND ME LUND DAALKE,TERE JAISA EK OR NIKAAL DUNGA MADARCHODð¤ð»ðð»â ï¸ ",
    "AUKAAT ME REH VRNA GAAND ME DANDA DAAL KE MUH SE NIKAAL DUNGA SHARIR BHI DANDE JESA DIKHEGA ðð¤­ð¤­",
    "TERI MUMMY KE SAATH LUDO KHELTE KHELTE USKE MUH ME APNA LODA DE DUNGAâð»âð»ð¬",
    "TERI VAHEEN KO APNE LUND PR ITNA JHULAAUNGA KI JHULTE JHULTE HI BACHA PAIDA KR DEGIðð¯ ",
    "TERI MAA KI CHUT MEI BATTERY LAGA KE POWERBANK BANA DUNGA ð ð¥ð¤©",
    "TERI MAA KI CHUT MEI C++ STRING ENCRYPTION LAGA DUNGA BAHTI HUYI CHUT RUK JAYEGIIIIðð¥ð",
    "TERI MAA KE GAAND MEI JHAADU DAL KE MOR ð¦ BANA DUNGAA ð¤©ð¥µð±",
    "TERI CHUT KI CHUT MEI SHOULDERING KAR DUNGAA HILATE HUYE BHI DARD HOGAAAð±ð¤®ðº",
    "TERI MAA KO REDI PE BAITHAL KE USSE USKI CHUT BILWAUNGAA ð° ðµð¤©",
    "BHOSDIKE TERI MAA KI CHUT MEI 4 HOLE HAI UNME MSEAL LAGA BAHUT BAHETI HAI BHOFDIKEðð¤®ð¤¢ð¤¢",
    "TERI BAHEN KI CHUT MEI BARGAD KA PED UGA DUNGAA CORONA MEI SAB OXYGEN LEKAR JAYENGEð¤¢ð¤©ð¥³",
    "TERI MAA KI CHUT MEI SUDO LAGA KE BIGSPAM LAGA KE 9999 FUCK LAGAA DU ð¤©ð¥³ð¥",
    "TERI VAHEN KE BHOSDIKE MEI BESAN KE LADDU BHAR DUNGAð¤©ð¥³ð¥ð",
    "TERI MAA KI CHUT KHOD KE USME CYLINDER â½ï¸ FIT KARKE USMEE DAL MAKHANI BANAUNGAAAð¤©ðð¥",
    "TERI MAA KI CHUT MEI SHEESHA DAL DUNGAAA AUR CHAURAHE PE TAANG DUNGA BHOSDIKEðð±ð¤©",
    "TERI MAA KI CHUT MEI CREDIT CARD DAL KE AGE SE 500 KE KAARE KAARE NOTE NIKALUNGAA BHOSDIKEð°ð°ð¤©",
    "TERI MAA KE SATH SUAR KA SEX KARWA DUNGAA EK SATH 6-6 BACHE DEGIð°ð¥ð±",
    "TERI BAHEN KI CHUT MEI APPLE KA 18W WALA CHARGER ð¥ð¤©",
    "TERI BAHEN KI GAAND MEI ONEPLUS KA WRAP CHARGER 30W HIGH POWER ð¥ðð",
    "TERI BAHEN KI CHUT KO AMAZON SE ORDER KARUNGA 10 rs MEI AUR FLIPKART PE 20 RS MEI BECH DUNGAð¤®ð¿ðð¤",
    "TERI MAA KI BADI BHUND ME ZOMATO DAL KE SUBWAY KA BFF VEG SUB COMBO [15cm , 16 inches ] ORDER COD KRVAUNGA OR TERI MAA JAB DILIVERY DENE AYEGI TAB USPE JAADU KRUNGA OR FIR 9 MONTH BAAD VO EK OR FREE DILIVERY DEGIððð¥³ð¥",
    "TERI BHEN KI CHUT KAALIðð¤£ð¥",
    "TERI MAA KI CHUT ME CHANGES COMMIT KRUGA FIR TERI BHEEN KI CHUT AUTOMATICALLY UPDATE HOJAAYEGIð¤ðð¤",
    "TERI MAUSI KE BHOSDE MEI INDIAN RAILWAY ðð¥ð",
    "TU TERI BAHEN TERA KHANDAN SAB BAHEN KE LAWDE RANDI HAI RANDI ð¤¢âð¥",
    "TERI BAHEN KI CHUT MEI IONIC BOND BANA KE VIRGINITY LOOSE KARWA DUNGA USKI ð ðð¤©",
    "TERI RANDI MAA SE PUCHNA BAAP KA NAAM BAHEN KE LODEEEEE ð¤©ð¥³ð³",
    "TU AUR TERI MAA DONO KI BHOSDE MEI METRO CHALWA DUNGA MADARXHOD ðð¤©ð±ð¥¶",
    "TERI MAA KO ITNA CHODUNGA TERA BAAP BHI USKO PAHCHANANE SE MANA KAR DEGAðð¿ð¤©",
    "TERI BAHEN KE BHOSDE MEI HAIR DRYER CHALA DUNGAAð¥ð¥ð¥",
    "TERI MAA KI CHUT MEI TELEGRAM KI SARI RANDIYON KA RANDI KHANA KHOL DUNGAAð¿ð¤®ð",
    "TERI MAA KI CHUT ALEXA DAL KEE DJ BAJAUNGAAA ð¶ â¬ï¸ð¤©ð¥",
    "TERI MAA KE BHOSDE MEI GITHUB DAL KE APNA BOT HOST KARUNGAA ð¤©ðð¤ð",
    "TERI BAHEN KA VPS BANA KE 24*7 BASH CHUDAI COMMAND DE DUNGAA ð¤©ð¥ð¥ð¥",
    "TERI MUMMY KI CHUT MEI TERE LAND KO DAL KE KAAT DUNGA MADARCHOD ðªðð¥",
    "SUN TERI MAA KA BHOSDA AUR TERI BAHEN KA BHI BHOSDA ð¿ðð",
    "TUJHE DEKH KE TERI RANDI BAHEN PE TARAS ATA HAI MUJHE BAHEN KE LODEEEE ð¿ð¥ð¤©ð¥",
    "SUN MADARCHOD JYADA NA UCHAL MAA CHOD DENGE EK MIN MEI âð¤£ð¥ð¤©",
    "APNI AMMA SE PUCHNA USKO US KAALI RAAT MEI KAUN CHODNEE AYA THAAA! TERE IS PAPA KA NAAM LEGI ðð¿ð³",
    "TOHAR BAHIN CHODU BBAHEN KE LAWDE USME MITTI DAL KE CEMENT SE BHAR DU ð ð¤¢ð¤©ð¥",
    "TUJHE AB TAK NAHI SMJH AYA KI MAI HI HU TUJHE PAIDA KARNE WALA BHOSDIKEE APNI MAA SE PUCH RANDI KE BACHEEEE ð¤©ðð¤ð",
    "TERI MAA KE BHOSDE MEI SPOTIFY DAL KE LOFI BAJAUNGA DIN BHAR ðð¶ð¶ð¥",
    "TERI MAA KA NAYA RANDI KHANA KHOLUNGA CHINTA MAT KAR ðð¤£ð¤£ð³",
    "TERA BAAP HU BHOSDIKE TERI MAA KO RANDI KHANE PE CHUDWA KE US PAISE KI DAARU PEETA HU ð·ð¤©ð¥",
    "TERI BAHEN KI CHUT MEI APNA BADA SA LODA GHUSSA DUNGAA KALLAAP KE MAR JAYEGI ð¤©ð³ð³ð¥",
    "TOHAR MUMMY KI CHUT MEI PURI KI PURI KINGFISHER KI BOTTLE DAL KE TOD DUNGA ANDER HI ð±ðð¤©",
    "TERI MAA KO ITNA CHODUNGA KI SAPNE MEI BHI MERI CHUDAI YAAD KAREGI RANDI ð¥³ððð¥",
    "TERI MUMMY AUR BAHEN KO DAUDA DAUDA NE CHODUNGA UNKE NO BOLNE PE BHI LAND GHUSA DUNGA ANDER TAK ððð¤£ð¥",
    "TERI MUMMY KI CHUT KO ONLINE OLX PE BECHUNGA AUR PAISE SE TERI BAHEN KA KOTHA KHOL DUNGA ðð¤©ðð",
    "TERI MAA KE BHOSDA ITNA CHODUNGA KI TU CAH KE BHI WO MAST CHUDAI SE DUR NHI JA PAYEGAA ððð¤©ð",
    "SUN BE RANDI KI AULAAD TU APNI BAHEN SE SEEKH KUCH KAISE GAAND MARWATE HAIðð¤¬ð¥ð¥",
    "TERI MAA KA YAAR HU MEI AUR TERI BAHEN KA PYAAR HU MEI AJA MERA LAND CHOOS LE ð¤©ð¤£ð¥",
    "TERI BHEN KI CHUT ME USERBOT LAGAAUNGA SASTE SPAM KE CHODE",
    "TERI MAA KI GAAND ME SARIYA DAAL DUNGA MADARCHOD USI SARIYE PR TANG KE BACHE PAIDA HONGE ð±ð±",
    "TERI MAA KI CHUT ME â HATTH DALKE ð¶ BACCHE NIKAL DUNGA ð",
    "TERI BEHN KI CHUT ME KELE KE CHILKE ð¤¤ð¤¤",
    "TERI MAA KI CHUT ME SUTLI BOMB FOD DUNGA TERI MAA KI JHAATE JAL KE KHAAK HO JAYEGIð£ð",
    "TERI VAHEEN KO HORLICKS PEELAKE CHODUNGA MADARCHODð",
    "TERI ITEM KI GAAND ME LUND DAALKE,TERE JAISA EK OR NIKAAL DUNGA MADARCHODðð¤¤ð",
    "TERI VAHEEN KO APNE LUND PR ITNA JHULAAUNGA KI JHULTE JHULTE HI BACHA PAIDA KR DEGI ð¦ð",
    "SUAR KE PILLE TERI MAAKO SADAK PR LITAKE CHOD DUNGA ððð¤¤",
    "ABE TERI MAAKA BHOSDA MADERCHOOD KR PILLE PAPA SE LADEGA TU ð¼ðð¤¤",
    "GALI GALI NE SHOR HE TERI MAA RANDI CHOR HE ððð¦",
    "ABE TERI BEHEN KO CHODU RANDIKE PILLE KUTTE KE CHODE ðð»ð¥",
    "TERI MAAKO AISE CHODA AISE CHODA TERI MAAA BED PEHI MUTH DIA ð¦ð¦ð¦ð¦",
    "TERI BEHEN KE BHOSDE ME AAAG LAGADIA MERA MOTA LUND DALKE ð¥ð¥ð¦ðð",
    "RANDIKE BACHHE TERI MAAKO CHODU CHAL NIKAL",
    "KITNA CHODU TERI RANDI MAAKI CHUTH ABB APNI BEHEN KO BHEJ ðð»ð¤¤",
    "TERI BEHEN KOTO CHOD CHODKE PURA FAAD DIA CHUTH ABB TERI GF KO BHEJ ðð¦ð¤¤",
    "TERI GF KO ETNA CHODA BEHEN KE LODE TERI GF TO MERI RANDI BANGAYI ABB CHAL TERI MAAKO CHODTA FIRSE â¥ï¸ð¦ðððð",
    "HARI HARI GHAAS ME JHOPDA TERI MAAKA BHOSDA ð¤£ð¤£ðð¦",
    "CHAL TERE BAAP KO BHEJ TERA BASKA NHI HE PAPA SE LADEGA TU",
    "TERI BEHEN KI CHUTH ME BOMB DALKE UDA DUNGA MAAKE LAWDE",
    "TERI MAAKO TRAIN ME LEJAKE TOP BED PE LITAKE CHOD DUNGA SUAR KE PILLE ð¤£ð¤£ðð",
    "TERI MAAAKE NUDES GOOGLE PE UPLOAD KARDUNGA BEHEN KE LAEWDE ð»ð¥",
    "TERI MAAAKE NUDES GOOGLE PE UPLOAD KARDUNGA BEHEN KE LAEWDE ð»ð¥",
    "TERI BEHEN KO CHOD CHODKE VIDEO BANAKE XNXX.COM PE NEELAM KARDUNGA KUTTE KE PILLE ð¦ð",
    "TERI MAAAKI CHUDAI KO PORNHUB.COM PE UPLOAD KARDUNGA SUAR KE CHODE ð¤£ðð¦",
    "ABE TERI BEHEN KO CHODU RANDIKE BACHHE TEREKO CHAKKO SE PILWAVUNGA RANDIKE BACHHE ð¤£ð¤£",
    "TERI MAAKI CHUTH FAADKE RAKDIA MAAKE LODE JAA ABB SILWALE ðð",
    "TERI BEHEN KI CHUTH ME MERA LUND KAALA",
    "TERI BEHEN LETI MERI LUND BADE MASTI SE TERI BEHEN KO MENE CHOD DALA BOHOT SASTE SE",
    "BETE TU BAAP SE LEGA PANGA TERI MAAA KO CHOD DUNGA KARKE NANGA ð¦ð",
    "HAHAHAH MERE BETE AGLI BAAR APNI MAAKO LEKE AAYA MATH KAT OR MERE MOTE LUND SE CHUDWAYA MATH KAR",
    "CHAL BETA TUJHE MAAF KIA ð¤£ ABB APNI GF KO BHEJ",
    "SHARAM KAR TERI BEHEN KA BHOSDA KITNA GAALIA SUNWAYEGA APNI MAAA BEHEN KE UPER",
    "ABE RANDIKE BACHHE AUKAT NHI HETO APNI RANDI MAAKO LEKE AAYA MATH KAR HAHAHAHA",
    "KIDZ MADARCHOD TERI MAAKO CHOD CHODKE TERR LIYE BHAI DEDIYA",
    "JUNGLE ME NACHTA HE MORE TERI MAAKI CHUDAI DEKKE SAB BOLTE ONCE MORE ONCE MORE ð¤£ð¤£ð¦ð",
    "GALI GALI ME REHTA HE SAND TERI MAAKO CHOD DALA OR BANA DIA RAND ð¤¤ð¤£",
    "SAB BOLTE MUJHKO PAPA KYOUNKI MENE BANADIA TERI MAAKO PREGNENT ð¤£ð¤£",
    "SUAR KE PILLE TERI MAAKI CHUTH ME SUAR KA LOUDA OR TERI BEHEN KI CHUTH ME MERA LODA",
    "CHAL CHAL APNI MAAKI CHUCHIYA DIKA",
    "HAHAHAHA BACHHE TERI MAAAKO CHOD DIA NANGA KARKE",
    "TERI GF HE BADI SEXY USKO PILAKE CHOODENGE PEPSI",
    "2 RUPAY KI PEPSI TERI MUMMY SABSE SEXY ðð¦",
    "TERI MAAKO CHEEMS SE CHUDWAVUNGA MADERCHOOD KE PILLE ð¦ð¤£",
    "TERI BEHEN KI CHUTH ME MUTHKE FARAR HOJAVUNGA HUI HUI HUI",
    "SPEED LAAA TERI BEHEN CHODU RANDIKE PILLE ðð¦ð¤£",
    "ARE RE MERE BETE KYOUN SPEED PAKAD NA PAAA RAHA APNE BAAP KA HAHAHð¤£ð¤£",
    "SUN SUN SUAR KE PILLE JHANTO KE SOUDAGAR APNI MUMMY KI NUDES BHEJ",
    "ABE SUN LODE TERI BEHEN KA BHOSDA FAAD DUNGA",
    "TERI MAAKO KHULE BAJAR ME CHOD DALA ð¤£ð¤£ð",
    "MADARCHOD",
    "BHOSDIKE",
    "LAAAWEEE KE BAAAAAL",
    "MAAAAR KI JHAAAAT KE BBBBBAAAAALLLLL",
    "MADRCHOD..",
    "TERI MA KI CHUT..",
    "LWDE KE BAAALLL.",
    "MACHAR KI JHAAT KE BAAALLLL",
    "TERI MA KI CHUT M DU TAPA TAP?",
    "TERI MA KA BHOSDAA",
    "TERI BHN SBSBE BDI RANDI.",
    "TERI MA OSSE BADI RANDDDDD",
    "TERA BAAP CHKAAAA",
    "KITNI CHODU TERI MA AB OR..",
    "TERI MA CHOD DI HM NE",
    "KITNI CHODU TERI MA AB OR..",
    "TERI MA CHOD DI HM NE",
    "TERI MA KE STH REELS BNEGA ROAD PEE",
    "TERI MA KI CHUT EK DAM TOP SEXY",
    "MALUM NA PHR KESE LETA HU M TERI MA KI CHUT TAPA TAPPPPP",
    "LUND KE CHODE TU KEREGA TYPIN",
    "SPEED PKD LWDEEEE",
    "BAAP KI SPEED MTCH KRRR",
    "LWDEEE",
    "PAPA KI SPEED MTCH NHI HO RHI KYA",
    "ALE ALE MELA BCHAAAA",
    "CHUD GYA PAPA SEEE",
    "KISAN KO KHODNA OR",
    "SALE RAPEKL KRDKA TERA",
    "HAHAHAAAAA",
    "HAHAHAAAAA",
    "KIDSSSS",
    "TERI MA CHUD GYI AB FRAR MT HONA",
    "YE LDNGE BAPP SE",
    "KIDSSS FRAR HAHAHH",
    "BHEN KE LWDE SHRM KR",
    "KITNI GLIYA PDWEGA APNI MA KO",
    "NALLEE",
    "SUAR KE PILLE TERI MAAKO SADAK PR LITAKE CHOD DUNGA ððð¤¤",
    "ABE TERI MAAKA BHOSDA MADERCHOOD KR PILLE PAPA SE LADEGA TU ð¼ðð¤¤",
    "GALI GALI NE SHOR HE TERI MAA RANDI CHOR HE ððð¦",
    "ABE TERI BEHEN KO CHODU RANDIKE PILLE KUTTE KE CHODE ðð»ð¥",
    "TERI MAAKO AISE CHODA AISE CHODA TERI MAAA BED PEHI MUTH DIA ð¦ð¦ð¦ð¦",
    "TERI BEHEN KE BHOSDE ME AAAG LAGADIA MERA MOTA LUND DALKE ð¥ð¥ð¦ðð",
    "RANDIKE BACHHE TERI MAAKO CHODU CHAL NIKAL",
    "KITNA CHODU TERI RANDI MAAKI CHUTH ABB APNI BEHEN KO BHEJ ðð»ð¤¤",
    "TERI BEHEN KOTO CHOD CHODKE PURA FAAD DIA CHUTH ABB TERI GF KO BHEJ ðð¦ð¤¤",
    "TERI GF KO ETNA CHODA BEHEN KE LODE TERI GF TO MERI RANDI BANGAYI ABB CHAL TERI MAAKO CHODTA FIRSE â¥ï¸ð¦ðððð",
    "HARI HARI GHAAS ME JHOPDA TERI MAAKA BHOSDA ð¤£ð¤£ðð¦",
    "CHAL TERE BAAP KO BHEJ TERA BASKA NHI HE PAPA SE LADEGA TU",
    "TERI BEHEN KI CHUTH ME BOMB DALKE UDA DUNGA MAAKE LAWDE",
    "TERI MAAKO TRAIN ME LEJAKE TOP BED PE LITAKE CHOD DUNGA SUAR KE PILLE ð¤£ð¤£ðð",
    "TERI MAAAKE NUDES GOOGLE PE UPLOAD KARDUNGA BEHEN KE LAEWDE ð»ð¥",
    "TERI MAAAKE NUDES GOOGLE PE UPLOAD KARDUNGA BEHEN KE LAEWDE ð»ð¥",
    "TERI BEHEN KO CHOD CHODKE VIDEO BANAKE XNXX.COM PE NEELAM KARDUNGA KUTTE KE PILLE ð¦ð",
    "TERI MAAAKI CHUDAI KO PORNHUB.COM PE UPLOAD KARDUNGA SUAR KE CHODE ð¤£ðð¦",
    "ABE TERI BEHEN KO CHODU RANDIKE BACHHE TEREKO CHAKKO SE PILWAVUNGA RANDIKE BACHHE ð¤£ð¤£",
    "TERI MAAKI CHUTH FAADKE RAKDIA MAAKE LODE JAA ABB SILWALE ðð",
    "TERI BEHEN KI CHUTH ME MERA LUND KAALA",
    "TERI BEHEN LETI MERI LUND BADE MASTI SE TERI BEHEN KO MENE CHOD DALA BOHOT SASTE SE",
    "BETE TU BAAP SE LEGA PANGA TERI MAAA KO CHOD DUNGA KARKE NANGA ð¦ð",
    "HAHAHAH MERE BETE AGLI BAAR APNI MAAKO LEKE AAYA MATH KAT OR MERE MOTE LUND SE CHUDWAYA MATH KAR",
    "CHAL BETA TUJHE MAAF KIA ð¤£ ABB APNI GF KO BHEJ",
    "SHARAM KAR TERI BEHEN KA BHOSDA KITNA GAALIA SUNWAYEGA APNI MAAA BEHEN KE UPER",
    "ABE RANDIKE BACHHE AUKAT NHI HETO APNI RANDI MAAKO LEKE AAYA MATH KAR HAHAHAHA",
    "KIDZ MADARCHOD TERI MAAKO CHOD CHODKE TERR LIYE BHAI DEDIYA",
    "JUNGLE ME NACHTA HE MORE TERI MAAKI CHUDAI DEKKE SAB BOLTE ONCE MORE ONCE MORE ð¤£ð¤£ð¦ð",
    "GALI GALI ME REHTA HE SAND TERI MAAKO CHOD DALA OR BANA DIA RAND ð¤¤ð¤£",
    "SAB BOLTE MUJHKO PAPA KYOUNKI MENE BANADIA TERI MAAKO PREGNENT ð¤£ð¤£",
    "SUAR KE PILLE TERI MAAKI CHUTH ME SUAR KA LOUDA OR TERI BEHEN KI CHUTH ME MERA LODA",
    "CHAL CHAL APNI MAAKI CHUCHIYA DIKA",
    "HAHAHAHA BACHHE TERI MAAAKO CHOD DIA NANGA KARKE",
    "TERI GF HE BADI SEXY USKO PILAKE CHOODENGE PEPSI",
    "2 RUPAY KI PEPSI TERI MUMMY SABSE SEXY ðð¦",
    "TERI MAAKO CHEEMS SE CHUDWAVUNGA MADERCHOOD KE PILLE ð¦ð¤£",
    "TERI BEHEN KI CHUTH ME MUTHKE FARAR HOJAVUNGA HUI HUI HUI",
    "SPEED LAAA TERI BEHEN CHODU RANDIKE PILLE ðð¦ð¤£",
    "ARE RE MERE BETE KYOUN SPEED PAKAD NA PAAA RAHA APNE BAAP KA HAHAHð¤£ð¤£",
    "SUN SUN SUAR KE PILLE JHANTO KE SOUDAGAR APNI MUMMY KI NUDES BHEJ",
    "ABE SUN LODE TERI BEHEN KA BHOSDA FAAD DUNGA",
    "TERI MAAKO KHULE BAJAR ME CHOD DALA ð¤£ð¤£ð",
    "SHRM KR",
    "MERE LUND KE BAAAAALLLLL",
    "KITNI GLIYA PDWYGA APNI MA BHEN KO",
    "RNDI KE LDKEEEEEEEEE",
    "KIDSSSSSSSSSSSS",
    "Apni gaand mein muthi daal",
    "Apni lund choos",
    "Apni ma ko ja choos",
    "Bhen ke laude",
    "Bhen ke takke",
    "Abla TERA KHAN DAN CHODNE KI BARIII",
    "BETE TERI MA SBSE BDI RAND",
    "LUND KE BAAAL JHAT KE PISSSUUUUUUU",
    "LUND PE LTKIT MAAALLLL KI BOND H TUUU",
    "KASH OS DIN MUTH MRKE SOJTA M TUN PAIDA NA HOTAA",
    "GLTI KRDI TUJW PAIDA KRKE",
    "SPEED PKDDD",
    "Gaand main LWDA DAL LE APNI MERAAA",
    "Gaand mein bambu DEDUNGAAAAAA",
    "GAND FTI KE BALKKK",
    "Gote kitne bhi bade ho, lund ke niche hi rehte hai",
    "Hazaar lund teri gaand main",
    "Jhaant ke pissu-",
    "TERI MA KI KALI CHUT",
    "Khotey ki aulda",
    "Kutte ka awlat",
    "Kutte ki jat",
    "Kutte ke tatte",
    "TETI MA KI.CHUT , tERI MA RNDIIIIIIIIIIIIIIIIIIII",
    "Lavde ke bal",
    "muh mei lele",
    "Lund Ke Pasine",
    "MERE LWDE KE BAAAAALLL",
    "HAHAHAAAAAA",
    "CHUD GYAAAAA",
    "Randi khanE KI ULADDD",
    "Sadi hui gaand",
    "Teri gaand main kute ka lund",
    "Teri maa ka bhosda",
    "Teri maa ki chut",
    "Tere gaand mein keede paday",
    "Ullu ke pathe",
    "SUNN MADERCHOD",
    "TERI MAA KA BHOSDA",
    "BEHEN K LUND",
    "TERI MAA KA CHUT KI CHTNIIII",
    "MERA LAWDA LELE TU AGAR CHAIYE TOH",
    "GAANDU",
    "CHUTIYA",
    "TERI MAA KI CHUT PE JCB CHADHAA DUNGA",
    "SAMJHAA LAWDE",
    "YA DU TERE GAAND ME TAPAA TAPï¿½ï¿½",
    "TERI BEHEN MERA ROZ LETI HAI",
    "TERI GF K SAATH MMS BANAA CHUKA HUï¿½ï¿½ï¿½ä¸ï¿½ä¸",
    "TU CHUTIYA TERA KHANDAAN CHUTIYA",
    "AUR KITNA BOLU BEY MANN BHAR GAYA MERAï¿½ä¸",
    "TERIIIIII MAAAA KI CHUTTT ME ABCD LIKH DUNGA MAA KE LODE",
    "TERI MAA KO LEKAR MAI FARAR",
    "RANIDIII",
    "BACHEE",
    "CHODU",
    "RANDI",
    "RANDI KE PILLE",
    "TERIIIII MAAA KO BHEJJJ",
    "TERAA BAAAAP HU",
    "teri MAA KI CHUT ME HAAT DAALLKE BHAAG JAANUGA",
    "Teri maa KO SARAK PE LETAA DUNGA",
    "TERI MAA KO GB ROAD PE LEJAKE BECH DUNGA",
    "Teri maa KI CHUT MÃ KAALI MITCH",
    "TERI MAA SASTI RANDI HAI",
    "TERI MAA KI CHUT ME KABUTAR DAAL KE SOUP BANAUNGA MADARCHOD",
    "TERI MAAA RANDI HAI",
    "TERI MAAA KI CHUT ME DETOL DAAL DUNGA MADARCHOD",
    "TERI MAA KAAA BHOSDAA",
    "TERI MAA KI CHUT ME LAPTOP",
    "Teri maa RANDI HAI",
    "TERI MAA KO BISTAR PE LETAAKE CHODUNGA",
    "TERI MAA KO AMERICA GHUMAAUNGA MADARCHOD",
    "TERI MAA KI CHUT ME NAARIYAL PHOR DUNGA",
    "TERI MAA KE GAND ME DETOL DAAL DUNGA",
    "TERI MAAA KO HORLICKS PILAUNGA MADARCHOD",
    "TERI MAA KO SARAK PE LETAAA DUNGAAA",
    "TERI MAA KAA BHOSDA",
    "MERAAA LUND PAKAD LE MADARCHOD",
    "CHUP TERI MAA AKAA BHOSDAA",
    "TERIII MAA CHUF GEYII KYAAA LAWDEEE",
    "TERIII MAA KAA BJSODAAA",
    "MADARXHODDD",
    "TERIUUI MAAA KAA BHSODAAA",
    "TERIIIIII BEHENNNN KO CHODDDUUUU MADARXHODDDD",
    "NIKAL MADARCHOD",
    "RANDI KE BACHE",
    "TERA MAA MERI FAN",
    "TERI SEXY BAHEN KI CHUT OP",
]


@legend.legend_cmd(
    pattern="abuse$",
    command=("abuse", menu_category),
    info={
        "header": "Random Sending Abuse Like spam to stop .restart ",
        "usage": "{tr}abuse",
    },
)
async def yashraid(e):
    reply_to = await reply_id(e)
    if await age_verification(e, reply_to):
        return
    type = await useless.importent(e)
    if type:
        return
    addgvar("spamwork", True)
    counter = int("1000")
    for _ in range(counter):
        if gvarstatus("spamwork") is None:
            return
        reply = random.choice(RAID)
        caption = f"{reply}"
        await e.client.send_message(e.chat_id, caption)


@legend.legend_cmd(
    pattern="gali$",
    command=("gali", menu_category),
    info={
        "header": "shows you some abuse sentences",
        "usage": "{tr}gali",
    },
)
async def abujjnsing(abused):
    "random abuse string"
    reply_text = random.choice(swtmemes.ABUSE_STRINGS)
    await eor(abused, reply_text)


@legend.legend_cmd(
    pattern="abusehard$",
    command=("abusehard", menu_category),
    info={
        "header": "shows you some gali sentences",
        "usage": "{tr}abusehard",
    },
)
async def fuckloedd(abusehard):
    "random gali string"
    reply_text = random.choice(swtmemes.ABUSEHARD_STRING)
    await eor(abusehard, reply_text)


@legend.legend_cmd(
    pattern="rendi$",
    command=("rendi", menu_category),
    info={
        "header": "shows you some gali sentences",
        "usage": "{tr}rendi",
    },
)
async def met(e):
    "random gali string"
    txt = random.choice(swtmemes.RENDISTR)
    await eor(e, txt)


@legend.legend_cmd(
    pattern="fuck$",
    command=("fuck", menu_category),
    info={
        "header": "shows you some gali sentences",
        "usage": "{tr}fuck",
    },
)
async def chuya(fuks):
    "random gali string"
    reply_text = random.choice(swtmemes.CHU_STRINGS)
    await eor(fuks, reply_text)


@legend.legend_cmd(
    pattern="thanos$",
    command=("thanos", menu_category),
    info={
        "header": "shows you some gali sentences",
        "usage": "{tr}thanos",
    },
)
async def thaos(thanos):
    "random gali string"
    reply_text = random.choice(swtmemes.THANOS_STRINGS)
    await eor(thanos, reply_text)


@legend.legend_cmd(
    pattern="gf$",
    command=("gf", menu_category),
    info={
        "header": "bad animation, try yourself ",
        "usage": "{tr}gf",
    },
)
async def akai(event):
    "Bad stuff"
    animation_interval = 5
    animation_ttl = range(21)
    kakashi = await eor(event, "BSDK tera gf h na ek ...!")
    animation_chars = [
        "`Ruk jaa , Abhi teri GF ko Fuck karta hu `",
        "`Making your Gf warm ð¥`",
        "`Pressing her boobs ð¤ð`",
        "`Stimulating her pussyð`",
        "`Fingering her pussy ð§ðð `",
        "`Asking her to taste my DICKð`",
        "`Requested acceptedð»ð, Ready to taste my DICKð`",
        "`Getting her ready to fuck ð`",
        "`Your GF Is Ready To Fuck`",
        "`Fucking Your GFðð\n\n\nYour GF's Pussy Get Red\nTrying new SEX position to make her Squirt\n\nAlmost Done. 0%\nâââââââââââââââââââââââââ `",
        "`Fucking Your GFðð\n\n\nYour GF's Pussy Get White\nShe squirted like a showerð§ð¦ð\n\nAlmost Done..\n\nFucked Percentage... 4%\nâââââââââââââââââââââââââ `",
        "`Fucking Your GFðð\n\n\nYour GF's Pussy Get Red\nDoing Extreme SEX with herð\n\nAlmost Done...\n\nFucked Percentage... 8%\nâââââââââââââââââââââââââ `",
        "`Fucking Your GFðð\n\n\nYour GF's Pussy Get Red\nWarming her Assð to Fuck!ðð\n\nAlmost Done....\n\nFucked Percentage... 20%\nâââââââââââââââââââââââââ `",
        "`Fucking Your GFðð\n\n\nYour GF's ASSð Get Red\nInserted my Penisð in her ASSð\n\nAlmost Done.....\n\nFucked Percentage... 36%\nâââââââââââââââââââââââââ `",
        "`Fucking Your GFðð\n\n\nYour GF's ASSð Get Red\ndoing extreme sex with her\n\nAlmost Done......\n\nFucked Percentage... 52%\nâââââââââââââââââââââââââ `",
        "`Fucking Your GFðð\n\n\nYour GF's Boobsð¤ð are Awesome\nPressing her tight Nipplesð¤ð\n\nAlmost Done.......\n\nFucked Percentage... 84%\nâââââââââââââââââââââââââ `",
        "`Fucking Your GFðð\n\n\nYour GF's Lips Get Horny\nDoing French Kiss with your GFðð\n\nAlmost Done........\n\nFucked Percentage... 89%\nâââââââââââââââââââââââââ `",
        "`Fucking Your GFðð\n\n\nYour GF's Boobsð¤ð are Awesome\nI am getting ready to cum in her Mouthð\n\nAlmost Done.......\n\nFucked Percentage... 90%\nâââââââââââââââââââââââââ `",
        "`Fucking Your GFðð\n\n\nYour GF's Boobsð¤ð are Awesome\nFinally, I have cummed in her Mouthðð\n\nAlmost Done.......\n\nFucked Percentage... 96%\nâââââââââââââââââââââââââ `",
        "`Fucking Your GFðð\n\n\nYour GF's is Awesome\nShe is Licking my Dickð in the Awesome Wayâð¤ð¤ðð\n\nAlmost Done.......\n\nFucked Percentage... 100%\nâââââââââââââââââââââââââ `",
        "`Fucking Your GFðð\n\n\nYour GF's ASSð Get Red\nCummed On her Mouthðð\n\nYour GF got Pleasure\n\nResult: Now I Have 1 More SEX Partner ðð`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 21])


@legend.legend_cmd(
    pattern="fk ([\s\S]*)",
    command=("fk", menu_category),
    info={
        "header": "bad animation, try yourself ",
        "usage": "{tr}fk <text>",
    },
)
async def kakai(event):
    "Bad stuff"
    name = event.pattern_match.group(1)
    animation_interval = 3
    animation_ttl = range(11)
    kakashi = await eor(event, "ðð")
    animation_chars = [
        f"ðð\n  ð  =====> Abey {name} Chutiya",
        f"ðð\n  ð  =====> Abey {name} Gay",
        f"ðð\n  ð  =====> Abey {name} Lodu",
        f"ðð\n  ð  =====> Abey {name} Gandu",
        f"ðð\n  ð  =====> Abey {name} Randi",
        f"ðð\n  ð  =====> Abey {name} Betichod",
        f"ðð\n  ð  =====> Abey {name} Behenchod",
        f"ðð\n  ð  =====> Abey {name} NaMard",
        f"ðð\n  ð  =====> Abey {name} Lavde",
        f"ðð\n  ð  =====> Abey {name} Bhosdk",
        f"ðð\n  ð  =====> Hi {name} Mc, How Are You Bsdk...",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 11])


@legend.legend_cmd(
    pattern="chod$",
    command=("chod", menu_category),
    info={
        "header": "bad animation, try yourself ",
        "usage": "{tr}chod",
    },
)
async def kaashi(event):
    "Bad stuff"
    animation_interval = 5
    animation_ttl = range(11)
    kakashi = await eor(event, "1 2 3..Searching Randi..")
    animation_chars = [
        "`Randi Founded`",
        "`Your Mom Is Going To Fuck`",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done... 0%\nâââââââââââââââââââââââââ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 4%\nâââââââââââââââââââââââââ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 8%\nâââââââââââââââââââââââââ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 20%\nâââââââââââââââââââââââââ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 36%\nâââââââââââââââââââââââââ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 52%\nâââââââââââââââââââââââââ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 84%\nâââââââââââââââââââââââââ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 100%\nâââââââââââââââââââââââââ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nYour mom get Pregnant\n\nResult: Now You Have 1 More Younger Brother `",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 11])


@legend.legend_cmd(
    pattern="rape$",
    command=("rape", menu_category),
    info={
        "header": "bad animation, try yourself ",
        "usage": "{tr}rape",
    },
)
async def kashi(event):
    "Bad stuff"
    animation_interval = 0.2
    animation_ttl = range(30)
    kakashi = await eor(event, "repe")
    animation_chars = [
        "**r**",
        "**ra**",
        "**rap**",
        "**rape**",
        "**rape_**",
        "**rape_t**",
        "**rape_tr**",
        "**rape_tra**",
        "**rape_trai**",
        "**rape_train**",
        "**ape_trainð**",
        "**pe_trainððð**",
        "**e_trainðððð**",
        "**_trainððððð**",
        "**trainðððððð**",
        "**rainððððððð**",
        "**ainðððððððð**",
        "**inððððððððð**",
        "**nðððððððððð**",
        "ðððððððððð",
        "ððððððððð",
        "ðððððððð",
        "ððððððð",
        "ðððððð",
        "ððððð",
        "ðððð",
        "ððð",
        "ðð",
        "ð",
        "**rApEd**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 30])


@legend.legend_cmd(
    pattern="kis$",
    command=("kis", menu_category),
    info={
        "header": "shows you fun kissing animation",
        "usage": "{tr}kis",
    },
)
async def _(event):
    "fun animation"
    legendevent = await eor(event, "`kiss`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["ð¤µ       ð°", "ð¤µ     ð°", "ð¤µ  ð°", "ð¤µðð°"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await legendevent.edit(animation_chars[i % 4])


@legend.legend_cmd(
    pattern="fuk$",
    command=("fuk", menu_category),
    info={
        "header": "shows you fun fucking animation",
        "usage": "{tr}fuk",
    },
)
async def _(event):
    "fun animation"
    legendevent = await eor(event, "`fuking....`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["ð       âï¸", "ð     âï¸", "ð  âï¸", "ðâï¸ð¦"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await legendevent.edit(animation_chars[i % 4])


@legend.legend_cmd(
    pattern="sex$",
    command=("sex", menu_category),
    info={
        "header": "shows you fun sex animation",
        "usage": "{tr}sex",
    },
)
async def _(event):
    "fun animation"
    legendevent = await eor(event, "`sex`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["ð¤µ       ð°", "ð¤µ     ð°", "ð¤µ  ð°", "ð¤µð¼ð°"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await legendevent.edit(animation_chars[i % 4])


@legend.legend_cmd(
    pattern="nikal$",
    command=("nikal", menu_category),
    info={
        "header": "bad animation, try yourself ",
        "usage": "{tr}nikal",
    },
)
async def kakhi(event):
    "Bad stuff"
    animation_interval = 0.5
    animation_ttl = range(6)
    kakashi = await eor(event, "nakal")
    animation_chars = [
        "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â    â¢³â¡â â¡â â â    â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â â   â    â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Nikal   â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â â __â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
        "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â   â â¢³â¡â â¡â â â    â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â â       â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Lavde   â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â |__|â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
        "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â      â â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â â â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Pehli   â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â          â¡\n  â â¢¿â£¯â â â (P)â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
        "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â      â â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â    â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Fursat  â¡\n â£â£¿â¡­â â â â â â¢±â    â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â â __ â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
        "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â    â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â  â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Meeee   â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â |__| â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
        "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â   â â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â   â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Nikal   â¡\n â£â£¿â¡­â â â â â â¢±â    â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â loduâ â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 6])


@legend.legend_cmd(
    pattern="gaali$",
    command=("gaali", menu_category),
    info={
        "header": "shows you some gali sentences",
        "usage": "{tr}gaali",
    },
)
async def lenssnd(event):
    "random gali string"
    await eor(
        event,
        "Madarchod Randi ke bacche Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu tere lode pe madhu makkhi Katelode ke ando pe Road roller chale tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga sale tere gand ke balo pe tel laga ke jala du me teko Anaconda leke gand me dalu tho muh se nikle maa ke lode hamesha chutiyo jaisa bartav kartha he tu maa ke Dai chawal drugs tere gand Me dalunga thi tatti nahi nikle maa darchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI CHUT MAI TALWAR DUNGA BC CHUT FAT JAEGI AUR USME SE ITNA KHOON NIKLEGA MZA AJAEGA DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN DA TERI MAA KI CHUT CHOD CHOD KE BHOSDABNADU MADARCHOD AUR USKE UPAR CENENT LAGADU KI TERE JESA GANDU INSAAN KABHI BAHR NA A SKE ESI GANDI CHUT MAI SE LODA LASUN MADRCHOD TERI MAA KI CHUT GASTI AMA KA CHUTIA BACHA TERI MAA KO CHOD CHOD K PAGAL KAR DUNGA MAA K LODY KISI SASTIII RANDII K BACHY TERI MAA KI CHOOT MAIN TEER MAARUN GANDU HARAMI TERI COLLEGE JATI BAJI KA ROAD PEY RAPE KARONGANDU KI OLAAD HARAM KI NASAL PAPA HUN TERA BHEN PESH KAR AB PAPA KO TERI MAA KKALE KUSS MAIN KISI !",
    )


@legend.legend_cmd(
    pattern="lgali$",
    command=("lgali", menu_category),
    info={
        "header": "shows you some gali sentences",
        "usage": "{tr}lgali",
    },
)
async def legd(event):
    "random gali string"
    await eor(
        event,
        "Behen ke lode madahrchod teri ma randi bhsdk tera pyra khandan randi teri kandan kai ma ka bhods lund katta madarchod tere lund pe road roller chale tere behen ki chut kate tura khandan ke gand me bomb phute teri ma ke bur me 100 log ke lund teri behen ke bur me 100 log ke lund madarchod behenchod mai ka loda behen ka loda randi teri behen ma ki chut behen ki chut teri chut ki chut harami phate hue condom ke nateeje tera baap ko paisa nahi tha to uses condom se teri maa ko chooda benchod lodo hai tu sabka chusta gay lund hai nahi be lund akuad me re hamare desh ki taraf bhi dekha to tatte ukhad ke kutto ko keladenge madharchod Madarchod Randi ke bacche.Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu tere lode pe madhu makkhi Katelode ke ando pe Road roller chale tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga sale tere gand ke balo pe tel laga ke jala du me teko Anaconda leke gand me dalu tho muh se nikle maa ke lode hamesha chutiyo jaisa bartav kartha he tu maa ke Dai chawal drugs tere gand Me dalunga thi tatti nahi nikle maa darchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI CHUT MAI TALWAR DUNGA BC CHUT FAT JAEGI AUR USME SE ITNA KHOON NIKLEGA MZA AJAEGA DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN DA TERI MAA KI CHUT CHOD CHOD KE BHOSDABNADU MADARCHOD AUR USKE UPAR CENENT LAGADU KI TERE JESA GANDU INSAAN KABHI BAHR NA A SKE ESI GANDI CHUT MAI SE LODA LASUN MADRCHOD TERI MAA KI CHUT GASTI AMA KA CHUTIA BACHA TERI MAA KO CHOD CHOD K PAGAL KAR DUNGA MAA K LODY KISI SASTIII RANDII K BACHY TERI MAA KI CHOOT MAIN TEER MAARUN GANDU HARAMI TERI COLLEGE JATI BAJI KA ROAD PEY RAPE KARONGANDU KI OLAAD HARAM KI NASAL PAPA HUN TERA BHEN PESH KAR AB PAPA KO TERI MAA KKALE KUSS MAIN KISI loda leke muh me nachne wale ma ki jaat lund kate tera tiri bb ko chode duniya tiri gand me parmanu dhamaka teri ma ka buur me garam oil ki kadhai teri behen ki bane porn aur upload ho pornhub me teri ma ko 100 logo ne choda tab tu paida hua tra papa gay tu gay tera khandan gay bc mc maki chut belen ki lodi ma ki lodi behen teri randi ma teri randi loda undono ke muh me loda katgaya to muh me lele aur kuch hame bola to tera loda tere muh me deke tere gand se nikalenge madarchod beti teru chodaye beti teri rundi teri beti ki bur me 1000 logo ka lund teri beti ka gangbang tere papa be lund nund na hone ke karan teri ma rundi teri ma randi hone ke karan tu aur tera bhai behen teri behen radi kuki teri ma randi behen radi hone ke karan ro 1000 se choda ke uske 10000 bacche tere lund par hathi dore teri gand me chiti kate kera pura satyanash ho *Main roz teri* *behno ki banjar chut me* *apna lawda daalke andar* *haryali lata tha magar aaj* *unke ke baare me* *sunke mujhe bhut afsos* *huwa..ki unko ab bada loudha chahye..ab mera balatkaaari* *lawda lagataar 4 ghante tk* *apne muh me kon* *rakhega..vo teri* *behne hi thi jo apni kaali* *magar rasilli chut mere* *saamne khol deti aur* *zameen pe naagin ki tarah* *rengne lgti thi jaise ki* *kisine unki chut pe naariyal* *tod diya ho vo b bada wala* *mumbai ka naariyal.",
    )


@legend.legend_cmd(
    pattern="egali$",
    command=("egali", menu_category),
    info={
        "header": "shows you some gali sentences",
        "usage": "{tr}egali",
    },
)
async def lana(event):
    "random gali string"
    await eor(
        event,
        "This is for you your a fucking waste of sperm madfaka I   don't know why your parents give birth a worthless shit like you  you faggot ass with a fucking gay bi sextual laurstic slutty minded kid lemaric siliastic  crow  face and ass hahaha your like a pork shit ð©madfaka tell your father to fuck you everynight so that u can have your pussy more effective to everyone  who did fucked you till now  bullshit say to Infront of everyone eyes like I eat bunny's pees at the same time while am sucking his dick bleh ð haha ðððð madfaka what u thought maybe u thought like am from India bsdk am not and that's why am fucking isolated from you ya know what your a fucking black ass who is in form of an human you will get fucked again by this bunny wait for it didle doddoy kid with a fucking phony dick ððððððððð fuck youði will come again and again  for fucking your black ass shit everytime you  will be in front of my eyes  i will be there for fucking your Lili crow as black face hahaha for youððððððmaderchod who the fuck are u u fucking inferior shitty asshole u know what shit you are the shit who drink my pees instead of drinking water now I will fuck ur mom one-day I went to your house with a condom then literally I went up to your mom shitty asshole and fucked  it like a real hard coocky dicky sumty dick I know like your mom enjoyed it a lot much then your sis caz your mom was a mature shit tho u know what u fucking cow face porky poopypants I also know where do u live and how do u eat let me give a brief description about where do u live you live in a fucking slum where ur mom sell her pussy in a reatil price yo and that the shitty reason how u eat three times hahahahaððððWe or I are gonna rape your whole ugly family even tho they are as much as ugly as my shitty poop but so what I will still fuck them and insist them by fucking harder to say it like Bunny Coney  is the best fucker in the  world he  even can defeat the most famous porn star Johnny sins hahaha ðððWell let me say some stories about your mom actually not your mom's only it's our strory tho Your mother name  is Mrs  Mia khalifa she comes of a fucking pornography hilometic whore family she can suck and lick and you know what she lick she lick my sweet heavy hunktik dick hehe she is so kind I meant  your mom caz she suck my dick too kindly wow  hehe ð ð   your mother Love my coocky dick very much and in back I also  love her sexy sweet pussy  as well mm we love each other  in this way hehe now am gonna tell how I fucked your mom well I used to sleep with her in first place then I slowly used to unfasten your mom bra and ð hehe after that I began my part what is too good to go with for me I literally fucked her every night like if I calculate in hours full night huhu I enjoyed those night even tho I still fuck her  lot hmm maybe she also miss those days like I do who knows however   maybe her happiness was know no bounds  and yh in her face I did seen a beams of joy for my hard core fucking hmm  well in profound respect I really wanna fuck her again and again caz I am  indebted to her asshole you know why let me tell you why well I only did fucked her pussy not asshole that's why One-day your sis we're going to her collage and I and some ma friend were waiting for her caz as much as we were concerned about her is she is a fucking bitch who earn money through her pussy postitution  and that's what makes us horny and greedy then that's why we all give her proposal about fucking her  vagina  or u can say pussy in few bucks after that we get Alas!!! And said wait what she is gonna give her fucking Hippocratic pussy in that much money for few bucks then I asked her hey why are u selling your pussy in a retail price then she replied like listen we don't get 3 times food that's why I and my mom's do it at last but not least after that   u know what I said  and what she did  she did fucked me like a fucking horny bitch I swear I enjoyed this part.",
    )
