import asyncio
import random

from Legendbot import legend
from Legendbot.core.managers import eod, eor
from Legendbot.helpers.functions import age_verification
from Legendbot.helpers.utils import reply_id
from Legendbot.plugins import useless
from Legendbot.sql_helper.globals import addgvar, gvarstatus
from Legendbot.sql_helper.raid_sql import (
    raddai,
    rget_all_users,
    rget_users,
    ris_added,
    rremove_ai,
    rremove_all_users,
    rremove_users,
)
from telethon.utils import get_display_name

menu_category = "fun"


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
    pattern="raid(?:\s|$)([\s\S]*)",
    command=("raid", menu_category),
    info={
        "header": "To Send Abuse rapidly with according to number",
        "usage": "{tr}raid <number> <reply>",
    },
)
async def spam(e):
    lol = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    reply_to = await reply_id(e)
    if await age_verification(e, reply_to):
        return
    type = await useless.importent(e)
    if type:
        return
    await e.get_reply_message()
    if e.reply_to_msg_id:
        addgvar("spamwork", True)
        a = await e.get_reply_message()
        b = await e.client.get_entity(a.sender_id)
        g = b.id
        c = b.first_name
        counter = int(lol[0])
        username = f"[{c}](tg://user?id={g})"
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            reply = random.choice(RAID)
            caption = f"{username} {reply}"
            async with e.client.action(e.chat_id, "typing"):
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.3)
    else:
        await e.reply("Check `.help -l raid`")


@legend.legend_cmd(
    pattern="replyraid$",
    command=("replyraid", menu_category),
    info={
        "header": "To add this person in raid.",
        "usage": "{tr}replyraid <reply>",
    },
)
async def add_ensns(event):
    "To raid for the replied person"
    if event.reply_to_msg_id is None:
        return await eor(event, "`Reply to a User's message to activate raid on `")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    legendevent = await eor(event, "`Adding Raid to user...`")
    reply_msg = await event.get_reply_message()
    b = await event.client.get_entity(reply_msg.sender_id)
    g = b.id
    c = b.first_name
    username = f"[{c}](tg://user?id={g})"
    chat_id = event.chat_id
    user_id = reply_msg.sender_id
    if event.is_private:
        chat_name = c
        chat_type = "Personal"
    else:
        chat_name = get_display_name(await event.get_chat())
        chat_type = "Group"
    user_name = c
    user_username = username
    if ris_added(chat_id, user_id):
        return await eor(event, "`The user is already enabled with Raid`")
    try:
        raddai(chat_id, user_id, chat_name, user_name, user_username, chat_type)
    except Exception as e:
        await eod(legendevent, f"**Error:**\n`{e}`")
    else:
        await eor(legendevent, "Raid Has Been Started")


@legend.legend_cmd(
    pattern="dreplyraid$",
    command=("dreplyraid", menu_category),
    info={
        "header": "To stop raid on it.",
        "usage": "{tr}dreplyraid <reply>",
    },
)
async def remove_chatbot(event):
    "To stop raid for that user"
    if event.reply_to_msg_id is None:
        return await eor(event, "Reply to a User's message to stop raid on him.")
    reply_msg = await event.get_reply_message()
    user_id = reply_msg.sender_id
    chat_id = event.chat_id
    if ris_added(chat_id, user_id):
        try:
            rremove_ai(chat_id, user_id)
        except Exception as e:
            await eod(event, f"**Error:**\n`{e}`")
        else:
            await eor(event, "Raid has been stopped for the user")
    else:
        await eor(event, "The user is not activated with raid")


@legend.legend_cmd(
    pattern="delraid( -a)?",
    command=("delraid", menu_category),
    info={
        "header": "To delete raid in this chat.",
        "description": "To stop raid for all enabled users in this chat only..",
        "flags": {"a": "To stop in all chats"},
        "usage": [
            "{tr}delraid",
            "{tr}delraid -a",
        ],
    },
)
async def delete_chbot(event):
    "To delete ai in this chat."
    input_str = event.pattern_match.group(1)
    if input_str:
        lecho = rget_all_users()
        if len(lecho) == 0:
            return await eod(
                event, "You havent enabled ai atleast for one user in any chat."
            )
        try:
            rremove_all_users()
        except Exception as e:
            await eod(event, f"**Error:**\n`{str(e)}`", 10)
        else:
            await eor(event, "Deleted ai for all enabled users in all chats.")
    else:
        lecho = rget_users(event.chat_id)
        if len(lecho) == 0:
            return await eod(
                event, "You havent enabled raid atleast for one user in this chat."
            )
        try:
            rremove_users(event.chat_id)
        except Exception as e:
            await eod(event, f"**Error:**\n`{e}`", 10)
        else:
            await eor(event, "Deleted Raid for all enabled users in this chat")


@legend.legend_cmd(
    pattern="listraid( -a)?$",
    command=("listraid", menu_category),
    info={
        "header": "shows the list of users for whom you enabled raid",
        "flags": {
            "a": "To list raid enabled users in all chats",
        },
        "usage": [
            "{tr}listraid",
            "{tr}listraid -a",
        ],
    },
)
async def list_raidbot(event):  # sourcery no-metrics
    "To list all users on who you enabled raid."
    input_str = event.pattern_match.group(1)
    private_chats = ""
    output_str = "**Ai enabled users:**\n\n"
    if input_str:
        lsts = rget_all_users()
        group_chats = ""
        if len(lsts) <= 0:
            return await eor(event, "There are no raid enabled users")
        for raid in lsts:
            if raid.chat_type == "Personal":
                if raid.user_username:
                    private_chats += (
                        f"â [{raid.user_name}](https://t.me/{raid.user_id})\n"
                    )
                else:
                    private_chats += (
                        f"â [{raid.user_name}](tg://user?id={raid.user_id})\n"
                    )
            elif raid.user_username:
                group_chats += f"â [{raid.user_name}](https://t.me/{raid.user_username}) in chat {raid.chat_name} of chat id `{raid.chat_id}`\n"
            else:
                group_chats += f"â [{raid.user_name}](tg://user?id={raid.user_id}) in chat {raid.chat_name} of chat id `{raid.chat_id}`\n"

        if private_chats != "":
            output_str += "**Private Chats**\n" + private_chats + "\n\n"
        if group_chats != "":
            output_str += "**Group Chats**\n" + group_chats
    else:
        lsts = rget_users(event.chat_id)
        if len(lsts) <= 0:
            return await eor(event, "There are no raid enabled users in this chat")
        for echos in lsts:
            if echos.user_username:
                private_chats += (
                    f"â [{echos.user_name}](https://t.me/{echos.user_username})\n"
                )
            else:
                private_chats += (
                    f"â [{echos.user_name}](tg://user?id={echos.user_id})\n"
                )
        output_str = "**raid enabled users in this chat are:**\n" + private_chats
    await eor(event, output_str)


@legend.legend_cmd(incoming=True, edited=False)
async def ai_reply(event):
    if ris_added(event.chat_id, event.sender_id) and (event.message.text):
        gvarstatus("AI_LANG") or "en"
        get_display_name(await event.client.get_me())
        try:
            await event.reply(random.choice(RAID))
        except Exception as e:
            LOGS.error(str(e))
