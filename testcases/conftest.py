from pytest import fixture
from itchat import Core
from utilities.wechat_bot import WechatBot

@fixture(name='core', scope='session')
def _core():
    core = Core()
    core.auto_login(enableCmdQR=2, statusStorageDir='wxpy.pkl', hotReload=True)
    return core
