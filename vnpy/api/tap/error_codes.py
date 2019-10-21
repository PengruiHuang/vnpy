error_map = {
    0: None,
    -1: "连接服务失败",
    -2: "链路认证失败",
    -3: "主机地址不可用",
    -4: "发送数据错误",
    -5: "测试编号不合法",
    -6: "没准备好测试网络",
    -7: "当前网络测试还没结束",
    -8: "没用可用的接入前置",
    -9: "数据路径不可用",
    -10: "重复登录",
    -11: "内部错误",
    -12: "上一次请求还没有结束",
    -13: "输入参数非法",
    -14: "授权码不合法",
    -15: "授权码超期",
    -16: "授权码类型不匹配",
    -17: "API还没有准备好",
    -18: "UDP端口监听失败",
    -19: "UDP正在监听",
    -20: "接口未实现",
    -21: "每次登陆只允许调用一次",
    -22: "超过下单频率。",
    -10000: "输入数据为NULL",
    -10001: "输入错误的:TAPIYNFLAG",
    -10002: "输入错误的:TAPILOGLEVEL",
    -10003: "输入错误的:TAPICommodityType",
    -10004: "输入错误的:TAPICallOrPutFlagType",
    -12001: "输入错误的:TAPIAccountType",
    -12003: "输入错误的:TAPIAccountState",
    -12004: "输入错误的:TAPIAccountFamilyType",
    -12005: "输入错误的:TAPIOrderTypeType",
    -12006: "输入错误的:TAPIOrderSourceType",
    -12007: "输入错误的:TAPITimeInForceType",
    -12008: "输入错误的:TAPISideType",
    -12009: "输入错误的:TAPIPositionEffectType",
    -12010: "输入错误的:TAPIHedgeFlagType",
    -12011: "输入错误的:TAPIOrderStateType",
    -12012: "输入错误的:TAPICalculateModeType",
    -12013: "输入错误的:TAPIMatchSourceType",
    -12014: "输入错误的:TAPIOpenCloseModeType",
    -12015: "输入错误的:TAPIFutureAlgType",
    -12016: "输入错误的:TAPIOptionAlgType",
    -12017: "输入错误的:TAPIBankAccountLWFlagType",
    -12021: "输入错误的:TAPIMarginCalculateModeType",
    -12022: "输入错误的:TAPIOptionMarginCalculateModeType",
    -12023: "输入错误的:TAPICmbDirectType",
    -12024: "输入错误的:TAPIDeliveryModeType",
    -12025: "输入错误的:TAPIContractTypeType",
    -12035: "输入错误的:TAPITacticsTypeType",
    -12036: "输入错误的:TAPIORDERACT",
    -12041: "输入错误的:TAPITriggerConditionType",
    -12042: "输入错误的:TAPITriggerPriceTypeType",
    -12043: "输入错误的:TAPITradingStateType",
    -12044: "输入错误的:TAPIMarketLevelType",
    -12045: "输入错误的:TAPIOrderQryTypeType",
    1: "主动断开",
    2: "被动断开",
    3: "读错误",
    4: "写错误",
    5: "缓冲区满",
    6: "异步操作错误",
    7: "解析数据错误",
    8: "连接超时",
    9: "初始化失败",
    10: "已经连接",
    11: "工作线程已结束",
    12: "操作正在进行，请稍后重试",
    13: "心跳检测失败",
    10001: "登录过程执行错误",
    10002: "登录用户不存在",
    10003: "需要进行动态认证",
    10004: "登录用户未授权",
    10005: "登录模块不正确",
    10006: "需要强制修改密码",
    10007: "登录状态禁止登陆",
    10008: "登录密码不正确",
    10009: "没有该模块登录权限",
    10010: "登录数量超限",
    10011: "登录用户不在服务器标识下可登录用户列表中",
    10012: "登录用户已被冻结",
    10013: "密码错误，用户冻结",
    10014: "客户状态不允许登录",
    10015: "需要进行二次认证",
    10016: None,
    10017: None,
    10018: "登录用户密码超过有效天数",
    10101: "登录用户信息查询失败",
    11001: "数据库操作失败",
    11501: "登录用户下属所有资金账号查询失败",
    11701: "登录用户密码修改失败",
    11702: "登录用户密码修改失败——原始密码错误",
    11703: "登录用户密码修改失败——不能与前n次密码相同",
    11704: "新密码不符合密码复杂度要求",
    20201: "资金账号信息查询失败",
    20701: "客户交易编码查询失败",
    22801: "合约信息查询失败",
    22901: "特殊期权标的查询失败",
    25501: "品种委托类型查询失败",
    25601: "品种委托时间有效性查询失败",
    28901: "用户下单频率查询失败",
    60001: "资金账号不存在",
    60002: "资金账号状态不正确",
    60003: "资金账号交易中心不一致",
    60004: "资金账号无期权交易权限",
    60005: "资金账号无品种交易权限",
    60006: "资金账号无开仓权限",
    60007: "资金账号风控项检查失败",
    60011: "下单无效的合约",
    60021: "客户权限禁止交易",
    60022: "客户品种分组禁止交易",
    60023: "客户合约特设禁止交易",
    60024: "系统权限禁止交易",
    60031: "持仓量超过最大限制",
    60032: "下单超过单笔最大量",
    60033: "下单合约无交易路由",
    60034: "委托价格超出偏离范围",
    60035: "超过GiveUp最大持仓量",
    60036: "下单自动审核失败",
    60037: "LME未准备就绪",
    60038: "平仓方式错误",
    60039: "下单对应的父账号资金不足",
    60040: "互换单的合约格式错误",
    60051: "下单资金不足",
    60052: "手续费参数错误",
    60053: "保证金参数错误",
    60061: "撤单无此系统号",
    60062: "此状态不允许撤单",
    60063: "录单不允许撤单",
    60071: "此状态不允许改单",
    60072: "人工单不允许改单",
    60081: "已删除报单不能转移",
    60082: "人工单不允许改单",
    60091: "录单重复",
    60092: "保证金参数错误",
    60100: "操作账号只可查询",
    60101: "合约行情价格修改失败",
    60102: "即使子帐号又是做市商不能应价",
    60103: "下单找不到交易编码",
    60104: "操作账号只可开仓",
    60105: "操作账号没有上期挂单查询权限",
    60106: "限期有效单不能小于当前交易日",
    60107: "该编码不允许申请或拆分组合",
    60108: "非本服务器标记下的账号不允许操作",
    60109: "行权或弃权量超过可用量",
    60110: "没有订单审核权限",
    60111: "下单超过上手单笔最大量",
    60115: "非大连应价单不允许两笔委托量不一致",
    60117: "申请不允许重复提交",
    60118: "超过账号下单频率限制",
    60119: "组合表不存在的组合方向或投保标志",
    61001: "订单操作频率过高",
    61002: "委托查询返回前不能进行下次查询",
    72001: "超过行情最大总订阅数",
    72002: "超过该交易所行情最大订阅数",
    72101: "没有该行情的订阅权限",
    72102: "没有该交易所下行情的订阅权限",
    72103: "品种不存在",
    72104: "合约可能不存在",
    83001: "不支持的行情协议",
    14001: "二次验证失败",
    14002: "二次验证超时",
    11000: "数据库连接失败",
    11002: "不允许一对多",
    11003: "删除失败-存在关联信息，",
    11004: "删除分组失败-分组有下属或在操作员下属中",
    12001: "登录用户密码修改失败-原始密码错误",
    12002: "登录用户密码修改失败-不能与前n次密码相同",
    12003: "登录用户密码修改失败-新密码不符合密码复杂度要求",
    13001: "一个币种组只能设置一个基币",
    13002: "基币只能是美元或港币",
    60012: "LME未准备就绪",
    60013: "不支持的下单类型",
    60014: "错误的埋单类型",
    60015: "不合法的委托类型",
    60025: "客户权限只可平仓",
    60026: "客户合约特设只可平仓",
    60027: "系统权限只可平仓",
    60028: "只可平仓提前天数限制只可平仓",
    60029: "客户品种风控权限禁止交易",
    60030: "客户品种风控权限只可平仓",
    60041: "未登录网关",
    60042: "未找到网关信息",
    60054: "总基币资金不足",
    60055: "超过保证金额度",
    60056: "总基币超过开仓比例限制",
    60057: "独立币种组超过开仓比例限制",
    60058: "风险阵列参数错误",
    60073: "风险报单不允许改单",
    60074: "成交量大于改单量",
    60075: "预埋单不允许改单",
    60112: "下单超过上手最大持仓量",
    60121: "开平方式错误",
    60122: "委托平仓持仓不足",
    60123: "成交平仓失败",
    60131: "未找到本地委托",
    60132: "与网关断开连接",
    60141: "录单成交重复",
    60142: "录单成交未找到对应委托",
    60143: "录单成交合约不存在",
    60144: "录单成交参数错误",
    60145: "录单成交委托状态错误",
    60151: "成交删除未找到成交",
    60152: "此状态成交不可删",
    60161: "不允许录入此状态订单",
    60162: "错误的修改订单请求",
    60163: "订单不可删，存在对应成交",
    60164: "不合法的委托状态",
    60165: "此状态不允许订单转移",
    60166: "订单不允许删除",
    60171: "做市商双边撤单未找到委托",
    60172: "做市商双边撤单客户不一致",
    60173: "做市商双边撤单品种不一致",
    60174: "做市商双边撤单合约不一致",
    60175: "做市商双边撤单买卖方向相同",
    60176: "做市商双边撤单买卖方向错误",
    60177: "做市商单边检查未通过",
    60181: "埋单激活失败，订单未找到",
    60182: "埋单激活失败，非有效状态",
    80001: "网关未就绪，未连接上手",
    80002: "品种错误",
    80003: "合约错误",
    80004: "报单字段有误",
    80005: "价格不合法",
    80006: "数量不合法",
    80007: "报单类型不合法",
    80008: "委托模式不合法",
    80009: "委托不存在（改单、撤单）",
    80010: "发送报单失败",
    80011: "被上手拒绝",
    90001: "前置不允许该模块登录",
    90002: "一次请求太多数据",
    90003: "前置没有所要数据",
    90004: "所查询的操作员信息不存在",
    90011: "前置与交易断开",
    90012: "前置与管理断开",
    90021: "下属资金账号不存在",
    90022: "该操作员不允许交易",
    90023: "查询频率过快",
    90024: "该授权不予许登录",
    90025: "自成交验证不通过",
    -23: "查询频率太快。",
    -24: "不符合调用条件。",
    -25: "改单撤单时没有找到对应订单。",
    -26: "日志路径为空。",
    -27: "打开日志文件失败",
    -28: "没有交易员登录权限",
    -29: "没有订单录入或者成交录入",
    -30: "没有订单修改和订单删除权限，成交删除权限",
    -31: "没有订单转移权限",
    -32: "成交录入时系统号为空",
    -33: "成交删除时成交号为空。",
    -34: "成交删除时没有找到对应的成交",
    -35: "订单修改时客户账号变动。",
    -36: "订单转移时客户账号没有变动",
    -37: "修改的电话密码位数不对或者包含特殊字符。",
    -38: "未绑定的二次认证信息",
    -39: "二次认证有效期内不能再申请二次认证码",
    -40: "没有设置客户密码的权限。",
    -41: "风险保单单客户无法撤销或更改",
    -42: "改单是客户账号填写与订单客户账号不一致",
    -11001: "输入错误的:TAPIBucketDateFlag",
    -11002: "输入错误的:TAPIHisQuoteType",
    -12002: "输入错误的:TAPIUserTypeType",
    -12018: "输入错误的:TAPIBankAccountStateType",
    -12019: "输入错误的:TAPIBankAccountSwapStateType",
    -12020: "输入错误的:TAPIBankAccountTransferStateType",
    -12026: "输入错误的:TAPIPartyTypeType",
    -12027: "输入错误的:TAPIPartyCertificateTypeType",
    -12028: "输入错误的:TAPIMsgReceiverType",
    -12029: "输入错误的:TAPIMsgTypeType",
    -12030: "输入错误的:TAPIMsgLevelType",
    -12031: "输入错误的:TAPITransferDirectType",
    -12032: "输入错误的:TAPITransferStateType",
    -12033: "输入错误的:TAPITransferTypeType",
    -12034: "输入错误的:TAPITransferDeviceIDType",
    -12037: "输入错误的:TAPIBillTypeType",
    -12038: "输入错误的:TAPIBillFileTypeType",
    -12039: "输入错误的:TAPIOFFFlagType",
    -12040: "输入错误的:TAPICashAdjustTypeType",
    -12046: "输入错误的: ClientID，ClientID包含特殊字符。",
    -13001: "历史行情查询参数不合法",
    -13002: "价格和数量中包含NAN或者INF不合法的数值",
    -12047: "输入错误的到期日",
    -12048: "错误的密码类型",
    -12049: "错误的结算数据类型",
}
