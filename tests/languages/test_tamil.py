import pickle

from pytest import mark

from revscoring.languages import tamil

from .util import compare_extraction

BAD = [
    "ஆபாசச்சொல்",
    "ஊம்ப",
    "ஊம்பு",
    "ஒக்காளி",
    "ஒத்தா",
    "ஒம்மால",
    "ஓத்த",
    "ஓத்தவன்",
    "ஓத்தா",
    "ஓப்பான்",
    "ஓலு",
    "ஓல்",
    "ஓல்மாரி",
    "ஓழி",
    "ஓழு",
    "ஓழ்",
    "ஓழ்மாரி",
    "கிழி",
    "கூதி",
    "கை அடிச்சு",
    "கைஅடி",
    "சுண்ணி",
    "சுன்னி",
    "சூத்த",
    "சூத்து",
    "செக்ஸ்கதைகள்",
    "செக்ஸ்படம்",
    "தாயோளி",
    "தேவடியாள்",
    "தேவுடியாள்",
    "பாலச்கரம்",
    "புண்ட",
    "புண்டநக்கி",
    "புண்டை",
    "புழுத்தி",
    "பூலு",
    "பூல்",
    "பெண்குறி",
    "பொச்சு",
    "மயிருபிடுங்கி",
    "மயிர்",
    "முட்டாள்",
    "முண்ட",
    "முண்டை",
    "முலை",
    "யோனி",
    "வல்லுறவு",
    "வாய்அடி",
    "விந்து",
    "aayava ootha alla sunni",
    "akkula thukki kami di",
    "alugina papali",
    "amarjith",
    "anaathai kaluthai",
    "arivu ketta koothi",
    "arippu edutha kuthi mavale",
    "auvusaari koodi",
    "avuthu kami",
    "baadu",
    "blousei thukkudy",
    "chunni",
    "enna oombuda elvedutha koodi",
    "ennoda poola oombuda",
    "erumbu",
    "gajak kol",
    "hakka kudi",
    "kaai",
    "kaai adithal",
    "kaai amuki",
    "kadiki",
    "kala viridi",
    "kaluthae",
    "kandaara oli",
    "kanji",
    "karung kuthi mavale",
    "keeshan appa",
    "kena punda",
    "ki adi",
    "koodhi",
    "koodhi payale",
    "koothi mayir",
    "koothi nuckie",
    "kudiya baadu",
    "kundi",
    "kunji payalae",
    "kusu koodhi",
    "kuthi mudiya thadavi kami di",
    "kuthi kolutha thevdia",
    "kuthia virikira thevdia",
    "loosu koodhi",
    "mairu pudungi",
    "makki punda",
    "mayire",
    "mayiru poodunghi",
    "mola sappi",
    "molai",
    "molaikku naduvule uttu okka",
    "molaikku naduvule utu olu da",
    "mollamaari",
    "monna naaye",
    "mukree Chodho",
    "munni thalai",
    "muttaa koodhi",
    "naara koodhi",
    "naara kudhi pethadha",
    "naii",
    "nalla thukki kami di nara kuthia",
    "nayee soothile un kunji",
    "oakka utta baadu",
    "okkala oli",
    "okkala ozhi",
    "oli the bengali",
    "olmaari",
    "olutha pundai",
    "ommala",
    "ommala okka",
    "ongaka pundek",
    "ongappan pundai",
    "oogili",
    "oombu",
    "oor othe thevidiya",
    "oor thevidya",
    "oore otha thevadiya",
    "otha",
    "oththa",
    "paal pappaali",
    "paaladanja papali punda",
    "pacha thevdia",
    "pae punda",
    "pandi un kunjila addi",
    "panni soothula currenta vekka",
    "pavadaiya thukki kami di",
    "panni",
    "papali",
    "parapunda maune",
    "pareh theyvidiya",
    "paruthesi",
    "patcha thevidiya",
    "pee thinnu",
    "pisasu",
    "pochchu",
    "pool payya",
    "poolu",
    "poolu aruntha punda mavan",
    "pottachi bonthule okkuria",
    "praana kudi",
    "preshaan",
    "pullu sappi",
    "puluthi",
    "puluthi kami",
    "puluthi vudu di",
    "puluthina poola umbudi",
    "punda mavale",
    "punda mavanae",
    "punda vaaya",
    "pundaa navane",
    "pundai nakki",
    "pundaye nakku",
    "pundek leh nandu kadikeh",
    "rajeena",
    "rose bud",
    "saapa naaye",
    "sakkilia koodhi",
    "sandhana thaayoli",
    "sappi",
    "selayai thukkudi",
    "seniyan",
    "somba koodhi",
    "soora koodhi",
    "soothu",
    "soru thunriya illa pee thunriya",
    "sunni",
    "sunni oombi aaya koodi",
    "sunni umbi",
    "sunniya oombu",
    "sunniya uruvudi thevdia",
    "suthu kolutha thatuvani",
    "thaanoombi thevidiya paiyan",
    "thambi",
    "thatuvani kuthi",
    "thaii olee mavane",
    "thanga thevdia",
    "thatuvani munda",
    "thatuvani punda",
    "thayoli machbhaat",
    "thenu olukkura punda mavale",
    "thevadiya mavan",
    "thevdiya", "thevidiya",
    "thonguna mammu naranna koodhi",
    "thoomiya kudiki",
    "thoronthu kami di",
    "thotti",
    "thukki kami",
    "un sooththula en poolu",
    "un vaila uttu okka",
    "unga aaya kuthi",
    "unga aya kudi aluku padi",
    "ungakkala okka",
    "vaile utu okka",
    "vaile vatchuko",
    "vallaipalam",
    "vesai",
    "viricha kuthi",
    "yethava",
    "yirichi kami"
]

INFORMAL = [
    "பொட்டை"
]

OTHER = [
    """
    இந்தோனேசிய ரூபாய் அல்லது ரூபியா (rupiah, Rp)
    இந்தோனேசியாவின் அலுவல்முறை நாணயம் ஆகும். இந்தோனேசிய
    வங்கியால் வெளியிடப்பட்டு கட்டுப்படுத்தப்படும் இதன் ஐ.எசு.ஓ 4217
    நாணயக் குறியீடு (ஐடிஆர்) IDR ஆகும். "ரூபியா" என்ற பெயர்
    இந்துத்தானிய சொல்லான ரூப்யா (روپیہ),(रुपया), மற்றும் சமசுகிருத
    வேரிலிருந்து (रूप्य; வார்ப்பு வெள்ளி) வந்துள்ளது. பேச்சு வழக்கில்
    இந்தோனேசியர்கள் வெள்ளி என்பதற்கான இந்தோனேசியச்
    சொல்லான "பெராக்" என்பதையும் பயன்படுத்துகின்றனர். ஒவ்வொரு
    ரூபியாவும் 100 சென்களாக பிரிக்கப்பட்டுள்ளது; பணவீக்கத்தால்
    சென் நாணயங்களும் வங்கித்தாள்களும் புழக்கத்திலிருந்து மறைந்து
    விட்டன.

    ரியாயு தீவுகளும் நியூ கினியின் இந்தோனேசியப் பகுதியும் முன்பு
    தங்களுக்கேயான ரூபியாவை பயன்படுத்தி வந்தன; ஆனால் முறையே
    1964, 1971ஆம் ஆண்டுகளில் இருந்து இங்கும் தேசிய ரூபியாவே
    செயலாக்கப்பட்டது.
    """
]


@mark.nottravis
def test_badwords():
    compare_extraction(tamil.badwords.revision.datasources.matches,
                       BAD, OTHER)

    assert tamil.badwords == pickle.loads(pickle.dumps(tamil.badwords))


@mark.nottravis
def test_informals():
    compare_extraction(tamil.informals.revision.datasources.matches,
                       INFORMAL, OTHER)

    assert tamil.informals == pickle.loads(pickle.dumps(tamil.informals))
