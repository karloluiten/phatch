# Phatch - Photo Batch Processor
# Copyright (C) 2007-2008 www.stani.be
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/
#
# Phatch recommends SPE (http://pythonide.stani.be) for editing python files.

# Embedded icon is taken from www.openclipart.org (public domain)

# Follows PEP8

from core import models
from lib.reverse_translation import _t

#---PIL


def init():
    global Image, ImageFilter, imtools
    from PIL import Image
    from PIL import ImageFilter
    from lib import imtools


def rnk(image, radius, rank=50, amount=100):
    """Apply a filter
    - amount: 0-1"""
    rank /= 100.0
    r = int((radius * radius - 1) * rank)
    image = imtools.convert_safe_mode(image)
    ranked = image.filter(ImageFilter.RankFilter(radius, r))
    if amount < 100:
        return imtools.blend(image, ranked, amount / 100)
    return ranked

#---Phatch


class Action(models.Action):
    """"""

    label = _t('Rank')
    author = 'Stani'
    email = 'spe.stani.be@gmail.com'
    init = staticmethod(init)
    pil = staticmethod(rnk)
    version = '0.1'
    tags = [_t('filter')]
    __doc__ = _t("Copies the rank'th pixel value")

    def interface(self, fields):
        fields[_t('Radius')] = self.RankSizeField(self.RANK_SIZES[0])
        fields[_t('Rank')] = self.SliderField(50, 0, 100)
        fields[_t('Amount')] = self.SliderField(100, 1, 100)

    icon = \
'x\xda\x01v\x0c\x89\xf3\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x000\x00\
\x00\x000\x08\x06\x00\x00\x00W\x02\xf9\x87\x00\x00\x00\x04sBIT\x08\x08\x08\
\x08|\x08d\x88\x00\x00\x0c-IDATh\x81\xed\x99k\x8c]\xd7U\xc7\x7f\xfb<\xee\xb9\
3\xf75c\x8f\xed\xb1\x9d\xd8N\xec\x986\x84\xd8NM\xe2\xa8q\xd4\xa4\x96\x08\x8f\
R\xd1*(B}%\x15\xaaB\xd5\xaa\xb4P\xa9\x02\tD!B\x88\x87\xe0\x0b\x02\tQ\xb5\x02\
Q\xc4\x17\xaa\x90\x86\x0f\x15\x12\xa9\xc0\x84<\x9c\x92\xb7\x13\xbb~e\xec\xf1\
\xbc\xee\xdc\xc79g\xbf\x16\x1f\xce\xb9w\xeeL\xc6\x1e;\r\x08\x89l\xe9?k\x9f{\
\xce\xec\xfd\xff\xaf\xb5\xcf\xda\x8f\x03\xef\x95\xf7\xca\xff\xef\xa2\xde\xcd\
\xc6\xea\xf5\x07\xb7LN>\xf0\xf1ju\xea\xde0\x8co\t\x02\xbf#\x08\xa4\xa9\x94\r\
\xc1\xe1=\xb9\xb5\xbam\x8c;kL\xf6b\x9a\x9e\xfe\xa7\xb9\xb9\xc7\x9e\x00\xe4\
\x9d\xf6\xf9n\x08P\xbbv}\xe3\x93cc[\x1f\xae\xd7\xa7\x8eT*\xf5j\x14)\x94\x12\
\xc0\xe3\xbd\xc7Z\x8b\xd6\x06k5"\x06\x11\x8dH\x8e\xf7\x19Z\xcf\xcf\xa6\xa9}\
\xbc\xd7{\xe5\xf7\xda\xed??\xf5\xbf*`\xe7\xce\xbf\xfcd\xab\xb5\xf7k\x8d\xc6\
\r\xef\xafVC\xaa\xd5\x90J% \x8a\x14a(\x88\xc8*\x01ijH\xd3\x8c<\xcf\x10\xd1x\
\x9f\ra\xccR\xda\xeb\xa5\xdf\xe9\xf7_\xfa|\xa7\xf3\xcd\xf9\xffQ\x01\xdb\xb7\
\xff\xee\xee[\xea\x93\x7fwp\xbc}\xd7\xb6\xa6U\xa7jw\xb18\xfe\x13T\xab\x01\
\xd5\xaa"\x8e\x07\x11\x10\x9c\xf3X\xeb\xc9\xf3B@\xbf\xaf\xe9t\xfat\xbbi\x19\
\x85\x14\xef3\x9c\xeb\xe1\\J\x9e\xb7///w\x7fmy\xf9\xb1o^\x0b\x97\xf0z\xc9\
\x1f\xda\xfa\xeb\x9f\xfa\xcc\xe4\xb9\'\x7fu\xec\xc9\x9b\xeeo\x9eQ\x87[\xf3\
\xdc\xd3z\x9d\x85[\x1a\xb4\xb6(Z-C\xb5\xda\xa0^\xaf0>\x1e2>\x1e\x91$\x8a8\
\x0e\x89\xa2\x800T\x84a\x00\x80\xd6\xbel\xd5S\xbc\x06\x1e\xa5\xa8\xc5\xb1\
\xfb\xf9 8\xb25\xcb\xbe\xff\xc4F|\xae+\x02\x1f\xdd\xf9\x89?~t\xdb\xc9/\xed\
\xb3\xa9\xaa4\x1a$\x13\x13D\xad\x16Q\xab\xc9\xf2/\xd6\xd9tg\r\xa5\xaa,-\xd5\
\x99\x9f\xdf\xcc\xfc\xfc\x04\x97/o\xe2\xcc\x99\x1d,/\xd7\xe8\xf5,\x9dNN\xa7c\
XZ\xea\xb3\xb4\xd4\xa3\xdb\xed\xe1}\x8aH\x8as}\xac\xedbm\x17c:t\xbb\xe9\xb7\
\x97\x97\xff\xe8\xa1\xabq\xba\xe6\x08<r\xe4C\x7f\xfd\xf9\xc9\xb3\x8f\xee\xca\
\x8c\xaaT*$\xad\x16\x95f\x93\xb8\xd9 j6\xb1\x87[\xd4\xa6\'\x08\xc3\x16\xe3\
\xe3u\xa6\xa6\x02n\xb8\xa1\xcf\xfe\xfd\x97\xb8\xed\xb6\xd7\xd8\xb2\xe5,I\xd2\
fy\xb9\x89\xb51"\x82s\x82\xd6\x0e\x11\x0f\xf8\xd2:D\n\x04\x81\xbe\r\xee\xdce\
\xcc\xf1\xef\xfcH\x02\xee\xdbu\xdf\xd7\xbe\xd8Z\xf8\xca\xb6\xaeP\x01\x92Z\
\x8dJ\xbd>$\xef6\xb5\x88?<A2\xdeB\xa9I\x94j\xa1T\x83 \xa8\xa1T\x858\x0e\x98\
\x9a\xea\xb2o\xdf9\xde\xf7\xbe\x17\x88\xe3Y\x16\x16\xaa\xf4zM\xb4\xb6\xa5\
\x087B\xde"b\xf1\xde\xa0T\xff\x80\xf7G\x16\x9c{\xfa\xe9w$\xa0V{p\xfa\x8b{/?\
\xfe\xe3\xa9\x0b*@\x0c\xc4\xf5:q\xadF\xd4\xa8\x136\x1ad\x07\x9a4\x0e6Qj\x92 \
\x98D\xa9\t\x94j\x02U\x94\x8a\xcb\x96\x04\xb0$I\xce\x9e=\xe79x\xf0i\x8c\xb9\
\xc4\xf9\xf3\xd3t\xbb\x01\xe0\xca(\xb82\xd5\x0eE(\xc8\xee\xd1z\xef\xb7\xe0\
\xe5\xceu\x0bx\xf8\xa6\x1b\x9f\xff\x98jO\r\xc9\x07AA\xbe^\'\xaa\x8d\xe3[u\
\xe4g\xea$\x13\xad\xd2\xf3\x93(5\x85R\x93@\x8cR\xbe$7\xc8\xff\x05\x82 e\xef\
\xde\xd3\xdc|\xf3q\xce\x9e\x85\x85\x85\x1d\x88\x18\xc0\xae\x8a\x80\xf7\x06\
\xe7\xfa\x89s\xcd[\xbd\x7f\xe6o\xd6\xf2\x0b\xaeF\xfe\xb6\xcd\x8f\xfc\xc2Gjs\
\xfb\x02@\x89\x14\x18\xd4\xcbg:\x87\xa1\xb1\xabH\x9bJ\xa9\xd2\'U`\x13JU\x81\
\x08\xa5\x02\x94RC\x00\xc3\xfa\xee\xddm\xbe\xf0\x85os\xd7]\xffH\x10@\x91W\
\x06\x18<\x17\x10Es\xc7\xe0\x97\x0e^\x97\x80{\x1b\xfa\x0f\xb7z\xcbh\xb38\x87\
\xf2\x1ee-\xed\xad\x96\xc6}v\xe8a\xc8\x80>\xd0\x06f\x80\x0e\x90\x02z\xe8]\
\xb0(e)Rg\x81J\xc5\xf2\xd0CO\xf1\xc0\x03\xdfB)3"v\x94\x9eD0\xfe\x1b\xd7,`r\
\xf2\xd1\xdbol\xb4o\x12Y\xb3L\xf1\x1e\x8caiR\x13~FS\xa9f@\xafD\x07X\x00.\x02\
\x17\x10\xb9\x04\xb4\x11\xe9\x94\xc22 /\xc7\xb8\x19\x8e\xf5A9z\xf4u\x8e\x1d\
\xfb\x07\x94\xd2\x05e\xf1\xab\xbaV\xea\xf2\xb1k\x16\xd0h\x1c\xfel3X*\xe7\xd3\
\x15\xa0\x14\xaf\x8c9.|\xdaP\xdf\x9e"\xd2G\xa4\x8bH\x1bX\x04.\x03\x97\x10\
\x99)\xedeD\x96\x10\xe9\xe0}\x17\xef\xfb\xc3\xd9\xb7@\x8e\x08C\x1c9\xf2\x06w\
\xdf\xfd\x04\xab\x1dW\xf4.\xd2\x99\x80\x8f\xff\xd4(\xcf\xe8J\x02*\x95\xca\
\xfd\xfd\xa0\x82w\x839\x12\xbcR<\xbe\xaf\xc6_=\xb8\x93\xddi\x95?Xl3\xbd\xa9[\
\x86\xda\xe3\xbdE\xa9\x14\xe8 \x12\x97^\xb4x?X2tp\xae[.\x1bzX\x9b\xe2\\\x8e\
\xf7\x94\x10D\xe0\xee\xbb_\xe7\xfc\xf91^y\xe5VD<"2"h\xf2#\xc0?o \xe0\xf6Z\
\x1c\x07\xfb\xbe7v\x88M\xc1\xbf\xb0=\xf7\x9c\x9d\xae\xf2\xd4\x1d\x13\xfc\xe0\
\xf0$>\x86\xd7\xa2\x88\xaf\x9fh\xf0\xd8\x9d\x1dZu!\x08,Ji\x94\xea\x03\t\x10"\
\xa2\xf0\xde\x96\x99$\xc3\xb9\xb4$^\xcc\xb4\xc5\xac+x\x0f\xce\xadX\xe7\x84\
\xa3G\x9feff\x9c\xd9\xd9\x89\xe1\xc4V\x14s\xeb\x86\x11\xd8\xb4\xe9\x9e\x0f*U\
\xad\x9e\xd7?\xc6\x9f~\xee4\xaa\x12@\x12BE\x81\x08\xca)\x0c\x86g\x92\x98\xdf\
|\xae\xceo\x1dXbs\xd3\xa0T\x86R\tJ\xc5\x88D\x88\x80\xf7Ed\xac\xd5X\x9b\xa2u\
\x1fc\xba\x18\xd3\xc5Z\x87s`\xad`\xad\x0c\xc9;\'T*\x9eC\x87\xfe\x93\'\x9f<\
\x8a\x88\xc7\xfb\x81\x00\xbbe\x94\xeb\xba\xef@\x18\xee\xd8/b\x91t\x12Yp\x88\
\x17p\x1e\x9c\xa0,(\x07\x81\x80\xb1\x96\x7f\x0bB\xbe\xfa|\x9d\x0b\xf3\x8bX;_\
b\x0ek\xe70f\x0ek\xe71\xa6@\x9e\xcfc\xcc"Y\xd6\xc6\x18\x8b1`\xed\x8a\x00k\
\x05c\xfc\xd0NO/\xb0k\xd7\x8b\xc3(\x96\x11\xa8o( \x08*\xcd"C(d\xa1\nV\x10\
\xeb\xc1\n\xca\x81r\x822\x108\xc0\n\'\x82\n_~\xbe\xc5\x9b3\xcbh=\x8f\xd6s\
\xe4\xf9,Z\xcf\x92\xe7\xb3\xe4\xf9\x1cY6G\x9e/\x90e]\x8c\x11\x8c\xa1\xb4\x05\
\xac\x15\xb4\xf6\xa5u\x18\xe3qN\xb8\xf9\xe67\x806\xde\x0f\xb2\xd5\xea\xb4\
\xb8\xae\x00\x11S\xf1\xbe\xdc=\xcdlB\xac\x03+`\x04\xac/\xa2`\x05e\x85\xc0A`\
\xe1\xcdh\x9c/\xbf\xb4\x95\x7f}\xbdO\x96\xcd\x93\xe7s\xe4\xf9<Y6O\x96-\x91\
\xe7)Z\x0b\xc6(\x8c\x81<\x17\xb4^\rcV\x8b\xc8s\xc7\xd8X\xca\xb6m\'Y\xd9uVz\
\x1b\n\xb06\xefx\xaf\xf1^#\x17\xb6\xe0\xb5C\x8cG\x8c[\x11\xe1\x84\xc0\x822\
\x85\r,\xccF5~\xe7\xad\xfd|\xe3\xd9Md\x99"\xcf\x15Z\x07\xa5U\xe49%\x8a\x08\
\x0c\x88\xe7\xb9G\xeb\x02y\xee\xc827R\xb7\xec\xd8q\x860LKv\xf1\xec\x86\x02\
\x9ck\x9fw\xae\xcc\xd337 s\n\xaf-\xa2\x0b\x11\xa2\x1dh\x0f\xda\xa3\x8c\x14V\
\x0bJ\x0b\x86\x80\xbf\xd57\xf0\xf5\xff\x98\xe6\xe2BH\x9e\xab\x12+\xe4\xf3\
\x1c\xb2\xcc\x97uO\x9e{\xd2\xb4 ^\\\x17\xde\x1fD!I\x0c\xdb\xb6]\x18P~e\x94\
\xeb\xba\x8b\xb9<\x97\x8b\x8d\xc6\xee\xaf(\x15\x05H\x8cR]\xd4\xf66 ()\x97\
\x14\xe5J@I\t_\xbc\xdc\x03;\xc38\xc7gj\xa8\xb6fg\xcd\x94\xde^\x19:\x03\xf2Y\
\xb6\x824u\xf4\xfb\xb6\xb4\x86^\xaf\x80\x08$I\xca\xc5\x8b\xd3\x88\xc4\xbf\r/\
\xbfqU\x01p!\x1d\x1f?\xfa\xcbA\xa0\x9a\x00,\xd7a\xf7\x9b\x10\x0b\x88\x1a\xee\
\x00\x95\x08\xb8\x12\xdeS,<\x8bk\xb1\x9e\xbe\x04\xbc\x905y\xf5lH\xcb\xe4\x8c\
G\xae$-W ^\x90\xef\xf5\x0c\xfd\xbe\xa5\xdf7\xc3mg\x928 \xc9\x16\x17\xbf\xff\
\xf0\x86\x11\x00\x88\xa2{?\x18E\xf6V\xa5\x14\xb81\xd0}\xd4\xf6v\x91R\x01\xbc\
\x94(\xebNV\xac\xf3E\xd62\x02V\x98\xf31\xcf,\x8e\xb30+4\\N \xa3\xc3\xc6\x0f\
\xc9\x0fl\xafg\xe8v\x0b\x11\xa3e\xf3\xe6\xa9\x1f\x9e:5\xffg\xd7$@\xe4\xfd\
\x8b\x95\n\x9f\x00\xa5@\xa0\xbd\x19i\x9e\x83\x9a\x01/\x88+\x16/R\xce\x0f2 ]Z\
\xb1\xbex\xf1m\x91\x00\xac\x13\xce\x99\n\xcf^\xaeri\xd6\x13g9\x11\x85\xc7\
\x07\xe4\xfb};\x1c6\xbd\x9eY\xc5\xc7\xda\x883gn\xfa\xd4\xe2\xe2\x85\x93\xa3\
\xbf_uS\xdfl~\xe9\xb5j5\xdc\x1f\x86U\xa2h\x8c\xa05O\xf0\xa1g\t\x9b!*\x0cP\
\x91B\x05AQ\x0f\xd4\xe82\x1e\x84B$\x85Xq\x1eo\x1db=\xde8H5;\xf3ev\x85]\xb6\
\x8c\xe5\xf4\xfb\x864\xb5t\xbb\x9a^\xcf\xe0\xdc\xeaUp\x92\xec\xb9\xf8\xdd\
\xef\xfep\xfbZ\x8eW\xdd\x91\x89\x1c^\n\xc3\xf4cE\xddA^C\xe6\x152=[\x0c\xa52\
\x12\xbe\xf4\xb2\xb8\xd2\xeb\xc6\x0fS\xaf\xd7\x16\x9f;\xbc\xb6\xb8\xdc\xe2\
\xb2\x02&\xb7\xcci8\xd9\x8dy\xed-a~\xc1\x90wr\x9c.\x16w\xaby\x8c\xc9\xf9\xf3\
\xdb\x7fnnn\xf6\xccZ\x8e\x1b\x1e\xabT\xab\xbf\xf2\xefI\x92\x1d\t\xc3*a\x98\
\x10\x86\x15\x82\xed\xa7\x08\x0e\x9f!H\x82"\x02Q\xb9\xf9\x18mM\x8a?\xe2\x05o\
\xfd0\x02\xbe\x8c\x80\xd3\x16\xa7-6\xd7\xd8\xdc`R\x8d\xedkj\xce\xd0\x8a\x1c\
\xcd\xc82\x19;\xaa\x89`\xed\xc1\'\x9ez\xea\xc4\xcf\xae\xc7\xef\x1a\xce\x85\
\x1e\xda\x93$\xe1\x0f\xe28h\x84aeE\xc4\x96s\xa8\xdbO\x13\xd4\x14*T\xc5\x10Z\
\xd3\x9cx\x8f\xf8B\xc4\x8a\x00\x87\xd3\x0eg,63\xd8\xdc`s\x8d7\xfem=+/l\t[\
\x97g\x9f;\xb3\xf5J\xec\xae\xe1X\xe5\xc5%\xe7>pZ\xa4\xf3Q\xefu(\xe2\xf0\xde \
\xbd\x06\xfe\xe2\x18\xbe\xb2\x80\x8fs|I\xca\x1b\x8f\xd3\xa6\xf0pn\xf1\xda\
\x15^N\r6\xd3\xd8Lc\xd2\x026\xd3\x98\xbe^\xc9lk\x8bL\xb5{\'v\xec\x81s\xfaG\
\x10\x00p\xe2E\xef\x8f.;w\xf9\x98\xf7&\xf0\xde\xe2\x9c\xc6\xe71\xfe\xad)\xdc\
r\x86K\xda8gp\xa6\x1c\x1a\x99\xc1\xe5\x03/\xaf#\xa0\xaf\xf1\xf6\xed^\x1f\x96\
hb\x997\xa7\x0e\x91\x1f\xbft5f\xd7y\xb8\xfb\xd9\xcf\xc1\xcc\x9f@6\xa6TD\x18\
\xc6\xe5\x89CHP\xed\xc1\xf4\x05\xd8\xda.\xce_\x84b\'\xe5=\xde\xf9\xe2ew\xae\
\xccL\x1b\x94p\xeb9NV\x0e\xd0\xfe\xaf\xc5\x8d\x1e\xddH@@A\xa7R"\x82\x0f\xff$\
\xb4\xfe\x02\x96v\xac\xdb\\\xd4\x87\x89yh-B\xc3\x14\xd3\xc8F\xc5\n\xf4\x12\
\xf05\xc7\xc4\xc4\xf78\xf1\xdc#\x0c\x8e0\x8a\xe3\x8e\x815k\xffu\xbd\xd6\x03\
\x8a\x83\x9d\xb1\x11\xf2\xf1\x1a$\xf0\xe0W\xa1\xfb\xd3\x90\'W$\x16\xf6a\xbc\
\x0bI\x06\x91\x83\xd0\x95K\x11\x05.\x02]\x81\xbc\x02y\xc3#;^\x86\x13\xbf\x0f\
\xaf\xbd1BX\x8f\x10_[\xd7\x14-\xad*c@\x8d\x15\x8f\x0f\x10\xaf\xff\xdb\xc4\
\x14\xdc\xffi\xb0w@\xa7~\xfd\x9f\x1b*\x1aZ\'\xe1\x85\xbf\x87W_\x1d!6\x80Ys\
\x9d\xaf}f\xb4\xc7\x08h\x8d\x10L\xd6\x10O\xd6\x111r\xef\xc0\x07`\xef\x1d 7B\
\xda\x84,.\xc6\xcf\xa0\x0b\'P\xb5EH\xd4\x1c\\|\t\x9e>\x0e\xb6[\x123k\x08\xae\
%\xbb\xee\xbdQ\x01\nh\x94QX\xcf\xeb\xf1:\xbf\xc7#\xd7QY\x8fJ$\xb0e;\x04\t\
\x88\x83\xd9\x99\xb2S\xc7\xea\xf1=\x8a\xf5\xbc~\xa5\x88\xe4k\x05\x0c\xe3J1\
\x8c\x06\x11X\x0fk\xc9F\x14)y\x14\x01o\x1fS\xc3#\xa6\x12\x031\x83\xb3\xc9\
\xf5^\xda\xf5\xc4\r\x85\\m\xd0\x0e2PR"\xe2\xed\x84G\x89\x07k\x88\xaf>\xa5]}\
\xc0w5!\x031\xa3\xa2\xd6\n\x1aN \xd7\xfb\xd6\x05#\xa4cV{\\\x95\xf7G\x05\x8c\
\xf6!#vT\x800\xf88\xb0"`\x80\xc1)\xf0\x15\xcb\xbb\xfa\xa1\xfb\x1a\xda\x7f\
\xc7\x1f\xb4\xdf+\xffW\xcb\x7f\x03{\x9d|\xecF\x00q\x1c\x00\x00\x00\x00IEND\
\xaeB`\x82\xfc+\x1c['
