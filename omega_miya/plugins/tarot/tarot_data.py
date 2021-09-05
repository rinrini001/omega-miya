"""
@Author         : Ailitonia
@Date           : 2021/08/31 21:24
@FileName       : tarot_data.py
@Project        : nonebot2_miya 
@Description    : 塔罗卡牌及卡组数据 虽然这里看起来使用 json 会更好 但还是用 dataclass 硬编码了:(
@GitHub         : https://github.com/Ailitonia
@Software       : PyCharm 
"""

from typing import List
from dataclasses import dataclass, field, fields
from .tarot_typing import Element, Constellation, TarotCard, TarotPack


@dataclass
class Elements:
    earth: Element = field(default=Element(id=0, orig_name='Earth', name='土元素'), init=False)
    water: Element = field(default=Element(id=0, orig_name='Water', name='水元素'), init=False)
    air: Element = field(default=Element(id=0, orig_name='Air', name='风元素'), init=False)
    fire: Element = field(default=Element(id=0, orig_name='Fire', name='火元素'), init=False)
    aether: Element = field(default=Element(id=0, orig_name='Aether', name='以太'), init=False)


@dataclass
class Constellations:
    pluto: Constellation = field(default=Element(id=-9, orig_name='Pluto', name='冥王星'), init=False)
    neptunus: Constellation = field(default=Element(id=-8, orig_name='Neptunus', name='海王星'), init=False)
    uranus: Constellation = field(default=Element(id=-7, orig_name='Uranus', name='天王星'), init=False)
    saturn: Constellation = field(default=Element(id=-6, orig_name='Saturn', name='土星'), init=False)
    jupiter: Constellation = field(default=Element(id=-5, orig_name='Jupiter', name='木星'), init=False)
    mars: Constellation = field(default=Element(id=-4, orig_name='Mars', name='火星'), init=False)
    earth: Constellation = field(default=Element(id=-3, orig_name='Earth', name='地球'), init=False)
    moon: Constellation = field(default=Element(id=-10, orig_name='Moon', name='月亮'), init=False)
    venus: Constellation = field(default=Element(id=-2, orig_name='Venus', name='金星'), init=False)
    mercury: Constellation = field(default=Element(id=-1, orig_name='Mercury', name='水星'), init=False)
    sun: Constellation = field(default=Element(id=0, orig_name='Sun', name='太阳'), init=False)
    aries: Constellation = field(default=Element(id=1, orig_name='Aries', name='白羊座'), init=False)
    taurus: Constellation = field(default=Element(id=2, orig_name='Taurus', name='金牛座'), init=False)
    gemini: Constellation = field(default=Element(id=3, orig_name='Gemini', name='双子座'), init=False)
    cancer: Constellation = field(default=Element(id=4, orig_name='Cancer', name='巨蟹座'), init=False)
    leo: Constellation = field(default=Element(id=5, orig_name='Leo', name='狮子座'), init=False)
    virgo: Constellation = field(default=Element(id=6, orig_name='Virgo', name='室女座'), init=False)
    libra: Constellation = field(default=Element(id=7, orig_name='Libra', name='天秤座'), init=False)
    scorpio: Constellation = field(default=Element(id=8, orig_name='Scorpio', name='天蝎座'), init=False)
    sagittarius: Constellation = field(default=Element(id=9, orig_name='Sagittarius', name='人马座'), init=False)
    capricorn: Constellation = field(default=Element(id=10, orig_name='Capricorn', name='摩羯座'), init=False)
    aquarius: Constellation = field(default=Element(id=11, orig_name='Aquarius', name='宝瓶座'), init=False)
    pisces: Constellation = field(default=Element(id=12, orig_name='Pisces', name='双鱼座'), init=False)


@dataclass
class TarotCards:
    """
    所有卡牌
    每个属性都是一张牌
    """
    @classmethod
    def get_all_cards(cls) -> List[TarotCard]:
        """
        获取所有塔罗牌的列表
        :return: List[TarotCard]
        """
        return [field_.default for field_ in fields(cls) if field_.type == TarotCard]

    blank: TarotCard = field(default=TarotCard(
        id=-1, index='blank', type='special', orig_name='Blank', name='空白',
        intro='空白的卡面，似乎可以用来作为卡牌背面图案使用',
        words='',
        desc='', upright='', reversed=''
    ), init=False)

    the_fool: TarotCard = field(default=TarotCard(
        id=0, index='the_fool', type='major_arcana', orig_name='The Fool', name='愚者',
        intro='愚人穿着色彩斑斓的服装，头上戴顶象征成功的桂冠，无视于前方的悬崖，昂首阔步向前行。\n\n他左手拿着一朵白玫瑰，白色象征纯洁，玫瑰象征热情。他的右手则轻轻握着一根杖，象征经验的包袱即系于其上。那根杖可不是普通的杖，它是一根权杖，象征力量。愚人脚边有只小白狗正狂吠着，似乎在提醒他要悬崖勒马，又好像随他一同起舞。无论如何，愚人仍旧保持着欢欣的神色，望向遥远的天空而非眼前的悬崖，好像悬崖下会有个天使扥住他似的，他就这样昂首阔步地向前走。远方的山脉象征他前方未知的旅程，白色的太阳自始至终都目睹着愚人的一举一动──他从哪里来？他往何处去？他又如何回来？',
        words='流浪',
        desc='愚人牌暗示着你现在不顾风险而有所行动。\n\n愚人是一张代表自发性行为的牌，一段跳脱某种状态的日子，或尽情享受眼前日子的一段时光。对旅游而言，这是一张积极的牌，暗示你将会活在当下，并且会有和生命紧密结合的感觉。“每天都充实，乐趣便在其中”是一句很适合这张牌的古谚语。当你周遭的人都对某事提防戒慎，你却打算去冒这个险时，愚人牌可能就会出现。\n\n愚人暗示通往满足之路是经由自发的行动，而长期的计划则是将来的事。',
        upright='盲目的、有勇气的、超越世俗的、展开新的阶段、有新的机会、追求自我的理想、展开一段旅行、超乎常人的勇气、漠视道德舆论的。',
        reversed='过于盲目、不顾现实的、横冲直撞的、拒绝负担责任的、违背常理的、逃避的心态、一段危险的旅程、想法如孩童般天真幼稚的。'
    ), init=False)

    the_magician: TarotCard = field(default=TarotCard(
        id=1, index='the_magician', type='major_arcana', orig_name='The Magician (I)', name='魔术师',
        intro='魔术师高举拿着权杖的右手指向天，左手食指指向地，他本人就是沟通上天与地面的桥梁。他身前的桌上放着象征四要素的权杖、圣杯、宝剑与星币，同时也代表塔罗牌的四个牌组。他身穿的大红袍子象征热情与主动，白色内衫表示纯洁与智慧的内在。缠绕他腰间的是一条青蛇，蛇虽然经常象征邪恶，但在这里代表的是智慧与启发。魔术师头顶上有个倒８符号，代表无限。画面前方和上方的红玫瑰象征热情，白百合象征智慧。此时，万事齐备，魔术师可以开始进行他的新计划了。和愚人牌同样鲜黄色的背景，预示未来成功的可能。',
        words='创造',
        desc='魔术牌意味着：现在是展开新计划的好时机。\n\n魔术师这张牌意味这是个着手新事物的适当时机。对的时间、对的机会、对的动机，使你的努力值回票价。对于展开行动、实现计划而言，这正是一个良好时机。由于你已为实现计划扎下良好基础，所以新的冒险很可能会实现。清楚的方向感和意志力的贯彻，大大的提升了成功的可能性。',
        upright='成功的、有实力的、聪明能干的、擅长沟通的、机智过人的、唯我独尊的、企划能力强的、透过更好的沟通而获得智慧、运用智慧影响他人、学习能力强的、有教育和学术上的能力、表达技巧良好的。',
        reversed='变魔术耍花招的、瞒骗的、失败的、狡猾的、善于谎言的、能力不足的、丧失信心的、以不正当手段获取认同的。'
    ), init=False)

    the_high_priestess: TarotCard = field(default=TarotCard(
        id=2, index='the_high_priestess', type='major_arcana', orig_name='The High Priestess (II)', name='女祭司',
        intro='相较于上一张魔术师纯粹阳性的力量，女祭司表现的则是纯粹阴性的力量。她身穿代表纯洁的白色内袍，与圣母的蓝色外袍，静默端坐。胸前挂个十字架，象征阴阳平衡、与神合一。\n\n她头戴的帽子是由上弦月、下弦月和一轮满月所构成的，象征所有的处女神祇。手上拿着滚动条，象征深奥的智慧，其上的TORA字样，意为“神圣律法”，而滚动条卷起并半遮着，暗示此律法不为人所知。在她脚边的一轮新月，为她的内袍衣角所固定住，袍子并延伸到图面之外。女祭司两侧一黑一白的柱子，存在于圣经故事中所罗门王在耶路撒冷所建的圣殿中，黑白柱上的B与J字样，分别是Boas和Jachin的缩写，黑柱是阴而白柱是阳，两柱象征二元性，坐在中间的女祭司则不偏不倚，统合两者的力量。柱子上面的喇叭造型，代表女祭司敏锐的感受性，上面的百合花纹则象征纯洁与和平。两柱之间有帷幕遮着，帷幕上的石榴代表“阴”，棕榈代表“阳”。帷幕把后方的景色遮住了，仔细一看，依稀可见由水、山丘与的蓝天构成的背景。水象征情感与潜意识，这一片水平静无波，但其静止的表面下蕴藏深沉的秘密。整个图面呈现象征智慧的蓝色调，双柱的意象在后面的牌中重复出现。',
        words='智慧',
        desc='女祭司意味着：这是向内探索、沉思，或按兵不动的时刻。\n\n女祭司代表去思考可以导致实际结果的构想。这并不是一张代表具体事物的牌，而是一张代表可能性的牌。我们每个人都在我们的人生当中持续的耕耘和收获，而女祭司就是散播那些种子或理念的行动。\n\n女祭司暗示你应该要相信你的直觉，因为在这一点上，有些东西你可能看不见。高位的女祭司是一张代表精神和心灵发展的牌。它代表了向内心探索的一段时期，以便为你人生的下一个阶段播种，或者去消化你在肉体的层次上所处理的事情。',
        upright='纯真无邪的、拥有直觉判断能力的、揭发真相的、运用潜意识的力量、掌握知识的、正确的判断、理性的思考、单恋的、精神上的恋爱、对爱情严苛的、回避爱情的、对学业有助益的。',
        reversed='冷酷无情的、无法正确思考的、错误的方向、迷信的、无理取闹的、情绪不安的、缺乏前瞻性的、严厉拒绝爱情的。'
    ), init=False)

    the_empress: TarotCard = field(default=TarotCard(
        id=3, index='the_empress', type='major_arcana', orig_name='The Empress (III)', name='女皇',
        intro='体态丰腴的皇后坐在宝座上，手持象征地球的圆形手杖，戴着由九颗珍珠组成的项链，象征九颗行星，也代表金星维纳斯。皇后头冠由十二个六角星组成，象征十二星座与一年的十二个月。更进一步，六角星本身是由一个正三角形和倒三角形组成，分别代表火要素和水要素。除了头冠之外，她还戴着香桃木叶作成的头环，象征金星维纳斯。她身穿的宽松袍子上面画满象征多产的石榴，宝座下方则是个绘有金星符号的心形枕头。她前方的麦田已经成熟，代表丰饶与多产；后方则是茂密的丝柏森林，与象征生命力的瀑布河流。',
        words='丰收',
        desc='女皇牌暗示家庭和谐及稳定。\n\n简单言之，女皇可能意味着实现计划，或朝向计划的下一个自然步骤迈进，亦即你又向目标靠近了一步。女皇牌也可能暗示一趟乡野之旅，或是休息一阵子并重返大自然的怀抱，因为她四周围绕着自然的产物。透过亲近自然，现在是你重新平衡自己的时候。这张牌意味家庭状态的稳定与和谐，而这通常是透过把爱从思考当中，带往内心来达成的。',
        upright='温柔顺从的、高贵美丽的、享受生活的、丰收的、生产的、温柔多情的、维护爱情的、充满女性魅力的、具有母爱的、有创造力的女性、沈浸爱情的、财运充裕的、快乐愉悦的。',
        reversed='骄傲放纵的、过度享乐的、浪费的、充满嫉妒心的、母性的独裁、占有欲、败家的女人、挥霍无度的、骄纵的、纵欲的、为爱颓废的、不正当的爱情、不伦之恋、美丽的诱惑。'
    ), init=False)

    the_emperor: TarotCard = field(default=TarotCard(
        id=4, index='the_emperor', type='major_arcana', orig_name='The Emperor (IV)', name='皇帝',
        intro='一国之尊的皇帝头戴皇冠，身着红袍，脚穿象征严格纪律的盔甲，左手拿着一颗球，右手持的是象征生命的古埃及十字架，自信满满的坐在王位上。\n\n王位上有四个牡羊头作为装饰，如图所示，皇帝牌正是代表牡羊座的牌。牡羊座是十二星座的头一个，具有勇敢、积极、有野心、有自信的特质。红袍加上橙色的背景，呈现红色的主色调，与牡羊座的特性不谋而合。背景严峻的山象征前方险峻的路途。我们可以比较皇帝与皇后的背景，一个是严峻山川，一个是丰饶大地，形成互补的局面。',
        words='支配',
        desc='皇帝表示一种训练和实际致力于生活。\n\n皇帝意味透过自律和实际的努力而达到成功。它可以代表你生活中一段相当稳定，且井然有序的时光。这张牌可以暗示遭遇到法律上的问题，或是碰到某个地位、权利都在你之上的人，例如法官、警员、父亲，或具有父亲形象的人。\n\n为了成功，现在正是你采取务实态度来面对人生的时候。你被周遭的人设下种种限制，但只要你能在这些限制之内努力的话，你还是可以达成你的目标。',
        upright='事业成功、物质丰厚、掌控爱情运的、有手段的、有方法的、阳刚的、独立自主的、有男性魅力的、大男人主义的、有处理事情的能力、有点独断的、想要实现野心与梦想的。',
        reversed='失败的、过于刚硬的、不利爱情运的、自以为是的、权威过度的、力量减弱的、丧失理智的、错误的判断、没有能力的、过于在乎世俗的、权力欲望过重的、权力使人腐败的、徒劳无功的。'
    ), init=False)

    the_hierophant: TarotCard = field(default=TarotCard(
        id=5, index='the_hierophant', type='major_arcana', orig_name='The Hierophant (V)', name='教皇',
        intro='教皇身穿大红袍子，端坐在信众前。他头戴象征权力的三层皇冠，分别代表身心灵三种层次的世界。\n\n他的右手食中指指向天，象征祝福﹔左手持着主字形的权杖，象征神圣与权力。他耳朵旁边垂挂的白色小物，代表内心的声音。教皇前方放着两把交叉的钥匙，在很多版本的塔罗牌里，钥匙是金色银色各一把，象征阳与阴，日与月，外在与内在，我们的课题就是要学会如何结合两者，而钥匙本身可用以开启智慧与神秘之门。教皇前方的两位信众，左边的身穿象征热情的红玫瑰花纹衣裳，右边则穿象征性灵成长的白百合衣裳（红玫瑰与白百合在魔术师也曾出现过）。教皇与信众三人的衣服都有牛轭形（Ｙ字形）装饰，牛轭的用途是促使受过训练的动物去工作的，出现在教皇牌的道理值得深思。教皇后方则是曾经在女祭司中出现的两根柱子，不过在这里它们是灰色的，灰色象征由经验而来的智慧﹔另一说则是教皇后方虽无女祭司的帷幕将潜意识隔离，但暗沉的灰色代表通往潜意识之路仍未开启。柱子上的图案象征肉体结合。',
        words='援助',
        desc='教皇代表需要为你的心灵成长，及人生方向付起责任。\n\n教皇暗示你向某人或某个团体的人屈服了。或许这正是你为自己，及心灵上的需求负起责任的时刻了。你目前的行事作风并非应付事情的唯一方式，假设你愿意加以探索的话，或许你就会找到新的可能。',
        upright='有智慧的、擅沟通的、适时的帮助、找到真理、有精神上的援助、得到贵人帮助、一个有影响力的导师、找到正确的方向、学业出现援助、爱情上出现长辈的干涉、媒人的帮助。',
        reversed='过于依赖的、错误的指导、盲目的安慰、无效的帮助、独裁的、疲劳轰炸的、精神洗脑的、以不正当手段取得认同的、毫无能力的、爱情遭破坏、第三者的介入。'
    ), init=False)

    the_lovers: TarotCard = field(default=TarotCard(
        id=6, index='the_lovers', type='major_arcana', orig_name='The Lovers (VI)', name='恋人',
        intro='恋人牌背景在伊甸园，亚当与夏娃分站两边，两者皆裸身，代表他们没什么需要隐藏的。两人所踩的土地相当肥沃，生机盎然。\n\n夏娃的背后是知识之树，生有五颗苹果，象征五种感官，有条蛇缠绕树上。蛇在世界文化中的象征丰富多元，此处可能象征智慧，也象征欲望与诱惑。牠由下往上缠绕在树上，暗示诱惑经常来自潜意识。亚当背后是生命之树，树上有十二团火焰，象征十二星座，也象征欲望之火。伟特说：“亚当与夏娃年轻诱人的躯体，象征未受有形物质污染之前的青春、童贞、纯真和爱”。两人背后的人物是风之天使拉斐尔（Raphael），风代表沟通，祂身穿的紫袍则是忠贞的象征，显示这个沟通的重要性。亚当看着夏娃，夏娃则望着天使，象征“意识─潜意识─超意识”与“身─心─灵”或是“理性─感性”之间的传导。天使之下，亚当夏娃中间有一座山，象征意义解读众多，主要有三种：一说是山代表阳性，水代表阴性，两者表现阴阳平衡，意味我们必须把阴与阳、理性与感性的能量调和。一说认为这座山象征正当思想的丰饶果实。另一说则认为它代表高峰经验与极乐。',
        words='结合',
        desc='恋人牌意味，为了爱的关系而做的某些决定。\n\n恋人是一张代表决定的牌，而且除非问的是某个特定的问题，否则它通常是指有关两性关系的决定。它可能是在描述沉浸在爱恋之中的过程，因为它可以意指一段两性关系中的最初，或者是罗曼蒂克的阶级。恋人牌也可以形容在决定到底要保留就有的关系，或转进新关系当中。它暗示你已经由过去经验而得到成长了，因此你可以安全的迈向一个新的阶段。',
        upright='爱情甜蜜的、被祝福的关系、刚萌芽的爱情、顺利交往的、美满的结合、面临工作学业的选择、面对爱情的抉择、下决定的时刻、合作顺利的。',
        reversed='遭遇分离、有第三者介入、感情不合、外力干涉、面临分手状况、爱情已远去、无法结合的、遭受破坏的关系、爱错了人、不被祝福的恋情、因一时的寂寞而结合。'
    ), init=False)

    the_chariot: TarotCard = field(default=TarotCard(
        id=7, index='the_chariot', type='major_arcana', orig_name='The Chariot (VII)', name='战车',
        intro='一位英勇的战士驾着一座由两只人面狮身兽拉着的战车。人面狮身兽一只是黑的，代表严厉，另一只是白的，代表慈悲。两兽同时来看，也是阴阳平衡的象征。\n\n战车上有四根柱子（四个代表上帝的希伯来字母YHWH或火水风土四要素）支撑着蓝色车棚，车棚上饰以六角星花纹，象征天体对战士成功的影响。英勇的战士手持象征意志与力量的矛形权杖，头戴象征统治的八角星头冠和象征胜利的桂冠，身穿盔甲。盔甲上的肩章呈现弦月形，显示战车牌与属月亮的巨蟹座之关联。斜挂的腰带上有占星学符号，裙上有各种炼金术的符号。胸前的四方形图案代表土要素，象征意志的力量。战车前方的翅膀图案是古埃及的图腾，代表灵感。翅膀下面是一个小盾牌，其上的红色的图案是一种印度图腾，为男性与女性生殖器结合的象征，也是二元性与一元性，类似中国的阴与阳，可能暗示编号七的战车牌走过愚人之旅的三分之一，已达性成熟的阶段。战士身后的河流就是圣经创世纪中四条伊甸园之河其中的一条，与皇后、皇帝和、死神牌中的河是同一条。再后面就是一座高墙耸立的城市。战士背对城市，暗示他把物质置于身后，向前开展心灵上的旅程。他手上没有缰绳，表示他不是用肉体来控制那两头朝不同方向行进的人面狮身兽，而完全凭借他旺盛过人的意志力。值得注意的一点是他站在城墙外守御，而非进攻，所以这位战士是位守护者、防御者，而不是侵略者。他是尽他的本分，并努力做到最好。',
        words='胜利',
        desc='战车牌意味训练有素的心智。\n\n战车可以代表一部车，或是坐车旅行。当这张牌出现时，它可能意味着你需要控制生命中互相对抗的力量。目前的情况可能会出现某些矛盾，而你正以理智在控制着它们。\n\n这是一张代表由于坚持而取得成功的牌。如果用来形容一个人的话，战车是暗示这个人（通常是指男人），掌控着她自己和周遭的事物。正立的战车也可能意指一桩重要的生意，或意义重大的成功。',
        upright='胜利的、凯旋而归的、不断的征服、有收获的、快速的解决、交通顺利的、充满信心的、不顾危险的、方向确定的、坚持向前的、冲劲十足的。',
        reversed='不易驾驭的、严重失败、交通意外、遭遇挫折的、遇到障碍的、挣扎的、意外冲击的、失去方向的、丧失理智的、鲁莽冲撞的。'
    ), init=False)

    strength: TarotCard = field(default=TarotCard(
        id=8, index='strength', type='major_arcana', orig_name='Strength (VIII)', name='力量',
        intro='代表力量的女人轻柔地合上狮子的嘴。女人头上有魔术师牌中出现的倒８符号，象征她的力量是无穷尽的。她头上戴着花环，腰间也系着花环，而且腰间花环还连系在狮子颈间，形成第二个倒８符号。狮子身体微倾，尾巴轻垂，表现出彻底的顺服，还伸出舌头来舔着女人的手。',
        words='意志',
        desc='力量牌暗示你拥有足够的内在力量去面对人生。\n\n这张力量牌意味你有能力面对生活和困难的环境，或者有能力以希望、内在力量及勇气去做改变。勇气并不代表你没有恐惧，而是虽然你有恐惧，你还是愿意对某人或某事有所承诺。\n\n这张牌象征你拥有内在的力量来面对你内在的恐惧和欲望，而非让它们屈服于你的意志。在健康的分析方面，这张牌可能是有关心脏或脊椎方面的毛病，不过这些毛病也可以透过内在能量来克服，而且这张牌也暗示你本身拥有这种能量。',
        upright='内在的力量使成功的、正确的信心、坦然的态度、以柔克刚的力量、有魅力的、精神力旺盛、有领导能力的、理性的处理态度、头脑清晰的。',
        reversed='丧失信心的、失去生命力的、沮丧的、失败的、失去魅力的、无助的、情绪化的、任性而为的、退缩的、没有能力处理问题的、充满负面情绪的。'
    ), init=False)

    the_hermit: TarotCard = field(default=TarotCard(
        id=9, index='the_hermit', type='major_arcana', orig_name='The Hermit (IX)', name='隐者',
        intro='身穿灰色斗篷和帽子的老人站在冰天雪地的山巅上，低头沉思，四周渺无人烟。他右手高高举着一盏灯，这是真理之灯，灯里是颗发亮的六角星，名称是所罗门的封印，散发出潜意识之光。老人左手拄着一根族长之杖，这跟杖在愚人、魔术师、战车都曾经出现过。愚人太过天真，不知杖的魔力，拿它来系包袱；魔术师用代表意识的右手运用杖的法力；战车把杖化为矛，也用右手紧握着；隐士则杖交左手，用以在启蒙之路上做前导。',
        words='探索',
        desc='隐士牌暗示着：省思的一段时间。\n\n隐士牌暗示一段反省的时间。它代表着一段想要让你的过去、现在，以及未来成为有意义的时间。这张牌代表去看咨商辅导员、持续一段梦想之旅，或为了开发你自己的沉思。它也代表成熟，以及你已经知道生命中真正重要的是什么。\n\n它可能意味着得到身体或心灵上的协助及智因；或是你帮助其他人发现人生理解及事件的导因。它也代表一段时间内，你会问自己如下的问题：我从何处来？我现在位于何处？又将往何处去？',
        upright='有骨气的、清高的、有智慧的、有法力的、自我修养的，生命的智慧情境、用智慧排除困难的、给予正确的指导方向、有鉴赏力的、三思而后行的、谨慎行动的。',
        reversed='假清高的、假道德的、没骨气、没有能力的、内心孤独寂寞的、缺乏支持的、错误的判断、被排挤的、没有足够智慧的、退缩的、自以为是的、与环境不合的。'
    ), init=False)

    wheel_of_fortune: TarotCard = field(default=TarotCard(
        id=10, index='wheel_of_fortune', type='major_arcana', orig_name='Wheel of Fortune (X)', name='命运之轮',
        intro='所有的大牌都有人物，命运之轮是唯一的例外，可见这张牌独树一格。深蓝色的天空悬着一个轮子，轮盘由三个圆圈构成（教宗的头冠也是），最里面的小圈代表创造力，中间是形成力，最外层是物质世界。小圈里头没有任何符号，因为创造力潜能无限；中间圆圈里有四个符号，从上方顺时针依序是炼金术中的汞风、硫、水，分别与风火水土四要素相关联，是形成物质世界的基本要素﹔最外层就是物质世界，上右下左四方位分别是TARO四个字母，这四个字母可以组成Rota（轮）、Orat（说）、Tora（律法）、Ator（哈扥尔女神），形成一个完整的句子“塔罗之轮述说哈扥尔女神的律法”，其余四个符号是希伯来字母YHVH，是上帝最古老的名字。轮盘从中心放射出八道直线，代表宇宙辐射能量。\n\n在轮盘左方有一条往下行进的蛇，是埃及神话中的邪恶之神Typhon，牠的向下沉沦带着轮子进入分崩离析的黑暗世界。相反的，背负轮盘的胡狼头动物渴求上升，牠是埃及神话中的阿努比神（Anubis）。而上方的人面狮身兽是智慧的象征，均衡持中，在变动中保持不变。牠拿着的宝剑代表风要素，表示心智慧力、思考力和智慧。\n\n四个角落的四只动物，从右上方顺时针看分别是老鹰、狮子、牛、人，而且他们都有翅膀。这四个动物出自圣经启示录第四章“宝座周围有四个活物，前后遍体都满了眼睛。第一个活物像狮子，第二个像牛犊，第三个脸面像人，第四个像飞鹰”，耶路撒冷圣经提到四活物象征四位福音书的作者（马太、马可、路加和约翰）。在占卜上这四个动物与占星学产生关联，分别代表四个固定星座和四要素，老鹰是天蝎座（水），狮子是狮子座（火），牛是金牛座（土），人是水瓶座（风）。牠们都在看书，汲取智慧，而翅膀赋予牠们在变动中保持稳定的能力。',
        words='轮回',
        desc='命运之轮意味着你境遇的改变。观察这个改变，并留意它的模式。\n\n生命是变化无常的，当牌面上的命运之轮是正立时，改变似乎是有利的；而当它倒立时，改变又似乎是有害的。它只是改变，而似乎有害的改变，事实上可能会是一种祝福。你必须超越现状，将眼光放远，来观察生命的消长。\n\n通常命运之轮象征你生命境遇的改变。或许你并不了解这些改变的原因，不过在这里，你如何因应改变是比较重要的。你要迎接生命所提供给你的机会，还是要抗拒改变呢？此牌正立时就是在告诉你，要去适应这些改变。',
        upright='忽然而来的幸运、即将转变的局势、顺应局势带来成功、把握命运给予的机会、意外的发展、不可预测的未来、突如其来的爱情运变动。',
        reversed='突如其来的厄运、无法抵抗局势的变化、事情的发展失去了掌控、错失良机、无法掌握命运的关键时刻而导致失败、不利的突发状况、没有答案、被人摆布、有人暗中操作。'
    ), init=False)

    justice: TarotCard = field(default=TarotCard(
        id=11, index='justice', type='major_arcana', orig_name='Justice (XI)', name='正义',
        intro='一个女人端坐在石凳上，右手持剑高高举起，左手在下拿着天秤。身穿红袍，头戴金冠，绿色披肩用一个方形扣子扣起。她的右脚微微往外踏出，似乎想站起来，而左脚仍隐藏在袍子里面。她高举宝剑，象征她的决心。宝剑不偏不倚，象征公正，且智慧可以戳破任何虚伪与幻象。宝剑两面都有刃，可行善可行恶，端看个人选择。左手的金色天秤和披肩的绿色都是天秤座的象征。手持天秤表示她正在评估，正要下某个决定，同时追求平衡。胸前的方形扣子中间是个圆形，象征四要素的调和。头上的金冠中心有个四方形宝石，加上金冠的三个方顶，加起来得到数字七，代表金星，也就是天秤座的守护星。后方是个紫色帷幕，象征隐藏的智慧。两边柱子象征正面和负面的力量。',
        words='均衡',
        desc='正义意味，这是一段你为你的人生决定负起责任的时光。\n\n正义意味事情已经达成它应有的使命。也就是说，你过往的决定或行为已经引导你走到了目前的境遇。你已经得到你应得的了，如果你对自己是够诚实的话，你肯定知道这点。它代表你应该对自己，以及周遭的人绝对的诚实。你应该自己，以及使你成为今天这个样子的种种决定负起责任。你的未来可能会因为你目前的决定、行为或理解而改变。',
        upright='明智的决定、看清了真相、正确的判断与选择、得到公平的待遇、走向正确的道路、理智与正义战胜一切、维持平衡的、诉讼得到正义与公平、重新调整使之平衡、不留情面的。',
        reversed='错误的决定、不公平的待遇、没有原则的、缺乏理想的、失去方向的、不合理的、存有偏见的、冥顽不灵的、小心眼、过于冷漠的、不懂感情的。'
    ), init=False)

    the_hanged_man: TarotCard = field(default=TarotCard(
        id=12, index='the_hanged_man', type='major_arcana', orig_name='The Hanged Man (XII)', name='倒吊人',
        intro='倒吊人图案简单，涵义却深远。我们看到一个男人在一棵Ｔ字形树上倒吊着。他两手背在背后，形成一个三角形。两腿交叉形成十字。十字和三角形结合在一起，就是一个炼金符号，象征伟大志业的完成，也象征低层次的欲望转化到高层次的灵魂（炼成黄金）。\n\n红裤子象征身心灵中的“身”，也就是人类的欲望和肉体。蓝上衣即身心灵中的“心”，象征知识。他的金发和光环象征智慧和心灵的进化，也就是“灵”。金色的鞋子则象征倒吊人崇高的理想。在某些版本的塔罗牌中，倒吊人就是神话中的奥丁（Odin），他身后的树就是北欧神话中的义格卓席尔巨树（Yggdrasil），也称作世界之树，由地狱（潜意识）开始生长，经过地面（意识），直达天庭（超意识）。还记得皇帝右手拿着一根象征生命的古埃及十字架吗？古埃及十字架代表希伯来的第十九个字母Tau，是属于世间的一个字母，而倒吊人倒吊的Ｔ字树，正是它的下半部，表示倒吊人仍然是入世的。',
        words='牺牲',
        desc='“以将有更美好的事物降临于你身上的信念，顺从于人生”是倒吊人这张牌所传达的讯息。\n\n倒吊人是一张代表投降的牌。它暗示，当你在这段期间内，透过对生命的顺从，并让它引领你到你需要去的地方，那么你便可以获益良多。\n\n倒吊人还是一张代表独立的牌。这段期间内，你应该顺着感觉走，或是接受自己，即使别人都认为你的方式很奇怪也不打紧。它也可能象征，经历了生命中一段艰难的时光后的心灵平静。\n\n现在不是挣扎的时候，静下来好好思考你过去的行为，以及未来的计划。这只是一个暂时的状态，只要你妥善的运用这段时间，对你应该是有好处的。让生命中的事物自然而然的发生，或许你会对结果感到惊喜。带着“会有更美好的事情临降，来取代你所捐弃的事物”的信念，顺从于人生。花点时间来观察潜伏于事件底下的生命潮流。生命会给你一段宁静的时光，远离世界的纷纷扰扰，所以善用这段时光将是明智之举。',
        upright='心甘情愿的牺牲奉献、以修练的方式来求道、不按常理的、反其道而行的、金钱上的损失、正专注于某个理想的、有坚定信仰的、长时间沈思的、需要沈淀的、成功之前的必经之道。',
        reversed='精神上的虐待、心不甘情不愿的牺牲、损失惨重的、受到亏待的、严重漏财的、不满足的、冷淡的、自私自利的、要求回报的付出、逃离綑绑和束缚、以错误的方式看世界。'
    ), init=False)

    death: TarotCard = field(default=TarotCard(
        id=13, index='death', type='major_arcana', orig_name='Death (XIII)', name='死神',
        intro='传统的死神牌，通常是由骷髅人拿着镰刀来代表，而伟特将死神的意象提升到更深一层的境界。\n\n最显眼的就是那位骑着白马的骷髅骑士。他身边有四个人，国王、主教、女人、小孩，象征无论是世俗或出世、男或女、老或少，都逃不过死亡这个自然现象。国王抗拒死亡，被骷髅骑士践踏过去﹔主教的权杖掉在地上，双手合十崇敬死亡﹔女人跪下，别过脸不忍看﹔小孩不懂死亡，好奇的望着骷髅骑士。其中主教可能就是编号五的教宗牌，他掉落在地上的权杖象征世俗权力遇到死亡时毫无用处，仔细一看权杖顶似乎有三层圆圈，和教宗牌戴在头上的权冠相同，而主教头上戴的帽子状似尖尖的鱼头，代表双鱼世纪的结束，也可能暗示死神牌关联的希伯来文Nun，意思是鱼。跪着的女人可能是力量牌中的那位女性，她们的衣着与头冠都极为相似。再回到骷髅骑士，他头上那根红羽毛和愚人所戴的是同一根，他的旗帜是黑色背景，象征光芒的不存，上面五瓣蔷薇的图案是蔷薇十字会的图腾，关于此图腾的说法众多，可能是代表随着死亡而来的新生，另一说是象征火星与生命力，还有一说是象征美丽纯洁与不朽。远方的河流就是流经伊甸园的四条河流之一，称为冥河（Styx），象征川流不息的生命循环。河上有艘船，船的上方有个类似洞穴的地方，右方有个箭头（在死神的脚跟处）指向洞穴，这个洞穴可能是“神曲”一书中但丁前往阴间的通道，而牌中右方一条小径通往两座塔中（月亮和节制都有相同背景，这两座塔也可能是女祭司背后的柱子），代表通往新耶路撒冷的神秘旅程。象征永生的朝阳在两座塔间升起，似乎在告诉我们死亡并不是一切的终点。',
        words='结束',
        desc='死亡牌意味某种状况的结束。\n\n死亡为旧事物画上休止符，并让路给新事物。死亡牌代表改变的一段其间。我们可以这样说，生命中的某个章节就要结束了，而你对这份改变的接纳，将是变化自然而然地发生。\n\n抱持着“生命将会带来某些比它从你身上拿走的更美好的东西”的信念。在潜意识中，你或许也在渴望改变的发生，死亡牌即意味着改变正要出现。不要抗拒这份改变，试着去接纳它吧。',
        upright='必须结束旧有的现状、面临重新开始的时刻到了、将不好的过去清除掉、专注于心的开始、挥别过去的历史、展开心的旅程、在心里做个了结、激烈的变化。',
        reversed='已经历经了重生阶段了、革命已经完成、挥别了过去、失去了、结束了、失败了、病了、走出阴霾的时刻到了、没有转圜余地了。'
    ), init=False)

    temperance: TarotCard = field(default=TarotCard(
        id=14, index='temperance', type='major_arcana', orig_name='Temperance (XIV)', name='节制',
        intro='十四号的节制牌，出现在死神牌之后。大天使麦可手持两个金杯，把左手杯中的水倒入右手杯中。\n\n金发的天使身着白袍，背长红翅膀，胸前有个方形图案（地元素），中间是个橘色的三角形（火元素），同样的图案在正义牌中也可看到。天使头上则戴个饼图案，中间有一个小点，是炼金术中代表黄金的符号，也就是终极目标。天使脸上闪耀着和谐的光辉，怡然自在，他/她的右脚踏入象征潜意识的池塘中，左脚站在象征显意识的岸边石头上，代表两者之间的融合。塘边生长一丛爱丽斯花。远方有一条小径通往淡蓝色的两座山间，双山顶间闪耀着王冠般的金色光芒，类似如此的图像也曾出现于前一张死神牌中的小径、双塔与朝阳。恋人与审判牌中也有天使的出现。另外，大天使对应希腊神话中的彩虹之神，暴风雨后的彩虹，意味着节制牌已经从死神带给我们的恐惧中超脱出来了。整张牌带给人宁静祥和的感受，让人们明白死亡之后终获新生。',
        words='净化',
        desc='节制代表行动及感情的融合，带来内心的平静感觉。\n\n节制是一张代表行为，而非观念的牌。它代表对某种特定状况的适当行为。显示一种因为行为及情绪的结合，而带来内在平静的感觉。节制意味着结合自发性及知识的能力，运用精神的知识及理解力来调节行为的能力。它是指知道每种状况来临时，应该采取什么适当的反映或行为。\n\n节制牌暗示你较高层次的自我，和较低层次的自我可以和谐共存。你带着一种方向感行动，不管那是精神上或实质上的行动。它代表尽力而为，以达到你可以达到的境界。',
        upright='良好的疏导、希望与承诺、得到调和、有节制的、平衡的、沟通良好的、健康的、成熟与均衡的个性、以机智处理问题、从过去的错误中学习、避免重蹈覆辙、净化的、有技巧的、有艺术才能的。',
        reversed='缺乏能力的、技术不佳的、不懂事的、需反省的、失去平衡状态、沟通不良的、缺乏自我控制力、不确定的、重复犯错的、挫败的、受阻碍的、暂时的分离、希望与承诺遥遥无期。'
    ), init=False)

    the_devil: TarotCard = field(default=TarotCard(
        id=15, index='the_devil', type='major_arcana', orig_name='The Devil (XV)', name='恶魔',
        intro='在恶魔牌上，我们看到和恋人相似的构图，只是恋人牌的天使在这里换成了恶魔，而亚当夏娃已然沉沦，上天的祝福变成了诅咒。\n\n牌中的恶魔有蝙蝠翅膀、羊角、羊腿和鸟足，象征动物的本能与天性。牠的驴耳则代表固执。恶魔头上的倒立星币，顶端指向地面，代表物质世界。恶魔右手向上摆出黑魔法的手势，与教宗的祝福手势形成对比。手心的符号代表土星，限制与惰性之星，也是魔羯座的守护星。恶魔左手则持着火炬，同样向下导引到物质世界，似乎在煽动亚当的欲望。注意恶魔坐的地方并不是三度空间的立方体，而是二度空间的长方形，象征人们只看见感官所见的现实，却非全部的真实，好比瞎子摸象。前方的亚当夏娃同样长出角和尾巴，显露出野兽本能。亚当的尾巴尖端是朵火焰，夏娃则是葡萄，都是恋人牌树上结的果实，表示她们误用了天赋。两个人被铁链锁住，乍看无处可逃，但仔细一看，其实系在她们脖子上的链子非常的松，只要愿意，随时可以挣脱，但她们却没有，表示这个枷锁是他们自己套在自己身上的。恶魔牌背景全黑，光芒不存，代表精神上的黑暗。',
        words='诱惑',
        desc='魔鬼牌代表错以为别无选择。\n\n魔鬼牌代表一种错误的概念，认为事情别无选择。觉得“我所拥有的就是这些”或“这是我唯一的选择”。在宗教的前因后果当中，魔鬼引诱男人使它遗忘掉精神的探索，以及他的神圣目的。在一般性的占卜中，魔鬼代表一种控制生命的需求，你对与自己的可能性缺乏完整的关照。\n\n魔鬼牌描述的是一种对生命物质化的观点，或像王尔德（OscarWilde）所说的：“知道所有东西的价格，却不知道任何东西的价值。”它可能暗示在某种状况内受到限制，却不愿意去改变。它是一种“偷鸡摸狗胜过杀人放火”的态度。',
        upright='不伦之恋、不正当的欲望、受诱惑的、违反世俗约定的、不道德的、有特殊的艺术才能、沉浸在消极里、沉溺在恐惧之中的、充满愤怒和怨恨、因恐惧而阻碍了自己、错误的方向、不忠诚的、秘密恋情。',
        reversed='解脱了不伦之恋、挣脱了世俗的枷锁、不顾道德的、逃避的、伤害自己的、欲望的化解、被诅咒的、欲望强大的、不利的环境、盲目做判断、被唾弃的。'
    ), init=False)

    the_tower: TarotCard = field(default=TarotCard(
        id=16, index='the_tower', type='major_arcana', orig_name='The Tower (XVI)', name='塔',
        intro='一座位于山巅上的高塔，被雷击中而毁坏，塔中两人头上脚下的坠落。塔顶有个王冠受雷殛而即将坠落。塔象征物质，王冠象征统治和成就，也代表物质与财富，受雷一殛，便荡然无存。天上的落雷是直接来自上帝的语言，两旁的火花有二十二个，象征塔罗二十二张大牌。灰色的云降下灾难之雨，不分性别阶级，平等的落向每一个人。背景全黑，这是一段黑暗的时期。',
        words='毁灭',
        desc='高塔象征生命中无可避免的改变。\n\n这种改变是是从根基到顶端的完全崩解与毁灭，是一种无可挽救的崩溃。这种改变是突然而来的，有时候激烈无比，这是一种易于顺从而难以抗拒的改变。当高塔牌出现时，便是到了改变的时刻。现在再来为改变做准备，或选择如何改变都已太迟，现在你需要做的就是丢掉旧东西。',
        upright='双方关系破裂、难以挽救的局面、组织瓦解了、损失惨重的、惨烈的破坏、毁灭性的事件、混乱的影响力、意外的发展、震惊扰人的问题、悲伤的、离别的、失望的、需要协助的、生活需要重建的。',
        reversed='全盘覆没、一切都已破坏殆尽、毫无转圜余地的、失去了、不安的、暴力的、已经遭逢厄运了、急需重建的。'
    ), init=False)

    the_star: TarotCard = field(default=TarotCard(
        id=17, index='the_star', type='major_arcana', orig_name='The Star (XVII)', name='星星',
        intro='一位赤裸的金发女子，左膝跪在象征显意识的地面上，右脚踏在象征潜意识的池水里。她左右手各持一个水壶，壶中装的是生命之水，她右手壶的水倾倒入池，激起阵阵涟漪，左手壶的水则倒在青翠的草地上，分成象征人类五种感官的五道水流，其中一道又流回池塘，再度充实潜意识之泉。她身后有棵树，树上有只象征智慧的朱鹭，同时也代表埃及神话中的托特之神，是所有艺术的创造者。女子的后方则是一大片广阔开满花的草原，和一座山脉，天空一颗巨大的金色八角星，七颗白色的小八角星则环绕在四周。',
        words='希望',
        desc='星星牌意味创造力和对生命的可能性的信心。\n\n星星是一张代表重新点燃希望的牌。它代表相信明天会更好的内在信心。你可以直接体验潜意识，而不是它的种种符号或意象。你可以体验这种强而有力的能量，并将它导入你的生命中。例如，艺术家利用这种能量来工作，以创作某些足以触动观赏者心情和灵魂的作品。它是一张代表信心、希望和内在平静的牌。',
        upright='未来充满希望的、新的诞生、无限的希望、情感面精神面的希望、达成目标的、健康纯洁的、美好的未来、好运即将到来、美丽的身心、光明的时机、平静的生活、和平的处境。',
        reversed='希望遥遥无期的、失去信心的、没有寄托的未来、失去目标的、感伤的、放弃希望的、好运远离的、毫无进展的、过于虚幻、假想的爱情运、偏执于理想、希望破灭的。'
    ), init=False)

    the_moon: TarotCard = field(default=TarotCard(
        id=18, index='the_moon', type='major_arcana', orig_name='The Moon (XVIII)', name='月亮',
        intro='相较于其它的牌，月亮整体呈现的图面经常令人感到诡异。近景是一只龙虾爬出池塘的景象，龙虾象征比恐惧和兽性更深的情绪，伟特说牠总是爬到一半又缩回去。中景处有频频吠叫的一只狗和一匹狼，分位于左右两边，分别象征人类内心中已驯化和未驯化的兽性。中间有一条通往两塔之间，延伸向远处山脉的小径上，这条小径是通往未知的出口，只有微弱的月光映照着。一轮月亮高挂空中，总共有三个层次，最右边的是新月，最左边的是满月，而中间的女人脸孔则是伟特所谓的“慈悲面”，从新月渐渐延伸向满月，越来越大。月亮的外围则有十六道大光芒，和十六道小光芒，其下有十五滴象征思想之露珠。',
        words='不安',
        desc='月亮象征倾听你的梦，以找到内心世界的平静。\n\n想象是相当强而有力的，它可以让内心很快的产生和平、和谐和欢乐；它也可以以同样快的速度产生痛苦、惊惧、悲伤和愤怒。月亮是一张代表梦和想象的牌。梦是转化为意象的潜意识能量。当这股能量强烈到无法被吸收或理解时，可能会导致狂野的梦、噩梦，甚至疯狂。月亮牌所代表的潜意识恐惧，必须由我们单独去面对。\n\n月亮代表强烈的梦想和经由梦传达到你意识思想中的直觉。强而有力的梦企图告诉你某些事情。倾听你的梦，你将会发现你所要找寻的答案。',
        upright='负面的情绪、不安和恐惧、充满恐惧感、阴森恐怖的感觉、黑暗的环境、景气低落、白日梦、忽略现实的、未知的危险、无法预料的威胁、胡思乱想的、不脚踏实地的、沉溺的、固执的。',
        reversed='度过低潮阶段、心情平复、黑暗即将过去、曙光乍现、景气复甦、挥别恐惧、从忧伤中甦醒、恢复理智的、看清现实的、摆脱欲望的、脚踏实地的、走出谎言欺骗。'
    ), init=False)

    the_sun: TarotCard = field(default=TarotCard(
        id=19, index='the_sun', type='major_arcana', orig_name='The Sun (XIX)', name='太阳',
        intro='可爱的裸体孩童骑在马背上，跨越灰色的围墙，脸上带着微笑。\n\n孩童头上戴着雏菊花环，以及一根红色的羽毛。这根羽毛就是在愚人与死神出现的同一根，象征太阳牌已经跨越了死亡的界限，而重获新生。围墙后面种满向日葵，里头是一座人造的花园，而孩童跃离了花园，代表他不需要这些人工的产物，他是最纯真、自然、不需隐藏的，如同他一丝不挂的身体。向日葵共有四朵，象征四要素昂与小阿尔克那的四个牌组。有趣的是，四朵向日葵是向着孩童，而不是太阳，表示这位快乐的孩童已经拥有足够的能量。马匹背上没有马鞍，孩童不用缰绳控制牠，甚至连双手也不用，显示马匹象征的能量已经受到充分控制。孩童左手持着红色旗帜，左手象征潜意识，红色旗帜象征行动，表示他已经不用像战车那样用象征意识的右手来掌控，他可以轻而易举、自然的控制一切。背景的太阳是生命的源头，万物赖以维生之源，总共有21道光芒，代表愚人以外的21张大阿尔克那，仔细一看在上方罗马数字的旁边有一道黑色的曲线光芒，代表愚人（另有一说是太阳中心圆形的部分是愚人）。这样的更改是为了避免原本的暧昧。',
        words='生命',
        desc='太阳象征欢乐、内在的平和，以及表达自我的需求。\n\n它也代表理解到幸福是一种选择。太阳代表一种令人愉悦的解脱。它表示觉醒的力量足以驱逐黑暗。它代表一种表达内在无意识和潜意识力量的天赋趋力。它是充满希望、理想主义，以天真率直的。\n\n太阳象征欢乐和内在平静，而且感觉宇宙是一个充满乐趣和创造性的地方。太阳是自由的充分显现。它从意识层心智的日常限制中彻底解放，转为一种开放、觉醒及自由状态。它是一种可以带来肉体自由的内心自由。太阳显示出欢乐、和平、幸福及有创意的生活态度，并且深深体会到生命之美。',
        upright='前景看好的、运势如日中天的、成功的未来、光明正大的恋情、热恋的、美满的婚姻、丰收的、事件进行顺畅的、物质上的快乐、有成就的、满足的生活、旺盛。',
        reversed='热情消退的、逐渐黯淡的、遭遇失败的、分离的、傲慢的、失去目标的、没有远景的、失去活力的、没有未来的、物质的贫乏、不快乐的人生阶段。'
    ), init=False)

    judgement: TarotCard = field(default=TarotCard(
        id=20, index='judgement', type='major_arcana', orig_name='Judgement (XX)', name='审判',
        intro='天使加百列（Gabriel）在空中居高临下吹号角，号角口处有七条放射状的线，象征七个音阶，能够将人类从物质世界的限制解放出来，并且疗愈人们的身心。\n\n喇叭绑着一张正方形红十字旗帜，象征业力的平衡。天使下方是个象征潜意识的海洋，在女祭司帘幕后面就曾出现过，如今已接近终点。海洋上漂浮着许多载着人的棺材，棺材象征物质世界的旧模式。棺材中人全都是灰色的，其中最显眼的是一位象征显意识的男性，含蓄地仰望天使；一位象征潜意识的女性伸出双手，大方迎接天使的呼唤；以及象征重生人格的小孩，背对着我们。远处则是白雪霭霭的高山，伟特说这是抽象思考的顶峰。',
        words='复活',
        desc='审判象征清晰的判断力。\n\n审判牌意指你对人生的老旧观念已经死亡，你正在接受内心的召唤，去过一种更有意义的生活。审判牌代表此时你有清晰的判断力。作为问题的答案，这牌暗示你拥有清晰的判断力。此时你理解了你由生命所展示的试炼及挑战中学习到了什么。\n\n审判牌也可能是在形容你了解你的精神目的，也知道要达成它的必要步骤。它代表你能清楚地看到自己，以及生命的时光。这会使你对如何开始又有何收获，产生莫大的喜悦或惊慌。收成十分就近了，你可以用你的正直和诚实来面对你的报偿。现在你审判你自己，如果你没有得到所希望的，实在也没有藉口可推诿了，因为你收割的正是你努力的产物。',
        upright='死而复生、调整心态重新来过、内心的觉醒、观念的翻新、超脱了束缚的、满意的结果、苦难的结束、重新检视过去而得到新的启发、一个新的开始、一段新的关系。',
        reversed='不公平的审判、无法度过考验的、旧事重演的、固执不改变的、自以为是的、对生命的看法狭隘的、后悔莫及的、自责的、不满意的结果、被击垮的。'
    ), init=False)

    the_world: TarotCard = field(default=TarotCard(
        id=21, index='the_world', type='major_arcana', orig_name='The World (XXI)', name='世界',
        intro='终于来到愚人旅程的终点。一位赤裸的舞者自由地在空中跳舞，她外貌看起来虽是女的，但在许多版本的塔罗牌中，她是雌雄同体，象征愚人终于成功将阴阳两股力量融合。\n\n舞者身体缠绕着象征高贵与神圣的紫色丝巾，象征神性其实就在每个人身上。舞者轻柔随意地手持两根权杖，象征进化与退化的力量，她同时具备两者。舞者身旁环绕着一个椭圆桂冠，桂冠象征成功，而它围绕成的椭圆形就像愚人的０号形状，愚人无限的潜力，在世界牌中发挥得淋漓尽致。桂冠上下各有一条红巾缠绕，形成倒８符号，象征无限与永恒，这在魔术师与力量牌都曾出现过。在图中四角有人、老鹰、狮子、牛，这些符号曾经在命运之轮出现过，牠们在命运之轮中还拿著书汲取知识，最后在世界牌中完成使命。',
        words='达成',
        desc='世界描述一种来自内心的快乐，它也可能暗示持久的成功。这是一张象征永久和持续成功的牌。你已经到达了成功之门的前方，成功女神让你耐心等待，她会让你进入成功之门的，只不过是时间问题罢了。成功之门周围是你经历过的幸福与哀伤，成功与失败，在到达乐土之前回忆一下过去的时光是很有必要的。这张牌暗示只要你拥有一颗感恩的心，就必能在你为自己打造的美丽世界中，寻找到幸福与快乐。\n\n牌的本意是“达成”，它告诉我们所有的事情都可以达成，所有的梦想都可以成为现实，没有不可能得到的事物。只要有耕耘，就能有相应的收获。',
        upright='完美的结局、重新开始的、生活上的完美境界、获得成功的、心理上的自由、完成成功的旅程、心灵的融合、自信十足带来成功、生活将有重大改变、获得完满的结果。',
        reversed='无法完美的、一段过往的结束、缺乏自尊的、感觉难受的、态度悲观的、丑恶的感情、无法挽回的局势、不完美的结局、无法再继续的、残缺的。'
    ), init=False)

    ace_of_wands: TarotCard = field(default=TarotCard(
        id=22, index='ace_of_wands', type='minor_arcana', orig_name='Ace of Wands', name='权杖首牌',
        intro='一只手从云中伸出，强而有力，握住一根长满绿叶的权杖。那根权杖是如此茂盛，以致鲜嫩的绿叶几乎从杖上“爆”开，有八片叶子脱离权杖，在空中飞舞。遍地青草溪流。远方的城堡似乎暗示着未来成功的可能。',
        words='行动',
        desc='权杖首牌暗示这是一个好的开始，放开手脚勇敢做。\n\n权杖首牌表示实践计划的能量和欲望。权杖首牌象征一个计划强而有力的开始，代表着手新计划的渴望、力量与勇气。这张牌推出已经开始的行动，而且一定会产生具体的结果，与纸上谈兵完全不同。首牌出现在采取行动的时候，他们不是代表任何的计划于决定，而是发动新事物的具体行为。',
        upright='Creation, Willpower, Inspiration, Desire, Creative spark, New initiative, New passion, Enthusiasm, Energy',
        reversed='Lack of energy, Lack of passion, Boredom, Delays, Blocks, Hesitancy, Creative blocks'
    ), init=False)

    two_of_wands: TarotCard = field(default=TarotCard(
        id=23, index='two_of_wands', type='minor_arcana', orig_name='Two of Wands', name='权杖二',
        intro='一位身穿领主服装的男子，站在他的城墙上，俯视他的辽阔领土，遥望远方海洋。他右手拿着一颗类似地球仪的球体，左手扶着一根权杖。右边的权杖则是被铁环系在墙上。城墙上有个白百合与红玫瑰交叉的图案，白百合象征纯洁的思想，红玫瑰象征热情，暗示两者之间必须取得平衡。',
        words='决定',
        desc='权杖二意味着一个决定。\n\n权杖二并不代表具体的行动，而是决定本身，通常是身体上的决定。行动是由权杖一所代表。在决定行动之前，权杖二代表对选择的评估，它是你所习惯的东西与你所想拥有的东西之间的一个抉择。\n\n权杖二暗示因成长而不满当前环境，需要决定未来行动方向的时机。他表示你目前所拥有的事实是不够的，你将决定下一步要怎么做。',
        upright='Planning, Making decisions, Leaving home, First steps, Leaving comfort, Taking risks',
        reversed='Fear of change, Playing safe, Bad planning, Overanalyzing, Not taking action, Playing it safe, Avoiding risk'
    ), init=False)

    three_of_wands: TarotCard = field(default=TarotCard(
        id=24, index='three_of_wands', type='minor_arcana', orig_name='Three of Wands', name='权杖三',
        intro='山巅上站着一个成功的商人，三根权杖笔直地竖立在地面上，商人右手握着其中一根，目送自己的贸易船出海。天空是鲜明的黄色，海映着天，也是黄色。',
        words='远见',
        desc='权杖三意味着面向远方，你的未来在你的眼光里。\n\n权杖三可以表示旅行或将计划付诸实行。可以代表当你寻求自我内在意义的时候，你仍可保持相对的沉静；表示你一边在扩展自身内在于外的新大道与利益，一边在维持一种平衡的状态。权杖三同时也暗示你正在考虑你最近的状况，并且寻找你内在与外在的意义。',
        upright='Looking ahead, Expansion, Rapid growth, Momentum, Confidence, Growth, Foresight',
        reversed='Obstacles, Delays, Frustration, Restriction, Limitations, Lack of progress'
    ), init=False)

    four_of_wands: TarotCard = field(default=TarotCard(
        id=25, index='four_of_wands', type='minor_arcana', orig_name='Four of Wands', name='权杖四',
        intro='四根巨大的权杖耸立在前方，其上挂着象征胜利的花环。两位女子手持花束高举头顶欢庆舞蹈着，远方隐约可见庆祝的人群，呈现一幅和谐且繁荣的景象。右边有护城河上有座桥，通往远方的表示稳固庄园城堡。',
        words='稳定',
        desc='权杖四意味着坚定牢固的合作。\n\n权杖四描出一个坚固的家庭或工作环境，欢乐与分享是每天生活的一部分。权杖四代表坚固，将权杖三中所决定的计划变得稳固或实在的行为。它经常暗示搬入新家或换工作，也表示你在目前的环境中安定下来。',
        upright='Community, Home, Celebration, Celebrations, Reunions, Parties, Gatherings, Stability, Belonging',
        reversed='Lack of support, Transience, Home conflicts, Instability, Feeling unwelcome, Lack of roots, Home conflict'
    ), init=False)

    five_of_wands: TarotCard = field(default=TarotCard(
        id=26, index='five_of_wands', type='minor_arcana', orig_name='Five of Wands', name='权杖五',
        intro='迥异于权杖四的和谐稳定局面，权杖五呈现一群年轻人混战的场面。每个人手上都拿着一根杖，彼此僵持不下，谁也不让谁。伟特说：这是一场模仿的战役。',
        words='冲突',
        desc='权杖五暗示缺乏和谐或者内在的冲突。\n\n权杖五是一张代表冲突的牌，虽然冲突不至于伤害任何人，但却是所有人全盘卷入。只是权杖类型的天性，总是把生活看成战争，因为如果没有障碍，就没有冒险了。而从另外一方面来看，这张牌比较可以形容成比较，较量，竞争。',
        upright='Competition, Rivalry, Conflict, Arguments, Aggression, Tension, Rivals, Clashes of ego',
        reversed='Avoiding conflict, Respecting differences. end of conflict, Cooperation, Agreements, Truces, Harmony, Peace'
    ), init=False)

    six_of_wands: TarotCard = field(default=TarotCard(
        id=27, index='six_of_wands', type='minor_arcana', orig_name='Six of Wands', name='权杖六',
        intro='一位年轻男子，戴着胜利的桂冠，骑着白马凯旋而归。四周都是围绕簇拥着他的群众。白色代表纯洁，马象征力量。红色的外衣象征积极主动与热忱。男子手持的权杖饰以胜利花环。艰辛奋斗已然过去，他现在抬头挺胸，享受属于他的荣耀时刻。',
        words='自信',
        desc='权杖六暗示着对人生充满自信的态度。\n\n在这张牌中，火的乐观主义使其欲求和期望得到成功。这不是错误的乐观主义或虚无的期待，而是来自过去的成功及自信的一种真正的信仰。权杖六也表示工作的升迁、证实达成目标，或仅是一种自信的生活态度。',
        upright='Victory, Success, Public reward, Triumph, Rewards, Recognition, Praise, Acclaim, Pride',
        reversed='Excess pride, Lack of recognition, Punishment, Failure, No rewards, Lack of achievement'
    ), init=False)

    seven_of_wands: TarotCard = field(default=TarotCard(
        id=28, index='seven_of_wands', type='minor_arcana', orig_name='Seven of Wands', name='权杖七',
        intro='绿衣男子站在青葱的山顶上，手持权杖，奋力迎击敌人从山下攻上的六根权杖。他高举右手，表情坚毅。',
        words='挑战',
        desc='权杖七暗示经由坚韧不拔而获得的成功。\n\n权杖七表示你需要更大的挑战。权杖七的讯息是“不要放弃”。继续努力前进，你将得到成功的回报。你投注于完成目标的体力与行动，将是值得的。',
        upright='Perseverance, Defensive, Maintaining control, Protectiveness, Standing up for yourself, Defending yourself, Protecting territory',
        reversed='Give up, Destroyed confidence, Overwhelmed, Giving up, Admitting defeat, Yielding, Lack of self belief, Surrender'
    ), init=False)

    eight_of_wands: TarotCard = field(default=TarotCard(
        id=29, index='eight_of_wands', type='minor_arcana', orig_name='Eight of Wands', name='权杖八',
        intro='八根权杖整齐划一的在空中航行，背景是蔚蓝的天空与青翠的山丘平原，还有一条宁静的小溪流过。',
        words='自由',
        desc='权杖八意味旅行及自由流动的能量。\n\n权杖八代表了海外旅行、自由流动的能量，以及达成目标的清晰路径。过去的努力就是在为现在的人生可以自由的旅行而铺路。权杖八表示你的目标清楚可见，而且正轻松的向它们迈进。这点可以从八根权杖自由而无约束的掠过天际看出来。权杖八没有拘束的本性反映了这是很少阻碍的时机。它表示你是自由的、可投注热情、直接追求目标。',
        upright='Rapid action, Movement, Quick decisions, Speed, Progress, Sudden changes, Excitement',
        reversed='Panic, Waiting, Slowdown, Slowness, Chaos, Delays, Losing momentum, Hastiness, Being unprepared'
    ), init=False)

    nine_of_wands: TarotCard = field(default=TarotCard(
        id=30, index='nine_of_wands', type='minor_arcana', orig_name='Nine of Wands', name='权杖九',
        intro='一个壮汉靠着长杖，似乎在等待着什么。他的头上扎绷带，显示他在过去战役中曾经受伤，尚未复原。但他并不畏惧，仍然紧锣密鼓等待着敌人的下一波来袭。他身后竖立八根权杖，井井有条，像是栅栏，包围着壮汉所守护的家园。',
        words='谨慎',
        desc='权杖九暗示重新评估目前承诺的时候。\n\n对于既存的问题纵是期待将来能够解决，现在这个人开始回顾过去的作为，以便看清他是怎么走到今天的。他已经渐渐知道所有行为都会产生结果，就好比他目前的生活就是过去作为的结果，而将来的生活则是由现在的决定和作为来引导的。\n\n这张牌代表逐渐意识到聚焦于承诺和目的是多么重要的事了。与其栽种五百颗混合的种子来期待有好的结果，不如仔细评估只耕耘一种特殊的品种，并且悉心照料它们，以享受耕耘后的收获。',
        upright='Resilience, Grit, Last stand, Persistence, Perseverance, Close to success, Fatigue',
        reversed='Exhaustion, Fatigue, Questioning motivations, Stubbornness, Rigidity, Defensiveness, Refusing compromise, Giving up'
    ), init=False)

    ten_of_wands: TarotCard = field(default=TarotCard(
        id=31, index='ten_of_wands', type='minor_arcana', orig_name='Ten of Wands', name='权杖十',
        intro='一个男人奋力的扛着十根沉重的权杖，朝着远方的房子前进。他被权杖的重量压得喘不过气，疲累万分，但他仍不愿放弃，为了生活，一步一脚印的往前走。',
        words='责任',
        desc='权杖十暗示一个委任某些责任的时机。\n\n权杖十描绘暗示一个委任某些责任的时机。他被这些权杖给压的沉下去，而且它们也遮住了他的方向（即远方的房子）。他急切地想要涉入这么多的情况当中，结果，因为种种承诺和问题而不胜负荷。权杖十通常伴随着一种态度：“如果你想妥适的完成它，你就要自己做。你觉得身负重任，所以不能去信任别人也能完成这件工作。\n\n尽管负担重重，然而权杖十代表你在付出极大努力后所获得的成功。或许你会因为交付出去某些责任而受惠，因为那会减轻你的压力，并且用时间去深思长期以来的憧憬。当你实现目标时。你有充分的理由为你的成就感到骄傲，因为权杖是证实了，要梦想成真就需要坚持和努力。',
        upright='Accomplishment, Responsibility, Burden, Duty, Stress, Obligation, Burning out, Struggles',
        reversed='Inability to delegate, Overstressed, Burnt out, Failure to delegate, Shouldering too much responsibility, Collapse, Breakdown'
    ), init=False)

    page_of_wands: TarotCard = field(default=TarotCard(
        id=32, index='page_of_wands', type='minor_arcana', orig_name='Page of Wands', name='权杖侍从',
        intro='权杖侍从把权杖拄在地上，好奇地看着杖顶，好像在研究什么东西。他的服装是明亮的鲜黄色，外衣上有权杖家族图腾火蜥蜴，有些蜥蜴的嘴没有真正咬到尾巴，形成不完整循环，但有些却有。牌的背景是沙漠和三个金字塔。',
        words='开始',
        desc='权杖侍从象征新的挑战，新的消息，跃跃欲试的梦想。\n\n权杖侍从意指该是开始某些新事物的时候了。它是展开一项新方案或旅行（如果有其他旅行牌出现在牌局中）的行动，且将指引你一个新方向。权杖侍从牌描述当开始一项新的事业时，一种可以感觉到年轻活力的行动。虽然对于行动会感到紧张，但是他仍然充满激情和热心，热衷于探索有用的经验以及展开新的冒险。',
        upright='Exploration, Excitement, Freedom, Adventure, Fresh ideas, Cheerfulness, Energetic, Fearless, Extroverted',
        reversed='Lack of direction, Procrastination, Creating conflict, Hasty, Impatient, Lacking ideas, Tantrums, Laziness, Boring, Unreliable, Distracted'
    ), init=False)

    knight_of_wands: TarotCard = field(default=TarotCard(
        id=33, index='knight_of_wands', type='minor_arcana', orig_name='Knight of Wands', name='权杖骑士',
        intro='权杖骑士骑着健马，高举权杖，表情自信地看着远方。他穿着明亮黄色服装，上面同样有权杖的家族象征火蜥蜴，但蜥蜴的嘴没有触碰到尾巴，形成一个不完整的循环。骑士的头盔顶端和背後都饰着红色的长穗，还戴着红手套，他以左手拉着缰绳，健马的前蹄高高举起。远方背景中出现三座金字塔，金字塔呈现在马脚的下方。',
        words='改变',
        desc='权杖骑士象征充满活力，信心满满的迎接改变。\n\n充满活力，信心满满的迎接改变。权杖骑士所代表的是火元素当中的火元素。这张牌可以象征行动、旅行、改变以及为了自身缘故的活动。看得出来权杖骑士正在思考未来的行动，骑士正全神贯注于对向往目标的积极追求。这张牌经常代表一种态度——完成某件事情唯一的办法就是自己动手做。瞄一眼这张牌就会得到火、活动、热情及活力的印象。权杖骑士暗示需要挑战、爱好旅游和学习，并有教学的能力。',
        upright='Action, Adventure, Fearlessness, Courageous, Energetic, Charming, Hero, Rebellious, Hot tempered, Free spirit',
        reversed='Anger, Impulsiveness, Recklessness, Arrogant, Reckless, Impatient, Lack of self control, Passive, Volatile, Domineering'
    ), init=False)

    queen_of_wands: TarotCard = field(default=TarotCard(
        id=34, index='queen_of_wands', type='minor_arcana', orig_name='Queen of Wands', name='权杖皇后',
        intro='权杖皇后戴着盛开绿叶的王冠，穿着阳光般金黄服饰，坐在宝座上。她的体态强健。她的左手拿着一朵向日葵，她的右手持权杖，眼光向左望。宝座的扶手是两只狮子，后面悬吊的帷幕上，再度出现火象的狮子图腾和向日葵。她前方有一只黑猫守护，这里的黑猫似乎也在保护权杖皇后，使她免于受伤害。远方有三座金字塔，天空则是一片既明亮又祥和的浅蓝色。',
        words='决心',
        desc='权杖皇后代表心灵的强大，透过内在力量而达到成功。\n\n权杖皇后牌可以说是透过内在的力量和自信而获得成功的。当你面对逆境时勇气会帮助你达成目标。相信你所做的事，以及做你所相信的事，可以帮助你了解你的目标。',
        upright='Courage, Determination, Joy, Confident, Self-assured, Passionate, Determined, Social, Charismatic, Vivacious, Optimistic',
        reversed='Selfishness, Jealousy, Insecurities, Demanding, Vengeful, Low confidence, Jealous, Selfish, Temperamental, Bully'
    ), init=False)

    king_of_wands: TarotCard = field(default=TarotCard(
        id=35, index='king_of_wands', type='minor_arcana', orig_name='King of Wands', name='权杖国王',
        intro='权杖国王坐在宝座上，身躯稍微向前倾，好像随时准备出发。他右手持权杖，杖上长有新鲜的绿叶。宝座和披风饰以狮子和火蜥蜴，地上还有一只火蜥蜴陪伴着他。',
        words='稳重',
        desc='权张国王代表经由自律而成功。\n\n权杖国王代表热忱坚定，魄力十足，经由自律而成功。他为人诚实、积极而坦率，而且经常愿意接受新挑战。他认为过程比结果还重要，而且拒绝任何拖泥带水的挑战。权杖国王描绘一个强壮的人，能够透过他的意志力来领导及统御别人。他对自己有坚强的信念，因为他的信心是建立在自身的经验上。他知道他的方法有效，因为他尝试过也试验过这种方法。自律可以让你超越自己，因此逆就会有充分的时间和体力来掌握更好的机会，让你完成已着手之事。',
        upright='Big picture, Leader, Overcoming challenges, Leadership, Vision, Taking control, Daring decisions, Boldness, Optimism',
        reversed='Impulsive, Overbearing, Unachievable expectations, Forceful, Domineering, Tyrant, Vicious, Powerless, Ineffective, Weak leader'
    ), init=False)

    ace_of_cups: TarotCard = field(default=TarotCard(
        id=36, index='ace_of_cups', type='minor_arcana', orig_name='Ace of Cups', name='圣杯首牌',
        intro='圣杯首牌是所有小牌的一号牌中最富象征意义的。图中的圣杯就是耶稣在最后晚餐中使用的杯子，杯上有个倒立的Ｍ字母。据说，在耶稣死后，他的鲜血就是由这个圣杯所承装着。\n\n白鸽是天主教中圣灵的象征，牠衔着象征耶稣身体的圣饼，自上而下彷佛要进入杯中。杯中有五道水涌出，下方的水面平静，只有少许涟漪，睡莲处处，睡莲茎长，向上伸展至水面。二十五滴水珠从四面落下，飘浮在空中。一只手从云中伸出，这只手和权杖一与宝剑一中的手截然不同，它是轻轻的捧着圣杯，而非用力抓住圣杯。',
        words='情感',
        desc='圣杯首牌意味情感的连接和满足。\n\n圣杯首牌正位是人际关系最好的开始，经常代表新感情的开端，对于人际关系是非常好的征兆。相对于权张首牌所代表的肉体上、体力上的开始，它暗示你已打开心扉接受新机会。它可能是一段新的两性关系，或既存关系的新阶段，或一种新层次的满足。此时正是你感觉情感满足的时刻。首牌描述的是透过感情和生活产生连接。你可能正经验着正立首牌的满足感或满意感。或许你正展开一项你全心期待的计划，或是一次旅行。',
        upright='New feelings, Spirituality, Intuition, Love, Emotional awakening, Creativity',
        reversed='Emotional loss, Blocked creativity, Emptiness, Coldness, Feeling unloved, Gloominess'
    ), init=False)

    two_of_cups: TarotCard = field(default=TarotCard(
        id=37, index='two_of_cups', type='minor_arcana', orig_name='Two of Cups', name='圣杯二',
        intro='一男一女面对彼此，向对方持杯致意。两人头上都戴着花环，男人身躯微微向前，左脚踏出，右手也伸向女人，而女人站姿端凝如山。他们中间浮着一根两条蛇缠绕的杖，称为“赫米斯之杖”，是治疗的象征。杖上的狮子头象征沟通，而两片翅膀象征圣灵，使人联想到恋人牌中的天使。远方是一座城镇。',
        words='平等',
        desc='圣杯二意指一种平等的伙伴关系或两性关系。\n\n圣杯二意指一种心灵上的契合。它形容一种既丰富又有创意的友谊或两性关系。其实，圣杯二讲的就是这两种力量的结合，若能同时拥有两种力量，且融合良好的话，会比单一力量更强大。当牌局中出现此牌时，它意味着连结你和对方的特质，那么你可能会获得某些比你单打独斗的成就还要来得大的东西。',
        upright='Unity, Partnership, Connection, Attraction, Close bonds, Joining forces, Mutual respect',
        reversed='Imbalance, Broken communication, Tension, Separation, Rejection, Division, Bad communication, Withdrawal'
    ), init=False)

    three_of_cups: TarotCard = field(default=TarotCard(
        id=38, index='three_of_cups', type='minor_arcana', orig_name='Three of Cups', name='圣杯三',
        intro='三个女子紧靠彼此，围成圆圈，高举圣杯互相庆贺。她们头上都戴着象征丰收的花圈，穿着色彩艳丽的袍子，脸上幸福洋溢。四周有藤蔓、葫芦及南瓜，一位女子手上提着一串葡萄，这些植物很容易让人联想到丰收的时节。这三位女子分别有不同颜色的头发与眼珠，穿戴的衣服花环也都各有不同，代表她们都是独立的个体，有独立的个性，但是，在这个团体中，她们都能尊重彼此，敬爱彼此。三人围成圆圈的型态，表示她们之间没有尊卑之分，在这个欢庆的场合里，每个人都是如此平等。',
        words='团聚',
        desc='圣杯三意味庆贺或重聚。\n\n圣杯三意指欢乐、分享或庆贺。圣杯三是一张代表庆祝、团圆或当所有参与者带来欢乐的一场聚会。这杖牌可一暗示由三人或更多的人来分享成功。圣杯三意味着一段庆祝的时光，一群志同道合的人们相聚，或代表这是个重大隆盛的晚宴。\n\n圣杯三也经常代表欢庆的场合，举凡各种宴会、聚餐、婚礼、弥月、尾牙、庆功宴等都算在内。其丰收的涵义表示事情有了好的结果，不管过程曾经有多艰辛。因此，圣杯三象征丰收的时节，长久的辛苦终于开花结果，获得成功。',
        upright='Friendship, Community, Happiness, Gatherings, Celebrations, Group events, Social events',
        reversed='Overindulgence, Gossip, Isolation, Scandal, Excess, Loneliness, Solitude, Imbalanced social life'
    ), init=False)

    four_of_cups: TarotCard = field(default=TarotCard(
        id=39, index='four_of_cups', type='minor_arcana', orig_name='Four of Cups', name='圣杯四',
        intro='一个男人百无聊赖地坐在树下，双眼紧闭，双手双脚合在一起，形成防御的姿态。他前方三个杯子象征他过去的经验。云中伸出一只手给他第四个杯子，他却视而不见，独自沉浸在自己的世界中。',
        words='不满',
        desc='圣杯四暗示要留意目前感情上的机会。\n\n圣杯四在告诉我们，应该睁开我们的双眼，在那些机会自眼前溜走之前好好的把握住它们。当你内心感到越充实时，你对外在的需求则越少。你越深思熟虑或将焦点放到内心，你就需要越稳定的基础（或与土地有更强的连结）来平衡你自己。\n\n这张牌带有一种沉闷及不悦的感觉，可能是求问者的生活日日如是，一成不变。其实生活未如想像般单调乏味的，只要求问者肯开阔视野，有些意料不到的事情便会发生。',
        upright='Apathy, Contemplation, Disconnectedness, Feeling disconnected, Melancholy, Boredom, Indifference, Discontent',
        reversed='Sudden awareness, Choosing happiness, Acceptance, Clarity, Awareness, Depression, Negativity'
    ), init=False)

    five_of_cups: TarotCard = field(default=TarotCard(
        id=40, index='five_of_cups', type='minor_arcana', orig_name='Five of Cups', name='圣杯五',
        intro='在灰暗的天空底下，有一个人身着黑色斗篷，低头哀悼地上三个倾倒的杯子，里头五颜六色的酒流了出来。他的前方是一条河，象征悲伤之流，但河上有座象征意识与决心的桥，通往远处的房子。灰暗的天色反映牌中人的沮丧的内心世界。从图面上无法分辨出这人是男是女，显示悲伤的情绪无论男女皆能体验。',
        words='悲观',
        desc='圣杯五代表在痛苦中回转身，寻找新的机会。\n\n圣杯五形容失落和悲伤。它可能是张代表分离的牌，或者有种和人生疏离的感觉。这段期间内，那些平稳而熟悉的事物似乎都逃离你了。在新机会现身前，你必须经历这段失落或孤立期。这张牌和所有的“五”（包括隐士牌）一样，在正立时都代表心胸窄狭，而倒立时，则有心胸宽大的意味。',
        upright='Loss, Grief, Self-pity, Disappointment, Sadness, Mourning, Discontent, Feeling let down',
        reversed='Acceptance, Moving on, Finding peace, Contentment, Seeing positives'
    ), init=False)

    six_of_cups: TarotCard = field(default=TarotCard(
        id=41, index='six_of_cups', type='minor_arcana', orig_name='Six of Cups', name='圣杯六',
        intro='在一座宁静安详的庄园里，有六个盛装星币花朵的圣杯。一个小男孩捧着圣杯，似乎在嗅着花香，又好像把圣杯献给小女孩。背景充斥代表快乐的鲜黄色，而天气晴和。让人彷佛有置身童话世界的感受。',
        words='安全',
        desc='圣杯六代表童真环境下的保障和安全。\n\n圣杯六描绘的是一种温柔而隐秘的情景，其中有某种程度的保障和安全，它带有一种可预知性。保障和安全倍受珍惜，不过这是以极高的代价换来的。因为没有什么冒险，所以通常没什么成长。\n\n圣杯六暗示以成长为代价而得到保障、安全和亲密。它可以意指你的居家或家庭状态的稳定。也可能是过去的事物或人们又出现了，等着你去处理。他也可以代表一种舒适的状态，让你有时间静下来，重新关注活力或安顿下来。',
        upright='Familiarity, Happy memories, Healing, Nostalgia, Memories, Comfort, Sentimentality, Pleasure',
        reversed='Moving forward, Leaving home, Independence, Stuck in past'
    ), init=False)

    seven_of_cups: TarotCard = field(default=TarotCard(
        id=42, index='seven_of_cups', type='minor_arcana', orig_name='Seven of Cups', name='圣杯七',
        intro='七个圣杯飘浮在云雾弥漫的半空中，杯中分别装着城堡（象征冒险）、珠宝（财富）、桂冠（胜利）、龙（恐惧，另一说是诱惑）、人头、盖着布发光的人（自己）以及蛇（智慧，另一说是嫉妒）。请注意桂冠的下方有颗不显眼的骷髅头，成功与死亡并存，似乎在给人什么警惕。有个人面对着这些圣杯，不知该如何选择，他的身体姿态似乎流露出些微恐惧。',
        words='梦想',
        desc='圣杯七代表应该认知你内在需求。\n\n圣杯七代表的是生活中的非现实层面，包括我们的梦境、幻想与白日梦，或是偶而异想天开的点子。这种想像通常只是空中楼阁，一般人不会真的把这些幻想付诸行动，因此圣杯七不是一张代表行动的牌，而只是一种个人想像的心理状态而已。这张牌描述的是：该去想想什么是你生活重要的部分。它显示出检视环境来确认你正走在通往满足之路的过程中。圣杯七意味着深思内在生活，已进行精神或情感的回顾。\n\n圣杯七是一张代表自我发现、心灵成长以及认识内在需求的牌。提醒你，充分了解自己与自己的行动，你需要行动，也需要思考。对行动有所思考能帮助你将直接的经验转变为知识，并更向智慧与理解靠近。没有思考，行动很快就会变得重复，而没有行动与经验，思考则可能变的索然无味，且毫无意义。这张圣杯七代表你需要向内探索自己，以追求所有爱的来源。你应该确认你所真正需要的是什么，并发现什么东西足以添满你的感情。',
        upright='Searching for purpose, Choices, Daydreaming, Illusion, Fantasy, Wishful thinking, Indecision',
        reversed='Lack of purpose, Diversion, Confusion, Disarray, Distractions, Clarity, Making choices'
    ), init=False)

    eight_of_cups: TarotCard = field(default=TarotCard(
        id=43, index='eight_of_cups', type='minor_arcana', orig_name='Eight of Cups', name='圣杯八',
        intro='身穿红衣红鞋的男子在暮色中，手持长杖，离开他先前辛苦建立的的八个杯子，越过河川，转身而去。四周沼泽密布，象征淤塞的情感，如同一滩死水。',
        words='突破',
        desc='圣杯八意味你已经突破某种状况，并显示你要追寻更多的东西。\n\n这张牌代表为了追寻一种新的满足，而放弃既有的满足方式。或许你正打算离职去找一个更有价值的工作，或者你正从你的爱的关系中撤退去寻找更深层的幸福。\n\n圣杯八意味着你正超越某人，或突破某特定状况。它表示一个人光理解还不够，还包括离开一种稳定的状态（圣杯六），去发现圣杯十所提供的满足感。没有任何人事物强迫你放弃目前的状态，除了你内心想达到更强烈满足的需求。要圆满的挑战成功，需要内在的力量，当八出现时，你就会拥有相对的勇气和力量。在大阿尔克纳牌中，第八张是力量牌。而所有塔罗牌的八也都和力量有关。',
        upright='Walking away, Disillusionment, Leaving behind, Abandonment, Letting go, Searching for truth',
        reversed='Avoidance, Fear of change, Fear of loss, Stagnation, Monotony, Accepting less, Staying in bad situation'
    ), init=False)

    nine_of_cups: TarotCard = field(default=TarotCard(
        id=44, index='nine_of_cups', type='minor_arcana', orig_name='Nine of Cups', name='圣杯九',
        intro='一个财主装扮的的男子坐在小凳上，双手抱胸，神情怡然自得。他身后的高桌上，覆盖蓝色桌布，九个圣杯排排站。背景则是一片光明的鲜黄色。',
        words='满足',
        desc='圣杯九意味对自己的满意和荣耀感。\n\n圣杯九的昵称叫做美梦成真，代表当事人的愿望极有可能实现，无论是精神或是物质方面。这张牌表示你了解自己真正的价值，而且就是你的价值造就了今天的你。\n\n圣杯九形容一种对能圆满达成工作而感到的骄傲和满足。你内心所拥有幸福和喜悦的感觉，可能是来自于你的工作环境、人际关系，或是来自一种心灵上的成就感。现在你内在的需求已经得到满足了，而你也能思考你所赢得的成功。在这张九牌当中有着从你对自己的爱里头所滋长出来的快乐、满足和平静。',
        upright='Satisfaction, Emotional stability, Luxury, Wishes coming true, Contentment, Success, Achievements, Recognition, Pleasure',
        reversed='Lack of inner joy, Smugness, Dissatisfaction, Unhappiness, Lack of fulfilment, Disappointment, Underachievement, Arrogance, Snobbery'
    ), init=False)

    ten_of_cups: TarotCard = field(default=TarotCard(
        id=45, index='ten_of_cups', type='minor_arcana', orig_name='Ten of Cups', name='圣杯十',
        intro='在卡面中我们看到一家四口和乐融融，父母亲搂抱对方，各举一只手迎向圣杯彩虹，两个孩子快乐的手牵手跳舞，背景是清翠的树木河流，和一栋房屋。',
        words='家庭',
        desc='圣杯十意味一个互利的团体或家庭状态。\n\n圣杯十是一张表示欢乐和分享的牌。它通常是在描述一个团队或家庭，他们在身体及精神上都能相互奉献及合作，并且共享所有的利益。圣杯十形容一个家庭或团体，而其中的每个人均能受益。因为每个人都坦然的付出和接受，因而团体的气氛和谐，大家也乐于付出。它暗示对家庭或工作环境（包括团队合作和分享）有所付出。这张是意味一个成功的家庭状态或聚合，其中每位参与者都充分的感受到对这个团体的归属感。',
        upright='Inner happiness, Fulfillment, Dreams coming true, Happiness, Homecomings, Emotional stability, Security, Domestic harmony',
        reversed='Shattered dreams, Broken family, Domestic disharmony, Unhappy home, Separation, Domestic conflict, Disharmony, Isolation​'
    ), init=False)

    page_of_cups: TarotCard = field(default=TarotCard(
        id=46, index='page_of_cups', type='minor_arcana', orig_name='Page of Cups', name='圣杯侍从',
        intro='圣杯侍从穿着花朵图案的衣服，身体很轻松地站着，左手叉腰，面带微笑，用好奇的眼光，没有任何压力地看着圣杯中蹦出的一条鱼。',
        words='奉献',
        desc='圣杯侍从意味有益于情感的奉献。\n\n圣杯侍从是想像力最丰富的孩子。他天真无邪，敏感细心，直觉性强，爱好幻想，好奇心重，甜美可人，喜欢作梦，常常问一些让人想都想不到的问题。他很随和，合作性高，可靠，关心别人的威受，也乐意为他人服务。这样的性格形成一位善解人意、敏感，多愁善感，强调感情交流互动的人。他认真对待他人，对於所爱的人更是忠诚。他也是一位勤勉好学和专心致志的人，自动自发地提供服务朝向特定目标努力，他热心助人，是值得信赖的好帮手，更是良好的工作伙伴。\n\n塔罗牌中的侍从牌都和学习有关，而且由于圣杯组牌涉及情感和直觉，所以这张牌可能意味着透过冥想，或其他任何类似的被动方式来进行心灵上的学习或发展。圣杯侍从代表一段新关系或圣以合伙关系的到来。一个让情感得到满足的机会。',
        upright='Happy surprise, Dreamer, Sensitivity, Idealism, Naivete, Innocence, Inner child, Head in the clouds',
        reversed='Emotional immaturity, Insecurity, Disappointment, Emotional vulnerability, Immaturity, Neglecting inner child, Escapism'
    ), init=False)

    knight_of_cups: TarotCard = field(default=TarotCard(
        id=47, index='knight_of_cups', type='minor_arcana', orig_name='Knight of Cups', name='圣杯骑士',
        intro='不同于权杖骑士或宝剑骑士的迅捷骑马姿态，圣杯骑士的白马很有绅士风度，优雅地行进，跟主人一样。圣杯骑士平举着圣杯，他的眼光有些梦幻，深深注视着圣杯。',
        words='选择',
        desc='圣杯骑士意味在感情和行动之间做出决定。\n\n圣杯骑士暗示来自某人的供给。它可能是指情感上的奉献，或某种更为实际的事物。它可能是指情感上的付出，或某种更为实际的事物。骑士也意味着一段决定是否等待或行动，让事情充分发展或找寻新机会的时期。为了发现满足，或许现在是随着心意（河流的象征）而为的时候了。',
        upright='Following the heart, Idealist, Romantic, Charming, Artistic, Graceful, Tactful, Diplomatic, Mediator, Negotiator',
        reversed='Moodiness, Disappointment, Tantrums, Turmoil, Avoiding conflict, Vanity'
    ), init=False)

    queen_of_cups: TarotCard = field(default=TarotCard(
        id=48, index='queen_of_cups', type='minor_arcana', orig_name='Queen of Cups', name='圣杯皇后',
        intro='圣杯皇后双手捧着圣杯，眼神直直的注视着圣杯。那圣杯是教堂形状，两臂各有一位天使，顶端是十字架，象征圣杯皇后的虔诚。她坐在海边的宝座上，宝座基部有个小美人鱼抓鱼的图案，顶部是两个小美人鱼共同抱着一个大蚌壳。',
        words='倾听',
        desc='圣杯皇后意味透过倾听直觉而成功。\n\n圣杯皇后意味透过倾听感觉，以及利用富创意的想象力而获得成功。她从经验得知，杂乱无章的想象所产生的结果通常是有限的，因此它可以将精力用在对身体、情感、精神及心灵上都相当有价值的行动上。虽然她可能显得温柔又细心，但眼神却意味着一种坚强的意志。爱调和她的意志，并增加个性上的深度。她带着爱心和怜悯行事，而且常常展现出浓浓的家庭感情。如果发生问题，她可能不会说出她的感觉，但仍然会对周遭的人给于支持，把自己的感情的困扰放在一边。',
        upright='Compassion, Calm, Comfort, Warmth, Kindness, Intuition, Healer, Counsellor, Supportive',
        reversed='Martyrdom, Insecurity, Dependence, Giving too much, Overly-sensitive, Needy, Fragile'
    ), init=False)

    king_of_cups: TarotCard = field(default=TarotCard(
        id=49, index='king_of_cups', type='minor_arcana', orig_name='King of Cups', name='圣杯国王',
        intro='国王坐在波涛汹涌海中央的宝座上，左边有条鱼跳出海面，右边有一艘帆船。他的内袍是代表水要素的蓝色，胸前还挂著鱼形项链。他左手拿著象征权力的杖，右手持圣杯，他却是圣杯家族中唯一不注视圣杯的人。',
        words='创作',
        desc='圣杯国王暗示透过创造和情感上的训练而成功。\n\n圣杯国王展现深度和理解力，他适合一个以满足他人的需求为主的位置。他感情已经成熟到能够清楚的考虑别人和自己的需求，而且常常以家庭及环境中的共同参与感为荣。\n\n圣杯国王暗示透过情感和创作上的训练而成功，经由落实精力在有创作的目标上，可以达到所追寻的成功。一种成熟、有创意的方法带来琛功，尤其是在创造和艺术的努力上。这张国王牌暗示你应该信赖你本能——别放弃。它暗示一种坚强又冷静的方式。想象加灵感，再加上实际的努力就会得到回报。',
        upright='Compassion, Control, Balance, Wise, Diplomatic, Balance between head and heart, Devoted, Advisor, Counsellor',
        reversed='Coldness, Moodiness, Bad advice, Overwhelmed, Anxious, Cold, Repressed, Withdrawn, Manipulative, Selfish'
    ), init=False)

    ace_of_swords: TarotCard = field(default=TarotCard(
        id=50, index='ace_of_swords', type='minor_arcana', orig_name='Ace of Swords', name='宝剑首牌',
        intro='一只手从云中伸出，紧紧握住宝剑，宝剑穿过皇冠与桂冠，而远方是毫无绿意的尖锐山头，以及灰白空旷的天际。',
        words='思想',
        desc='宝剑首牌代表毅然决然的行动，开始计划一项新的冒险。\n\n宝剑首牌代表的是一个开始，时涉及以相信冒险或方案的行动。权杖首牌描述身体上的行动，杯子牌的首牌则是情感上的行动，而这张首牌叙述一个意念的形成，或是为未来的行动所准备的计划。这张牌代表清晰的思考，或明确的了解到完成一项计划所需要的是什么。\n\n同时这把双面的宝剑强调着现实、成就与成功所必须负担的责任和应得的报酬。宝剑一只是一个开端，一种可能。未来究竟要如何发展，掌握在持剑者的手中。',
        upright='Breakthrough, Clarity, Sharp mind, New idea, Concentration, Vision, Force, Focus, Truth',
        reversed='Confusion, Brutality, Chaos, Miscommunication, Hostility, Arguments, Destruction'
    ), init=False)

    two_of_swords: TarotCard = field(default=TarotCard(
        id=51, index='two_of_swords', type='minor_arcana', orig_name='Two of Swords', name='宝剑二',
        intro='身穿浅灰长袍的女人坐在灰石凳上，背对着澎湃汹涌、暗礁满布的海洋。她眼蒙白布，双手持剑，在胸前交叉不动。天际高挂一轮新月。',
        words='抉择',
        desc='宝剑二意味着做出一个决断，无论对与错，不要试图逃避。\n\n宝剑意味为你需要作决定或在两个选择当中择其一。这是二则一的抉择，或许在目前这个阶段，你对于所做的选择会产生怎样的结果，洞察力还不够。你在做决定的时候，并没有对你的环境做通盘的考虑，或者是，你没有考虑到你的抉择会带来怎样的结果。\n\n正视你所恐惧的，如此你才能明了你周遭事物对你有什么意义。一个正确决定的报偿正等着你，它的第一个回报是解脱感，这解脱感来自于你能够锁定一个方向。',
        upright='Difficult choices, Indecision, Stalemate, Stuck in the middle, Denial, Hidden information',
        reversed='Lesser of two evils, No right choice, Confusion, Indecision, Hesitancy, Anxiety, Too much information, Truth revealed'
    ), init=False)

    three_of_swords: TarotCard = field(default=TarotCard(
        id=52, index='three_of_swords', type='minor_arcana', orig_name='Three of Swords', name='宝剑三',
        intro='映入眼帘的是一幅令人痛苦的画面。即使是完全没有接触过塔罗牌的朋友，也可以轻易道出宝剑三的涵义──伤心。三把剑合力刺进一颗鲜红的心，背景是灰暗的雨和云。某些版本的塔罗牌给这张牌一个更直接的名称，叫做“悲伤”。',
        words='悲伤',
        desc='宝剑三意味着伤心在所难免，请接受你的痛苦和悲伤。\n\n宝剑三代表的是，你正强烈的经验这悲伤和失落的一段时间。当出现这张牌时，内心的困惑、悲痛和沉重是很明显的，它表示强烈的失望。但你要知道：去体验你的悲伤是很重要的，因为在这么做的同时，你也扫除了障碍，让即将到来的机会可以接近你。记住，悲伤是会过去的。\n\n虽然痛苦，但我们要看破痛苦的假象。宝剑三凌空的心，告诉我们需要再去深入思考，以获得解脱和更深的觉醒，三把宝剑只是一种试炼，这颗心也可以是一种假托，而不是我们真正的心灵。以承受和接纳的态度，来化解宝剑成为优美的思考认知。',
        upright='Heartbreak, Suffering, Grief, Separation, Sadness, Sorrow, Upset, Loss, Trauma, Tears',
        reversed='Recovery, Forgiveness, Moving on. healing, Reconciliation, Repressing emotions'
    ), init=False)

    four_of_swords: TarotCard = field(default=TarotCard(
        id=53, index='four_of_swords', type='minor_arcana', orig_name='Four of Swords', name='宝剑四',
        intro='图中的男人在类似修道院的建筑物内休息，双手合抱胸前，呈现安详的状态。彩绘玻璃表现一个祈祷者跪在圣母面前的画面，好像在寻求什么建议，以获得内心的宁静。三把宝剑挂在墙上不用，但他身旁仍保有一把宝剑，当他醒来，随时可以拿起宝剑来采取行动。',
        words='沉思',
        desc='宝剑四暗示在危机中安静的思考，退隐中的深思熟虑。\n\n\n宝剑四这张牌可能象征自生活中撤离：身体上退隐到自家当中，或在精神上退隐到梦想和幻想当中。这是一张反省过去行为和计划未来的牌。他说明精神层面的巩固：采取让过去行为有意义的行动，以及排除那些已经被证实为不正确、或没有建设性的想法和信念。如此一来就有可能运用过去的经验来帮助你获得未来的成功。在经历了宝剑三的痛苦之后，随之而来的是对你自己和你的人生有更深层的了解。',
        upright='Rest, Restoration, Contemplation, Relaxation, Peace, Sanctuary, Recuperation, Self-protection, Rejuvenation',
        reversed='Restlessness, Burnout, Stress, Recovery, Awakening, Re-entering world, Release from isolation'
    ), init=False)

    five_of_swords: TarotCard = field(default=TarotCard(
        id=54, index='five_of_swords', type='minor_arcana', orig_name='Five of Swords', name='宝剑五',
        intro='红发的男子右手抱着两把剑，左手拄着另一把，回头注视远方两个失败者，嘴角似乎带着微笑。很明显的，他们刚结束一场争执，也许暴力相向。地上还散落着两把剑。另外两人中，一人怅然离去，一人用手摀着脸，似乎难以接受，或者感到伤心羞辱。天空中被风吹散的云彷佛也在说着他们争执的故事，看来很不宁静。',
        words='纷争',
        desc='宝剑五意味误会加深，争吵和紧张，解决的机会十分渺茫。\n\n宝剑五这张牌代表争吵、紧张和冲突，这可能使指你与自己内在的交战，或和你周遭人的不协调。假如这个冲突是指你和别人的，则其前提很有可能来自你的思想。在这种冲突的情况下，每个人对于事情的解决方法都各有见地，却没有人愿意聆听他人的心声。',
        upright='Unbridled ambition, Win at all costs, Sneakiness, Arguments, Disputes, Aggression, Bullying, Intimidation, Conflict, Hostility, Stress',
        reversed='Lingering resentment, Desire to reconcile, Forgiveness, Reconciliation, Resolution, Compromise, Revenge, Regret, Remorse, Cutting losses'
    ), init=False)

    six_of_swords: TarotCard = field(default=TarotCard(
        id=55, index='six_of_swords', type='minor_arcana', orig_name='Six of Swords', name='宝剑六',
        intro='一艘小船上插着六把宝剑，船上有一个女人、一个小孩与一位船夫。\n\n船缓缓的朝远方的岸边前进，而此端的水汹涌，彼方的水平静。象征伤害的六把剑插在船身上，以及三个主角哀伤的背影，构成宝剑六缓慢低回的基调。沉重的剑身让船夫只能缓行，疗伤的过程亦同。但是我们不能把宝剑抽起，否则船会沉，正如我们不能把过去的哀伤连根拔起，只能轻轻的抚平。也许你该庆幸，这些宝剑并不能使船沉没。',
        words='平静',
        desc='宝剑六暗示远离是非，在混乱之后，逐渐回复平静。\n\n这是受伤后康复的过程，不管伤多重，总是能痊愈。水象征情绪，这端汹涌的水是你烦扰的过去，前方大片平静的水面，预示未来安详的情绪。船夫手持黑色长篙，黑色象征潜质，将来什么都还是可能发生，不要将自己困死了。宝剑六是一个信道，领你向未来的幸福快乐前进，光明的日子就在前方。\n\n这张牌暗示你正带着你的剑（问题），从过去走向未来。或许你根本没注意到它们，然而它们却是与你紧紧相随。这是一个从艰困时刻过渡到一个较为平衡状态的过程。即使现时的问题及困难如何复杂，最终都会得到解决，求问者届时心情自然轻松不少。宝剑六可能是在说明当你转移向新的经验时，你也正慢慢的远离困境，情绪从过去释放出来。',
        upright='Transition, Leaving behind, Moving on, Departure, Distance, Accepting lessons',
        reversed='Emotional baggage, Unresolved issues, Resisting transition, Stuck in past, Returning to trouble, Running away from problems, Trapped'
    ), init=False)

    seven_of_swords: TarotCard = field(default=TarotCard(
        id=56, index='seven_of_swords', type='minor_arcana', orig_name='Seven of Swords', name='宝剑七',
        intro='图中的男子身处军营中，趁着远方敌人炊饭没有防备时，悄悄偷走五把剑，还留着两把在原处。',
        words='逃避',
        desc='宝剑七意味另辟蹊径，若要成功的话，需要一种新的方法。\n\n宝剑七所传达的讯息是：不要放弃。去找寻另一种可以达成目标的方法吧。坐下来，检查一下你所有的选择，以便发现先前未曾预见的可能性。你当然还有时间来完成你的愿望，然而在方法上需要更有弹性，各种行动的不同组合方式，就有可能会带来不同的结果。\n\n宝剑七暗示经由审慎评估各种可能，你就能找到有效的解决之道。透过详细的规划和不放弃的决心，你就能得到更多。比如你目前正汲汲营营于某件重要的事，理智所提供的解决方案会让你不需要如此费劲。\n\n宝剑七同时也是一张秘密、隐藏动机和不坦诚的牌。牌中暗示求问者欲逃避一段令他不愉快的事情，这件事可能会令他有金钱损失或与面子有关，求问者若肯勇敢面对，并应用智慧及交际手段去补救。',
        upright='Deception, Trickery, Tactics and strategy, Lies, Scheming, Strategy, Resourcefulness, Sneakiness, Cunning',
        reversed='Coming clean, Rethinking approach, Deception, Confession, Conscience, Regret, Maliciousness, Truth revealed'
    ), init=False)

    eight_of_swords: TarotCard = field(default=TarotCard(
        id=57, index='eight_of_swords', type='minor_arcana', orig_name='Eight of Swords', name='宝剑八',
        intro='一个女人眼睛被布蒙住，上半身被捆绑着，身处八把宝剑群中。地上满是象征羞辱的泥泞，而远方是座矗立于峭壁之上的城堡，象征绑住她的权威。',
        words='限制',
        desc='宝剑八暗示限制及丧失个人的能力。\n\n宝剑八代表的是你被限制住的一段时间，或是在某种情况下你失去个人的能力。你觉得动弹不得，受到限制，而且没有办法看清楚你前面的路。\n\n塔罗牌的“八”是代表力量的牌。而对于宝剑八里面的女人，这份力量源自于倾听她内在的声音的能力。双眼被蒙蔽让她无法透过视觉来做判断，她显得那么的无能为力，然而第一眼看上去这是个阻碍，但其实却是助力。阻碍那个女人控制自己所处环境的力量，却使得她能够走进自己的内心世界倾听内在的声音，并且留心它所发出的指令。如果你想做出有效率的决定，现在是留心你的自我精神层次的时候了。\n\n去探索那等待着你的道路吧，利用你内在的力量和个人的能力，将自己从目前的情况中释放出来，并且把那些曾经屈服于他人的个人能量重新召唤回来。你的信念其实才是你最大的限制。好好自省并检视这些信念，因为事实上目前的“眼罩”是在帮助你，因为它可以让你不会分心。',
        upright='Imprisonment, Entrapment, Self-victimization, Trapped, Restricted, Victimised, Paralysed, Helpless, Powerless',
        reversed='Self acceptance, New perspective, Freedom, Release, Taking control, Survivor, Facing fears, Empowered, Surrender'
    ), init=False)

    nine_of_swords: TarotCard = field(default=TarotCard(
        id=58, index='nine_of_swords', type='minor_arcana', orig_name='Nine of Swords', name='宝剑九',
        intro='午夜梦回，一个女子从睡梦中惊醒，把脸埋在双手中。墙上横挂着九把剑，看起来彷佛从后面刺穿那女子，带给人极大的压迫感。棉被图案是由象征热情的玫瑰，以及星座符号组成的。床侧则雕刻着一人击败另一人的画面。',
        words='梦魇',
        desc='宝剑九暗示由梦境传达的直觉，或对问题的担心。\n\n宝剑九代表的是强烈的梦。或许你的潜意识正努力教导你某些事情，去倾听你的梦境。宝剑九是一张代表担心和情绪骚动的牌。这种担心可能是对自己或周遭的一切。也可以代表鲜明的梦境或梦魇，而梦魇则可能是在传达一种强烈的讯息，即你生命当中某些不对劲的事物，已由潜意识而浮现在你的意识层面了。\n\n假设你将你的梦境写成日志，或许会发现一个共同的线索或是明显的讯息。那么你的梦就可以变成一项接近你潜意识的有效工具了。',
        upright='Anxiety, Hopelessness, Trauma, Fear, Negativity, Breaking point, Despair, Nightmares, Isolation',
        reversed='Hope, Reaching out, Despair, Recovery, Learning to cope, Facing life, Finding help, Shame, Guilt, Mental health issues'
    ), init=False)

    ten_of_swords: TarotCard = field(default=TarotCard(
        id=59, index='ten_of_swords', type='minor_arcana', orig_name='Ten of Swords', name='宝剑十',
        intro='一个俯卧的男人，背上插着十把剑，有一把甚至从插进耳朵里去。这画面实在令人怵目惊心。牌面中有一半被黑色的天空和乌云所占去，多少暗示宝剑十这张牌是大家避之唯恐不及的所谓的“坏牌”。',
        words='失败',
        desc='宝剑十意味着痛苦挥之不去，在另一个开始之前某种状况的结束。\n\n这张牌暗示在某种情况下，你已到了最低潮的时刻，你也可能是被一些无用的事物，或对生命具破坏性的信念给绊住了。但远方微弱的阳光暗示着，尾随这艰困时刻的将会是新的以及更好的事物。你对人生的思想或信念导致你此刻的境遇，从这里，你的思想将会带领你到任何你认为能够去的地方。\n\n宝剑十代表一种情况的结束。可能指两性关系的结束，或某关系中的一个阶段的结束，或一项事业的失败。你生命中的某些事物已经结束了，虽然这毫无疑问的会是一段艰难的时期，不过好消息是，它终究会过去，接受这个事实有助于新事物来取代旧的的。',
        upright='Failure, Collapse, Defeat, Ruin, Bitterness, Exhaustion, Dead end, Victimization, Betrayal',
        reversed="Can't get worse, Only upwards, Inevitable end, Survival, Improvement, Healing, Lessons learned, Despair, Relapse"
    ), init=False)

    page_of_swords: TarotCard = field(default=TarotCard(
        id=60, index='page_of_swords', type='minor_arcana', orig_name='Page of Swords', name='宝剑侍从',
        intro='宝剑侍从两手握著宝剑，眼光却朝著远方。他的头发和背景中的树都被风吹得飞扬。远方天空中有十只小鸟成群飞舞。背景灰云带来些许混乱的气氛',
        words='幻想',
        desc='宝剑侍从象征太多的梦想，而行动却不够。\n\n你可以发现到这个侍从双脚离地甚远，这个思考敏捷的年轻人喜欢说话、有很多点子和创新的概念，而这些成双出现的点子却无法搭在一起。这表示一种生活的态度，这种态度要求你透过梦境和思想让自己从现实抽离出来。\n\n宝剑侍从可能代表有关你目前所拥有的一个构想或计划的消息。但却没有付诸行动。对那些依赖创意和思考维生的人而言，这可说是一张正面的牌，但是也可能暗示脚踏实地是必要的，假设你想生产实际或有形的东西。',
        upright='Curiosity, Restlessness, Mental energy, Curious, Witty, Chatty, Communicative, Inspired, Vigilant, Alert, Mental agility',
        reversed='Deception, Manipulation, All talk, Scatterbrained, Cynical, Sarcastic, Gossipy, Insulting, Rude, Lack of planning'
    ), init=False)

    knight_of_swords: TarotCard = field(default=TarotCard(
        id=61, index='knight_of_swords', type='minor_arcana', orig_name='Knight of Swords', name='宝剑骑士',
        intro='宝剑骑士和圣杯骑士同样骑着白马，但宝剑骑士这匹马在狂风中极速奔驰，与圣杯骑士平缓前进的马形成强烈对比。宝剑骑士将宝剑高举过头，表情狰狞，向前冲杀。马鞍上饰以蝴蝶和鸟，象征风要素。他穿着铁甲，外袍也有鸟的图案，而靴子前后都带着尖刺，在战场上毫不留情。云和树都被狂风吹得七零八落。空中飞翔的鸟，队形也略显散乱。',
        words='急躁',
        desc='宝剑骑士暗示要达成愿望需要有敏捷的行动。\n\n宝剑骑士代表的是迅速的行动：跃进或跳出某种情景。作为某个问题的答案，它暗示着一个快速的动作或出其不意的行为是有需要的。已经没有时间去想该做何选择了——去做就对了。\n\n这张牌通常是代表一个年轻人，他不按牌理出牌、缺少耐心、思考敏捷。这是属于年轻人的力量，他要走往自己的道路。是一种英勇的行径或者说英雄气概的展现。当然这种冲撞的行动，也可能极具破坏力，能造成摧毁的状况。他的意志力坚强，专注而犀利，有着清明的勇气和专一凝聚的心志。',
        upright='Action, Impulsiveness, Defending beliefs, Assertive, Direct, Impatient, Intellectual, Daring, Focused, Perfectionist, Ambitious',
        reversed='No direction, Disregard for consequences, Unpredictability, Rude, Tactless, Forceful, Bully, Aggressive, Vicious, Ruthless, Arrogant'
    ), init=False)

    queen_of_swords: TarotCard = field(default=TarotCard(
        id=62, index='queen_of_swords', type='minor_arcana', orig_name='Queen of Swords', name='宝剑皇后',
        intro='宝剑皇后戴著蝴蝶花纹的王冠，象征灵魂，也象征风要素。她穿着灰色内袍，和蓝天灰云花纹的披风。她的表情坚毅，似乎皱著眉头，左手却对世界敞开。她右手高举宝剑，剑尖笔直向上。她的宝座扶手之下有个人头花纹，那是风之精灵，宝座的底部又有蝴蝶花纹。宝剑皇后的头顶上有只高飞的鸟。背景天空是深蓝色的，还有大片的灰云。',
        words='理智',
        desc='宝剑皇后代表淡定冷静，经过深思熟虑所得到的成就。\n\n宝剑皇后是一张思索感情的牌。它可能意味运用心智到情感中的行动，好让感觉有意义。作为某个问题的答案，宝剑皇后暗示透过清晰思考而获致成功。\n\n现在正是你反省过去的行为或目前情况的时刻了。密切的观察那些接近你的事物，以确认你不会再重陷困境中。你可能会想从生活当中撤退，好好的思考你自己，以及未来的方向。',
        upright='Complexity, Perceptiveness, Clear mindedness, Honest, Independent, Principled, Fair, Constructive criticism, Objective, Perceptive',
        reversed='Cold hearted, Cruel, Bitterness, Pessimistic, Malicious, Manipulative, Harsh, Bitter, Spiteful, Deceitful, Unforgiving'
    ), init=False)

    king_of_swords: TarotCard = field(default=TarotCard(
        id=63, index='king_of_swords', type='minor_arcana', orig_name='King of Swords', name='宝剑国王',
        intro='宝剑国王是四张国王牌中唯一以正面出现的。他穿著蓝色内袍和红色披风，他的右手持剑，剑尖偏右，偏向行动的那一边。左手戴着象征权力的戒指，轻松的放在腿上。他后方帷幕上饰有象征灵魂和风要素的蝴蝶花纹。天空中的鸟的数量有两只，象征在智慧与行动之间的选择，对宝剑国王而言，智慧必须用行动来实现。',
        words='公正',
        desc='宝剑国王暗示将梦想化为现实，用构想去做一些真实的事。\n\n宝剑国王是客观理性，凡事讲求合理和公正，具有坚定而一贯的信念和完整的思想体系，很难被他人所影响。他凭借事实和原则而下决定，不会情感用事或主观成见，并且会考虑得十分周到，显出谨慎和深沉的特色。\n\n宝剑象征着人的思想和决心，这位国王手执宝剑，自然具有着掌握思考的能力，并且很重视理念和原则，在意的是合理与正义。宝剑国王代表对清楚的思想的追求、诚实，以及将只是倒入现实的需求。作为某个问题的答案，这张国王牌可以说是透过清楚而有效之计划而达到成功。',
        upright='Head over heart, Discipline, Truth, Reason, Authority, Integrity, Morality, Serious, High standards, Strict',
        reversed='Manipulative, Cruel, Weakness, Irrational, Dictator, Oppressive, Inhumane, Controlling, Cold, Ruthless, Dishonest'
    ), init=False)

    ace_of_pentacles: TarotCard = field(default=TarotCard(
        id=64, index='ace_of_pentacles', type='minor_arcana', orig_name='Ace of Pentacles', name='星币首牌',
        intro='云中伸出一只手，捧着一枚星币。背景是花草满布的繁盛庭园，绿树拱门外的远方有座白色的山，暗示星币一不只有关物质，也可以延伸到精神层面。',
        words='物质',
        desc='星币首牌暗示，你有足够的钱好执行你的计划。\n\n星币首牌是张将梦想化为实质的牌。圣杯牌组中，我们有梦﹔星币牌组中，我们筑梦，梦想不再只是空中楼阁。星币首牌让我们稳健，踏实，有安全感。星币首牌和务实的开始有关。它意味你有足够的金钱、精力，或充分的条件，来开始一项新计划。它暗示你可以平衡掉花费。不论目前花掉了多少钱，赚回来的绝对够本。',
        upright='Opportunity, Prosperity, New venture, New opportunities, Resources, Abundance, Security, Stability, Manifestation',
        reversed='Lost opportunity, Missed chance, Bad investment, Missed chances, Scarcity, Deficiency, Instability, Stinginess, Bad investments'
    ), init=False)

    two_of_pentacles: TarotCard = field(default=TarotCard(
        id=65, index='two_of_pentacles', type='minor_arcana', orig_name='Two of Pentacles', name='星币二',
        intro='一个红衣装扮，头戴高帽，类似街头艺人的男子，正在耍弄两个星币，星币外围的带子形成８自形无限符号，魔术师和力量牌中也有这个符号。他背后的海面起伏剧烈，两艘船正在其上行驶。',
        words='两难',
        desc='星币二暗示与金钱有关的决定。\n\n星币二显示一个专注于钱财的人。此时他并没有重大的财务压力，只是要决定那张账单要先付而已。保持弹性，是星币二带给我们的另一个课题。除了随机应变的弹性，星币二也求取平衡。\n\n星币二描述着权衡各种机会的轻重，而这次它们是属于身体或物质的层面上。这象征着介于两个选择之间的决定。你有没有办法现在就抉择，或是再等一会儿会不会比较好呢？',
        upright='Balancing decisions, Priorities, Adapting to change, Balancing resources, Adaptation, Resourcefulness, Flexibility, Stretching resources',
        reversed='Loss of balance, Disorganized, Overwhelmed, Imbalance, Unorganized, Messiness, Chaos, Overextending'
    ), init=False)

    three_of_pentacles: TarotCard = field(default=TarotCard(
        id=66, index='three_of_pentacles', type='minor_arcana', orig_name='Three of Pentacles', name='星币三',
        intro='在一座修道院里头，有位雕刻师正在工作，旁边两位修道人拿着草图，似乎正在和雕刻师讨论工作的进度。',
        words='学习',
        desc='星币三暗示透过研究、学习，或者将构想付诸实现，而改善自身的境遇。\n\n这张牌代表扎根于稳固的基础上，建立某些具有持久价值的东西。也许你是在建造一栋房子，开始学习一个对你有助益的课程，或为稳固的两性关系或生意打基础。星币三对自我发展而言是张正面的牌。星币三表示去作某些将可以改善你环境事情的一段时间。它可能是开始一个课程、阅读书籍，或如果它是出现在事业的分析中，那就是你在工作当中学习拥有一个机会去建立某种具有永久价值的东西。\n\n星币三是一个鼓励，鼓励当事人不管在进行什么样的工作，都可以仔细计划，然后放手去做，因为他具备完成工作所需要的专业能力，他有充足的才干来达成手边任何任务。星币三的成功不是偶然，他不仅有专业能力，还实实在在的工作。',
        upright='Teamwork, Collaboration, Building, Shared goals, Apprenticeship, Effort, Pooling energy',
        reversed='Lack of teamwork, Disorganized, Group conflict, Lack of cohesion, Apathy, Poor motivation, Conflict, Ego, Competition'
    ), init=False)

    four_of_pentacles: TarotCard = field(default=TarotCard(
        id=67, index='four_of_pentacles', type='minor_arcana', orig_name='Four of Pentacles', name='星币四',
        intro='图中的男人戴着皇冠，身穿象征统治威权的红色袍子，下摆饰以蓝边，显示出崇高的领主身分。他坐在一个箱子上，头顶一枚星币，双手紧抓着另一枚，双脚又各踩着两枚，紧张的神情似乎深怕他失去任何一丁点财产。这个人虽有钱，却孤绝于城市人群之外。',
        words='节约',
        desc='星币四意味厚积薄发，节省你的金钱或体能以迎接更大的挑战。\n\n星币四正位置常代表物质上的获利与稳定，获利的来源可能是工作，也可能是接受赠与或遗产。然而，星币四代表物质上的稳定，却不保证心灵上的成长。星币四意味你正在节约金钱、节省精力，或是节制。它也可能意味经由节约金钱、偿还债务及量入为出，而是你的财务状况日趋稳定。或许你在设计增加收入或减少指出，以确保自己进来的钱比出去的多。',
        upright='Conservation, Frugality, Security, Possessiveness, Insecurity, Hoarding, Stinginess, Stability, Savings, Materialism, Wealth, Boundaries, Guardedness',
        reversed='Greediness, Stinginess, Possessiveness, Generosity, Giving, Spending, Openness, Financial insecurity, Reckless spending'
    ), init=False)

    five_of_pentacles: TarotCard = field(default=TarotCard(
        id=68, index='five_of_pentacles', type='minor_arcana', orig_name='Five of Pentacles', name='星币五',
        intro='冰天雪地中，两个乞丐蹒跚前行，又瘸又驼背，身上的衣服破烂不堪。他们经过一间象征物质与精神庇护的教堂，却视而不见，挺着饥饿且疲惫的身躯，径自赶路。',
        words='困难',
        desc='星币五意味对那些充实你的事物的疏离感。\n\n卡面上的两个人本可以选择如何去发现、跟随及落实精神之路。教堂其实只是他们的一种选择。它代表把精神价值介绍给那些无意去追求的人。在五这张牌中，这些人没有看见它，因此丧失了一个改变的机会。外在悲惨是内在悲惨的一种反映，所以当星币五出现时，你需要接受生命提供给你的改变机会。“如果你想改变这个世界，请先改变你自己”是这张牌的答案。\n\n就整体观点来看，星币五说的是财务上的困难、贫穷、疾病和内在的寂寞。在不断的挣扎当中，你很容易窄化你对问题的焦点，而忽略了你的机会。当这张五出现时，深度的心灵改变是有其需要的，否则虽然有外在的助力，可能还是解决不了你的问题。你目前的人生观并非你的支柱，而现在你必须问自己，是否仍愿意保有这些信念。',
        upright='Need, Poverty, Insecurity, Hardship, Loss, Isolation, Feeling abandoned, Adversity, Struggle, Unemployment, Alienation, Disgrace',
        reversed='Recovery, Charity, Improvement, Positive changes, Recovery from loss, Overcoming adversity, Forgiveness, Feeling welcomed'
    ), init=False)

    six_of_pentacles: TarotCard = field(default=TarotCard(
        id=69, index='six_of_pentacles', type='minor_arcana', orig_name='Six of Pentacles', name='星币六',
        intro='一个商人装扮的男子，脚边跪着两个乞丐。商人右手施舍其中一名乞丐，左手拿着象征平衡的天秤。',
        words='施舍',
        desc='星币六暗示没有绝对的公平，其中一人比另一人更有控制力。\n\n星币六是在形容一种结构性的关系，其中一人比另一人更有控制力。是一张有很多层面的牌，而它的意义又会随着问题或周遭的牌而改变，在这张牌中，看似公平和正当，不过，请注意，两个乞丐是跪在富翁的面前。在这个关系里，他是处于有权力的地位。星币六是在形容一种关系：一个人支配另外一个人。\n\n跪在地上的人事实上是受制于他的，暗示着局面是由他所控制，而他是透过他的财富来掌控这一切。这个站着的人深谙拥有金钱就是拥有权力。他就越能选择自己的人生。施与受中间不只是金钱，知识、经验、技术的传授也算。所以星币六也代表知识、经验、技术的传授或是学习。',
        upright='Charity, Generosity, Sharing, Community, Material help, Support, Giving and receiving, Gratitude',
        reversed='Strings attached, Stinginess, Power and domination, Power dynamics, Abuse of generosity, Strings attached gifts, Inequality, Extortion'
    ), init=False)

    seven_of_pentacles: TarotCard = field(default=TarotCard(
        id=70, index='seven_of_pentacles', type='minor_arcana', orig_name='Seven of Pentacles', name='星币七',
        intro='一位农夫把下巴架在杖上，低头看着他长久辛勤得来的收成。这丛农作物在他的耕耘下，已经可以自己成长茁壮了。农夫的表情似乎很满足，又彷佛在思考下一步该怎么做。',
        words='规划',
        desc='星币七意味着思考未来的财务或物质状况。\n\n星币七暗示目前工作即将完结，只剩下一点尾巴要收而已。经历过去长时间段孜孜不倦的努力，现在可以暂停一下，看看自己目前的成就，想想下一步的行止。星币七是一种实际面上的投资与等待，并且具有时间性，能解释出过去和未来的现象。代表过去曾经付出努力，投注了资源和精神，如今正在等待成果，未来也将有机运得到这些回收。处于一种回顾和期待的状态。\n\n星币七代表思考和计划未来的一段时间。你的生活或目前的状况尚称平稳，所以你有时间可以安静的计划未来的步骤。这可能包括进一步的学习、强调休闲、谨慎地经营现有财物，甚至再创另一种事业，以补充现有的事业。花些时间多做思考吧，因为你的决定有可能对将来产生很大的影响。',
        upright='Hard work, Perseverance, Diligence, Harvest, Rewards, Results, Growth, Progress, Patience, Planning',
        reversed='Work without results, Distractions, Lack of rewards, Unfinished work, Procrastination, Low effort, Waste, Lack of growth, Setbacks, Impatience, Lack of reward'
    ), init=False)

    eight_of_pentacles: TarotCard = field(default=TarotCard(
        id=71, index='eight_of_pentacles', type='minor_arcana', orig_name='Eight of Pentacles', name='星币八',
        intro='一位雕刻匠坐在长板凳上，专注而勤劳地刻着星币星币，他前面已经完成六个了，脚边还有一个未完成。有一条黄色的道路连接远方的市镇与雕刻匠，连接工作与社会，无论什么工作，目的都是服务人群，雕刻匠并未忘记这一点。',
        words='上进',
        desc='星币八暗示对某人或某种状况的承诺。\n\n星币八是代表工作赚钱的一张牌，也表示能够累积财富，集中心力在赚取金钱上。这是一张代表承诺并专注于眼前工作的牌，而意念当中这乃是为了较长的目标而努力。\n\n星币八暗示对一个人或一种状况的深度承诺。现在你则着重于你的技巧以及如何变得更精炼。可以透过不懈的努力，或进一步的学习让技艺更上层楼。这张牌时说你已经在群体当中找到了自己的位置，并且在做适合你做的事情。你明白工作不应该是沉闷无味的，而是一种自我完成的机会。工作不仅只是为了填满你时间、胃或口袋，更重要的是让你的人生完整。',
        upright='Apprenticeship, Passion, High standards, Skill, Talent, Craftsmanship, Quality, Expertise, Mastery, Commitment, Dedication, Accomplishment',
        reversed='Lack of passion, Uninspired, No motivation, Lack of quality, Rushed job, Bad reputation, Lack of motivation, Mediocrity, Laziness, Low skill, Dead-end job'
    ), init=False)

    nine_of_pentacles: TarotCard = field(default=TarotCard(
        id=72, index='nine_of_pentacles', type='minor_arcana', orig_name='Nine of Pentacles', name='星币九',
        intro='一位衣着华丽的女子站在她的庄园中，四周葡萄茂盛，正是收成时节。她右手扶在星币上，大拇指还扣着一根葡萄藤，左手则戴着白手套，让她的小鸟站在上面，小鸟的头部却被红布遮住了。',
        words='自律',
        desc='星币九代表收获与安逸，丰富的物质生活与相对应的束缚。\n\n星币九是一张代表自信或自我依赖的牌，那可说是要达到超凡成就的必要条件。你的自信如果在搭配上自律的话，那将使你在许多层面上获益。\n\n大体上来说，星币九形容由于过去的努力而带来的一种舒适的生活。星币九代表财富的成功与富足，显示对于生活实际投入的层面，并表达了物质与精神层面的相互关系。',
        upright='Fruits of labor, Rewards, Luxury, Rewarded efforts, Success, Achievement, Independence, Leisure, Material security, Self-sufficiency',
        reversed='Reckless spending, Living beyond means, False success, Being guarded, Material instability, Superficiality'
    ), init=False)

    ten_of_pentacles: TarotCard = field(default=TarotCard(
        id=73, index='ten_of_pentacles', type='minor_arcana', orig_name='Ten of Pentacles', name='星币十',
        intro='星币十的近景是一位老年人，他舒服的坐着，身旁围绕着两只狗。拱门外的市镇中有一对青年男女，似乎在讨论什么，还有一个小孩子。十个星币排列成生命之树的符号。',
        words='富裕',
        desc='星币十意味归于平静的物质上的成功。\n\n星币十意味物质上的成功，星币十画的是一个安稳而舒适的居家环境。从墙上盾形家徽看得出这是一个富裕而巩固的环境，这个家庭拥有能提供舒适物质环境的一切条件。那么，为什么每个人都没有面对着别人呢？这老人是坐着的，他的注意力放在动物们的身上，年轻人背对我们，而女人也没有面对他，却稍稍侧着脸继续和他谈话。小孩子被忽略了，这些人彼此之间也没有真正的关联。它们得到别人所渴望的物质世界，不过很显然这也使他们感到沉闷，并陷入公式化的生活中，一旦这种公式消失，将无所适从。\n\n星币十是整组牌可能性的充分显示。他缺乏权杖的热情、宝剑的理想以及圣杯牌的情感。在这里可以找到物质上的安全感和稳定，但也付出了代价。',
        upright='Legacy, Culmination, Inheritance, Roots, Family, Ancestry, Windfall, Foundations, Privilege, Affluence, Stability, Tradition',
        reversed='Fleeting success, Lack of stability, Lack of resources, Family disputes, Bankruptcy, Debt, Conflict over money, Instability, Breaking traditions'
    ), init=False)

    page_of_pentacles: TarotCard = field(default=TarotCard(
        id=74, index='page_of_pentacles', type='minor_arcana', orig_name='Page of Pentacles', name='星币侍从',
        intro='星币待从双脚坚稳的站立在地面上，高高捧着星币，他所着迷的东西，在眼前仔细地观察着。他头戴红色软帽头饰，带子围着肩颈。身上的穿着是以棕色为底，套着绿色的外衣，鞋子和腰带也是棕色的。他站在青葱且长满花朵的草地上，远方有茂密的树丛，画面的右下还有一座山。',
        words='勤奋',
        desc='星币侍从意味着为理想而努力学习。\n\n星币侍从象征有关金钱、新工作或学习一门课程的消息。它可以表示去学习某些将会产生实质效益的事物。这个侍从通常代表学生的勤奋向学。透过学习一门课程，或于工作中学习，发挥了自己的能力。有时候这个侍从可能暗示你对于正在学习的科目，变得更专注，甚至更重视学习的成果。',
        upright='Ambition, Desire, Diligence, Ambitious, Diligent, Goal oriented, Planner, Consistent, Star student, Studious, Grounded, Loyal, Faithful, Dependable',
        reversed='Lack of commitment, Greediness, Laziness, Foolish, Immature, Irresponsible, Lazy, Underachiever, Procrastinator, Missed chances, Poor prospects'
    ), init=False)

    knight_of_pentacles: TarotCard = field(default=TarotCard(
        id=75, index='knight_of_pentacles', type='minor_arcana', orig_name='Knight of Pentacles', name='星币骑士',
        intro='星币骑士笔直地坐在黑马背上，仔细打量手上的星币。黑色的强壮马匹配着厚实的红色马鞍和缰绳，侧面垂着红色的软坐垫，牢牢地站在地面，是四张骑士牌中唯一不动的座骑。骑士戴着头盔，头盔顶端饰有穗状的绿叶，黑马的头顶也有相同的叶穗。他身着厚重盔甲，外披一件暗红色战袍，也戴着红色的手套。星币骑士处于空旷的大地上，眼前应是一望无际。远方的地面是一片经过细心耕耘的田地，背景是一片鲜黄色。',
        words='稳健',
        desc='星币骑士代表稳健而认真的计划。\n\n星币骑士通常指的是强化你的计划，并朝确定的目标迈进。它意味着为了实现一个目标而努力工作。就一个人而言，这个人对于承诺非常的认真，不论是对事业、个人雄心或两性关系。通常，他相信这个格言：“如果你想做好一件事，那就自己动手吧。”',
        upright='Efficiency, Hard work, Responsibility, Practical, Reliable, Efficient, Stoic, Slow and steady, Hard-working, Committed, Patient, Conservative',
        reversed='Laziness, Obsessiveness, Work without reward, Workaholic, Dull, Boring, No initiative, Cheap, Irresponsible, Gambler, Risky investments'
    ), init=False)

    queen_of_pentacles: TarotCard = field(default=TarotCard(
        id=76, index='queen_of_pentacles', type='minor_arcana', orig_name='Queen of Pentacles', name='星币皇后',
        intro='星币皇后的面貌端庄而正直，双手捧着星币，并低头凝望着星币，神情若有所思。她的后冠是圆顶的，中间有插着两根红色羽毛，星币皇后的后袍是红色的，内衫露出的袖子是白色的，是红白对立的组合，绿色的披风由头上往下延伸到椅上。皇后的宝座处在长满丰盛植物的平原上，在茂密的林荫中，玫瑰花围绕成的拱门之下，所在的草地之上盛开着多株玫瑰花，。座椅是精工雕琢的，刻满了纹饰。有许多植物和天使的图案，很像圣杯皇后的座椅，扶前端有羊头的浮雕，椅侧有小孩的浮雕，椅背刻满了藤蔓瓜叶。宝座旁的近景是一片肥沃的土地，满是绿草和花朵。',
        words='安定',
        desc='星币皇后意味着喜爱大自然，又有良好的商业眼光。\n\n从一般观点来看，星币皇后是一张代表信任自己能力的牌。她意味经由深思熟虑而带来成功。作为一个人，星币皇后通常有着敏锐的生意眼光，而且总是喜欢存点钱在身边，好让自己有安全感。在有需要的时候她会很节俭，而且不会任意炫耀财富。她是一个可靠、实际的人，知道应该在那里下功夫可以得到最大的成功。\n\n这张皇后牌是指务实、可靠，并擅长喂养植物和动物。她也喜欢经常到乡间旅行，或漫步于大自然中，因为她需要和自然保持接触，让生命有完整而踏实的感觉。',
        upright='Practicality, Creature comforts, Financial security, Generous, Caring, Nurturing, Homebody, Good business sense, Practical, Comforting, Welcoming, Sensible, Luxurious',
        reversed='Self-centeredness, Jealousy, Smothering, Selfish, Unkempt, Jealous, Insecure, Greedy, Materialistic, Gold digger, Intolerant, Self-absorbed, Envious'
    ), init=False)

    king_of_pentacles: TarotCard = field(default=TarotCard(
        id=77, index='king_of_pentacles', type='minor_arcana', orig_name='King of Pentacles', name='星币国王',
        intro='星币国王悠然自得的坐在他的花园里。他的左手拿着星币，右手拿着权杖，姿态轻松。花围中长满象征丰收成果的葡萄和各种植物，他的服装也满是葡萄图案，整个人似乎与大自然融成一体。宝座上有牛头图案，是星币的家族图腾。国王的右手靠在座椅的扶手上，掌中握着宝球权柄。左手持拥五芒星金币，并垫起左脚让这枚大金币更稳定确实地置于膝上。国王慵懒地靠在椅背上，低眼安然地端详着他的金币。',
        words='坚定',
        desc='星币国王表示务实而坚定的态度可以带来成功。\n\n星币国王暗示透过身体力行而达到成功。它也可以说是务实的努力带来物质上的成功。星币国王代表的是一个脚踏实地而又成熟的人。他的个性稳健、可靠且保守，并能努力履行其承诺，谨慎的负起他应负的责任。他不像权杖国王般富冒险精神，或像圣杯国王那么有创意，但他可凭藉着慢慢而稳定的步伐，以及认真的实践来达到成功。',
        upright='Abundance, Prosperity, Security, Ambitious, Safe, Kind, Patriarchal, Protective, Businessman, Provider, Sensual, Reliable',
        reversed='Greed, Indulgence, Sensuality, Materialistic, Wasteful, Chauvanist, Poor financial decisions, Gambler, Exploitative, Possessive'
    ), init=False)


class TarotPacks(object):
    """
    定义套牌
    """
    SpecialCard: TarotPack = TarotPack(
        name='special',
        cards=[card for card in TarotCards.get_all_cards() if card.type == 'special'])

    MajorArcana: TarotPack = TarotPack(
        name='major_arcana',
        cards=[card for card in TarotCards.get_all_cards() if card.type == 'major_arcana'])

    MinorArcana: TarotPack = TarotPack(
        name='minor_arcana',
        cards=[card for card in TarotCards.get_all_cards() if card.type == 'minor_arcana'])

    RiderWaite: TarotPack = TarotPack(
        name='rider_waite',
        cards=[card for card in TarotCards.get_all_cards() if (
                card.type == 'major_arcana' or card.type == 'minor_arcana')])


__all__ = [
    'TarotCards',
    'TarotPacks'
]
