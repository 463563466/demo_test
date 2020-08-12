
# coding:utf-8
import re

fmt_content =  '浙江省高级人民法院民 事 判 决 书（2009）浙知终字第ＺＬ9911××××.7187号上诉人（原审原告）浙江新安化工集团ＺＬ××××××××.7股份有限公司，住所地浙江省建德市新安江镇。法定代表人王伟，董事长。委托代理人（特别授权代理）宋深海，浙江浙经律师事务所律师；委托代理人（特别授权代理）翁霁明，浙江浙经律师事务所律师。上诉人（原审被告）浙江金帆达生化股份有限公司，住所地浙江省桐庐县横村镇。法定代表人孔鑫明，董事长。委托代理人（特别授权代理）刘卫平，上海锦天城律师事务所律师；委托代理人（特别授权代理）郭勤贵，北京市金杜律师事务所律师。上诉人浙江新安化工集团股份有限公司（以下简称新安公司）、浙江金帆达生化股份有限公司（以下简称金帆达公司）因侵犯发明专利权纠纷一案，均不服浙江省杭州市中级人民法院（2008）杭民三初字第14号民事判决，向本院提起上诉。本院于2009年12月4日立案受理后，依法组成合议庭，并于2010年2月1日、6月28日两次公开开庭进行了审理。上诉人新安公司的委托代理人宋深海、翁霁明，上诉人金帆达公司的法定代表人孔鑫明及其委托代理人刘卫平、黄裕华（参加第一次庭审）、郭勤贵（参加第二次庭审）到庭参加诉讼。本案现已审理终结。原判认定：1999年11月8日，新安公司向国家知识产权局申请了一项“草甘膦酸合成中水解辅续工序”方法发明专利。该专利申请经实质审查，于2001年11月28日授予专利权，专利号为：ＺＬ9911××××.7。其专利独立权利要求为：草甘膦酸合成水解辅续工序，所述的合成是以多聚甲醛、甘氨酸、三乙胺、亚膦酸二甲酯为原料，以低级醇为溶剂的烷剂酯法合成，其特征是：（1）一级处理，将所述水解的尾气通经水洗塔水洗，除去尾气中的甲缩醛、甲醇，得一级处理后的气体；（2）二级处理，将所述的一级处理后气体通经碱液吸收塔洗涤，除去气体轴的酸性物质，得二级处理后气体；（3）三级处理，将所述的二级处理后气体通经浓硫酸干燥塔干燥，得三级处理后气体。2003年12月，该专利获得了中国专利优秀奖。2008年1月30日，原审法院前往金帆达公司进行证据保全，确认在该公司草甘膦尾气回收氯甲烷的生产现场中包含了“水洗泵”、“碱洗塔”及“硫酸塔”、除沫器，鼓风机，气柜、气柜后冷凝器，除沫器、氯甲烷成品槽等相关设备装置，并以拍照、拍摄等形式进行证据保全。原审法院保全过程中，金帆达公司拒绝提供相应图纸等资料并进行阻拦，致使证据保全无法继续进行。同年2月4日，原审法院第二次前往金帆达公司进行证据保全，金帆达公司向原审法院提供了一套“尾气处理生产工艺流程图”，但原审法院发现涉案生产现场明显发生了改变：第一次所看到的“水洗泵”变成了“季碱液泵”，而且在相关的塔前面增加了一系列桶，分别标注为不同的化学液名称。原审法院在杭州市安全生产监督管理局、建德市公安局调取的两套金帆达公司“氯甲烷回收生产工艺流程图”相一致，从图纸所反映的“氯甲烷回收生产工艺流程图”来看，其所对应的设备及步骤分别为：一级水洗塔、一级水洗槽，一级冷却器、一级循环泵，二级水洗塔、二级水洗泵、二级水洗槽，二级冷却器、二级循环泵，三级水洗塔、三级水洗槽，三级冷却器、三级循环泵，碱洗塔、碱洗槽，碱洗冷却器、碱洗泵，除沫器，鼓风机，气柜、气柜后冷凝器，除沫器，一级硫酸塔、一级循环槽，一级冷却器、一级循环泵，二级硫酸塔、二级循环槽，二级冷却器、二级循环泵，三级硫酸塔、三级循环槽，三级冷却器、三级循环泵，四级硫酸塔、四级循环槽，四级冷却器、四级循环泵等。而根据金帆达公司交付给杭州市安全生产监督管理局备案6000吨草甘膦技改项目的安全预评价报告（浙江泰鸽安全科技有限公司出具）显示：金帆达公司的氯甲烷回收车间流程为：来自草甘膦车间的氯甲烷从一级水洗塔底部进入，经一级水洗后出一级水洗塔顶部进入二级水洗塔底部，二级水洗后出三级水洗塔顶部进入碱洗塔底部，从碱洗塔顶部出来的氯甲烷经除沫器除去液体，由鼓风机送至气柜，从气柜出来的氯甲烷先进气柜后冷凝器冷凝后，经除沫器除去液体后经过一级硫酸塔，二级硫酸塔三级硫酸铜，四级硫酸塔后至除沫器除掉液体由压缩机压缩后经冷却器、压缩器、冷凝器冷却后至氯甲烷成品槽。上述图纸的形成时间显示为2004年。根据浙江省环境保护科学设计研究院所提供的金帆达年产6000吨草甘膦（制剂）技改项目环评报告（该报告所依据的材料均由金帆达公司提供），该氯甲烷回收车间流程为：来自草甘膦车间的氯甲烷从一级水洗塔底部进入，经一级水洗后出一级水洗塔顶部进入二级水洗塔底部，二级水洗后出三级水洗塔顶部进入碱洗塔底部底部，三级水洗后出三级水洗塔顶部进入碱洗塔底部，从碱洗塔顶部出来的氯甲烷经除沫器除去液体，由鼓风机送至气柜，从气柜出来的氯甲烷先经气柜后冷凝器冷凝后，经除沫器除去液体后依次经过一级稀硫酸塔、二级浓硫酸塔、三级浓硫酸塔，四级浓硫酸塔后至除沫器除掉液体由压缩机压缩后通过压缩后冷却器，压缩器后冷凝器冷却后至氯甲烷成品槽。原审法院证据保全时金帆达公司所提供的“尾气处理工艺流程图”与该院从杭州化医工程设计院提取的“尾气处理工艺流程图”内容一致，其所对应的设备及步骤分别为：一级季碱化反应器、一级水洗槽，一级冷却器、一级循环泵，二级季碱化反应器、二级水洗泵、二级水洗槽，二级冷却器、二级循环泵，三级季碱化反应器、三级水洗槽，三级冷却器、三级循环泵，碱洗塔、碱洗槽，碱洗冷却器、碱洗泵，除沫器，鼓风机，气柜、气柜后冷凝器，除沫器，一级硫酸塔、一级循环槽，一级冷却器、一级循环泵，二级硫酸塔、二级循环槽，二级冷却器、二级循环泵，三级硫酸塔、三级循环槽，三级冷却器、三级循环泵，四级硫酸塔、四级循环槽，四级冷却器、四级循环泵等。杭州化医工程设计院工作人员张永良在接受建德市公安局的询问时确认：2004年，金帆达公司委托杭州化医工程设计院设计一套草甘膦工艺技术改造方案，杭州化医工程设计院遂根据金帆达公司提供的材料由张永良设计出了一整套“氯甲烷回收生产工艺流程图”（即杭州化医工程设计院向建德市公安局提供的图纸，内容与金帆达公司上报给杭州市安全生产监督管理局、浙江省环境保护科学设计研究院的图纸一致），并交付给金帆达公司使用。2007年底，金帆达公司找到杭州化医工程设计院，以申请专利为由要求对2004年版的“氯甲烷回收生产工艺流程图”进行部分修改，杭州化医工程设计院根据金帆达公司的要求，于2007年12月20日、2008年2月27日在第一套流程图的基础上进行两次修改，最终形成了三套“氯甲烷回收生产工艺流程图”。杭州化医工程设计院在原审法院调取证据时提供的是第三套图纸（2008年2月27日修改的版本）。庭审比对中，金帆达公司确认其“草甘膦尾气回收氯甲烷”中的合成也是以多聚甲醛、甘氨酸、三乙胺、亚膦酸二甲酯为原料，以低级醇为溶剂的烷剂酯法合成。在具体的三级处理所除去尾气中的原料成份与涉案专利独立权利所包含的原料成份一致，只是其附带除去了尾气中的吡啶。根据金帆达公司的审计单位浙江天健东方会计师事务所所提供的材料，金帆达公司2004年至2007年生产、销售的氯甲烷利润情况如下：2004年毛利为人民币1957301.60元；2005年的毛利为4876795.95元；2006年毛利为2375469.67元，2007年毛利为14098533.21元。金帆达公司向浙江省农药工业协会申报的草甘膦产量为：2005年3935吨，2006年11203吨，2007年23337吨。新安公司认为一吨草甘膦可以生产出0.5吨氯甲烷；金帆达公司认为其一吨草甘膦只能生产出0.4吨氯甲烷成品。另查明，金帆达公司原名杭州金帆达化工有限公司，2007年7月变更为现在的名称。新安公司认为金帆达公司的行为侵犯其专利权，遂于2008年1月14日向原审法院起诉，请求判令金帆达公司：1.停止侵权、销毁侵权的氯甲烷回收生产设备；2.赔偿新安公司经济损失5480万元（算至2007年底止，2008年1月1日以后至停止侵权日止的损失另行计算）；3.在全国性公开媒体上公开向新安公司赔礼道歉；4.承担全部诉讼费用。2009年5月5日，新安公司撤回要求金帆达公司停止侵权的诉讼请求。原审法院认为，新安公司拥有的专利号为ＺＬ9911××××.7“草甘膦酸合成中水解辅续工序”方法发明专利在有效期限内，法律状态稳定，并已履行了缴纳专利年费的义务，故该专利为有效专利，应受国家法律保护。新安公司取得对侵犯ＺＬ9911××××.7发明专利的行为之诉权。根据原审法院查明的事实及双方的控辩意见，本案的争议焦点在于金帆达公司使用的“氯甲烷回收生产工艺”是否落入ＺＬ9911××××.7发明专利的保护范围。对此，新安公司认为，金帆达公司所使用的生产工艺包含了其专利独立权利中的全部必要技术特征，属于相同侵权。金帆达公司认为，其使用的相关工艺与涉案专利并不相同，也不等同，其工艺第一级处理是季碱液洗而非专利中的水洗，且两者的气源也不相同，未落入涉案专利的保护范围。原审法院认为，根据《中华人民共和国专利法》第五十六条规定：“发明与实用新型专利权的保护范围以其权利要求的内容为准，说明书及附图可以用于解释权利要求。”因此判断被控侵权方法是否落入涉案专利权的保护范围，应在涉案专利权的权利要求所描述的专利方法与被控侵权方法之间进行比对，即比对被控侵权方法所具备的技术特征与独立权利要求所描述的专利方法的技术特征。如果被控侵权方法的技术特征完全覆盖了涉案专利权独立权利要求的全部必要技术特征，则被控侵权方法落入了专利权的保护范围，其中专利保护范围包括与该专利技术相同或等同的特征所确定的范围。本案中，ＺＬ9911××××.7发明专利独立权利要求所包含的必要技术特征包括如下几个方面：1.所述的合成是以多聚甲醛、甘氨酸、三乙胺、亚膦酸二甲酯为原料，以低级醇为溶剂的烷剂酯法合成；2.一级处理，将所述水解的尾气通经水洗塔水洗，除去尾气中的甲缩醛、甲醇，得一级处理后的气体；3.二级处理，将所述的一级处理后气体通经碱液吸收塔洗涤，除去气体轴的酸性物质，得二级处理后气体；4.三级处理，将所述的二级处理后气体通经浓硫酸干燥塔干燥，得三级处理后气体。由于金帆达公司拒不配合法院进行证据保全，固定被控生产现场，且擅自改动现场，致使被控现场无法复原，从而导致对现在的生产现场进行技术比对失去了实际意义，因此，金帆达公司提出将现在的生产现场与涉案专利进行技术比对的司法鉴定申请，原审法院不予准许，金帆达公司应当承担由此带来的法律后果，原审法院将以相应的工艺图纸，结合相关的录像、照片与涉案专利进行技术比对。从本案查明的事实来看，金帆达公司实际拥有三套“氯甲烷回收生产工艺流程图”，其2004年版图纸与后两套图纸（2007年年底版及2008年2月版）的区别在于第一级处理的设备为洗季碱液器还是水洗塔（泵），所对应的步骤系水洗还是季碱液洗。对此，原审法院认为，该院第一次前往生产现场证据保全时发现该设备所标注的名称为“水洗泵”，金帆达公司提供给浙江省环境保护科学设计研究院、杭州市安全生产监督管理局的图纸上亦明确标明是水洗塔，且该“氯甲烷回收生产工艺流程图”的设计者也证实金帆达公司在2007年之前实际使用的图纸为2004年版，即其第一级处理的设备及对应的步骤为水洗塔和水洗，因此，该院有理由相信金帆达公司被控生产现场使用的是其2004年版的“氯甲烷回收生产工艺流程图”，即金帆达公司使用的“氯甲烷回收生产工艺”中的第一级处理中的设备为水洗塔（泵），而非碱化反应器，其所对应的第一级处理为水洗而非季碱液洗。因金帆达公司使用的2004年版“氯甲烷回收生产工艺流程图”所包含的设备及步骤与涉案专利独立权利要求中所含的步骤完全一致，金帆达公司亦确认两者所对应原料成份一致；鉴于新安公司仅指控金帆达公司在2007年年底之前实施的专利侵权行为，且金帆达公司在2007年年底前一直使用的是其2004年版的“氯甲烷回收生产工艺流程图”，因此，原审法院认为，金帆达公司在其草甘膦尾气回收氯甲烷生产中使用的工艺包含了ZL99119970.7发明专利权独立权利要求的全部必要技术特征，已落入了涉案专利的保护范围，金帆达公司的行为构成专利侵权。金帆达公司虽辩称其工艺中的气源以及相对应的步骤均与涉案专利不同，但这既与其所使用的“氯甲烷回收生产工艺流程图”及修改后的“尾气处理工艺流程图”不相一致，也未得到其他证据相佐证，原审法院对其异议不予采信。新安公司要求金帆达公司赔偿经济损失的请求正当,应予以支持。因本案属于专利方法侵权纠纷，金帆达公司在氯甲烷回收生产工艺生产中使用的设备本身并不侵权，故新安公司要求销毁氯甲烷回收生产设备于法无据，原审法院不予支持。对于新安公司要求金帆达公司赔礼道歉的诉请，原审法院认为，专利权在表现为技术侵权时并不具有人身权性质，而赔礼道歉属于人身权受到侵害时的救济方式，故新安公司要求金帆达公司赔礼道歉之诉讼请求缺乏法律依据，原审法院不予支持。对于金帆达公司提出其使用的是公知技术之抗辩，原审法院认为，所谓公知技术，是指在涉案专利申请日或优先权日之前他人已有的相同或实质上相同的另一项在先技术。本案中，金帆达公司以公知技术进行抗辩，即负有举证之责任，金帆达公司应当证明其所使用的落入专利保护范围的技术在专利申请之前已经存在，但金帆达公司并未提供相应的证据证明在涉案专利申请日或优先权日之前他人已有的相同或实质上相同的另一项在先技术全部覆盖了涉案专利所有必要的技术特征，也未能证明新安公司在涉案专利申请之前已经将专利方法进入公知领域，故金帆达公司的上述公知技术抗辩不能成立，原审法院不予支持。关于本案赔偿数额。原审法院认为，新安公司没有向该院提供有效证据证明其在被侵权期间因侵权所受到的具体损失，故该院不能确定其具体的损失数额；金帆达公司未按照该院证据保全要求提交其使用侵权工艺获得的氯甲烷产品的具体生产、销售数量、时间及销售利润证据，致使该院无法查明侵权人在侵权期间因侵权所获得的具体利益，金帆达公司持有上述证据无正当理由拒不提供，应当承担相应的法律责任。根据金帆达公司2004年至2007年的审计报告，其2004年至2007年生产、销售的氯甲烷毛利合计为人民币23308100.43元；而根据金帆达公司2005年至2007年度的草甘膦数量（38475吨），按照金帆达公司自己确定的0.4的折算比例，其2005年至2007年可回收氯甲烷15390吨，再根据其2004年每吨毛利约为1081元（金帆达公司自己报表中的数据）计算，金帆达公司三年就可获毛利为16636590元，五年累计应当超过2000万元。因此，从上述两种计算方式来看，扣除其他合理费用，金帆达公司从2003年至2007年的获利明显超过人民币2000万元。鉴于金帆达公司持有证据无正当理由拒不提供，致使该院无法查明金帆达公司侵权获利的具体数额，结合上述因素，该院确定金帆达公司赔偿新安公司人民币2000万元。金帆达公司虽主张该氯甲烷总量并非全由侵权工艺生产，其中相当部分系另行购买、其他关联公司提供或通过二甲脂原料提炼而成，但并未提供有效证据予以佐证，原审法院对其该主张不予采信。综上，依照《中华人民共和国专利法》第十一条第一款、第五十六条第一款、第六十条，《最高人民法院关于审理专利纠纷案件适用法律问题的若干规定》第十七条、第二十条、第二十二条，《中华人民共和国民事诉讼法》第六十四条、最高人民法院《关于民事诉讼证据的若干规定》第二条、第七十五条之规定，原审法院于2009年8月10日判决：一、浙江金帆达生化股份有限公司赔偿浙江新安化工集团股份有限公司经济损失人民币20000000元（包括浙江新安化工集团股份有限公司为制止侵权所支出的合理费用），于判决生效之日起十日内履行完毕。二、驳回浙江新安化工集团股份有限公司的其他诉讼请求。如果未按判决指定的期间履行给付金钱义务，应当依照《中华人民共和国民事诉讼法》第二百二十九条之规定，加倍支付迟延履行期间的债务利息。案件受理费人民币315800元，由浙江金帆达生化股份有限公司负担215228元，浙江新安化工集团股份有限公司负担100572元；财产保全申请费人民币5000元，由浙江金帆达生化股份有限公司负担。宣判后，新安公司、金帆达公司均不服，向本院提起上诉。上诉人新安公司上诉称：金帆达公司侵权时间长、侵权技术使用范围广，所获得的利益远不止2000万元，且新安公司所受到的经济损失也不止5480万元，原判确定的侵权赔偿数额偏低，请求二审法院改判支持其一审诉讼请求。上诉人金帆达公司答辩称：1.新安公司指控金帆达公司窃取其技术和商业秘密没有事实依据；2.新安公司根据浙江省农药协会的不正确统计数据计算金帆达公司获利超过2000万元没有依据；3.新安公司称其经济损失超过5480万元没有任何证据，将金帆达公司的所有生产能力均认为是其应有的垄断份额是错误的。故请求二审法院驳回新安公司的上诉。上诉人金帆达公司上诉称：一、原判认定金帆达公司涉案行为构成专利侵权错误：1.金帆达公司不存在拒绝原审法院证据保全的行为，原审法院就此推定金帆达公司构成侵权显属不公；2.金帆达公司没有实际使用和全部使用涉案专利的技术方案，所使用的工艺方法与涉案专利不相同也不等同；3.原审法院仅凭新安公司的证据和自行取证证据认定金帆达公司构成专利侵权证据不足，且金帆达公司在设计图纸和报告中的氯甲烷生产流程属于公知技术，不构成专利侵权；4.金帆达公司使用的是自己享有知识产权的生产工艺技术。二、原判确定的赔偿数额不当：1.原判认定金帆达公司自2003年开始生产氯甲烷没有证据；2.原判认定的金帆达公司生产的氯甲烷数量没有事实依据；3.原判认定金帆达公司生产的氯甲烷利润均为侵权所得没有依据。综上，请求二审法院依法改判，支持金帆达公司的上诉请求。上诉人新安公司答辩称：1.原审法院证据保全程序合法，第一次现场保全的证据具有可信性和真实性，采用金帆达公司2004年的“氯甲烷回收生产工艺流程图”作为技术比对对象正确，据此认定侵权事实清楚，证据充分；2.从一审庭审中金帆达公司法定代表人的陈述以及原审法院调取的相关资料均可以认定金帆达公司使用的氯甲烷回收工艺包含了新安公司涉案发明专利的全部必要技术特征，构成专利侵权；3.新安公司的涉案专利具有有效性和稳定性，并不属于公知技术；4.原判确定的2000万元赔偿数额偏低，金帆达公司的实际产品数量及利润远大于其申报数和审计数。在二审第一次庭审中，新安公司向本院提交了以下证据：证据1.雷崧僧等人撰写的《我国草甘膦生产工艺及其技术进步》，登载于1999年第4期《农药》；证据2.涉案专利申请公开文本（公开号CN1260348A）；证据3.周芦文等人撰写的《草甘膦生产过程及控制系统综述》，登载于2006年第9期《农药》；证据4.吴美宁撰写的《草甘膦合成工艺优化探讨》，登载于1998年5月《浙江师大学报》；证据5.峁庆文撰写的《草甘膦生产工艺综述及其发展趋势》，登载于2008年6月《安徽化工》；证据6.程能林编著的《溶剂手册》。上述证据1-6用以证明涉案专利并未做过任何不当修改，涉案专利权利稳定。证据7.2003年10月《中国化工报》文章《冲出峡谷下五洋》；证据8.《媒体眼中的新安化工》文章《新安化工集团股份有限公司反倾销专记》；证据9.2008年9月《中国化工报》文章《碧水环绕中，圆一个绿色的梦想》；证据10.胡志鹏撰写的《草甘膦行业的现状与发展趋势》，登载于2008年2月《上海化工》；证据11.2007年11月12日《中国化工报》文章《三农公司实现氯甲烷回收》。上述证据7-11用以证明涉案专利的显著进步，具有巨大的社会效益、经济效益和环保效益，并极大地提升了中国相关企业的国际竞争力。证据12.杭州市环保局行政处罚案件列表；证据13.杭州市十大典型环境违法案件查处情况的通报。上述证据12、13用以证明金帆达公司因违法生产，多次被政府主管部门行政处罚，存在多次违法历史记录。证据14.金帆达公司氯甲烷销售发票；证据15.新安公司氯甲烷销售发票；证据16.其他公司氯甲烷销售发票。上述证据14-16用以证明侵权期间氯甲烷市场价格，证明金帆达公司生产销售侵权产品、获取部分非法利润的事实。第二次庭审中，新安公司提供以下证据：证据17.国家知识产权局专利复审委员会（以下简称专利复审委）维持专利有效的决定，用以证明涉案专利的稳定性和有效性。证据18.工业和信息化部的通知，用以证明涉案专利技术已经列入国家草甘膦行业的推广技术。金帆达公司质证后认为：证据1真实性无异议，关联性有异议。该文章的作者是新安公司员工，其证据证明效力不强。且该证据证明生产草甘膦的几种生产工艺是多样化的，反而证明涉案专利经过修改过的权利要求和说明是超范围的修改。证据2真实性无异议，关联性有异议。最终的专利权利要求和说明书已经作了修改，恰恰证明了涉案专利的修改是无效的。证据3-5真实性无异议，但证明了涉案专利经过修改后是违法的。证据6的证明目的有异议。证据7-11均为复印件，即使有原件，对真实性仍有异议。这些宣传资料反映的事实无从确认，且也不能证明涉案专利具有创造性。同时证据11关于福建三农集团对氯甲烷的回收，恰恰证明了氯甲烷回收属于公知技术。证据12、13虽然表明金帆达公司曾经存在过未达标的事项，但与本案专利侵权没有关联性，且金帆达公司通过整改已经达标，现在继续生产。证据14-16的发票上只记载了不统一的氯甲烷价格，表明金帆达公司销售氯甲烷的利润非常低，且金帆达公司的氯甲烷系采用自有技术生产的，不是侵权产品，不能证明金帆达公司生产、销售侵权产品的事实。综上，该16份证据不能证明新安公司提出的损失远远超过5480万的上诉理由，与其上诉请求无关。证据17的真实性、合法性无异议，对关联性有异议，金帆达公司已就该无效决定向北京市第一中级人民法院提起行政诉讼，该院已发了受理案件通知书。证据18的真实性、合法性无异议，对关联性有异议，该证据恰恰证明此项技术是一项广为使用的公知技术。第一次庭审中，金帆达公司向本院提交了如下证据：证据1.“草甘膦生产尾气的综合处理方法”发明专利证书和说明书；证据2.“与草甘膦联产百草枯的生产方法”发明专利证书和说明书。上述证据1、2用以证明金帆达公司的生产方法是自有技术，并已获得发明专利，经国家知识产权局审核确认与现有技术（包括涉案新安公司的技术）不同，金帆达公司按照自有专利方法生产不构成对新安公司的专利侵权。证据3.“草甘膦酸生产母液处理工艺”发明专利证书和发明专利说明书；证据4.荣誉证书9份。上述证据3、4用以证明金帆达公司具有自主研发和技术创新能力，完全有能力研发被控侵权的生产技术和方法。证据5.2009年9月24日专利复审委《无效宣告请求受理通知书》；证据6.2010年1月12日专利复审委召开无效宣告请求口头审理的通知书。上述证据5、6用以证明涉案发明专利已在专利复审委进入无效宣告审理阶段，并已召开专利无效申请的口头审理。证据7.涉案专利原始申请文本以及审查历史文档，用以证明：（1）涉案发明专利权利要求1和说明书技术方案部分在专利审查过程中进行过超范围修改，违反了《中华人民共和国专利法》（以下简称《专利法》）第三十三条的规定，并且损害了第三人的利益；（2）涉案发明专利权利要求1-4缺乏必要的技术特征，不符合《专利法》第二十六条以及《专利法实施细则》第二十一条的规定，应属无效。证据8.美国专利US4，486，359恩及其中文译文，公开日期1984年12月4日，用以证明：（1）涉案专利权利要求1前序的必要技术特征早已在该专利申请日前被公开；（2）新安公司在原始专利申请文件中仅仅提到了使用甲醇，修改后的限定以低级醇为溶剂的技术方案超出了原始记载甲醇为溶剂的范围，损害了第三人的利益，违反了《专利法》第三十三条的规定；（3）涉案专利权利要求书缺乏盐酸水解这一技术特征，应属无效。证据9.1998年出版的《浙江化工》第29卷第4期38-40页文献，用以证明该文献在涉案专利申请日前已公开了专利权利要求1的必要技术特征和权利要求4的技术特征。证据10.1998年《农药》第37卷第6期文献，用以证明该文献在涉案专利申请日前已经公开了专利权利要求2、3。证据11.氯甲烷回收操作记录15份，用以证明2008年1月30日至2月5日期间原审法院保全的设备处于24小时生产运行状态，金帆达公司没有对设备进行改动。证据12.桐庐县气象要素，用以证明在2008年1月30日至2月4日期间桐庐县范围下大雪，在该气象条件下金帆达公司无法改动保全的设备。证据13.浙江省民政厅证明，用以证明浙江省农药工业协会的法定代表人王伟即为新安公司的法定代表人，与本案有利害关系，其所提供的证据不能作为本案确定新安公司损失的依据。证据14.发票12份，用以证明金帆达公司审计报告中生产销售的草甘膦数量包括了其向其他公司采购部分草甘膦转销售的数量，原审法院以其生产销售的草甘膦全部数量为依据计算氯甲烷产量错误。证据15.杭州市履行禁止化学武器公约工作领导小组办公室（以下简称杭州市禁化武办）调查表，用以证明：（1）金帆达公司审计报告中氯甲烷的产量部分来源于亚磷酸二甲脂的生产，原判认定氯甲烷的产量来源于草甘膦的生产错误；（2）金帆达公司2005年至2007年草甘膦的实际年产量。证据16.杭州市环境保护局《关于“杭州金帆达化工有限公司年产6000吨草甘膦原粉技改项目环境影响报告书”审批意见》；证据17.杭州市环境保护局《建设项目环境保护设施竣工验收审批意见》。上述证据16、17用以证明金帆达公司第一条生产线于2004年12月14日通过杭州市环境保护局审批后开始建设，年产量6000吨，原审法院确定金帆达公司草甘膦年产量缺乏依据。证据18.杭州市环境保护局《环境违法行为限期整改通知书》；证据19.杭州市环境保护局《关于杭州金帆达化工有限公司生产延续环保意见》；证据20.杭州市环境保护局《关于杭州金帆达化工有限公司生产6000吨草甘膦技改项目环境影响报告书审查意见的函》。上述证据18-20用以证明金帆达公司仅有一条年产6000吨草甘膦的生产线，其第二条生产线被环保部门责令停产，至2008年11月才获批投入生产。第二次庭审中，金帆达公司提供以下证据：证据21.杭州市禁化武办2004年度宣布工作布置，用以证明杭州市禁化委办于2004年12月将金帆达公司列入禁化武公约监督检查的组织范围，对金帆达公司填报监控化学品和生产的情况列入了强制管理。证据22.2010年6月24日桐庐县经济贸易局的证明，用以证明2006年8月20日和8月22日国际禁化武组织专家组对金帆达公司进行了监督、现场视察。证据23.《监控化学品管理条例》，用以证明金帆达公司生产的亚磷酸二甲酯和草甘膦属于化学品监控产品，该条例对企业的监管有非常详细的规定。证据24.浙江省人民政府浙政办发（2007）第10号文件，用以证明金帆达公司企业的管理监管是在政府部门的严密监管下，生产设施列入监管范围。证据25.北京市第一中级人民法院的案件受理通知书。证据26.工业和信息化部关于14个重点行业清洁生产企业的推行方案，用于证明涉案专利技术是一项公知技术。新安公司质证后认为：证据1、2专利证书的申请及授权日均为2008年以后，新安公司起诉的是2007年以前金帆达公司的侵权事实，故该证据与本案无关；该专利涉及的是草甘膦生产尾气的综合处理方法，与涉案专利不同，缺乏关联性；且至今金帆达公司也没有实施该专利。证据3、4有关金帆达公司法定代表人个人的荣誉证书，与金帆达公司的证明对象缺乏关联性。同时，该证据所涉的草甘膦生产母液的处理与本案涉及到的侵权技术和产品没有必然的联系，不能以金帆达公司具备该工艺，就认定具有自主研发被控侵权的技术和方法的能力。证据5、6与本案无关，金帆达公司的无效请求是在一审判决之后提出的，根据有关司法解释，金帆达公司没有在答辩期内甚至一审期间提出无效申请，应当视为金帆达公司已经放弃了无效抗辩。证据7真实性无异议，但是涉及专利权的超范围修改，与本案无关。证据8没有合格的中文译本，不具备证据的形式要件。证据9不能证明涉案专利是公知技术。证据10与本案的公知技术抗辩没有关联。证据11系金帆达公司事后单方制作，不具有可信性。证据12仅表明原审法院证据保全和财产保全时天气状况，并不能证明金帆达公司提出的原始现场没有进行变动的主张，事实上原审法院前后两次录像和照片已经清楚表明存在变动。证据13不能证明2009年9月20日以前浙江省农药工业协会的法定代表人是王伟，所涉的金帆达公司草甘膦数量也来源于金帆达公司自己的上报数量，且原判只是将此证据中草甘膦数量作为一部分参考依据，侵权数额的认定主要来源于审计报告和其他证据。证据14真实性无异议，但草甘膦的数量明显偏少，不足以推翻原判认定的草甘膦利润。证据15不能确定该调查材料的调查方法以及调查的对象，对其真实性、合法性均有异议。证据16、17仅是有关政府部门的批文，不能反映金帆达公司的实际产能，实际上该生产线的设计能力、有关功率等已经达到年产18000吨的能力。证据18-20可以看出金帆达公司确有违法生产的情形，也仅是表明了有关政府部门的手续，并不能证明金帆达公司的实际产能和产量。证据21-24均不属于新证据。证据25新安公司没有收到，且该材料与本案无关。证据26提到是企业自主研发的草甘膦酸清洁回收技术，不能证明金帆达公司的证明目的。经审查，本院认为，新安公司提供的证据1-6以及金帆达公司提供的证据5-10均是针对金帆达公司提出专利无效请求所提出的证据，因涉案专利现已经专利复审委审查决定宣告维持专利权全部有效，故对该些证据无需再行认证，本院不作认定。新安公司提供的证据7-11均系复印件，且相关宣传报道性的文章所拟证明的目的与本案的事实认定并无关联性，本院不予认定。证据12、13关于金帆达公司被行政处罚的事实与本案侵权事实的判定没有关联性，本院不予认定。证据14-16与确定本案的赔偿数额具有一定的关联性，本院予以认定。证据17因金帆达公司没有异议，本院予以认定。证据18因金帆达公司亦提供了相同的证据，本院予以认定。至于金帆达公司提供的证据1-2所涉的专利均系2008年之后授权，而新安公司起诉指控的是2007年以前的侵权事实，故该证据与本案不具有关联性；且该两份证据与证据3所显示的金帆达公司享有的专利技术方案、工艺方法、步骤与涉案专利及被控侵权的技术方案并不相同，故与本案的侵权判定没有关联性，本院不予认定。证据4有关金帆达公司法定代表人个人的荣誉证书，与本案侵权事实判定亦无关联性，本院不予认定。证据11系金帆达公司单方制作，新安公司对此提出异议，本院不予认定。证据12因原审法院两次证据保全表明金帆达公司的生产现场已经发生了变动，故该证据的待证事实与客观事实不符，本院不予认定。证据13为浙江省民政厅的证明，新安公司对其真实性没有提出异议，本院对其真实性予以认定。但本院注意到浙江省农药工业协会的数据系金帆达公司自行申报，原审法院向浙江省农药工业协会调取的材料也并非该院在确定赔偿数额时的唯一考量依据，故该证据与确定本案争议事实之间并无关联性。证据14因新安公司对其真实性没有异议，本院予以认定。证据15因新安公司对真实性和合法性均提出异议，且也不能证明该些调查表系杭州市禁化武办出具，故本院不予认定。证据18-20为有关部门的批文，本院予以认定，但有关金帆达公司的实际产能和产量还需结合本案的其他证据予以综合确定。证据21-24是有关金帆达公司企业管理纳入政府部门监管范围的证据，与本案争议事实并无关联性，本院不予认定。证据25系法院的法律文书，本院予以认定。证据26与新安公司提供的证据18一致，本院予以认定，该证据能够证明在2010年2月22日工业和信息化部发布的《农药行业清洁生产技术推行方案》中包括了涉案专利技术，但并不能证明金帆达公司提出的涉案专利技术为一项公知技术的主张。二审中，金帆达公司向本院提出了中止诉讼申请书，请求中止本案诉讼，等待专利复审委的无效审查决定。由于在二审期间涉案专利权已经专利复审委宣告全部有效，故对该申请本院不予准许。同时，金帆达公司还提出调查证据申请，请求本院向浙江省或杭州市禁化武办调取金帆达公司2005至2007年草甘膦的实际年产量的材料。根据其申请，本院于2010年6月10向浙江省禁化武办调取证据，浙江省禁化武办出具证明一份，载明：金帆达公司向我办申报的草甘膦生产能力及产量数据为：2005年生产能力2900吨/年和6000吨/年，生产产量1222.8吨和3396.02吨；2006年生产能力12000吨/年，生产产量8672.45吨；2007年生产能力12000吨/年，生产产量10946.01吨。经庭审质证，新安公司认为对该证据的形式真实性无异议，但内容真实性不予认可：1.浙江省禁化武办明确该数据是金帆达公司单方申报，并未核实；2.该证据没有包括2004年产量，而审计部门提供的证据可以表明在2004年金帆达公司已经在销售氯甲烷，并产生利润；3.该证据没有反映金帆达公司老厂区的6000吨生产能力和生产数据。金帆达公司对该证据的真实性和合法性均予以确认，并认为其是据实填报，数据真实。本院认为，浙江省禁化武办的证明系本院调取，真实性和合法性可以认定，但浙江省禁化武办在出具证明时表示该数据系企业自行申报，故对本案中有关金帆达公司的实际产量本院还将结合其他证据予以综合确定。2010年5月12日，本院召集双方当事人对金帆达公司的草甘膦尾气回收氯甲烷生产现场进行勘验，新安公司勘验后认为金帆达公司的设备与原审法院第一、二次证据保全时的设备均不相同，该生产现场已经不能成为被控侵权技术比对的对象。金帆达公司则认为该些设备与其提供给原审法院的图纸相对应，至于一些包装桶的变化并不会改变设备的内容。本院认为，由于新安公司在一审中明确表示撤回要求金帆达公司停止侵权的诉讼请求，追究其从开始生产到2007年止的侵权行为，故本案在确定被控侵权的技术方法时应以2007年之前金帆达公司所使用的技术方案作为侵权的比对对象。而原审法院曾在2008年1月30日前往金帆达公司进行第一次证据保全，拍摄了部分照片和录像，但在保全过程中受到金帆达公司的阻拦致使证据保全没有全部完成。至第二次证据保全时，原审法院发现生产现场发生了明显改变。本院认为，原审法院的第一次证据保全本应最能客观、真实地反映金帆达公司当时的被控侵权方法，并以此作为比对对象，但由于金帆达公司的不配合导致被控侵权方法无法全部固定，对此金帆达公司应承担相应的法律后果。新安公司对本院的现场勘验中金帆达公司的生产步骤和设备均提出异议，且此次生产现场与金帆达公司提供给浙江省环境保护科学设计研究院和杭州市安全生产监督局的图纸中记载的内容并不相一致，故本院对此次现场勘验中所涉的金帆达公司的生产方法和工艺流程不予认可，即不作为本案被控侵权方法的比对对象。综上，除原审查明的事实外，本院二审另查明：新安公司涉案专利技术曾获得中国专利优秀奖、国家科学技术进步二等奖、浙江省科学技术进步一等奖。2009年9月14日，金帆达公司向专利复审委提出涉案专利无效宣告请求。2010年3月23日，专利复审委作出第14584号无效宣告请求审查决定，维持涉案专利权全部有效。同年6月22日，金帆达公司不服该审查决定，向北京市第一中级人民法院提起行政诉讼。根据上诉人新安公司和金帆达公司的上诉请求和理由以及各自的答辩意见，本院认为本案的二审争议焦点为：1.金帆达公司在其草甘膦尾气回收氯甲烷生产中所使用的方法是否落入了新安公司专利保护范围；2.金帆达公司使用涉案方法是否属于现有技术；3.原判确定的赔偿数额是否合理。分析认定如下：关于争议焦点1，本院认为，要确定金帆达公司在其草甘膦尾气回收氯甲烷生产中所使用的方法是否落入了新安公司专利保护范围，首先需要确定的是金帆达公司在其草甘膦尾气回收氯甲烷生产中所使用的方法，即被控侵权方法的内容。原审法院向杭州市安全生产监督管理局、建德市公安局调取的金帆达公司“氯甲烷回收生产工艺流程图”上的设备设置和步骤与原审法院从杭州市安全生产监督管理局调取的金帆达公司备案的安全预评价报告以及从浙江省环境保护科学设计研究院调取的金帆达公司年产6000吨草甘膦技改项目环评报告中的“氯甲烷回收车间流程”相对应，且上述图纸的形成时间为2004年。虽然金帆达公司向原审法院提供了另一套“尾气处理工艺流程图”，与原审法院向杭州化医工程设计院调取的图纸相一致，但杭州化医工程设计院工作人员在建德市公安局询问时陈述2004年受金帆达公司的委托设计了一整套“氯甲烷回收生产工艺流程图”（提交给建德市公安局），2007年底应金帆达公司要求修改形成了新的图纸（提交给原审法院）。对此，本院认为，上述有关金帆达公司涉案的工艺流程图、安评报告、环评报告均系原审法院前往有关部门依法调取，该些证据材料有的是金帆达公司自行提供，有的是有关部门根据金帆达公司提供的材料编制，还有的是金帆达公司委托的设计单位提供，且与原审法院第一次证据保全时发现的部分设备名称标注相吻合，具有较强的证明效力，完全可以作为本案金帆达公司的被控侵权方法予以认定。关于金帆达公司提供的“尾气处理工艺流程图”，作为当时设计单位的杭州化医工程设计院已经对此证据的形成时间作了合理解释，故对该份图纸本院不作为比对对象。金帆达公司在二审中提出其出于对技术保护的需要，在当时上报给杭州市安全生产监督管理局的图纸中没有反映季碱化反应器，实际使用中并没有使用水洗步骤，而是采用季碱液洗步骤的抗辩理由，没有相应的证据予以支持，且与原审法院调取的证据以及第一次证据保全的生产现场不相一致，本院不予采信。故在本案已经无法将金帆达公司目前的生产现场作为被控侵权方法作为比对对象的情况下，原审法院依据第一次证据保全时拍摄的部分照片和录像，同时结合该院调查取证的工艺图纸、流程作为被控侵权方法的内容进行技术比对并无不当。金帆达公司对此提出的上诉理由不能成立。根据《中华人民共和国专利法》（2000年第二次修正）第五十六条第一款的规定，发明或者实用新型专利权的保护范围以其权利要求的内容为准，说明书及附图可以用于解释权利要求。新安公司涉案专利的独立权利要求为：草甘膦酸合成水解辅续工序，所述的合成是以多聚甲醛、甘氨酸、三乙胺、亚膦酸二甲酯为原料，以低级醇为溶剂的烷剂酯法合成，其特征是：（1）一级处理，将所述水解的尾气通经水洗塔水洗，除去尾气中的甲缩醛、甲醇，得一级处理后的气体；（2）二级处理，将所述的一级处理后气体通经碱液吸收塔洗涤，除去气体轴的酸性物质，得二级处理后气体；（3）三级处理，将所述的二级处理后气体通经浓硫酸干燥塔干燥，得三级处理后气体。将前述金帆达公司的“氯甲烷回收生产工艺流程图”和“氯甲烷回收车间流程”中显示的草甘膦尾气回收氯甲烷生产工艺与新安公司的涉案专利方法相比对，两者无论是设备配置、操作步骤，还是三级处理的工艺流程均相同。在一审庭审中，金帆达公司确认其也是以多聚甲醛、甘氨酸、三乙胺、亚膦酸二甲酯为原料，以低级醇为溶剂的烷剂酯法合成。在二审现场勘验时，金帆达公司提出其在气体回收时加入了亚磷酸二甲脂的气体，与专利方法的气源不同。对此，本院认为，金帆达公司的“氯甲烷回收生产工艺流程图”和“氯甲烷回收车间流程”中并没有反映出金帆达公司在草甘膦尾气之外还掺入了亚磷酸二甲脂气体。况且，由于涉案专利为一项“草甘膦酸合成中水解辅续工序”，即针对草甘膦的副产物氯甲烷的回收工艺，专利复审委在无效审查决定中认为该专利对现有技术的贡献“不在于草甘膦酸本身的合成路径和工艺，而在于通过对草甘膦酸传统工艺机理的研究，意外地发现其尾气中含有相当量的氯甲烷，从而在传统水解工序中追加尾气回收工序，设置三级处理对氯甲烷进行回收”。故即使如金帆达公司所述在草甘膦尾气之外还掺入了亚磷酸二甲脂气体，亦与涉案专利的技术方法无涉，只要其在草甘膦尾气回收氯甲烷中所采用的工艺方法与专利方法相同，仍然落入了涉案专利的保护范围。关于争议焦点2，金帆达公司主张其使用的涉案被控侵权方法为现有技术，并将此作为理由之一向专利复审委提出专利无效宣告请求，同时提交了本案的二审证据8-10作为对比文件。但将该现有技术与涉案被控侵权方法相比较，现有技术并没有涉及草甘膦酸的合成，也没有公开草甘膦酸合成过程中水解产生尾气需要处理，更没有给出需对所产生的尾气进行三级处理步骤的启示。为此，专利复审委在无效审查决定中也明确认为，现有技术中没有给出将其与专利技术方案的区别技术特征应用到现有技术中以解决存在的技术问题的启示，且专利技术方案能够产生有益的技术效果，则该技术方案具有突出的实质性特点和显著的进步。故金帆达公司提出其使用的是现有技术的主张亦不能成立。关于争议焦点3，根据最高人民法院《关于民事诉讼证据的若干规定》第二条第一款的规定，当事人对自己提出的诉讼请求所依据的事实或者反驳对方诉讼请求所依据的事实有责任提供证据加以证明。新安公司指控金帆达公司自2003年至2007年的侵权行为，所主张的赔偿数额为5480万元，系根据金帆达公司草甘膦原粉的生产能力、回收氯甲烷比例、氯甲烷的销售价格计算出氯甲烷收入后，减去氯甲烷的回收成本后计算出损失数额。为支持其上述主张，新安公司向原审法院提供了其公司2005－2007年审计报告，金帆达公司的增值税发票、年度财务报表，氯甲烷回收率及计算方法、损失计算清单等证据。而金帆达公司在接到原审法院通知后，拒不提供其使用被控侵权方法获得的氯甲烷产品数量和收入。经审查，从原审法院调取的审计资料看，金帆达公司从2004年至2007年生产销售的氯甲烷产品毛利共计23308100.43元。同时根据金帆达公司向浙江省农药工业协会申报的2005年至2007年的草甘膦产量共计38475吨；根据二审浙江省禁化武办出具的证明，其申报的2005年至2007年的草甘膦产量为24237.28吨。依据上述两组数据，按照金帆达公司确定的草甘膦与氯甲烷成品的比例1：0.4以及审计报告中的平均氯甲烷单位毛利计算，该三年的累计获利大约在1500万元以上。虽然金帆达公司主张其氯甲烷的产量并非全部由被控侵权方法生产，还存在其他途径，但并没有提供证据予以佐证或加以区分，本院不予采信。同时，本院还注意到以下因素：1.新安公司的涉案专利为发明专利，曾获得中国专利优秀奖、国家科学技术进步二等奖、浙江省科学技术进步一等奖等荣誉，并被工业和信息化部列入国家草甘膦行业的推广技术，具有较高的创新程度和市场价值，同时该专利技术主要解决了排空尾气中存在的氯甲烷所带来的浪费和环境污染问题，也具有较高的社会价值和经济价值；2.金帆达公司的注册资本为9000万元，侵权的持续时间较长，情节较为恶劣。故综合上述因素，本院认为原审法院确定的2000万元赔偿数额合理。新安公司和金帆达公司对此提出的上诉理由均不能成立。综上，本院认为，新安公司的涉案发明专利权应受法律保护。金帆达公司未经专利权人许可，为生产经营目的使用与新安公司涉案专利方法相同的方法，构成专利侵权，应承担相应的侵权责任。原判在认定侵权成立的情况下，综合金帆达公司因侵权可能获得的利益等因素，酌情确定2000万元的赔偿数额并无不当。新安公司提出赔偿数额偏低的上诉理由不能成立，本院不予支持。金帆达公司提出的上诉理由均不能成立，本院亦不予支持。原判认定事实清楚，适用法律正确。依照《中华人民共和国民事诉讼法》第一百五十三条第一款第（一）项之规定，判决如下：驳回浙江新安化工集团股份有限公司、浙江金帆达生化股份有限公司的上诉，维持原判。本案二审案件受理费357600元，由新安公司负担215800元，金帆达公司负担141800元。本判决为终审判决。审　判　长　　王亦非代理审判员　　周卓华代理审判员　　陈　宇二〇一〇年九月六日书　记　员　　郝梦君'

case_reason = ''


fmt_content_r = fmt_content.replace('&amp;', '&').replace('&times;', '×').replace('&ldquo;', '“').\
            replace('&rdquo;', '”').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '“').\
            replace('&hellip;','…').replace('&middot;', '·').replace('&mdash;', '—').replace('&nbsp;', ' ')
zhengju = re.findall('证据.*', fmt_content_r)
kangbian = re.findall('现有技术抗辩.*', fmt_content_r)
wenxian = re.findall('参考文献.*', fmt_content_r)
duibi = re.findall('对比文件.*', fmt_content_r)
fujian = re.findall('附件.*', fmt_content_r)
fmt_content_n = fmt_content_r
if len(zhengju) > 0:
    fmt_content_n = fmt_content.replace(zhengju[0], '')
if len(kangbian) > 0:
    fmt_content_n = fmt_content.replace(kangbian[0], '')
if len(wenxian) > 0:
    fmt_content_n = fmt_content.replace(wenxian[0], '')
if len(duibi) > 0:
    fmt_content_n = fmt_content.replace(duibi[0], '')
if len(fujian) > 0:
    fmt_content_n = fmt_content.replace(fujian[0], '')
test_str_num = 'null'
if case_reason != '侵害商标专用权纠纷':
    data_num = []
    # ZL开头
    num_1_1 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]8[5-9][1-3]\d{5}\.?[\dＸｘXx×]?', fmt_content_n)
    num_1_2 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?8[5-9][1-3]\d{5}\.?[\dＸｘXx×]?', fmt_content_n)
    num_1_3 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?8[5-9][1-3]\d{5}\.?[\dＸｘXx×]?', fmt_content_n)
    num_1_4 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]9[0-9][1-3]\d{5}\.?[\dＸｘXx×]?', fmt_content_n)
    num_1_5 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?9[0-9][1-3]\d{5}\.?[\dＸｘXx×]?', fmt_content_n)
    num_1_6 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?9[0-9][1-3]\d{5}\.?[\dＸｘXx×]?', fmt_content_n)
    num_2_1 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]0[0-3][1-3]\d{5}\.?[\dＸｘXx×]?', fmt_content_n)
    num_2_2 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?0[0-3][1-3]\d{5}\.?[\dＸｘXx×]?', fmt_content_n)
    num_2_3 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?0[0-3][1-3]\d{5}\.?[\dＸｘXx×]?', fmt_content_n)
    num_2_4 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]200[3-9][1-3]\d{7}\.?[\dＸｘXx×]?', fmt_content_n)
    num_2_5 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?200[3-9][1-3]\d{7}\.?[\dＸｘXx×]?', fmt_content_n)
    num_2_6 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?200[3-9][1-3]\d{7}\.?[\dＸｘXx×]?', fmt_content_n)
    num_3_1 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]201[0-9][1-3]\d{7}\.?[\dＸｘXx×]?', fmt_content_n)
    num_3_2 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?201[0-9][1-3]\d{7}\.?[\dＸｘXx×]?', fmt_content_n)
    num_3_3 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?201[0-9][1-3]\d{7}\.?[\dＸｘXx×]?', fmt_content_n)
    num_3_4 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]2020[1-3]\d{7}\.?[\dＸｘXx×]?', fmt_content_n)
    num_3_5 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?2020[1-3]\d{7}\.?[\dＸｘXx×]?', fmt_content_n)
    num_3_6 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?2020[1-3]\d{7}\.?[\dＸｘXx×]?', fmt_content_n)

    num_3_7 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]8[5-9][1-3]\d{1}[ＸｘXx×]{4}\.?[\dＸｘXx×]?', fmt_content_n)
    num_3_8 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc][LＬlｌNＮｎn]8[5-9][1-3]\d{1}[ＸｘXx×]{4}\.?[\dＸｘXx×]?', fmt_content_n)
    num_3_9 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc][LＬlｌNＮｎn]8[5-9][1-3]\d{1}[ＸｘXx×]{4}\.?[\dＸｘXx×]?', fmt_content_n)

    num_3_10 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]9[0-9][1-3]\d{1}[ＸｘXx×]{4}\.?[\dＸｘXx×]?', fmt_content_n)
    num_3_11 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc][LＬlｌNＮｎn]9[0-9][1-3]\d{1}[ＸｘXx×]{4}\.?[\dＸｘXx×]?', fmt_content_n)
    num_3_12 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc][LＬlｌNＮｎn]9[0-9][1-3]\d{1}[ＸｘXx×]{4}\.?[\dＸｘXx×]?', fmt_content_n)

    num_4_1 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]200[3-9][1-3]\d{3}[ＸｘXx×]{4}\.?[\dＸｘXx×]?', fmt_content_n)
    num_4_2 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?200[3-9][1-3]\d{3}[ＸｘXx×]{4}\.?[\dＸｘXx×]?', fmt_content_n)
    num_4_3 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?200[3-9][1-3]\d{3}[ＸｘXx×]{4}\.?[\dＸｘXx×]?', fmt_content_n)
    num_4_4 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]201[0-9][1-3]\d{3}[ＸｘXx×]{4}\.?[\dＸｘXx×]?', fmt_content_n)
    num_4_5 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?201[0-9][1-3]\d{3}[ＸｘXx×]{4}\.?[\dＸｘXx×]?', fmt_content_n)
    num_4_6 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?201[0-9][1-3]\d{3}[ＸｘXx×]{4}\.?[\dＸｘXx×]?', fmt_content_n)
    num_5_1 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn]2020[1-3]\d{3}[ＸｘXx×]{4}\.?[\dＸｘXx×]?', fmt_content_n)
    num_5_2 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?2020[1-3]\d{3}[ＸｘXx×]{4}\.?[\dＸｘXx×]?', fmt_content_n)
    num_5_3 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?2020[1-3]\d{3}[ＸｘXx×]{4}\.?[\dＸｘXx×]?', fmt_content_n)
    num_5_4 = re.findall('[ZＺzｚCＣｃc][LＬlｌNＮｎn][ＸｘXx×]{8,12}\.?[\dＸｘXx×]?', fmt_content_n)
    num_5_5 = re.findall('专利号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[ＸｘXx×]{12}\.?[\dＸｘXx×]?', fmt_content_n)
    num_5_6 = re.findall('申请号为?是?\s?:?[ZＺzｚCＣｃc]?[LＬlｌNＮｎn]?[ＸｘXx×]{12}\.?[\dＸｘXx×]?', fmt_content_n)




    # 第开头
    num_6_1 = re.findall('第8[5-9][1-3]\d{5}\.?[\dＸｘXx×]?号、?名?称?为?“[^”，；。]+”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?',
                         fmt_content_n)
    num_6_2 = re.findall('第9[0-9][1-3]\d{5}\.?[\dＸｘXx×]?号、?名?称?为?“[^”，；。]+”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?',
                         fmt_content_n)
    num_6_3 = re.findall('第0[0-3][1-3]\d{5}\.?[\dＸｘXx×]?号、?名?称?为?“[^”，；。]+”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?',
                         fmt_content_n)
    num_6_4 = re.findall('第200[3-9][1-3]\d{7}\.?[\dＸｘXx×]?号、?名?称?为?“[^”，；。]+”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?',
                         fmt_content_n)
    num_6_5 = re.findall('第201[0-9][1-3]\d{7}\.?[\dＸｘXx×]?号、?名?称?为?“[^”，；。]+”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?',
                         fmt_content_n)
    num_6_6 = re.findall('第2020[1-3]\d{7}\.?[\dＸｘXx×]?号、?名?称?为?“[^”，；。]+”的?涉?案?专?利?发?明?实?用?新?型?外?观?申?请?', fmt_content_n)

    # 专利名称
    data_name = []
    # name_1_1 = re.findall('“.*?”，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}发明',fmt_content_n)
    name_1_1_1 = re.findall('“[^”，；。]+”发明', fmt_content_n)
    name_1_1_2 = re.findall('“[^”，；。]+”、发明', fmt_content_n)
    name_1_1_3 = re.findall('“[^”，；。]+”，发明', fmt_content_n)
    name_1_1_4 = re.findall('“[^”，；。]+”涉案发明', fmt_content_n)
    name_1_1_5 = re.findall('“[^”，；。]+”的发明', fmt_content_n)
    # name_1_2 = re.findall('“.*?”，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}实用新型',fmt_content_n)
    name_1_2_1 = re.findall('“[^”，；。]+”实用新型', fmt_content_n)
    name_1_2_1 = re.findall('"[^”，；。]+"实用新型', fmt_content_n)
    name_1_2_2 = re.findall('“[^”，；。]+”、实用新型', fmt_content_n)
    name_1_2_3 = re.findall('“[^”，；。]+”，实用新型', fmt_content_n)
    name_1_2_4 = re.findall('“[^”，；。]+”涉案实用新型', fmt_content_n)
    name_1_2_5 = re.findall('“[^”，；。]+”的实用新型', fmt_content_n)
    # name_1_3 = re.findall('“.*?”，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}外观',fmt_content_n)
    name_1_3_1 = re.findall('“[^”，；。]+”外观', fmt_content_n)
    name_1_3_2 = re.findall('“[^”，；。]+”、外观', fmt_content_n)
    name_1_3_3 = re.findall('“[^”，；。]+”，外观', fmt_content_n)
    name_1_3_4 = re.findall('“[^”，；。]+”涉案外观', fmt_content_n)
    name_1_3_5 = re.findall('“[^”，；。]+”的外观', fmt_content_n)
    # name_1_4 = re.findall('“.*?”，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}专利',fmt_content_n)
    name_1_4_1 = re.findall('“[^”，；。]+”专利', fmt_content_n)
    name_1_4_2 = re.findall('“[^”，；。]+”、专利', fmt_content_n)
    name_1_4_3 = re.findall('“[^”，；。]+”，专利', fmt_content_n)
    name_1_4_4 = re.findall('“[^”，；。]+”涉案专利', fmt_content_n)
    name_1_4_5 = re.findall('“[^”，；。]+”的专利', fmt_content_n)
    # name_1_5 = re.findall('“.*?”，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}申请',fmt_content_n)
    name_1_5_1 = re.findall('“[^”，；。]+”申请', fmt_content_n)
    name_1_5_2 = re.findall('“[^”，；。]+”、申请', fmt_content_n)
    name_1_5_3 = re.findall('“[^”，；。]+”，申请', fmt_content_n)
    name_1_5_4 = re.findall('“[^”，；。]+”涉案申请', fmt_content_n)
    name_1_5_5 = re.findall('“[^”，；。]+”的申请', fmt_content_n)

    # name_2_1 = re.findall('发明名{0,1}称{0,1}为{0,1}”.*?”',fmt_content_n)
    name_2_1_1 = re.findall('发明“[^”，；。]+”', fmt_content_n)
    name_2_1_2 = re.findall('发明名称“[^”，；。]+”', fmt_content_n)
    name_2_1_3 = re.findall('发明为“[^”，；。]+”', fmt_content_n)
    name_2_1_4 = re.findall('发明名称为“[^”，；。]+”', fmt_content_n)
    # name_2_2 = re.findall('实用新型名{0,1}称{0,1}为{0,1}”.*?”',fmt_content_n)
    name_2_2_1 = re.findall('实用新型“[^”，；。]+”', fmt_content_n)
    name_2_2_2 = re.findall('实用新型名称“[^”，；。]+”', fmt_content_n)
    name_2_2_3 = re.findall('实用新型为“[^”，；。]+”', fmt_content_n)
    name_2_2_4 = re.findall('实用新型名称为“[^”，；。]+”', fmt_content_n)
    # name_2_3 = re.findall('外观设计名{0,1}称{0,1}为{0,1}”.*?”',fmt_content_n)
    name_2_3_1 = re.findall('外观设计“[^”，；。]+”', fmt_content_n)
    name_2_3_2 = re.findall('外观设计名称“[^”，；。]+”', fmt_content_n)
    name_2_3_3 = re.findall('外观设计为“[^”，；。]+”', fmt_content_n)
    name_2_3_4 = re.findall('外观设计名称为“[^”，；。]+”', fmt_content_n)
    # name_2_4 = re.findall('专利名{0,1}称{0,1}为{0,1}”.*?”',fmt_content_n)
    name_2_4_1 = re.findall('专利“[^”，；。]+”', fmt_content_n)
    name_2_4_2 = re.findall('专利名称“[^”，；。]+”', fmt_content_n)
    name_2_4_3 = re.findall('专利为“[^”，；。]+”', fmt_content_n)
    name_2_4_4 = re.findall('专利名称为“[^”，；。]+”', fmt_content_n)
    # name_2_5 = re.findall('申请名{0,1}称{0,1}为{0,1}”.*?”',fmt_content_n)
    name_2_5_1 = re.findall('申请“[^”，；。]+”', fmt_content_n)
    name_2_5_2 = re.findall('申请名称“[^”，；。]+”', fmt_content_n)
    name_2_5_3 = re.findall('申请为“[^”，；。]+”', fmt_content_n)
    name_2_5_4 = re.findall('申请名称为“[^”，；。]+”', fmt_content_n)

    name_3_1 = re.findall('名称为“[^”，；。]+”（专利', fmt_content_n)
    name_3_2 = re.findall('名称为“[^”，；。]+”（发明', fmt_content_n)
    name_3_3 = re.findall('名称为“[^”，；。]+”（实用新型', fmt_content_n)
    name_3_4 = re.findall('名称为“[^”，；。]+”（外观设计', fmt_content_n)
    name_3_5 = re.findall('名称为“[^”，；。]+”（申请', fmt_content_n)

    # name_4_1 = re.findall('《.*?》，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}发明',fmt_content_n)
    name_4_1_1 = re.findall('《[^》，；。]+》发明', fmt_content_n)
    name_4_1_2 = re.findall('《[^》，；。]+》、发明', fmt_content_n)
    name_4_1_3 = re.findall('《[^》，；。]+》，发明', fmt_content_n)
    name_4_1_4 = re.findall('《[^》，；。]+》涉案发明', fmt_content_n)
    name_4_1_5 = re.findall('《[^》，；。]+》的发明', fmt_content_n)
    # name_4_2 = re.findall('《[^》，；。]+》，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}实用新型',fmt_content_n)
    name_4_2_1 = re.findall('《[^》，；。]+》实用新型', fmt_content_n)
    name_4_2_2 = re.findall('《[^》，；。]+》、实用新型', fmt_content_n)
    name_4_2_3 = re.findall('《[^》，；。]+》，实用新型', fmt_content_n)
    name_4_2_4 = re.findall('《[^》，；。]+》涉案实用新型', fmt_content_n)
    name_4_2_5 = re.findall('《[^》，；。]+》的实用新型', fmt_content_n)
    # name_4_3 = re.findall('《[^》，；。]+》，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}外观',fmt_content_n)
    name_4_3_1 = re.findall('《[^》，；。]+》外观', fmt_content_n)
    name_4_3_2 = re.findall('《[^》，；。]+》、外观', fmt_content_n)
    name_4_3_3 = re.findall('《[^》，；。]+》，外观', fmt_content_n)
    name_4_3_4 = re.findall('《[^》，；。]+》涉案外观', fmt_content_n)
    name_4_3_5 = re.findall('《[^》，；。]+》的外观', fmt_content_n)
    # name_4_4 = re.findall('《[^》，；。]+》，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}专利',fmt_content_n)
    name_4_4_1 = re.findall('《[^》，；。]+》专利', fmt_content_n)
    name_4_4_2 = re.findall('《[^》，；。]+》、专利', fmt_content_n)
    name_4_4_3 = re.findall('《[^》，；。]+》，专利', fmt_content_n)
    name_4_4_4 = re.findall('《[^》，；。]+》涉案专利', fmt_content_n)
    name_4_4_5 = re.findall('《[^》，；。]+》的专利', fmt_content_n)
    # name_4_5 = re.findall('《[^》，；。]+》，{0,1}、{0,1}的{0,1}涉{0,1}案{0,1}申请',fmt_content_n)
    name_4_5_1 = re.findall('《[^》，；。]+》申请', fmt_content_n)
    name_4_5_2 = re.findall('《[^》，；。]+》、申请', fmt_content_n)
    name_4_5_3 = re.findall('《[^》，；。]+》，申请', fmt_content_n)
    name_4_5_4 = re.findall('《[^》，；。]+》涉案申请', fmt_content_n)
    name_4_5_5 = re.findall('《[^》，；。]+》的申请', fmt_content_n)

    # name_5_1 = re.findall('发明名{0,1}称{0,1}为{0,1}《[^》，；。]+》',fmt_content_n)
    name_5_1_1 = re.findall('发明《[^》，；。]+》', fmt_content_n)
    name_5_1_2 = re.findall('发明名称《[^》，；。]+》', fmt_content_n)
    name_5_1_3 = re.findall('发明为《[^》，；。]+》', fmt_content_n)
    name_5_1_4 = re.findall('发明名称为《[^》，；。]+》', fmt_content_n)
    # name_5_2 = re.findall('实用新型名{0,1}称{0,1}为{0,1}《[^》，；。]+》',fmt_content_n)
    name_5_2_1 = re.findall('实用新型《[^》，；。]+》', fmt_content_n)
    name_5_2_2 = re.findall('实用新型名称《[^》，；。]+》', fmt_content_n)
    name_5_2_3 = re.findall('实用新型为《[^》，；。]+》', fmt_content_n)
    name_5_2_4 = re.findall('实用新型名称为《[^》，；。]+》', fmt_content_n)
    # name_5_3 = re.findall('外观设计名{0,1}称{0,1}为{0,1}《[^》，；。]+》',fmt_content_n)
    name_5_3_1 = re.findall('外观设计《[^》，；。]+》', fmt_content_n)
    name_5_3_2 = re.findall('外观设计名称《[^》，；。]+》', fmt_content_n)
    name_5_3_3 = re.findall('外观设计为《[^》，；。]+》', fmt_content_n)
    name_5_3_4 = re.findall('外观设计名称为《[^》，；。]+》', fmt_content_n)
    # name_5_4 = re.findall('专利名{0,1}称{0,1}为{0,1}《[^》，；。]+》',fmt_content_n)
    name_5_4_1 = re.findall('专利《[^》，；。]+》', fmt_content_n)
    name_5_4_2 = re.findall('专利名称《[^》，；。]+》', fmt_content_n)
    name_5_4_3 = re.findall('专利为《[^》，；。]+》', fmt_content_n)
    name_5_4_4 = re.findall('专利名称为《[^》，；。]+》', fmt_content_n)
    # name_5_5 = re.findall('申请名{0,1}称{0,1}为{0,1}《[^》，；。]+》',fmt_content_n)
    name_5_5_1 = re.findall('申请《[^》，；。]+》', fmt_content_n)
    name_5_5_2 = re.findall('申请名称《[^》，；。]+》', fmt_content_n)
    name_5_5_3 = re.findall('申请为《[^》，；。]+》', fmt_content_n)
    name_5_5_4 = re.findall('申请名称为《[^》，；。]+》', fmt_content_n)

    name_6_1 = re.findall('名称为《[^》，；。]+》（专利', fmt_content_n)
    name_6_2 = re.findall('名称为《[^》，；。]+》（发明', fmt_content_n)
    name_6_3 = re.findall('名称为《[^》，；。]+》（实用新型', fmt_content_n)
    name_6_4 = re.findall('名称为《[^》，；。]+》（外观设计', fmt_content_n)
    name_6_5 = re.findall('名称为《[^》，；。]+》（申请', fmt_content_n)