#   --------------------------------注释&变量区--------------------------------
#   入口 https://app.zhuanbang.net/invite/7079
#   找请求头中NiuToken的值
#  NiuToken=**** 只要**** NiuToken=不要填 NiuToken=不要填 NiuToken=不要填
#   变量名：yuanshen_zb 多号@分割
#   --------------------------------一般不动区--------------------------------
#                     _ooOoo_
#                    o8888888o
#                    88" . "88
#                    (| -_- |)
#                     O\ = /O
#                 ____/`---'\____
#               .   ' \\| |// `.
#                / \\||| : |||// \
#              / _||||| -:- |||||- \
#                | | \\\ - /// | |
#              | \_| ''\---/'' | |
#               \ .-\__ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___\_<|>_/___.' >'"".
#        | | : `- \`.;`\ _ /`;.`/ - ` : | |
#          \ \ `-. \_ __\ /__ _/ .-` / /
#  ======`-.____`-.___\_____/___.-`____.-'======
#                     `=---='
# 
#  .............................................
#           佛祖保佑             永无BUG
#           佛祖镇楼             BUG辟邪
#佛曰:  
#        写字楼里写字间，写字间里程序员；  
#        程序人员写程序，又拿程序换酒钱。  
#        酒醒只在网上坐，酒醉还来网下眠；  
#        酒醉酒醒日复日，网上网下年复年。  
#        但愿老死电脑间，不愿鞠躬老板前；  
#        奔驰宝马贵者趣，公交自行程序员。  
#        别人笑我忒疯癫，我笑自己命太贱；  
#        不见满街漂亮妹，哪个归得程序员？
#
#   --------------------------------代码区--------------------------------
qmvxw='''
cron: 30 10 * * *
new Env('望潮阅读抽奖');
群组：https://t.me/yangmaoxz
频道地址：https://t.me/ymxzpd

使用方法：
0.青龙控制面板，依赖管理安装python依赖：gmssl
0.青龙控制面板，依赖管理安装python依赖：gmssl
1.打开app，点击阅读有礼
2.抓包https://xmt.taizhou.com.cn/prod-api/user-read/app/login接口的id,sessionId,deviceId参数
3.配置文件添加
单账户：export wcread="[ {'name': 'xxx','aid': 'id', 'sid': 'sessionId', 'deviceId':'deviceId'}]"
多账户：export wcread="[
{'name': 'xxx','aid': 'xxxx', 'sid': 'xxxx', 'deviceId':'xxxx'},
{'name': 'xxx','aid': 'xxxx', 'sid': 'xxxx', 'deviceId':'xxxx'}
]"
参数说明：
bz:备注名随意填写
aid:2步骤中的id参数
sid:2步骤中的sessionId参数
deviceId:2步骤中的deviceId参数
'''
import lzma,base64
AnrcGzdaCYhvPxkyTINbwSFuLHVeJEKRipDOWlqoQfUmMBXtsj=base64.b64decode
AnrcGzdaCYhvPxkyTINbwSFuLHVeJEKRipDOWlqoQfUmMBXtsg=lzma.decompress
exec(AnrcGzdaCYhvPxkyTINbwSFuLHVeJEKRipDOWlqoQfUmMBXtsg(AnrcGzdaCYhvPxkyTINbwSFuLHVeJEKRipDOWlqoQfUmMBXtsj('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')))


