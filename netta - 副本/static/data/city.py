# coding:utf-8
# _author_:Junjie
# date:2019/4/8
city = {'中国': {'北京': ['东城', '西城', '朝阳', '丰台', '石景山', '海淀', '门头沟', '房山', '通州', '顺义', '昌平', '大兴', '平谷', '怀柔', '密云', '延庆'], '天津': ['和平', '河东', '河西', '南开', '河北', '红桥', '滨海新区', '东丽', '西青', '津南', '北辰', '宁河', '武清', '静海', '宝坻', '蓟县'], '河北': ['石家庄', '唐山', '秦皇岛', '邯郸', '邢台', '保定', '张家口', '承德', '沧州', '廊坊', '衡水'], '山西': ['太原', '大同', '阳泉', '长治', '晋城', '朔州', '晋中', '运城', '忻州', '临汾', '吕梁'], '内蒙古': ['呼和浩特', '包头', '乌海', '赤峰', '通辽', '鄂尔多斯', '呼伦贝尔', '巴彦淖尔', '乌兰察布', '兴安', '锡林郭勒', '阿拉善'], '辽宁': ['沈阳', '大连', '鞍山', '抚顺', '本溪', '丹东', '锦州', '营口', '阜新', '辽阳', '盘锦', '铁岭', '朝阳', '葫芦岛'], '吉林': ['长春', '吉林', '四平', '辽源', '通化', '白山', '松原', '白城', '延边'], '黑龙江': ['哈尔滨', '齐齐哈尔', '鸡西', '鹤岗', '双鸭山', '大庆', '伊春', '佳木斯', '七台河', '牡丹江', '黑河', '绥化', '大兴安岭'], '上海': ['黄浦', '卢湾', '徐汇', '长宁', '静安', '普陀', '闸北', '虹口', '杨浦', '闵行', '宝山', '嘉定', '浦东新区', '金山', '松江', '奉贤', '青浦', '崇明'], '江苏': ['南京', '无锡', '徐州', '常州', '苏州', '南通', '连云港', '淮安', '盐城', '扬州', '镇江', '泰州', '宿迁'], '浙江': ['杭州', '宁波', '温州', '嘉兴', '湖州', '绍兴', '金华', '衢州', '舟山', '台州', '丽水'], '安徽': ['合肥', '芜湖', '蚌埠', '淮南', '马鞍山', '淮北', '铜陵', '安庆', '黄山', '滁州', '阜阳', '宿州', '六安', '亳州', '池州', '宣城'], '福建': ['福州', '厦门', '莆田', '三明', '泉州', '漳州', '南平', '龙岩', '宁德'], '江西': ['南昌', '景德镇', '萍乡', '九江', '新余', '鹰潭', '赣州', '吉安', '宜春', '抚州', '上饶'], '山东': ['济南', '青岛', '淄博', '枣庄', '东营', '烟台', '潍坊', '济宁', '泰安', '威海', '日照', '莱芜', '临沂', '德州', '聊城', '滨州', '菏泽'], '河南': ['郑州', '开封', '洛阳', '平顶山', '安阳', '鹤壁', '新乡', '焦作', '濮阳', '许昌', '漯河', '三门峡', '南阳', '商丘', '信阳', '周口', '驻马店', '济源'], '湖北': ['武汉', '黄石', '十堰', '宜昌', '襄阳', '鄂州', '荆门', '孝感', '荆州', '黄冈', '咸宁', '随州', '恩施', '仙桃', '潜江', '天门', '神农架'], '湖南': ['长沙', '株洲', '湘潭', '衡阳', '邵阳', '岳阳', '常德', '张家界', '益阳', '郴州', '永州', '怀化', '娄底', '湘西'], '广东': ['广州', '韶关', '深圳', '珠海', '汕头', '佛山', '江门', '湛江', '茂名', '肇庆', '惠州', '梅州', '汕尾', '河源', '阳江', '清远', '东莞', '中山', '潮州', '揭阳', '云浮'], '广西': ['南宁', '柳州', '桂林', '梧州', '北海', '防城港', '钦州', '贵港', '玉林', '百色', '贺州', '河池', '来宾', '崇左'], '海南': ['海口', '三亚', '三沙', '五指山', '琼海', '儋州', '文昌', '万宁', '东方', '定安', '屯昌', '澄迈', '临高', '白沙', '昌江', '乐东', '陵水', '保亭', '琼中'], '重庆': ['万州', '涪陵', '渝中', '大渡口', '江北', '沙坪坝', '九龙坡', '南岸', '北碚', '两江新区', '万盛', '双桥', '渝北', '巴南', '长寿', '綦江', '潼南', '铜梁', '大足', '荣昌', '璧山', '梁平', '城口', '丰都', '垫江', '武隆', '忠县', '开县', '云阳', '奉节', '巫山', '巫溪', '黔江', '石柱', '秀山', '酉阳', '彭水', '江津', '合川', '永川', '南川'], '四川': ['成都', '自贡', '攀枝花', '泸州', '德阳', '绵阳', '广元', '遂宁', '内江', '乐山', '南充', '眉山', '宜宾', '广安', '达州', '雅安', '巴中', '资阳', '阿坝', '甘孜', '凉山'], '贵州': ['贵阳', '六盘水', '遵义', '安顺', '铜仁', '黔西南', '毕节', '黔东南', '黔南'], '云南': ['昆明', '曲靖', '玉溪', '保山', '昭通', '丽江', '普洱', '临沧', '楚雄', '红河', '文山', '西双版纳', '大理', '德宏', '怒江', '迪庆'], '西藏': ['拉萨', '昌都', '山南', '日喀则', '那曲', '阿里', '林芝'], '陕西': ['西安', '铜川', '宝鸡', '咸阳', '渭南', '延安', '汉中', '榆林', '安康', '商洛'], '甘肃': ['兰州市', '嘉峪关', '金昌', '白银', '天水', '武威', '张掖', '平凉', '酒泉', '庆阳', '定西', '陇南', '临夏', '甘南'], '青海': ['西宁', '海东', '海北', '黄南', '海南', '果洛', '玉树', '海西'], '宁夏': ['银川', '石嘴山', '吴忠', '固原', '中卫'], '新疆': ['乌鲁木齐', '克拉玛依', '吐鲁番', '哈密', '昌吉', '博尔塔拉', '巴音郭楞', '阿克苏', '克孜勒苏', '喀什', '和田', '伊犁', '塔城', '阿勒泰', '石河子', '阿拉尔', '图木舒克', '五家渠', '北屯'], '台湾': ['台北市', '高雄市', '基隆市', '台中市', '台南市', '新竹市', '嘉义市', '台北县', '宜兰县', '桃园县', '新竹县', '苗栗县', '台中县', '彰化县', '南投县', '云林县', '嘉义县', '台南县', '高雄县', '屏东县', '台东县', '花莲县', '澎湖县'], '香港': ['中西区', '东区', '九龙城区', '观塘区', '南区', '深水埗区', '黄大仙区', '湾仔区', '油尖旺区', '离岛区', '葵青区', '北区', '西贡区', '沙田区', '屯门区', '大埔区', '荃湾区', '元朗区'], '澳门': ['花地玛堂区', '圣安多尼堂区', '大堂区', '望德堂区', '风顺堂区', '氹仔', '路环']}, '阿尔巴尼亚': ['爱尔巴桑', '迪勃拉', '地拉那', '都拉斯', '发罗拉', '费里', '吉诺卡斯特', '科尔察', '库克斯', '莱什', '培拉特', '斯库台'], '阿尔及利亚': ['阿德拉尔', '阿尔及尔', '艾因·德夫拉', '艾因·蒂姆尚特', '安纳巴', '奥兰', '巴特纳', '贝贾亚', '贝沙尔', '贝伊德', '比斯克拉', '布尔吉·布阿雷里吉', '布利达', '布迈德斯', '布依拉', '蒂巴扎', '蒂斯姆西勒特', '盖尔达耶', '盖尔马', '罕西拉', '赫利赞', '吉杰尔', '杰勒法', '君士坦丁', '拉格瓦特', '马斯卡拉', '麦迪亚', '密拉', '莫斯塔加纳姆', '姆西拉', '纳阿马', '塞蒂夫', '赛伊达', '斯基克达', '苏克·阿赫拉斯', '塔里夫', '塔曼拉塞特', '特贝萨', '特莱姆森', '提济乌祖', '提亚雷特', '廷杜夫', '瓦德', '瓦尔格拉', '乌姆布阿基', '西迪贝勒阿贝斯', '谢里夫', '伊利齐'], '阿富汗': ['赫拉特', '喀布尔', '坎大哈', '马扎里沙里夫'], '阿根廷': ['巴拉那', '别德马', '波萨达斯', '布兰卡港', '布宜诺斯艾利斯', '福莫萨', '胡胡伊', '卡塔马卡', '科尔多瓦', '科连特斯', '克劳斯城', '肯考迪娅', '拉里奥哈', '拉普拉塔', '雷西斯滕匹亚', '里奥加耶戈斯', '里奥夸尔托', '里瓦达维亚海军准将城', '罗萨里奥', '罗森', '马德普拉塔', '门多萨', '内乌肯', '萨尔塔', '圣地亚哥-德尔埃斯特罗', '圣菲', '圣胡安', '圣拉斐尔', '圣路易斯', '圣罗莎', '圣米格尔-德图库曼', '圣尼古拉斯', '特雷利乌', '乌斯怀亚'], '阿拉伯联合酋长国': ['阿布扎比', '艾因', '迪拜', '沙迦'], '阿鲁巴': {}, '阿曼': ['巴提奈地区', '达希莱地区', '东部地区', '马斯喀特省', '穆桑达姆省', '内地地区', '中部地区', '佐法尔省'], '阿塞拜疆': ['阿布歇隆', '哈奇马斯', '卡尔巴卡尔', '卡扎赫', '连科兰', '密尔-卡拉巴赫', '穆甘-萨连', '纳戈尔诺－卡拉巴赫', '纳希切万', '普利亚拉克斯', '舍基', '苏姆盖特', '锡尔万', '占贾'], '阿森松岛': {}, '埃及': ['阿斯旺', '古尔代盖', '开罗', '苏布拉开马', '亚历山大'], '埃塞俄比亚': ['阿法尔', '阿姆哈拉', '奥罗米亚', '宾香古尔', '德雷达瓦', '甘贝拉各族', '哈勒里民族', '南方各族', '索马里', '提格雷', '亚的斯亚贝巴'], '爱尔兰': ['奥法利', '蒂珀雷里', '都柏林', '多内加尔', '戈尔韦', '基尔代尔', '基尔肯尼', '卡范', '卡洛', '凯里', '科克', '克莱尔', '朗福德', '劳斯', '崂斯', '利默里克', '利特里姆', '罗斯康芒', '梅奥', '米斯', '莫内根', '斯莱戈', '威克洛', '韦克斯福德', '沃特福德', '西米斯'], '爱沙尼亚': ['贝尔瓦', '哈留', '拉普拉', '里亚内', '帕尔努', '萨雷', '塔尔图', '瓦尔加', '维良地', '维鲁', '沃鲁', '希尤', '耶尔韦', '耶盖瓦', '依达－维鲁'], '安道尔': ['安道尔城', '奥尔迪诺', '恩坎普', '卡尼略', '莱塞斯卡尔德－恩戈尔达', '马萨纳', '圣胡利娅－德洛里亚'], '安哥拉': ['北宽扎', '北隆达', '本戈', '本格拉', '比耶', '卡宾达', '库内内', '宽多库邦戈', '罗安达', '马兰热', '莫希科', '纳米贝', '南宽扎', '南隆达', '万博', '威拉', '威热', '扎伊尔'], '安圭拉': {}, '安提瓜岛和巴布达': {}, '澳大利亚': {'北部地区': ['北帕默斯顿', '达尔文'], '堪培拉': ['堪培拉'], '昆士兰': ['布里斯班', '黄金海岸', '凯恩斯', '日光海岸', '汤斯维尔', '图文巴'], '南澳大利亚': ['阿德莱德', '奥古斯塔港', '甘比亚山', '怀阿拉', '林肯港', '默里布里奇', '皮里港', '维克托港'], '塔斯马尼亚': ['伯尼港', '德文波特', '霍巴特', '朗塞斯顿'], '维多利亚': ['吉朗', '墨尔本'], '西澳大利亚': ['奥尔巴尼', '班伯里', '弗里曼特尔港', '杰拉尔顿', '卡尔古利', '曼哲拉', '珀斯'], '新南威尔士': ['纽卡斯尔', '伍伦贡', '悉尼']}, '奥地利': ['布尔根兰', '蒂罗尔', '福拉尔贝格', '克恩顿', '萨尔茨堡', '上奥地利', '施蒂利亚', '维也纳', '下奥地利'], '奥兰群岛': {}, '巴巴多斯岛': {}, '巴布亚新几内亚': ['北部', '布干维尔', '东部高地', '东塞皮克', '东新不列颠', '恩加', '海湾', '马当', '马努斯', '米尔恩湾', '莫尔兹比港', '莫罗贝', '南部高地', '钦布', '桑道恩', '西部', '西部高地', '西新不列颠', '新爱尔兰'], '巴哈马': {}, '巴基斯坦': ['白沙瓦', '费萨拉巴德', '故吉软瓦拉', '海德拉巴', '卡拉奇', '拉合尔', '拉瓦尔品第', '木尔坦', '伊斯兰堡'], '巴拉圭': ['阿曼拜', '阿耶斯总统省', '巴拉瓜里', '博克龙', '瓜伊拉', '卡瓜苏', '卡嫩迪尤', '卡萨帕', '康塞普西翁', '科迪勒拉', '米西奥内斯', '涅恩布库', '上巴拉圭', '上巴拉那', '圣佩德罗', '亚松森特别区', '伊塔普亚', '中央'], '巴勒斯坦': ['加沙地带', '西岸'], '巴林': ['北部', '哈德', '哈马德', '里法', '麦纳麦', '穆哈拉格', '西部', '伊萨城', '中部'], '巴拿马': {}, '巴西': ['阿克里', '阿拉戈斯', '阿马帕', '巴拉那', '巴西利亚', '巴伊亚', '北里奥格兰德', '伯南布哥', '戈亚斯', '朗多尼亚', '里约热内卢', '罗赖马', '马拉尼昂', '马托格罗索', '米纳斯吉拉斯', '南里奥格兰德', '南马托格罗索', '帕拉', '帕拉伊巴', '皮奥伊', '塞阿拉', '塞尔希培', '圣埃斯皮里图', '圣保罗', '圣卡塔琳娜', '托坎廷斯', '亚马孙'], '白俄罗斯': ['布列斯特', '戈梅利', '格罗德诺', '明斯克市', '莫吉廖夫', '维捷布斯克'], '百慕大': {}, '保加利亚': ['布尔加斯', '卡斯科伏', '鲁塞', '洛维奇', '蒙塔纳', '普罗夫迪夫', '索非亚', '索非亚市', '瓦尔纳'], '北马里亚纳群岛': {}, '贝宁': ['阿黎博里', '阿塔科拉', '滨海', '波希康市', '博尔古', '大西洋', '高原', '库福', '莫诺', '丘陵', '韦梅', '峡谷', '祖'], '比利时': ['埃诺', '安特卫普', '布拉班特-瓦隆', '布鲁塞尔', '东佛兰德', '佛兰芒-布拉班特', '列日', '林堡', '卢森堡', '那慕尔', '西佛兰德'], '冰岛': {}, '波多黎各': {}, '波兰': ['埃尔布隆格', '奥尔什丁', '奥斯特罗文卡', '比得哥什', '彼得库夫', '比托姆', '比亚瓦波德拉斯卡', '比亚维斯托克', '波莱', '波兹南', '达布罗瓦戈尼察', '大波兰地区戈茹夫', '弗罗茨瓦夫', '弗沃茨瓦韦克', '格但斯克', '格丁尼亚', '格利维采', '格鲁琼兹', '海乌姆', '华沙', '霍茹夫', '卡利什', '卡托维兹', '凯尔采', '科宁', '科沙林', '克拉科夫', '克罗斯诺', '拉多姆', '莱格尼察', '莱什诺', '卢布林', '鲁达', '罗兹', '绿山城', '米什洛维采', '皮瓦', '普热梅希尔', '普沃茨克', '切哈努夫', '热舒夫', '什切青', '斯凯尔涅维采', '斯武普斯克', '苏瓦乌基', '索波特', '索斯诺维茨', '塔尔努夫', '塔尔诺布热格', '特切', '托伦', '瓦乌布日赫', '沃姆扎', '希米亚诺维采', '希维诺乌伊希切', '希维托赫洛维采', '谢德尔采', '谢拉兹', '新松奇', '雅沃兹诺', '耶莱尼亚古拉', '扎布热', '扎莫希奇'], '玻利维亚': ['奥尔托', '奥鲁罗', '贝尼', '波多西', '基拉科洛', '科恰班巴', '拉巴斯', '潘多', '丘基萨卡', '萨卡巴', '圣克鲁斯', '塔里哈'], '波斯尼亚和黑塞哥维那': ['波萨维纳', '波斯尼亚－波德里涅', '多米斯拉夫格勒', '黑塞哥维那－涅雷特瓦', '萨拉热窝', '图兹拉－波德里涅', '乌纳－萨纳', '西波斯尼亚', '西黑塞哥维那', '泽尼察－多博伊', '中波斯尼亚'], '博茨瓦纳': {}, '伯利兹': ['伯利兹', '橘园', '卡约', '科罗萨尔', '斯坦港', '托莱多'], '不丹': {}, '布基纳法索': ['巴雷', '巴姆', '巴瓦', '巴泽加', '波尼', '布尔古', '布尔基恩德', '布古里巴', '冈祖尔古', '古尔马', '济罗', '卡焦戈', '凯内杜古', '科蒙加里', '科莫埃', '孔皮恩加', '孔西', '库尔佩罗戈', '库尔维奥戈', '库里滕加', '雷拉巴', '罗卢姆', '穆翁', '纳门滕加', '纳乌里', '纳亚拉', '尼亚尼亚', '努姆比埃尔', '帕索雷', '塞诺', '桑吉', '桑马滕加', '苏鲁', '苏姆', '塔波阿', '图伊', '乌埃', '乌布里滕加', '乌达兰', '锡西里', '亚加', '亚滕加', '伊奥巴', '宗德韦奥戈', '宗多马'], '布隆迪': ['布班扎', '布鲁里', '布琼布拉城市', '布琼布拉乡村', '恩戈齐', '基龙多', '基特加', '卡鲁济', '卡扬扎', '坎库佐', '鲁塔纳', '鲁伊吉', '马坎巴', '穆拉姆维亚', '穆瓦洛', '穆因加', '锡比托凯'], '布韦岛': {}, '朝鲜': ['海州', '惠山', '江界', '开城', '罗先', '南浦', '平壤', '清津', '沙里院', '咸兴', '新义州', '元山'], '丹麦': ['奥胡斯', '北日德兰', '博恩霍尔姆', '菲特烈堡', '菲茵', '哥本哈根', '里伯', '灵克宾', '罗斯基勒', '南日德兰', '斯多斯特姆', '维堡', '维厄勒', '西希兰'], '德国': ['阿恩斯贝格', '爱尔福特', '安斯巴格', '奥格斯堡', '柏林', '拜伊罗特', '比勒费尔德', '波茨坦', '波鸿', '不来梅', '不伦瑞克', '达姆施塔特', '代特莫尔特', '德累斯顿', '德绍', '杜塞尔多夫', '法兰克福', '弗赖堡', '哈雷', '汉堡', '汉诺威', '基尔', '吉森', '卡尔斯鲁厄', '卡塞尔', '开姆尼斯', '科布伦次', '科隆', '莱比锡', '兰茨胡特', '吕讷堡', '马格德堡', '曼海姆', '美因兹', '明斯特', '慕尼黑', '纽伦堡', '什未林', '斯图加特', '特里尔', '威斯巴登', '维尔茨堡'], '东帝汶': ['阿伊莱乌', '阿伊纳罗', '埃尔梅拉', '安贝诺', '包考', '博博纳罗', '帝力', '科瓦利马', '劳滕', '利基卡', '马纳图托', '马努法伊', '维克克'], '多哥': ['滨海区', '草原区', '高原区', '卡拉区', '中部区'], '多米尼加': {}, '多米尼加共和国': {}, '俄罗斯': ['阿巴坎', '阿尔汉格尔斯克', '阿金斯科耶', '阿纳德尔', '阿斯特拉罕', '埃利斯塔', '奥廖尔', '奥伦堡', '巴尔瑙尔', '奔萨', '彼得罗巴甫洛夫斯克', '彼得罗扎沃茨克', '彼尔姆', '比罗比詹', '别尔哥罗德', '伯力', '布拉戈维申斯克', '布良斯克', '车里雅宾斯克', '赤塔', '顿河畔罗斯托夫', '鄂木斯克', '伏尔加格勒', '弗拉基米尔', '弗拉季高加索', '戈尔诺－阿尔泰斯克', '格罗兹尼', '海参崴', '汉特－曼西斯克', '基洛夫', '加里宁格勒', '喀山', '卡卢加', '科斯特罗马', '克拉斯诺达尔', '克拉斯诺亚尔斯克', '克麦罗沃', '克孜勒', '库德姆卡尔', '库尔干', '库尔斯克', '利佩茨克', '梁赞', '马哈奇卡拉', '马加丹', '马加斯', '迈科普', '摩尔曼斯克', '莫斯科', '纳尔奇克', '纳里扬马尔', '南萨哈林斯克', '诺夫哥罗德', '帕拉纳', '普斯科夫', '切博克萨雷', '切尔克斯克', '秋明', '萨拉托夫', '萨兰斯克', '萨列哈尔德', '萨马拉', '瑟克特夫卡尔', '圣彼得堡', '斯摩棱斯克', '斯塔夫罗波尔', '坦波夫', '特维尔', '图拉', '托木斯克', '沃罗涅什', '沃洛格达', '乌法', '乌兰乌德', '乌里扬诺夫斯克', '乌斯季奥尔登斯基', '下诺夫哥罗德', '新西伯利亚', '雅库茨克', '雅罗斯拉夫尔', '叶卡捷林堡', '伊尔库茨克', '伊热夫斯克', '伊万诺沃', '约什卡尔奥拉'], '厄瓜多尔': ['阿苏艾', '埃尔奥罗', '埃斯梅拉尔达斯', '玻利瓦尔', '瓜亚斯', '加拉帕戈斯', '卡尔奇', '卡尼亚尔', '科托帕希', '洛哈', '洛斯里奥斯', '马纳比', '莫罗纳－圣地亚哥', '纳波，奥雷利亚纳', '帕斯塔萨', '皮钦查', '钦博拉索', '萨莫拉－钦奇佩', '苏昆毕奥斯', '通古拉瓦', '因巴布拉'], '厄立特里亚': ['安塞巴', '北红海', '加什·巴尔卡', '南部', '南红海', '中部'], '法国': ['阿尔勒', '阿雅克修', '艾克斯', '奥尔良', '巴黎', '贝桑松', '第戎', '弗雷瑞斯', '卡昂', '雷恩', '里昂', '里尔', '利摩日', '鲁昂', '马赛', '梅斯', '蒙彼利埃', '南特', '尼斯', '沙隆', '图卢兹', '瓦朗斯', '亚眠'], '法罗群岛': {}, '法属波利尼西亚': {}, '法属圭亚那': {}, '法属南部领地': {}, '梵蒂冈': {}, '菲律宾': ['达沃', '卡卢坎', '马尼拉', '宿务'], '斐济': {}, '芬兰': ['埃斯波', '奥卢', '波里', '博尔沃', '海门林纳', '赫尔辛基', '卡亚尼', '科科拉', '科特卡', '库奥皮奥', '拉赫蒂', '拉彭兰塔', '罗瓦涅米', '玛丽港', '米凯利', '坦佩雷', '图尔库', '瓦萨', '万塔', '约恩苏'], '佛得角': ['保尔', '波多诺伏', '博阿维斯塔岛', '布拉瓦岛', '大里贝拉', '福古岛', '马尤岛', '莫斯特罗', '普拉亚', '萨尔岛', '圣安唐岛', '圣地亚哥岛', '圣多明戈', '圣菲利普', '圣卡塔琳娜', '圣克鲁斯', '圣米戈尔', '圣尼古拉岛', '圣维森特岛', '塔拉法尔'], '弗兰克群岛': {}, '冈比亚': {}, '刚果': {}, '刚果民主共和国': {}, '哥伦比亚': ['阿劳卡', '安提奥基亚', '北桑坦德', '波哥大首都区', '博利瓦尔', '博亚卡', '大西洋', '瓜维亚雷', '瓜希拉', '瓜伊尼亚', '金迪奥', '卡尔达斯', '卡克塔', '卡萨纳雷', '考卡', '考卡山谷', '科尔多巴', '昆迪纳马卡', '利萨拉尔达', '马格达雷那', '梅塔', '纳里尼奥', '普图马约', '乔科', '塞萨尔', '桑坦德', '圣安德烈斯-普罗维登西亚', '苏克雷', '托利马', '维查达', '沃佩斯', '乌伊拉', '亚马孙'], '哥斯达黎加': ['阿拉胡埃拉', '埃雷迪亚', '瓜纳卡斯特', '卡塔戈', '利蒙', '蓬塔雷纳斯', '圣何塞'], '格恩西岛': {}, '格林纳达': {}, '格陵兰': {}, '古巴': ['奥尔金', '比那尔德里奥', '比亚克拉拉', '格拉玛', '关塔那摩', '哈瓦那', '哈瓦那城', '卡马圭', '拉斯图纳斯', '马坦萨斯', '马亚里', '曼萨尼罗', '青年岛特区', '圣地亚哥', '圣斯皮里图斯', '西恩富戈斯', '谢戈德阿维拉'], '瓜德罗普': {}, '关岛': {}, '圭亚那': ['埃塞奎博群岛-西德梅拉拉', '巴里马-瓦伊尼', '波默伦-苏佩纳姆', '波塔罗-锡帕鲁尼', '德梅拉拉-马海卡', '东伯比斯-科兰太因', '库尤尼-马扎鲁尼', '马海卡-伯比斯', '上德梅拉拉-伯比斯', '上塔库图-上埃塞奎博'], '哈萨克斯坦': ['阿尔卡累克', '阿克莫拉', '阿克苏', '阿克托别', '阿拉木图', '阿雷斯', '阿斯塔纳市', '阿特劳', '埃基巴斯图兹', '巴尔喀什', '巴甫洛达尔', '北哈萨克斯坦', '东哈萨克斯坦', '济良诺夫斯克', '江布尔', '杰兹卡兹甘', '卡拉干达', '卡拉扎尔', '卡普恰盖', '科斯塔奈', '克孜勒奥尔达', '肯套', '库尔恰托夫', '利萨科夫斯克', '列宁诺戈尔斯克', '鲁德内', '曼格斯套', '南哈萨克斯坦', '萨兰', '塞梅伊', '沙赫京斯克', '斯捷普诺戈尔斯克', '铁克利', '铁米尔套', '突厥斯坦', '西哈萨克斯坦', '扎纳奥津'], '海地': {}, '韩国': {'大邱': ['达城郡', '大邱', '寿城区'], '大田': [], '釜山': [], '光州': [], '济州特别自治道': [], '江原道': ['春川市', '东海市', '高城郡', '横城郡', '洪川郡', '华川郡', '江陵市', '旌善郡', '麟蹄郡', '宁越郡', '平昌郡', '三陟市', '束草市', '太白市', '铁原郡', '襄阳郡', '杨口郡', '原州市'], '京畿道': ['安城市', '安山市', '安养市', '抱川市', '城南市', '东豆川市', '富川市', '高阳市', '光明市', '广州市', '果川市', '河南市', '华城市', '加平郡', '金浦市', '九里市', '军浦市', '骊州郡', '利川市', '涟川郡', '龙仁市', '南杨州市', '平泽市', '坡州市', '始兴市', '水原市', '乌山市', '扬平郡', '杨州市', '仪旺市', '议政府市'], '庆尚北道': ['安东市', '奉化郡', '高灵郡', '龟尾市', '金泉市', '军威郡', '醴泉郡', '浦项市', '漆谷郡', '淸道郡', '靑松郡', '庆山市', '庆州市', '荣州市', '尙州市', '蔚珍郡', '闻庆市', '星州郡', '义城郡', '英阳郡', '盈德郡', '永川市', '郁陵郡'], '庆尚南道': ['昌宁郡', '昌原市', '固城郡', '河东郡', '金海市', '晋州市', '居昌郡', '巨济市', '梁山市', '马山市', '密阳市', '南海郡', '山淸郡', '泗川市', '统营市', '陜川郡', '咸安郡', '咸阳郡', '宜宁郡', '鎭海市'], '全罗北道': ['淳昌郡', '扶安郡', '高敞郡', '金堤市', '井邑市', '茂朱郡', '南原市', '全州市', '群山市', '任实郡', '完州郡', '益山市', '长水郡', '鎭安郡'], '全罗南道': ['宝城郡', '高兴郡', '谷城郡', '莞岛郡', '光阳市', '海南郡', '和顺郡', '康津郡', '丽水市', '灵光郡', '灵岩郡', '罗州市', '木浦市', '求礼郡', '顺天市', '潭阳郡', '务安郡', '咸平郡', '新安郡', '长城郡', '长兴郡', '珍岛郡'], '仁川': [], '首尔': [], '蔚山': [], '忠清北道': ['报恩郡', '曾坪郡', '丹阳郡', '堤川市', '槐山郡', '淸原郡', '淸州市', '沃川郡', '阴城郡', '永同郡', '鎭川郡', '忠州市'], '忠清南道': ['保宁市', '扶余郡', '公州市', '洪城郡', '鸡龙市', '锦山郡', '礼山郡', '论山市', '青阳郡', '瑞山市', '舒川郡', '泰安郡', '唐津郡', '天安市', '牙山市', '燕岐郡']}, '荷兰': ['阿尔梅勒', '阿默斯福特', '阿姆斯特丹', '阿纳姆', '阿珀尔多伦', '阿森', '埃德', '埃门', '埃因霍芬', '布雷达', '蒂尔堡', '多德雷赫特', '恩斯赫德', '格罗宁根', '哈勒姆', '海牙', '霍夫多尔普', '莱顿', '莱利斯塔德', '鹿特丹', '吕伐登', '马斯特里赫特', '米德尔堡', '奈梅亨', '斯海尔托亨博思', '乌得勒支', '兹沃勒', '佐特尔梅'], '荷属安地列斯': {}, '赫德和麦克唐纳群岛': {}, '洪都拉斯': ['阿特兰蒂达', '埃尔帕拉伊索', '奥科特佩克', '奥兰乔', '弗朗西斯科-莫拉桑', '格拉西亚斯-阿迪奥斯', '海湾群岛', '科尔特斯', '科隆', '科马亚瓜', '科潘', '拉巴斯', '伦皮拉', '乔卢特卡', '乔罗马', '山谷', '圣巴巴拉', '因蒂布卡', '约罗'], '基里巴斯': ['菲尼克斯群岛', '吉尔伯特群岛', '莱恩群岛'], '吉布提': ['阿里萨比赫区', '奥博克区', '迪基勒区', '塔朱拉区'], '吉尔吉斯斯坦': ['奥什', '巴特肯', '比什凯克市', '楚河', '贾拉拉巴德', '卡拉巴尔塔', '卡拉库尔', '坎特', '科克扬加克', '迈利赛', '纳伦', '苏卢克图', '塔拉斯', '塔什库梅尔', '乌兹根', '伊塞克湖'], '几内亚': ['博凯', '恩泽雷科雷', '法拉纳', '金迪亚', '康康', '科纳克里', '拉贝', '玛木'], '几内亚比绍': {}, '加拿大': ['阿伯茨福', '埃德蒙顿', '奥沙瓦', '巴里', '布列塔尼角', '多伦多', '弗雷德里顿', '圭尔夫', '哈利法克斯', '哈密尔顿', '怀特霍斯', '基劳纳', '基奇纳', '金斯敦', '卡里加里', '魁北克', '里贾纳', '伦敦', '蒙特利尔', '萨德伯里', '萨斯卡通', '三河城', '桑德贝', '舍布鲁克', '圣卡塔琳娜', '圣约翰斯', '维多利亚', '温哥华', '温尼伯', '温莎', '渥太华', '夏洛特敦', '耶洛奈夫', '伊魁特'], '加纳': ['阿散蒂', '奥布阿西', '北部', '布朗阿哈福', '大阿克拉', '东部', '上东部', '上西部', '沃尔特', '西部', '中部'], '加蓬': ['奥果韦-洛洛', '奥果韦-伊温多', '滨海奥果韦', '恩古涅', '河口', '尼扬加', '上奥果韦', '沃勒-恩特姆', '中奥果韦'], '柬埔寨': ['奥多棉吉', '白马市', '柏威夏', '拜林市', '班迭棉吉', '磅清扬', '磅士卑', '磅同', '磅湛', '波罗勉', '茶胶', '柴桢', '干丹', '戈公', '贡布', '金边市', '桔井', '腊塔纳基里', '马德望', '蒙多基里', '菩萨', '上丁', '西哈努克市', '暹粒'], '捷克共和国': ['奥洛穆茨', '比尔森', '布拉格直辖市', '赫拉德茨-克拉洛韦', '卡罗维发利', '利贝雷克', '摩拉维亚-西里西亚', '南摩拉维亚', '帕尔杜比采', '维索基纳', '乌斯季', '中捷克', '兹林'], '津巴布韦': ['北马塔贝莱兰', '布拉瓦约', '东马绍纳兰', '哈拉雷', '马尼卡兰', '马斯温戈', '南马塔贝莱兰', '西马绍纳兰', '中部', '中马绍纳兰'], '喀麦隆': ['阿达马瓦', '北部', '北端', '滨海', '东部', '南部', '西北', '西部', '西南', '中央'], '卡塔尔': ['北部', '多哈', '古韦里耶', '豪尔', '杰里扬拜特奈', '赖扬', '沃克拉', '乌姆锡拉勒', '朱迈利耶'], '开曼群岛': {}, '科科斯群岛': {}, '科摩罗': {}, '科特迪瓦': ['阿涅比', '巴芬', '邦达马河谷', '登盖莱', '恩济－科莫埃', '弗罗马格尔', '湖泊', '马拉韦', '南邦达马', '南科莫埃', '萨桑德拉', '萨瓦纳', '山地', '沃罗杜古', '下萨桑德拉', '泻湖', '赞赞', '中卡瓦利', '中科莫埃'], '科威特': {}, '克罗地亚': ['奥西耶克-巴拉尼亚', '别洛瓦尔-比洛戈拉', '滨海和山区', '波热加-斯拉沃尼亚', '布罗德-波萨维纳', '杜布罗夫斯克-内雷特瓦', '卡尔洛瓦茨', '科普里夫尼察-克里热夫齐', '克拉皮纳-扎戈列', '利卡-塞尼', '梅吉穆列', '萨格勒布', '萨格勒布市', '斯普利特-达尔马提亚', '瓦拉日丁', '维罗维蒂察-波德拉维纳', '武科瓦尔-斯里耶姆', '希贝尼克-克宁', '锡萨克-莫斯拉维纳', '伊斯特拉', '扎达尔'], '肯尼亚': ['埃尔格约-马拉奎特', '巴林戈', '邦戈马', '博美特', '布希亚', '恩布', '霍马湾', '基安布', '基里菲', '基里尼亚加', '基苏木', '基图伊', '基西', '加里萨', '卡卡梅加', '卡耶亚多', '凯里乔', '夸勒', '拉木', '莱基皮亚', '马查科斯', '马瓜尼', '马萨布布', '曼德拉', '梅鲁', '蒙巴萨', '米戈利', '穆兰卡', '纳库鲁', '纳罗克', '南迪', '内罗毕', '尼蒂', '尼亚米拉', '年达鲁阿', '涅里', '桑布卢', '塔纳河', '泰塔塔维塔', '特兰斯-恩佐亚', '图尔卡纳', '瓦吉尔', '瓦辛基苏', '韦希加', '西波克特', '夏亚', '伊希约洛', '中央'], '库克群岛': {}, '拉脱维亚': ['阿卢克斯内', '爱兹克劳克雷', '奥格雷', '巴尔维', '包斯卡', '采西斯', '多贝莱', '古尔贝内', '杰卡布皮尔斯', '克拉斯拉瓦', '库尔迪加', '雷泽克内', '里加', '利耶帕亚', '林巴济', '卢扎', '马多纳', '普雷利', '萨尔杜斯', '塔尔西', '陶格夫皮尔斯', '图库马', '瓦尔加', '瓦尔米耶拉', '文茨皮尔斯', '叶尔加瓦'], '莱索托': ['伯里亚', '布塔布泰', '古廷', '加查斯内克', '莱里贝', '马费滕', '马塞卢', '莫哈莱斯胡克', '莫霍特隆', '塔巴采卡'], '老挝': ['阿速坡', '波里坎赛', '博乔', '川圹', '丰沙里', '甘蒙', '华潘', '琅勃拉邦', '琅南塔', '赛宋本行政特区', '色贡', '沙拉湾', '沙湾拿吉', '沙耶武里', '万象', '乌多姆赛', '占巴塞'], '黎巴嫩': ['北部', '贝卡', '贝鲁特', '黎巴嫩山', '奈拜提耶市', '南部'], '利比里亚': ['巴波卢', '邦', '博波卢', '博米', '大巴萨', '大吉德', '大角山', '大克鲁', '菲什敦', '吉河', '里弗塞斯', '洛法', '马吉比', '马里兰', '蒙特塞拉多', '宁巴', '锡诺'], '利比亚': {}, '立陶宛': ['阿利图斯', '考纳斯', '克莱佩达', '马里扬泊列', '帕涅韦日斯', '陶拉格', '特尔希艾', '维尔纽斯', '乌田纳', '希奥利艾', '亚克曼'], '列支敦士登': {}, '留尼旺岛': {}, '卢森堡': ['迪基希', '格雷文马赫', '卢森堡'], '卢旺达': ['比温巴', '布塔雷', '恩延扎', '基本古', '基布耶', '基加利-恩加利', '基加利市', '吉孔戈罗', '吉塞尼', '吉塔拉马', '卡布加', '卢瓦马加纳', '鲁汉戈', '鲁亨盖里', '尚古古', '乌姆塔拉'], '罗马尼亚': ['阿尔巴尤利亚', '阿拉德', '奥拉迪亚', '巴克乌', '巴亚马雷', '比斯特里察', '博托沙尼', '布加勒斯特', '布拉索夫', '布勒伊拉', '布泽乌', '德罗贝塔-塞维林堡', '德瓦', '蒂米什瓦拉', '福克沙尼', '加拉茨', '久尔久', '康斯坦察', '克拉约瓦', '克勒拉希', '克卢日纳波卡', '勒姆尼库沃尔恰', '雷希察', '梅尔库里亚丘克', '皮特什蒂', '皮亚特拉尼亚姆茨', '普洛耶什蒂', '萨图·马雷', '圣格奥尔基', '斯拉蒂纳', '斯洛博齐亚', '苏恰瓦', '特尔戈维什泰', '特尔古穆列什', '特尔古日乌', '图尔恰', '瓦斯卢伊', '锡比乌', '雅西', '亚厉山德里亚', '扎勒乌'], '马达加斯加': ['安齐拉纳纳', '菲亚纳兰楚阿', '马哈赞加', '塔那那利佛', '图阿马西拉', '图利亚拉'], '马尔代夫': ['阿杜', '北阿里', '北蒂拉杜马蒂', '北马洛斯马杜卢', '北米拉杜马杜卢', '北尼兰杜', '北苏瓦迪瓦', '法迪福卢', '费利杜', '福阿穆拉库', '哈杜马蒂', '科卢马杜卢', '马累', '马累岛', '穆拉库', '南阿里', '南蒂拉杜马蒂', '南马洛斯马杜卢', '南米拉杜马杜卢', '南尼兰杜', '南苏瓦迪瓦'], '马耳他': {}, '马拉维': ['北部区', '南部区', '中央区'], '马来西亚': {'槟榔屿': ['北海', '槟城', '大山脚', '高渊'], '玻璃市': ['加央'], '丁加奴': ['甘马挽', '瓜拉丁加奴', '龙运', '马江', '实兆', '乌鲁', '勿述'], '吉打': ['巴东得腊', '笨筒', '浮罗交怡', '哥打士打', '古邦巴素', '瓜拉姆达', '华玲', '居林', '万拉峇鲁'], '吉兰丹': ['巴西富地', '巴西马', '丹那美拉', '道北', '登卓', '哥打巴鲁', '瓜拉吉赖', '话望生', '马樟', '日里'], '吉隆坡': ['吉隆坡'], '马六甲': ['马六甲市', '亚罗牙也', '野新'], '纳闽': ['纳闽', '维多利亚'], '彭亨': ['百乐', '北根', '淡马鲁', '而连突', '关丹', '金马仑高原', '劳勿', '立卑', '马兰', '文冬', '云冰'], '霹雳': ['安顺', '丹绒马', '和丰', '紅土坎', '华都牙也', '江沙', '太平', '怡保'], '柔佛': ['笨珍', '丰盛港', '哥打丁宜', '居銮', '峇株巴辖', '麻坡', '昔加末', '新山'], '森美兰': ['波德申', '淡边', '芙蓉', '瓜拉庇劳', '林茂', '仁保', '日叻务'], '沙巴': ['吧巴', '保佛', '比鲁兰', '必达士', '兵南邦', '担布南', '丹南', '斗湖', '斗亚兰', '哥打基纳巴鲁', '哥打马鲁都', '根地咬', '古达', '古打毛律', '古纳', '瓜拉班尤', '京那巴登岸', '兰脑', '拿笃', '纳巴湾', '山打根', '西比陶', '仙本那'], '沙捞越': ['古晋', '加帛', '林梦', '美里', '民都鲁', '木胶', '木中', '三马拉汉', '斯里阿曼', '泗里街', '泗务'], '雪兰莪': ['八打灵', '鹅麦', '瓜拉冷岳', '瓜拉雪兰莪', '沙白安南', '乌鲁冷岳', '乌鲁雪兰莪', '雪邦']}, '马里': ['巴马科首都区', '基达尔', '加奥', '卡伊', '库利科罗', '莫普提', '塞古', '通布图', '锡卡索'], '马其顿': {}, '马绍尔群岛': {}, '马提尼克': {}, '马约特岛': {}, '曼岛': {}, '毛里求斯': {}, '毛里塔尼亚': ['阿德拉尔', '阿萨巴', '卜拉克纳', '东胡德', '戈尔戈勒', '吉迪马卡', '努瓦迪布湾', '努瓦克肖特特区', '塔甘特', '特拉扎', '提里斯-宰穆尔', '西胡德', '因希里'], '美国': {'阿肯色': ['费耶特维尔', '史密斯堡', '小石城'], '阿拉巴马': ['伯明罕', '蒙哥马利', '莫比尔'], '阿拉斯加': ['安克雷奇', '费尔班克斯', '朱诺'], '爱达荷': ['爱达荷福尔斯', '波卡特洛', '博伊西', '布莱克富特', '科达伦', '刘易斯顿', '莫斯科', '墨菲', '楠帕', '岂彻姆', '森瓦利', '亚美利加瀑布城'], '爱荷华': ['达文波特', '得梅因', '锡达拉皮兹'], '北达科他': ['俾斯麦', '大福克斯', '法戈', '迈诺特'], '北卡罗来纳': ['艾许维尔', '杜罕', '格林斯伯勒', '教堂山', '罗利', '洛利杜罕都会区', '夏洛特'], '宾夕法尼亚': ['阿伦敦', '费城', '匹兹堡'], '德克萨斯': ['埃尔帕索', '奥斯汀', '达拉斯', '哥帕斯基斯蒂', '交维斯顿', '拉雷多', '麦亚伦', '圣安东尼奥', '休斯敦'], '俄亥俄': ['代顿', '哥伦布', '克利夫兰', '托莱多', '辛辛那提'], '俄克拉荷马': ['俄克拉荷马城', '诺曼', '塔尔萨'], '俄勒冈': ['本德', '波特兰', '达尔斯', '达拉斯', '蒂拉穆克', '格兰茨帕斯', '胡德里弗', '火山口湖', '科瓦利斯', '库斯贝', '梅德福', '塞勒姆', '圣海伦斯', '斯普林菲尔德', '尤金'], '佛罗里达': ['奥兰多', '基韦斯特', '杰克逊维尔', '卡纳维尔角', '罗德岱堡', '迈阿密', '圣彼德斯堡市', '塔拉哈西', '坦帕'], '佛蒙特': ['伯灵顿', '拉特兰', '南伯灵顿'], '哥伦比亚特区': ['华盛顿哥伦比亚特区'], '华盛顿': ['斯波坎', '塔科马', '西雅图'], '怀俄明': ['埃文斯顿', '卡斯珀', '拉勒米', '罗克斯普林斯', '夏延', '谢里登'], '加利福尼亚': ['旧金山', '洛杉矶', '圣迭戈', '圣何塞'], '堪萨斯': ['阿比林', '奥弗兰公园', '哈钦森', '堪萨斯城', '莱文沃思', '劳伦斯', '曼哈顿', '托皮卡', '威奇托'], '康涅狄格': ['布里奇波特', '达里恩', '格林尼治', '哈特福德', '米德尔顿', '纽黑文', '韦斯特波特', '沃特伯里', '新不列颠'], '科罗拉多': ['阿斯彭', '奥罗拉', '博尔德', '大章克申', '丹佛', '柯林斯堡', '科罗拉多斯普林斯', '韦尔'], '肯塔基': ['列克星敦', '路易斯维尔', '欧文斯伯勒'], '路易斯安那': ['巴吞鲁日', '什里夫波特', '新奥尔良'], '罗德岛': ['波塔基特', '克兰斯顿', '纽波特', '普罗维登斯', '韦斯特利', '文索基特', '沃威克'], '马里兰': ['巴尔的摩', '盖瑟斯堡', '罗克维尔'], '马萨诸塞': ['波士顿', '斯普林菲尔德', '伍斯特'], '蒙大拿': ['比灵斯', '大瀑布村', '米苏拉'], '密苏里': ['哥伦比亚', '杰佛逊市', '堪萨斯城', '圣路易斯', '斯普林菲尔德'], '密西西比': ['比洛克西', '格尔夫波特', '格林维尔', '哈蒂斯堡', '杰克逊', '默里迪恩', '维克斯堡'], '密歇根': ['安娜堡', '巴特尔克里克', '贝城', '大急流城', '迪尔伯恩', '底特律', '弗林特', '怀恩多特', '卡拉马袓', '兰辛', '马斯基根', '庞菷亚克', '萨吉诺', '苏圣玛丽', '沃伦', '休伦港'], '缅因': ['班戈', '波特兰', '刘易斯顿'], '明尼苏达': ['罗切斯特', '明尼阿波利斯', '圣保罗'], '南达科他': ['阿伯丁', '拉皮德城', '苏福尔斯'], '南卡罗来纳': ['北查尔斯顿', '查尔斯顿', '哥伦比亚'], '内布拉斯加': ['奥马哈', '贝尔维尤', '林肯'], '内华达': ['埃尔科', '北拉斯维加斯', '弗吉尼亚城', '亨德森', '卡森城', '拉斯维加斯', '里诺', '斯帕克斯'], '纽约': ['布法罗', '罗切斯特', '纽约市'], '特拉华': ['多佛', '纽瓦克', '威明顿'], '田纳西': ['布利斯托', '查塔努加', '金斯波特', '孟菲斯', '纳什维尔', '诺克斯维尔', '三城区', '士麦那', '斯普林希尔', '约翰逊城'], '威斯康星': ['阿普尓顿', '奥什科什', '格林贝', '基诺沙', '拉克罗斯', '拉辛', '马尼托沃克', '迈迪逊', '密尔沃基', '欧克莱尓', '沃索', '希博伊根'], '维吉尼亚': ['弗吉尼亚比奇', '诺福克', '切萨皮克'], '西佛吉尼亚': ['查尔斯顿', '亨廷顿', '帕克斯堡'], '夏威夷': ['凯卢阿', '檀香山', '希洛'], '新罕布什尔': ['康科德', '曼彻斯特', '纳舒厄'], '新墨西哥': ['阿尔伯克基', '拉斯克鲁塞斯', '罗斯韦尔', '圣菲'], '新泽西': ['纽瓦克', '帕特森', '泽西城'], '亚利桑那': ['凤凰城', '格兰代尔', '梅萨', '史卡兹代尔', '坦普', '图森', '优玛'], '伊利诺斯': ['奥尔顿', '奥罗拉', '布卢明顿', '丹维尓', '迪卡尔布', '迪凯持', '东圣路易斯', '厄巴纳-香槟', '盖尔斯堡', '卡本代尔', '罗克艾兰', '罗克福德', '诺黙尔', '皮奥里亚', '森特勒利亚', '斯普林菲尔德', '沃其根', '芝加哥'], '印第安那': ['埃文斯维尔', '韦恩堡', '印第安纳波利斯'], '犹他': ['奥格登', '雷登', '欧仁', '帕克城', '普罗沃', '圣乔治', '西瓦利城', '盐湖城'], '佐治亚': ['奥古斯塔', '哥伦布', '梅肯', '沙瓦纳', '亚特兰大']}, '美属萨摩亚': ['阿纳', '阿图阿', '艾加伊勒泰', '法塞莱莱阿加', '加盖福毛加', '加加埃毛加', '帕劳利', '萨图帕伊泰阿', '萨瓦伊岛', '图阿马萨加', '瓦奥福诺蒂', '韦西加诺', '乌波卢岛'], '美属外岛': {}, '蒙古': ['巴彦洪格尔', '巴彦乌勒盖', '布尔干', '达尔汗乌勒', '东方', '东戈壁', '鄂尔浑', '戈壁阿尔泰', '戈壁苏木贝尔', '后杭爱', '科布多', '肯特', '库苏古尔', '南戈壁', '前杭爱', '色楞格', '苏赫巴托尔', '乌布苏', '乌兰巴托市', '扎布汗', '中戈壁', '中央'], '蒙特塞拉特': {}, '孟加拉': ['达卡', '吉大港', '库尔纳'], '密克罗尼西亚': {}, '秘鲁': ['阿雷基帕', '阿普里马克', '阿亚库乔', '安卡什', '胡利亚卡', '胡宁', '卡哈马卡', '卡亚俄', '库斯科', '拉利伯塔德', '兰巴耶克', '利马', '洛雷托', '马德雷德迪奥斯', '莫克瓜', '帕斯科', '皮乌拉', '普诺', '钦博特', '钦查阿尔塔', '圣马丁', '苏拉纳', '塔克纳', '通贝斯', '瓦努科', '万卡维利卡', '乌卡亚利', '亚马孙', '伊卡'], '缅甸': ['勃固省', '掸邦', '德林达依省', '克伦邦', '克钦邦', '克耶邦', '马圭省', '曼德勒省', '孟邦', '钦邦', '若开邦', '实皆省', '仰光省', '伊洛瓦底省'], '摩尔多瓦': {}, '摩洛哥': ['丹吉尔', '得土安', '非斯', '卡萨布兰卡', '拉巴特', '马拉喀什', '梅克内斯', '乌季达', '西撒哈拉'], '摩纳哥': {}, '莫桑比克': {}, '墨西哥': ['阿瓜斯卡连斯特', '阿卡普尔科', '埃莫西约', '埃佩切', '奥夫雷贡城', '奥里萨巴', '巴利城', '巴亚尔塔港', '比利亚埃尔莫萨', '波萨里卡', '蒂华纳', '杜兰戈', '恩塞纳达', '瓜达拉哈拉', '瓜纳华托', '哈拉帕', '华雷斯', '华雷斯港', '卡门', '科利马', '克雷塔罗', '库埃纳瓦卡', '库利阿坎', '夸察夸拉克斯', '拉巴斯', '莱昂', '雷诺萨', '洛斯莫奇斯', '马萨特兰', '马塔莫罗斯', '梅里达', '蒙克洛瓦', '蒙特雷', '莫雷利亚', '墨西哥城', '墨西卡利', '诺加莱斯', '帕丘卡', '普埃布拉', '奇尔潘辛戈', '奇瓦瓦', '切图马尔', '萨尔蒂约', '萨卡特卡斯', '塞拉亚', '圣路易斯波托亚', '塔帕丘拉', '坦皮科', '特拉斯卡拉', '特皮克', '特瓦坎', '图斯特拉-古铁雷斯', '托雷翁', '托卢卡', '瓦哈卡', '维多利亚城', '韦拉克鲁斯', '乌鲁阿潘', '新拉雷多', '伊拉普阿托'], '纳米比亚': ['埃龙戈', '奥汉圭纳', '奥卡万戈', '奥马赫科', '奥姆沙蒂', '奥乔宗蒂约巴', '奥沙纳', '奥希科托', '哈达普', '霍马斯', '卡拉斯', '卡普里维', '库内内'], '南非': ['阿平顿', '艾利弗山', '彼德马里茨堡', '彼德斯堡', '比勒陀利亚', '比索', '布雷达斯多普', '布隆方丹', '布隆克斯特斯普利特', '德阿尔', '德班', '邓迪', '东巴克利', '东伦敦', '弗雷堡', '弗里尼欣', '格罗布莱斯达尔', '基雅尼', '金伯利', '开普敦', '克莱克斯多普', '库鲁曼', '昆士敦', '莱迪史密斯', '兰德方丹', '理查兹湾', '利斯滕堡', '米德尔堡', '姆库泽', '穆里斯堡', '内尔斯普雷特', '尼尔斯特隆', '纽卡斯尔', '乔治', '萨索尔堡', '瑟孔达', '特克索波', '特隆普斯堡', '跳羚', '图拉马哈谢', '托霍延杜', '韦茨肖克', '韦尔科姆', '乌伦迪', '乌姆塔塔', '伍斯特', '西博福特', '谢普斯通港', '伊丽莎白港', '约翰内斯堡'], '南极洲': {}, '南乔治亚和南桑德威奇群岛': {}, '瑙鲁': {}, '尼泊尔': ['巴格马蒂', '道拉吉里', '甘达基', '戈西', '格尔纳利', '贾纳克布尔', '拉布蒂', '蓝毗尼', '马哈卡利', '梅吉', '纳拉亚尼', '佩里', '萨加玛塔', '塞蒂'], '尼加拉瓜': ['埃斯特利', '北大西洋', '博阿科', '格拉纳达', '卡拉索', '莱昂', '里瓦斯', '马德里斯', '马那瓜', '马萨亚', '马塔加尔帕', '南大西洋', '奇南德加', '琼塔莱斯', '圣胡安河', '希诺特加', '新塞哥维亚'], '尼日尔': ['阿加德兹', '迪法', '蒂拉贝里', '多索', '津德尔', '马拉迪', '尼亚美市', '塔瓦'], '尼日利亚': ['阿比亚', '奥博莫绍', '卡诺', '拉各斯', '伊巴丹'], '纽埃': {}, '挪威': ['阿克什胡斯', '奥普兰', '奥斯陆市', '北特伦德拉格', '布斯克吕', '东阿格德尔', '东福尔', '芬马克', '海德马克', '霍达兰', '罗加兰', '默勒－鲁姆斯达尔', '南特伦德拉格', '诺尔兰', '松恩－菲尤拉讷', '泰勒马克', '特罗姆斯', '西阿格德尔', '西福尔'], '诺福克': {}, '帕劳群岛': {}, '皮特凯恩': {}, '葡萄牙': ['滨海阿连特茹', '滨海皮尼亚尔', '波尔图', '杜罗', '恩特拉杜罗伏日', '法鲁', '丰沙尔', '卡瓦多', '科瓦贝拉', '里斯本', '利巴特茹', '梅地奥特茹', '米尼奥-利马', '内贝拉北', '内贝拉南', '内皮尼亚尔北', '内皮尼亚尔南', '蓬塔德尔加达', '塞图巴尔半岛', '山后', '上阿连特茹', '上特拉斯山', '塔梅加', '万福', '西部', '下阿连特茹', '下伏日', '下蒙德古', '中阿连特茹'], '乔治亚': {}, '日本': ['爱媛', '爱知', '北海道', '兵库', '冲绳', '茨城', '大阪', '大分', '岛根', '徳岛', '东京', '福岛', '福冈', '福井', '富山', '冈山', '高知', '宮城', '宫崎', '广岛', '和歌山', '京都', '静冈', '枥木', '鹿儿岛', '奈良', '鸟取', '岐阜', '埼玉', '千叶', '青森', '秋田', '群马', '三重', '山口', '山梨', '山形', '神奈川', '石川', '香川', '新潟', '熊本', '岩手', '长崎', '长野', '滋贺', '佐贺'], '瑞典': ['北博滕', '布莱金厄', '达拉纳', '东约特兰', '厄勒布鲁', '哥得兰', '哈兰', '卡尔马', '克鲁努贝里', '南曼兰', '斯德哥尔摩', '斯科耐', '韦姆兰', '乌普萨拉', '西博滕', '西曼兰', '西诺尔兰', '西约特兰', '延雪平', '耶夫勒堡', '耶姆特兰'], '瑞士': ['阿尔高', '巴塞尔城市', '巴塞尔乡村', '伯尔尼', '楚格', '弗里堡', '格拉鲁斯', '格劳宾登', '卢塞恩', '洛桑', '纳沙泰尔', '内阿彭策尔', '日内瓦', '汝拉', '沙夫豪森', '上瓦尔登', '圣加仑', '施维茨', '苏黎世', '索洛图恩', '提契诺', '图尔高', '瓦莱', '外阿彭策尔', '沃', '乌里', '下瓦尔登'], '萨尔瓦多': ['阿波帕', '阿瓦查潘', '滨海', '查拉特南戈', '德尔加多', '基埃-恩特姆', '卡瓦尼亚斯', '库斯卡特兰', '拉巴斯', '拉利伯塔德', '拉乌尼翁', '梅基卡诺斯', '莫拉桑', '圣安娜', '圣米格尔', '圣萨尔瓦多', '圣维森特', '松索纳特', '索亚潘戈', '韦莱-恩萨斯', '乌苏卢坦', '伊洛潘戈', '中南'], '萨摩亚': {}, '塞尔维亚,黑山': ['贝尔格莱德', '波德戈里察', '克拉古涅瓦茨', '尼什', '诺维萨德', '普里什蒂纳', '苏博蒂察', '泽蒙'], '塞拉利昂': ['北部', '东部', '南部', '西部区'], '塞内加尔': ['达喀尔', '法蒂克', '济金绍尔', '捷斯', '久尔贝勒', '考拉克', '科尔达', '卢加', '马塔姆', '圣路易', '坦巴昆达'], '塞浦路斯': ['法马古斯塔', '凯里尼亚', '拉纳卡', '利马索尔', '尼科西亚', '帕福斯'], '塞舌尔': {}, '沙特阿拉伯': ['阿尔阿尔', '艾卜哈', '巴哈', '布赖代', '达曼', '哈费尔巴廷', '哈伊勒', '海米斯穆谢特', '海耶', '胡富夫', '吉达', '吉赞', '利雅得', '麦地那', '麦加', '姆巴拉兹', '纳季兰', '塞卡卡', '塔布克', '塔伊夫', '延布', '朱拜勒'], '圣诞岛': {}, '圣多美和普林西比': {}, '圣赫勒拿': {}, '圣基茨和尼维斯': {}, '圣卢西亚': {}, '圣马力诺': {}, '圣皮埃尔和米克隆群岛': {}, '圣文森特和格林纳丁斯': {}, '斯里兰卡': ['阿努拉德普勒', '安帕赖', '巴杜勒', '拜蒂克洛', '波隆纳鲁沃', '汉班托特', '基里诺奇', '加勒', '加姆珀哈', '贾夫纳', '卡卢特勒', '凯格勒', '康提', '科伦坡', '库鲁内格勒', '拉特纳普勒', '马纳尔', '马特莱', '马特勒', '莫讷勒格勒', '穆莱蒂武', '努沃勒埃利耶', '普塔勒姆', '亭可马里', '瓦武尼亚'], '斯洛伐克': ['班斯卡-比斯特里察', '布拉迪斯拉发', '科希策', '尼特拉', '普雷绍夫', '日利纳', '特尔纳瓦', '特伦钦'], '斯洛文尼亚': ['奥巴尔诺-克拉', '奥斯雷德涅斯洛文', '波德拉夫', '波穆尔', '多雷尼', '戈雷尼', '戈里', '科洛', '诺特拉尼', '萨维尼', '斯波德涅波萨夫', '扎萨夫'], '斯瓦尔巴和扬马廷': {}, '斯威士兰': {}, '苏丹': ['北部', '赤道', '达尔富尔', '东部', '加扎勒河', '喀土穆', '科尔多凡', '上尼罗', '中部'], '苏里南': ['布罗科蓬多', '科罗尼', '科默韦讷', '马罗韦讷', '尼克里', '帕拉', '帕拉马里博', '萨拉马卡', '瓦尼卡', '西帕里韦尼'], '所罗门群岛': ['瓜达尔卡纳尔', '霍尼亚拉', '拉纳尔和贝罗纳', '马基拉', '马莱塔', '乔伊索', '泰莫图', '西部', '伊萨贝尔', '中部群岛'], '索马里': {}, '塔吉克斯坦': ['杜尚别', '霍罗格', '卡尼巴达姆', '科法尔尼洪', '苦盏', '库尔干-秋别', '库洛布', '洛贡', '努雷克', '彭吉肯特', '萨班特', '塔博沙尔', '图尔孙扎德', '乌拉秋别', '伊斯法拉'], '泰国': ['安纳乍能', '巴蜀', '巴吞他尼', '巴真', '北碧', '北标', '北大年', '北揽', '北榄坡', '北柳', '碧差汶', '博达伦', '猜那', '猜也奔', '程逸', '春蓬', '春武里', '达', '达叻', '大城', '董里', '佛丕', '佛统', '甘烹碧', '红统', '华富里', '加拉信', '甲米', '尖竹汶', '孔敬', '拉农', '廊开', '廊莫那浦', '叻丕', '黎', '黎逸', '龙仔厝', '罗勇', '洛坤', '玛哈沙拉堪', '曼谷', '莫达汉', '那空那育', '那空帕农', '难', '南奔', '暖武里', '帕', '帕尧', '攀牙', '彭世洛', '披集', '普吉', '清莱', '清迈', '色军', '沙敦', '沙缴', '四色菊', '宋卡', '素可泰', '素叻', '素林', '素攀武里', '陶公', '乌隆', '乌泰他尼', '乌汶', '武里南', '信武里', '耶梭通', '也拉', '夜丰颂', '夜功'], '坦桑尼亚': ['阿鲁沙', '奔巴北', '奔巴南', '滨海', '达累斯萨拉姆', '多多马', '基戈马', '卡盖拉', '林迪', '鲁夸', '鲁伍马', '马腊', '曼亚拉', '莫洛戈罗', '姆贝亚', '姆特瓦拉', '姆万扎', '乞力马扎罗', '桑给巴尔', '桑给巴尔北', '桑给巴尔南', '桑给巴尔市和西', '塔波拉', '坦噶', '辛吉达', '欣延加', '伊林加'], '汤加': ['埃瓦', '哈派', '纽阿斯', '汤加塔布', '瓦瓦乌'], '特克斯和凯克特斯群岛': {}, '特里斯坦达昆哈': {}, '特立尼达和多巴哥': {}, '突尼斯': ['艾尔亚奈', '巴杰', '本阿鲁斯', '比塞大', '吉比利', '加贝斯', '加夫萨', '坚杜拜', '卡夫', '卡塞林', '凯鲁万', '马赫迪耶', '马努巴', '梅德宁', '莫纳斯提尔', '纳布勒', '斯法克斯', '苏塞', '泰塔温', '突尼斯', '托泽尔', '西迪布济德', '锡勒亚奈', '宰格万'], '图瓦卢': {}, '土耳其': ['阿达纳', '阿德亚曼', '阿尔达罕', '阿尔特温', '阿菲永', '阿克萨赖', '阿勒', '阿马西亚', '埃迪尔内', '埃尔津詹', '埃尔祖鲁姆', '埃拉泽', '埃斯基谢希尔', '艾登', '安卡拉', '安塔利亚', '奥尔杜', '巴尔腾', '巴勒克埃西尔', '巴特曼', '巴伊布尔特', '比莱吉克', '比特利斯', '宾格尔', '博卢', '布尔杜尔', '布尔萨', '昌克勒', '代尼兹利', '迪亚巴克尔', '凡', '哈卡里', '哈塔伊', '基利斯', '吉雷松', '加济安泰普', '居米什哈内', '卡尔斯', '卡赫拉曼马拉什', '卡拉比克', '卡拉曼', '卡斯塔莫努', '开塞利', '科贾埃利', '柯克拉雷利', '科尼亚', '克尔谢希尔', '克勒克卡莱', '拉飞', '里泽', '马尔丁', '马拉蒂亚', '马尼萨', '穆拉', '穆什', '内夫谢希尔', '尼代', '恰纳卡莱', '乔鲁姆', '屈塔希亚', '萨卡里亚', '萨姆松', '泰基尔达', '特拉布宗', '通杰利', '托卡特', '乌萨克', '锡尔纳克', '锡尔特', '锡诺普', '锡瓦斯', '伊迪尔', '伊切尔', '伊斯帕尔塔', '伊斯坦布尔', '伊兹密尔', '约兹加特', '宗古尔达克'], '土库曼斯坦': ['阿哈尔', '阿什哈巴德市', '巴尔坎', '达沙古兹', '列巴普', '马雷', '涅比特达格'], '托克劳': {}, '瓦利斯和福图纳': {}, '瓦努阿图': ['马朗帕', '彭纳马', '桑马', '塔菲阿', '托尔巴', '谢法'], '危地马拉': ['埃尔普罗格雷索', '埃斯昆特拉', '哈拉帕', '胡蒂亚帕', '基切', '克萨尔特南戈', '雷塔卢莱乌', '米克斯科', '佩滕', '奇基穆拉', '奇马尔特南戈', '萨卡帕', '萨卡特佩克斯', '上韦拉帕斯', '圣罗莎', '圣马科斯', '苏奇特佩克斯', '索洛拉', '托托尼卡潘', '危地马拉', '韦韦特南戈', '下韦拉帕斯', '新城', '伊萨瓦尔'], '维尔京群岛，美属': {}, '维尔京群岛，英属': {}, '委内瑞拉': ['阿拉瓜', '阿马库罗三角洲', '阿普雷', '安索阿特吉', '巴里纳斯', '玻利瓦尔', '波图格萨', '法尔孔', '瓜里科', '加拉加斯', '卡拉沃沃', '科赫德斯', '拉腊', '联邦属地', '梅里达', '米兰达', '莫纳加斯', '苏克雷', '苏利亚', '塔奇拉', '特鲁希略', '新埃斯帕塔', '亚拉奎', '亚马孙'], '文莱': {}, '乌干达': ['阿鲁阿', '阿帕克', '阿朱马尼', '本迪布焦', '布吉里', '布西亚', '布谢尼', '恩通加莫', '古卢', '霍伊马', '基巴莱', '基博加', '基恩乔乔', '基索罗', '基特古姆', '金贾', '卡巴莱', '卡巴罗莱', '卡贝拉马伊多', '卡兰加拉', '卡姆文盖', '卡穆利', '卡农古', '卡普乔鲁瓦', '卡塞塞', '卡塔奎', '卡永加', '坎帕拉', '科蒂多', '库米', '拉卡伊', '利拉', '卢韦罗', '鲁昆吉里', '马萨卡', '马辛迪', '马尤盖', '莫罗托', '莫约', '姆巴拉拉', '姆巴莱', '姆皮吉', '穆本德', '穆科诺', '纳卡皮里皮里特', '纳卡松戈拉', '内比', '帕德尔', '帕利萨', '森巴布莱', '索罗提', '托罗罗', '瓦基索', '锡龙科', '伊甘加', '永贝'], '乌克兰': ['敖德萨', '波尔塔瓦', '第聂伯罗波得罗夫斯克', '顿涅茨克', '哈尔科夫', '赫尔松州', '赫梅利尼茨基', '基辅', '基洛夫格勒', '捷尔诺波尔', '克里米亚自治共和国', '利沃夫', '卢甘斯克', '罗夫诺', '尼古拉耶夫', '切尔卡瑟', '切尔尼戈夫', '切尔诺夫策', '日托米尔', '苏梅', '外喀尔巴阡', '文尼察', '沃伦', '伊万－弗兰科夫州', '扎波罗热'], '乌拉圭': ['阿蒂加斯', '杜拉斯诺', '佛罗里达', '弗洛雷斯', '卡内洛内斯', '科洛尼亚', '拉瓦耶哈', '里韦拉', '罗恰', '马尔多纳多', '蒙得维的亚', '内格罗河', '派桑杜', '萨尔托', '塞罗拉尔戈', '三十三人', '圣何塞', '索里亚诺', '塔夸伦博'], '乌兹别克斯坦': ['安集延', '布哈拉', '费尔干纳', '花拉子模', '吉扎克', '卡拉卡尔帕克斯坦共和国', '卡什卡达里亚', '纳曼干', '纳沃伊', '撒马尔罕', '苏尔汉河', '塔什干', '塔什干市', '锡尔河'], '西班牙': ['阿尔梅里亚', '阿尔瓦塞特', '阿拉瓦', '阿利坎特', '阿斯图利亚斯', '阿维拉', '奥伦塞', '巴达霍斯', '巴利阿里', '巴利亚多利德', '巴伦西亚', '巴塞罗那', '比斯开', '布尔戈斯', '格拉纳达', '瓜达拉哈拉', '哈恩', '赫罗纳', '吉普斯夸', '加的斯', '卡塞雷斯', '卡斯蒂利亚', '卡斯特利翁', '科尔多瓦', '昆卡', '拉科鲁尼亚', '拉里奥哈', '拉斯帕尔马斯', '莱昂', '莱里达', '卢戈', '马德里', '马拉加', '穆尔西亚', '纳瓦拉', '帕伦西亚', '蓬特韦德拉', '萨拉戈萨', '萨拉曼卡', '萨莫拉', '塞哥维亚', '塞维利亚', '桑坦德', '圣克鲁斯-德特内里费', '索里亚', '塔拉戈纳', '特鲁埃尔', '托莱多', '韦尔瓦', '韦斯卡'], '希腊': ['比雷埃夫斯', '多德卡尼斯', '干尼亚', '基克拉迪', '拉西锡', '莱斯博斯', '雷西姆农', '萨摩斯', '雅典', '伊拉克里翁'], '新加坡': {}, '新喀里多尼亚': {}, '新西兰': ['奥克兰', '北岸', '北帕默斯顿', '北远', '布莱尼姆', '达尼丁', '格雷茅斯', '哈密尔顿', '黑斯廷斯', '怀塔科拉', '吉斯伯恩', '凯帕拉', '克赖斯特彻奇', '里士满', '马努考', '纳尔逊', '内皮尔', '斯特拉特福德', '陶马鲁努伊', '瓦卡塔尼', '旺阿雷', '旺格努伊', '新普利茅斯', '因弗卡吉尔'], '匈牙利': ['巴兰尼亚', '巴奇-基什孔', '包尔绍德-奥包乌伊-曾普伦', '贝凯什', '布达佩斯', '费耶尔', '豪伊杜-比豪尔', '赫维什', '加兹-纳杰孔-索尔诺克', '杰尔-莫松-肖普朗', '科马罗姆', '诺格拉德', '佩斯', '琼格拉德', '绍莫吉', '索博尔奇-索特马尔-贝拉格', '托尔瑙', '维斯普雷姆', '沃什', '佐洛'], '叙利亚': ['阿勒颇', '大马士革', '大马士革市', '代尔祖尔', '德拉', '哈马', '哈塞克', '霍姆斯', '加布', '卡米什利', '库奈特拉', '拉卡', '拉塔基亚', '苏韦达', '塔尔图斯', '伊德利卜'], '牙买加': ['波特兰', '汉诺威', '金斯敦', '克拉伦登', '曼彻斯特', '圣安德鲁斯', '圣安娜', '圣凯瑟琳', '圣玛丽', '圣托马斯', '圣伊丽莎白', '圣詹姆斯', '特里洛尼', '西摩兰'], '亚美尼亚': ['阿尔马维尔', '阿拉加措特恩', '阿拉拉特', '埃里温市', '格加尔库尼克', '科泰克', '洛里', '塔武什', '瓦约茨·佐尔', '希拉克', '休尼克'], '也门': ['阿比扬', '阿姆兰', '贝达', '达利', '哈德拉毛', '哈杰', '荷台达', '焦夫', '拉赫季', '马里卜', '迈赫拉', '迈赫维特', '萨达', '萨那', '赛文', '舍卜沃', '塔伊兹', '希赫尔', '亚丁', '伊卜', '扎玛尔'], '伊拉克': {}, '伊朗': {}, '以色列': ['阿什杜德', '贝尔谢巴', '贝特雁', '海法', '霍隆', '内坦亚', '特拉维夫', '耶路撒冷'], '意大利': ['阿斯蒂', '阿斯科利皮切诺', '安科纳', '奥尔比亚', '奥里斯塔诺', '奥斯塔', '巴勒莫', '巴里', '贝加莫', '贝内文托', '比萨', '波代诺内', '波坦察', '博洛尼亚', '布拉', '布雷西亚', '布林迪西', '的里雅斯特', '都灵', '费拉拉', '佛罗伦萨', '福贾', '卡利亚里', '卡塞塔', '卡塔尼亚', '卡坦扎罗', '坎波巴索', '科摩', '科森扎', '克罗托内', '库内奥', '拉奎拉', '拉斯佩齐亚', '莱科', '莱切', '雷焦艾米利亚', '雷焦卡拉布里亚', '里窝那', '罗马', '马萨', '马泰拉', '蒙扎', '米兰', '摩德纳', '墨西拿', '那不勒斯', '努奥罗', '诺瓦拉', '帕尔马', '帕维亚', '佩鲁贾', '热那亚', '萨莱诺', '萨萨里', '萨沃纳', '塔兰托', '特拉帕尼', '特伦托', '威尼斯', '韦尔切利', '维泰博', '乌迪内', '锡拉库扎', '锡耶纳', '亚历山德里亚', '伊塞尔尼亚'], '印度': ['艾藻尔', '班加罗尔', '本地治里', '博帕尔', '布巴内斯瓦尔', '昌迪加尔', '达曼', '第乌', '甘托克', '哥印拜陀', '加尔各答', '加里加尔', '贾巴尔普尔', '贾朗达尔', '焦特布尔', '金奈', '卡瓦拉蒂', '科希马', '马埃', '马杜赖', '森伯尔布尔', '特里凡得琅', '乌代布尔', '西隆', '锡尔萨瓦', '新德里', '亚南', '因帕尔', '印多尔', '斋普尔'], '印度尼西亚': ['巴厘', '邦加－勿里洞群岛', '北苏拉威西', '北苏门答腊', '大雅加达首都特区', '东加里曼丹', '东南苏拉威西', '东努沙登加拉', '东爪哇', '廖内', '马鲁古', '明古鲁', '楠榜', '南加里曼丹', '南苏拉威西', '南苏门答腊', '日惹特区', '万丹', '西努沙登加拉', '西苏门答腊', '西爪哇', '雅加达', '亚齐', '伊里安查亚', '占碑', '中加里曼丹', '中苏拉威西', '中爪哇'], '英国': {'北爱尔兰': ['贝尔法斯特', '德里', '利斯本', '纽里'], '苏格兰': ['阿伯丁', '爱丁堡', '丹迪', '格拉斯哥', '斯特灵', '因弗内斯'], '威尔士': ['班戈', '卡迪夫', '纽波特', '斯旺西'], '英格兰': ['埃克塞特', '巴斯', '彼得伯勒', '伯明翰', '布拉德福德', '布莱顿与赫福', '布里斯托尔', '德比', '德罕', '格洛斯特', '赫尔河畔京斯敦', '赫里福德', '剑桥', '卡莱尔', '坎特伯雷', '考文垂', '兰开斯特', '里彭', '利奇菲尔德', '利物浦', '利茲', '列斯特', '林肯', '伦敦', '曼彻斯特', '南安普敦', '牛津', '纽卡斯尔', '诺丁汉', '诺里奇', '朴茨茅斯', '普雷斯顿', '普利茅斯', '奇切斯特', '切斯特', '桑德兰', '圣阿本斯', '索尔斯堡', '索福特', '特鲁罗', '特伦特河畔斯多克', '威尔斯', '韦克菲尔德', '温彻斯特', '伍尔弗汉普顿', '伍斯特', '谢菲尔德', '伊利', '约克']}, '英属印度洋领地': {}, '约旦': ['阿吉隆', '安曼', '拜勒加', '杰拉什', '卡拉克', '鲁赛法', '马安', '马德巴', '马夫拉克', '塔菲拉', '亚喀巴', '伊尔比德', '扎尔卡'], '越南': ['海防', '河内', '胡志明市'], '赞比亚': ['北方', '东方', '卢阿普拉', '卢萨卡', '南方', '铜带', '西北', '西方', '中央'], '泽西岛': {}, '乍得': {}, '直布罗陀': {}, '智利': ['阿劳卡尼亚大区', '阿塔卡马大区', '安托法加斯塔大区', '比奥比奥大区', '复活节岛', '湖大区', '科金博大区', '马乌莱大区', '麦哲伦-智利南极大区', '圣地亚哥', '塔拉帕卡大区', '瓦尔帕莱索大区', '伊瓦涅斯将军的艾森大区'], '中非共和国': ['巴明吉-班戈兰', '班吉直辖市', '宾博', '凯莫', '洛巴伊', '曼贝雷-卡代', '姆博穆', '纳纳-格里比齐', '纳纳-曼贝雷', '桑加-姆巴埃雷', '上科托', '上姆博穆', '瓦卡', '瓦卡加', '瓦姆', '瓦姆-彭代', '翁贝拉-姆波科', '下科托']}
